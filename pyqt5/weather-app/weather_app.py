import os.path
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont, QPixmap
from datetime import datetime, timezone

from dotenv import load_dotenv
load_dotenv()


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get weather", self)
        self.temperature_label = QLabel(self)
        self.weather_icon_label = QLabel(self)
        self.description_label = QLabel(self)
        self.wind_arrow_label = QLabel(self)
        self.wind_info_label = QLabel(self)
        self.sun_icon_label = QLabel(self)
        self.sun_info_label = QLabel(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Weather App")
        icon_path = "icon.png"
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon("icon.png"))

        font = QFont("Segoe UI", 10)
        font.setStyleHint(QFont.SansSerif)
        QApplication.setFont(font)

        self.city_input.setPlaceholderText("Enter city name")

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        input_hbox = QHBoxLayout()
        input_hbox.addWidget(self.city_input)
        input_hbox.addWidget(self.get_weather_button)
        main_layout.addLayout(input_hbox)

        emoji_temp_hbox = QHBoxLayout()
        emoji_temp_hbox.setSpacing(12)
        emoji_temp_hbox.addWidget(self.weather_icon_label)
        emoji_temp_hbox.addWidget(self.temperature_label)

        centered_hbox = QHBoxLayout()
        centered_hbox.addStretch()
        centered_hbox.addLayout(emoji_temp_hbox)
        centered_hbox.addStretch()
        main_layout.addLayout(centered_hbox)

        main_layout.addWidget(self.description_label, alignment=Qt.AlignCenter)

        main_layout.addSpacing(20)

        bottom_hbox = QHBoxLayout()
        bottom_hbox.setSpacing(30)

        sun_hbox = QHBoxLayout()
        sun_hbox.setSpacing(8)
        sun_hbox.addWidget(self.sun_icon_label)
        sun_hbox.addWidget(self.sun_info_label)
        sun_hbox.addStretch()

        wind_hbox = QHBoxLayout()
        wind_hbox.setSpacing(8)
        wind_hbox.addWidget(self.wind_arrow_label)
        wind_hbox.addWidget(self.wind_info_label)
        wind_hbox.addStretch()

        bottom_hbox.addLayout(sun_hbox)
        bottom_hbox.addStretch()
        bottom_hbox.addLayout(wind_hbox)

        main_layout.addLayout(bottom_hbox)
        self.setLayout(main_layout)

        self.setStyleSheet("""
            QWidget {
                background-color: hsl(217, 52%, 65%);
            }
            QLabel, QPushButton {
                color: white;
            }
            QLineEdit#city_input {
                background-color: white;
                font-size: 28px;
                padding: 10px;
                color: hsl(217, 52%, 35%);
                border: none;
                border-radius: 8px;
                selection-background-color: hsl(217, 52%, 40%);
            }
            QPushButton#get_weather_button {
                font-size: 28px;
                font-weight: bold;
                padding: 10px;
                background-color: hsl(217, 52%, 45%);
                border: none;
                border-radius: 8px;
            }
            QPushButton#get_weather_button:hover {
                background-color: hsl(217, 52%, 60%);
            }
            QLabel#temperature_label {
                font-size: 72px;
                font-weight: bold;
                qproperty-alignment: AlignCenter;
            }
            QLabel#description_label {
                font-size: 28px;
                qproperty-alignment: AlignCenter;
            }
            QLabel#wind_info_label, QLabel#sun_info_label {
                font-size: 20px;
                color: white;
            }        
        """)

        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.weather_icon_label.setObjectName("weather_icon_label")
        self.description_label.setObjectName("description_label")
        self.wind_arrow_label.setObjectName("wind_arrow_label")
        self.wind_info_label.setObjectName("wind_info_label")
        self.sun_icon_label.setObjectName("sun_icon_label")
        self.sun_info_label.setObjectName("sun_info_label")

        self.get_weather_button.clicked.connect(self.get_weather)
        self.city_input.returnPressed.connect(self.get_weather)

    def get_weather(self):
        api_key = os.getenv("OPENWEATHER_API_KEY")
        city = self.city_input.text().strip()

        if not city:
            self.display_error("Please enter a city name")
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError:
            status = response.status_code
            msg = {
                400: "Bad request:\nPlease check your input",
                401: "Unauthorized:\nInvalid API key",
                404: "Not Found:\nCity not found",
                500: "Internal Server Error:\nPlease try again later",
                502: "Bad Gateway:\nInvalid response from server",
                503: "Service Unavailable:\nServer is down",
                504: "Gateway Timeout:\nNo response from server"
            }.get(status, f"HTTP error occurred:\n{status}")
            self.display_error(msg)
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.RequestException as e:
            self.display_error(f"Request Error:\n{str(e)}")

    def display_error(self, message):
        self.temperature_label.setText(message)
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.weather_icon_label.clear()
        self.description_label.clear()
        self.wind_arrow_label.clear()
        self.sun_icon_label.clear()
        self.sun_info_label.clear()
        self.wind_info_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 72px;")

        temperature_c = data["main"]["temp"] - 273.15
        feels_like_c = data["main"]["feels_like"] - 273.15
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]

        self.temperature_label.setText(f"{temperature_c:.1f}°C")
        self.description_label.setText(f"{weather_description.capitalize()}. Feels like: {feels_like_c:.1f}°C")

        icon_path = self.get_weather_icon(weather_id)
        if os.path.exists(icon_path):
            pixmap = QPixmap(icon_path).scaled(96, 96, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.weather_icon_label.setPixmap(pixmap)
        else:
            self.weather_icon_label.setText(self.get_weather_emoji(weather_id))

        wind_speed = data["wind"]["speed"]
        wind_deg = data["wind"]["deg"]
        wind_dir = self.get_wind_direction(wind_deg)
        wind_gust = data["wind"].get("gust", "—")

        dir_file = self.get_wind_direction_file(wind_deg)
        if os.path.exists(dir_file):
            pixmap = QPixmap(dir_file).scaled(96, 96, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.wind_arrow_label.setPixmap(pixmap)
        else:
            self.wind_arrow_label.setText(self.get_wind_arrow_emoji(wind_deg))

        self.wind_info_label.setText(f"Speed: {wind_speed} m/s\nDirection: {wind_dir}\nGust: {wind_gust} m/s")

        sun_path = "sun.png"
        if os.path.exists(sun_path):
            pixmap = QPixmap(sun_path).scaled(96, 96, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.sun_icon_label.setPixmap(pixmap)
        else:
            self.sun_icon_label.setText("☀")

        sunrise_unix = data["sys"]["sunrise"]
        sunset_unix = data["sys"]["sunset"]

        sunrise_dt = datetime.fromtimestamp(sunrise_unix, tz=timezone.utc).strftime("%H:%M UTC")
        sunset_dt = datetime.fromtimestamp(sunset_unix, tz=timezone.utc).strftime("%H:%M UTC")

        day_length_sec = sunset_unix - sunrise_unix
        hours, remainder = divmod(day_length_sec, 3600)
        minutes, _ = divmod(remainder, 60)
        day_length_str = f"{hours}h {minutes}m"

        self.sun_info_label.setText(f"Day length: {day_length_str}\nSunrise: {sunrise_dt}\nSunset: {sunset_dt}")

    @staticmethod
    def get_wind_direction(degrees):
        directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        index = int((degrees + 22.5) // 45) % 8
        return directions[index]

    @staticmethod
    def get_wind_direction_file(degrees):
        directions = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
        index = int((degrees + 22.5) // 45) % 8
        filename = directions[index] + ".png"
        return os.path.join("directions", filename)

    @staticmethod
    def get_wind_arrow_emoji(degrees):
        arrows = ["↑", "↗", "→", "↘", "↓", "↙", "←", "↖"]
        index = int((degrees + 22.5) // 45) % 8
        return arrows[index]

    @staticmethod
    def get_weather_icon(weather_id):
        if 200 <= weather_id <= 232:
            return "icons/thunderstorm.png"
        elif 300 <= weather_id <= 321:
            return "icons/rain.png"
        elif 500 <= weather_id <= 531:
            return "icons/rain.png"
        elif 600 <= weather_id <= 622:
            return "icons/snow.png"
        elif 701 <= weather_id <= 751:
            return "icons/mist.png"
        elif weather_id in (761, 771):
            return "icons/dust.png"
        elif weather_id == 762:
            return "icons/volcano.png"
        elif weather_id == 781:
            return "icons/tornado.png"
        elif weather_id == 800:
            return "icons/clear.png"
        elif 801 <= weather_id <= 804:
            return "icons/cloud.png"
        else:
            return "icons/unknown.png"

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌨️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 751:
            return "🌫️"
        elif weather_id in (761, 771):
            return "💨"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return "❓"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
