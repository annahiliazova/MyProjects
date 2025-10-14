import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage

base_url = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champions/"
summary_url = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-summary.json"

base_video_url = "https://d28xe8vt774jo5.cloudfront.net/"


class ChampionLookupApp(QWidget):
    def __init__(self):
        super().__init__()
        self.name_input = QLineEdit()
        self.lookup_button = QPushButton("Search")
        self.champion_image_label = QLabel()
        self.name_role_difficulty_label = QLabel()
        self.description_label = QLabel()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("LOL Champion Lookup")
        self.resize(900, 700)

        self.setStyleSheet("""
            QLineEdit {
                border: 2px solid #c8aa6e;
                padding: 8px;
                font-size: 20px;
            }
            QPushButton {
                padding: 8px 16px;
                border: none;
                font-size: 20px;
            }
        """)

        main_layout = QVBoxLayout()
        search_layout = QHBoxLayout()

        self.name_input.setPlaceholderText("Enter champion name...")

        search_layout.addWidget(self.name_input)
        search_layout.addWidget(self.lookup_button)

        card_layout = QHBoxLayout()

        self.champion_image_label.setFixedSize(244, 443)
        self.champion_image_label.setStyleSheet("border: 1px solid #c8aa6e;")
        self.champion_image_label.setText("Champion\nImage")
        self.champion_image_label.setAlignment(Qt.AlignCenter)

        right_layout = QVBoxLayout()

        self.name_role_difficulty_label.setStyleSheet(
            "border: 1px solid #c8aa6e; font-size: 30px;")
        self.name_role_difficulty_label.setFixedHeight(80)

        self.description_label.setStyleSheet(
            "border: 1px solid #c8aa6e; font-size: 20px;")
        self.description_label.setFixedHeight(353)  # 443 - 80 - 20 (spacing) = 343
        self.description_label.setWordWrap(True)

        right_layout.addWidget(self.name_role_difficulty_label)
        right_layout.addWidget(self.description_label)

        card_layout.addWidget(self.champion_image_label)
        card_layout.addLayout(right_layout)

        main_layout.addLayout(search_layout)
        main_layout.addLayout(card_layout)

        self.setLayout(main_layout)
        self.lookup_button.clicked.connect(self.on_search)
        self.name_input.returnPressed.connect(self.on_search)

    def on_search(self):
        name = self.name_input.text().strip()
        if name:
            self.load_champion(name)

    def get_champion_id(self, name):
        try:
            response = requests.get(summary_url)
            if response.status_code == 200:
                champions = response.json()
                for champ in champions:
                    if champ["name"].lower() == name.lower():
                        return champ["id"]
            return None
        except Exception as e:
            print(f"Error fetching champion list: {e}")
            return None

    def find_champion_image_url(self, data):
        try:
            for skin in data.get("skins", []):
                if skin.get("isBase", False):
                    load_screen_path = skin.get("loadScreenPath")
                    if load_screen_path:
                        clean_path = load_screen_path.replace("/lol-game-data/assets/",
                                                              "plugins/rcp-be-lol-game-data/global/default/")
                        clean_path = clean_path.lower()
                        full_url = f"https://raw.communitydragon.org/latest/{clean_path}"
                        try:
                            response = requests.head(full_url, timeout=5)
                            if response.status_code == 200:
                                print(f"Found image from skin data: {full_url}")
                                return full_url
                        except:
                            continue
        except Exception as e:
            print(f"Error getting skin data: {e}")
        return None

    def load_champion(self, name):
        champ_id = self.get_champion_id(name)
        if champ_id is None:
            self.name_role_difficulty_label.setText(f" Champion '{name}' not found")
            self.description_label.setText("")
            self.champion_image_label.setText("Not Found")
            return

        url = f"{base_url}{champ_id}.json"
        try:
            response = requests.get(url)
            if response.status_code != 200:
                raise Exception(f"HTTP {response.status_code}")

            data = response.json()
            champ_name = data["name"]
            roles_list = data.get("roles", [])
            roles_str = ", ".join(roles_list)
            difficulty = data["tacticalInfo"]["difficulty"] * "⭐"

            display_text = f"{champ_name.capitalize()} ◦ {roles_str} ◦ Difficulty: {difficulty}"
            bio = data["shortBio"]

            self.name_role_difficulty_label.setText(display_text)
            self.description_label.setText(bio)

            icon_url = self.find_champion_image_url(data)

            if icon_url:
                icon_response = requests.get(icon_url, timeout=10)
                if icon_response.status_code == 200:
                    image = QImage.fromData(icon_response.content)
                    pixmap = QPixmap.fromImage(image)
                    self.champion_image_label.setPixmap(
                        pixmap.scaled(244, 443, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                else:
                    self.champion_image_label.setText("No Image")
            else:
                self.champion_image_label.setText("No Image")

        except Exception as e:
            self.name_role_difficulty_label.setText("Error loading champion")
            self.description_label.setText(str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChampionLookupApp()
    window.show()
    sys.exit(app.exec_())
