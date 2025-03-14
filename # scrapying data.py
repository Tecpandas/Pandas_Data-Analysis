from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                                QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QPalette, QColor
from PySide6.QtWidgets import QMessageBox
import requests
from bs4 import BeautifulSoup
import re

class WebScraperApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ScrapeYard")
        self.setGeometry(100, 100, 600, 500)
        self.setStyleSheet("""
            QWidget {
                background-color: #282c34;
                color: #abb2bf;
                font-family: "Arial", sans-serif;
                font-size: 14px;
            }
            QLabel {
                background-color: transparent;
            }
            QLineEdit, QTextEdit, QComboBox {
                background-color: #3e4451;
                color: #d1d5db;
                border: 1px solid #5c6370;
                padding: 8px;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #61afef;
                color: #282c34;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #569cd6;
            }
            QComboBox::drop-down {
                border: 0px;
            }
            QComboBox::down-arrow {
                image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAh0lEQVQ4T93VMQrDQBBF4S2EBhK4x6gYQgJjYQEpYwMd6AYSOEgCYwUqYI6c0c42sX1z3rysznL/53k/4EioAEQn29hR0M4Qo0k8748cQz9mQYt1+b/451K7nC/l/M/gI6IAYk3g+R9j6g/55H/r04jUf8Dk7w4g6y1x/cAAAAASUVORK5CYII=);
                width: 14px;
                height: 14px;
            }

        """)
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)

        # Header Label
        self.header_label = QLabel("ScrapeYard")
        font = QFont("Arial", 20, QFont.Bold)
        self.header_label.setFont(font)
        self.header_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.header_label)

        # URL Entry
        self.url_label = QLabel("Website URL:")
        main_layout.addWidget(self.url_label)
        self.url_entry = QLineEdit()
        main_layout.addWidget(self.url_entry)

        # Parser Entry
        self.parser_label = QLabel("HTML Parser (e.g., 'html.parser'):")
        main_layout.addWidget(self.parser_label)
        self.parser_entry = QLineEdit()
        self.parser_entry.setText('html.parser')
        main_layout.addWidget(self.parser_entry)

        # Filter Type Dropdown
        self.filter_label = QLabel("Filter Type:")
        main_layout.addWidget(self.filter_label)
        self.filter_type = QComboBox()
        self.filter_type.addItems(["All Text", "Sentence", "Word"])
        main_layout.addWidget(self.filter_type)

        # Scrape Button
        self.scrape_button = QPushButton("Scrape")
        self.scrape_button.clicked.connect(self.start_scrape)
        main_layout.addWidget(self.scrape_button)

        # Output Area (Scrollable)
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        main_layout.addWidget(self.output_area)

        # Progress Indicator
        self.progress_label = QLabel("")
        self.progress_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.progress_label)

        self.setLayout(main_layout)

    def start_scrape(self):
        self.scrape_button.setEnabled(False)
        self.progress_label.setText("Scraping in progress...")
        QTimer.singleShot(100, self.scrape)  # Non-blocking

    def scrape(self):
        url = self.url_entry.text()
        parser = self.parser_entry.text()
        filter_type = self.filter_type.currentText()

        if not url or not parser:
            QMessageBox.critical(self, "Error", "Please fill all fields!")
            self.reset_ui()
            return

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, parser)
            all_text = soup.get_text(separator='\n')

            if all_text.strip():
                if filter_type == "All Text":
                    filtered_data = all_text
                elif filter_type == "Sentence":
                    filtered_data = "\n".join(re.split(r'[.!?]\s+', all_text.strip()))
                elif filter_type == "Word":
                    filtered_data = " ".join(re.findall(r'\b\w+\b', all_text))
                else:
                    filtered_data = all_text

                self.output_area.setText(filtered_data)
            else:
                QMessageBox.information(self, "Info", "No text data found on the webpage.")

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Network error: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
        finally:
            self.reset_ui()

    def reset_ui(self):
        self.scrape_button.setEnabled(True)
        self.progress_label.setText("")


if __name__ == "__main__":
    app = QApplication([])
    window = WebScraperApp()
    window.show()
    app.exec_()