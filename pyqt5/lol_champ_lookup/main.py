import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import random

BASE_URL = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champions/"
SUMMARY_URL = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-summary.json"
html = f"""
<html>
<body style="margin:0; padding:0; background:black; display:flex; justify-content:center; align-items:center; width:100%; height:100%;">
    <video autoplay muted playsinline loop style="height:100%; width:100%; object-fit:cover; background:black;">
        <source src="https://d28xe8vt774jo5.cloudfront.net/champion-abilities/0777/ability_0777_W1.webm" type="video/webm">
        Your browser does not support the video tag.
    </video>
</body>
</html>
"""

class ChampionLookupApp(QWidget):
    def __init__(self):
        super().__init__()
        self.name_input = QLineEdit()
        self.lookup_button = QPushButton("Search")
        self.random_button = QPushButton("Surprise me!")
        self.champion_image_label = QLabel("Champion\nImage")
        self.name_role_difficulty_label = QLabel()
        self.description_label = QLabel()
        self.abilities_label = QLabel("Abilities")
        self.video_label = QLabel()
        self.web_view = QWebEngineView()

        self.ability_labels = []
        self.ability_buttons = []
        self.ability_names = ["Passive", "Q", "W", "E", "R"]

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("LOL Champion Lookup")
        self.resize(900, 700)
        self.name_input.setPlaceholderText("Enter champion name...")
        self.champion_image_label.setAlignment(Qt.AlignCenter)
        self.create_ability_widgets()
        self.set_style()
        self.setup_layout()
        self.web_view.setHtml(html)
        self.lookup_button.clicked.connect(self.on_search)
        self.name_input.returnPressed.connect(self.on_search)
        self.random_button.clicked.connect(self.surprise)

    def create_ability_widgets(self):
        for ability_name in self.ability_names:
            label = QLabel()
            button = QPushButton(ability_name)

            self.ability_labels.append(label)
            self.ability_buttons.append(button)

    def set_style(self):
        gold_color = "#c8aa6e"
        dark_gold = "#937341"
        bg_light = "#f5f5f5"
        bg_lighter = "#ffffff"
        text_color = "#333333"
        border_color = "#d4af37"
        accent_color = "#e8e1d1"

        # Устанавливаем object names для элементов
        self.lookup_button.setObjectName("LookupButton")
        self.random_button.setObjectName("RandomButton")
        for i, button in enumerate(self.ability_buttons):
            button.setObjectName(f"AbilityButton_{i}")

        # Общий стиль приложения
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {bg_lighter};
                color: {text_color};
            }}

            QLineEdit {{
                border: 2px solid {border_color};
                border-radius: 6px;
                background-color: {bg_light};
                color: {text_color};
                padding: 12px;
                font-size: 18px;
                font-weight: bold;
            }}

            QLabel {{
                border: 2px solid {border_color};
                background-color: {bg_light};
                color: {text_color};
                padding: 15px;
            }}

            #LookupButton, #RandomButton {{
                background-color: {gold_color};
                color: white;
                border: 2px solid {dark_gold};
                border-radius: 6px;
                padding: 12px 24px;
                font-size: 18px;
                font-weight: bold;
            }}

            #LookupButton:hover, #RandomButton:hover {{
                background-color: {dark_gold};
            }}

            #LookupButton:pressed, #RandomButton:pressed {{
                background-color: #7a6239;
            }}

            QLabel[objectName="abilities_label"] {{
                color: {dark_gold};
                font-size: 20px;
                font-weight: bold;
                padding: 10px 0;
                border: none;
                background-color: transparent;
            }}

            QLabel[objectName="champion_image_label"] {{
                border: 2px solid {border_color};
                background-color: {bg_light};
                color: {text_color};
                padding: 0px;
            }}

            QLabel[objectName="name_role_difficulty_label"] {{
                font-size: 24px;
                font-weight: bold;
            }}

            QLabel[objectName="description_label"] {{
                font-size: 16px;
                line-height: 1.4;
            }}

            QLabel[objectName^="ability_label"] {{
                border: 2px solid {border_color};
                border-radius: 6px;
                background-color: {accent_color};
                padding: 0px;
            }}

            QPushButton[objectName^="AbilityButton_"] {{
                background-color: {gold_color};
                color: white;
                border: 2px solid {dark_gold};
                border-radius: 6px;
                font-size: 16px;
                font-weight: bold;
                padding: 8px;
            }}

            QPushButton[objectName^="AbilityButton_"]:hover {{
                background-color: {dark_gold};
            }}

            QPushButton[objectName^="AbilityButton_"]:pressed {{
                background-color: #7a6239;
            }}

            QWebEngineView#web_view {{
                border: 2px solid {border_color};
                border-radius: 6px;
                background-color: {accent_color};
            }}
        """)

        # Устанавливаем object names для QLabel'ов
        self.abilities_label.setObjectName("abilities_label")
        self.champion_image_label.setObjectName("champion_image_label")
        self.name_role_difficulty_label.setObjectName("name_role_difficulty_label")
        self.description_label.setObjectName("description_label")
        self.web_view.setObjectName("web_view")

        for i, label in enumerate(self.ability_labels):
            label.setObjectName(f"ability_label_{i}")

        # Размеры элементов
        self.champion_image_label.setFixedSize(244, 443)
        self.name_role_difficulty_label.setFixedHeight(80)
        self.description_label.setWordWrap(True)

        for label, button in zip(self.ability_labels, self.ability_buttons):
            label.setFixedSize(64, 64)
            label.setAlignment(Qt.AlignCenter)
            button.setFixedSize(180, 64)

        self.web_view.setFixedHeight(320)

        # Выравнивание текста
        self.name_role_difficulty_label.setAlignment(Qt.AlignVCenter)
        self.description_label.setAlignment(Qt.AlignVCenter)

    def setup_layout(self):
        search_layout = QHBoxLayout()
        search_layout.addWidget(self.name_input)
        search_layout.addWidget(self.lookup_button)
        search_layout.addWidget(self.random_button)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.name_role_difficulty_label)
        right_layout.addWidget(self.description_label)

        card_layout = QHBoxLayout()
        card_layout.addWidget(self.champion_image_label)
        card_layout.addLayout(right_layout)

        abilities_layout = QVBoxLayout()
        for label, button in zip(self.ability_labels, self.ability_buttons):
            ability_layout = QHBoxLayout()
            ability_layout.addWidget(label)
            ability_layout.addWidget(button)
            abilities_layout.addLayout(ability_layout)

        with_video_layout = QHBoxLayout()
        with_video_layout.addLayout(abilities_layout)
        with_video_layout.addWidget(self.web_view)

        main_layout = QVBoxLayout()
        main_layout.addLayout(search_layout)
        main_layout.addLayout(card_layout)
        main_layout.addWidget(self.abilities_label)
        main_layout.addLayout(with_video_layout)

        self.setLayout(main_layout)

    def surprise(self):
        try:
            champions = requests.get(SUMMARY_URL).json()
            if champions:
                random_champ = random.choice(champions)
                if random_champ:
                    self.name_input.setText(random_champ["name"])
                    self.load_champion(random_champ["name"])
            return None
        except:
            return None

    def on_search(self):
        name = self.name_input.text().strip()
        if name:
            self.load_champion(name)

    def load_champion(self, name):
        try:
            champions = requests.get(SUMMARY_URL).json()
            champ_data = next((c for c in champions if c["name"].lower() == name.lower()), None)

            if not champ_data:
                self.show_error(f"Champion '{name}' not found")
                return

            champ_url = f"{BASE_URL}{champ_data['id']}.json"
            data = requests.get(champ_url).json()

            self.update_ui(data)

        except Exception as e:
            self.show_error(f"Error: {e}")

    def update_ui(self, data):
        name = data["name"]
        roles = ", ".join(role.capitalize() for role in data.get("roles", []))
        difficulty = "⭐" * data["tacticalInfo"]["difficulty"]
        display_text = f"{name} ◦ {roles} ◦ Difficulty: {difficulty}"

        self.name_role_difficulty_label.setText(display_text)
        self.description_label.setText(data["shortBio"])

        self.load_champion_image(data)

    def load_champion_image(self, data):
        for skin in data.get("skins", []):
            if skin.get("isBase", False):
                image_path = skin.get("loadScreenPath", "").replace(
                    "/lol-game-data/assets/",
                    "plugins/rcp-be-lol-game-data/global/default/"
                ).lower()
                image_url = f"https://raw.communitydragon.org/latest/{image_path}"

                try:
                    response = requests.get(image_url, timeout=10)
                    if response.status_code == 200:
                        pixmap = QPixmap()
                        pixmap.loadFromData(response.content)
                        self.champion_image_label.setPixmap(pixmap.scaled(244, 443, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                        return
                except:
                    self.champion_image_label.setText("No Image")
        self.champion_image_label.setText("No Image")

    def show_error(self, message):
        self.name_role_difficulty_label.setText("Error")
        self.description_label.setText(message)
        self.champion_image_label.setText("Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChampionLookupApp()
    window.show()
    sys.exit(app.exec_())
