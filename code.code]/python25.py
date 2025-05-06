import sys
import cv2
import pytesseract
from nltk.sentiment import SentimentIntensityAnalyzer
from PyQt5 import QtWidgets, QtGui, uic, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('gui1.ui', self)

        # Kết nối các nút bấm
        self.Quet_button.clicked.connect(self.extract_and_analyze)
        self.Huy_button.clicked.connect(self.close)
        self.taianh_button.clicked.connect(self.load_image)
        self.lammoi_button.clicked.connect(self.clear_tables)
        self.return_button.clicked.connect(self.close)

        # Khởi tạo biến để lưu đường dẫn ảnh
        self.image_path = ""

    def analyze_sentiment(self, text):
        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(text)
        return sentiment

    def extract_text_from_image(self, image_path):
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)
        return text

    def extract_and_analyze(self):
        if self.image_path:
            text = self.extract_text_from_image(self.image_path)
            self.anh_tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(text))

            sentiment = self.analyze_sentiment(text)
            self.vanban_tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(sentiment)))
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please load an image first.")

    def load_image(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Chọn tệp tin", "", "Images (*.png *.xpm *.jpg);;All Files (*)")
        if file_path:
            print("Tệp đã chọn:", file_path)
        pixmap = QtGui.QPixmap(file_path)  # Sử dụng QtGui.QPixmap
        # Hiển thị ảnh trong bảng
        self.anh_tableWidget.setRowCount(1)
        self.anh_tableWidget.setColumnCount(1)
        self.anh_tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem())
        self.anh_tableWidget.item(0, 0).setIcon(QtGui.QIcon(pixmap))
        self.anh_tableWidget.setRowHeight(0, 300)
        self.anh_tableWidget.setColumnWidth(0, 300)
        QtWidgets.QMessageBox.information(self, "Image Loaded", "Image loaded successfully!")
    def clear_tables(self):
        self.anh_tableWidget.clearContents()
        self.vanban_tableWidget.clearContents()
        self.label_hienanh.clear()  # Nếu bạn đã thêm label hiển thị ảnh

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())