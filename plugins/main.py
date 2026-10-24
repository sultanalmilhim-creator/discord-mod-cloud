import sys
import json
import urllib.request
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QLabel, QPushButton, QListWidget, QMessageBox)
from PyQt6.QtCore import Qt

# رابط السحاب المباشر الخاص بك على GitHub
MANIFEST_URL = "https://raw.githubusercontent.com/sultanalmilhim-creator/discord-mod-cloud/main/manifest.json"

class DiscordCloudModApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.loadCloudData()

    def initUI(self):
        self.setWindowTitle("أداة ديسكورد السحابية المخصصة")
        self.resize(600, 450)
        
        # جعل الواجهة بالكامل من اليمين لليسار (RTL) للغة العربية
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        
        # تصميم الواجهة (Dark Mode)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e2e;
                color: #cdd6f4;
                font-family: 'Segoe UI', Tahoma, sans-serif;
            }
            QLabel {
                color: #cdd6f4;
                font-size: 14px;
            }
            QPushButton {
                background-color: #89b4fa;
                color: #11111b;
                border-radius: 6px;
                padding: 10px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #b4befe;
            }
            QListWidget {
                background-color: #181825;
                border: 1px solid #313244;
                border-radius: 6px;
                color: #cdd6f4;
                padding: 5px;
                font-size: 13px;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # عنوان الإعلان القادم من السحاب
        self.title_label = QLabel("جاري جلب الإعلانات من السحاب...")
        self.title_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #fab387;")
        layout.addWidget(self.title_label)

        # حالة الاتصال بالسحاب
        self.status_label = QLabel("حالة السحاب: جاري الاتصال...")
        layout.addWidget(self.status_label)

        # قائمة الإضافات المسحوبة من GitHub
        plugins_title = QLabel("الإضافات المتاحة سحابياً:")
        plugins_title.setStyleSheet("font-weight: bold; margin-top: 10px; color: #a6e3a1;")
        layout.addWidget(plugins_title)

        self.plugins_list = QListWidget()
        layout.addWidget(self.plugins_list)

        # زر التثبيت
        self.action_btn = QPushButton("تطبيق وتثبيت الإضافات في ديسكورد")
        self.action_btn.clicked.connect(self.applyModifications)
        layout.addWidget(self.action_btn)

    def loadCloudData(self):
        try:
            # طلب البيانات من رابط الـ GitHub الخاص بك
            req = urllib.request.Request(
                MANIFEST_URL, 
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode('utf-8'))
                
                # جلب الإعلان وتحديث الحالة
                announcement = data.get("announcement", "مرحباً بك")
                self.title_label.setText(announcement)
                self.status_label.setText("حالة السحاب: متصل بنجاح 🟢 (السحاب يعمل بكفاءة)")
                
                # تعبئة القائمة بالإضافات الموجودة في المستودع
                self.plugins_list.clear()
                for plugin in data.get("plugins", []):
                    item_text = f"📦 {plugin['name']} — {plugin['description']} (الإصدار: {plugin['version']})"
                    self.plugins_list.addItem(item_text)
                    
        except Exception as e:
            self.status_label.setText("حالة السحاب: فشل الاتصال 🔴")
            QMessageBox.warning(self, "خطأ في الاتصال", fُ"تعذر جلب البيانات من السحاب:\n{str(e)}")

    def applyModifications(self):
        QMessageBox.information(self, "تم بنجاح", "تم قراءة الإضافات السحابية وتجهيزها للحقن في ديسكورد!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DiscordCloudModApp()
    window.show()
    sys.exit(app.exec())
