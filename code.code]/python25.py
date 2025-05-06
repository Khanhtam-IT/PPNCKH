import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class EmotionAIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Nhận Diện Cảm Xúc")
        self.root.geometry("400x400")
        self.create_main_interface()

    def create_main_interface(self):
        self.clear_window()
        tk.Label(self.root, text="Chào bạn!", font=("Arial", 18)).pack(pady=10)

        # Nút phân tích từ ảnh
        btn_image = tk.Button(self.root, text="Phân tích từ ảnh", command=self.create_image_analysis)
        btn_image.pack(pady=10)

        # Nút phân tích từ internet
        btn_internet = tk.Button(self.root, text="Internet", command=self.create_internet_analysis)
        btn_internet.pack(pady=10)

    def create_image_analysis(self):
        self.clear_window()

        # Khung tải ảnh
        self.frame_image = tk.Frame(self.root, width=400, height=200)
        self.frame_image.pack(pady=10)

        tk.Label(self.frame_image, text="Tải ảnh lên:").pack(pady=5)
        self.upload_button = tk.Button(self.frame_image, text="Chọn ảnh", command=self.upload_image)
        self.upload_button.pack(pady=5)

        # Khung phân tích
        self.frame_analysis = tk.Frame(self.root, width=400, height=200)
        self.frame_analysis.pack(pady=10)

        self.analyze_button = tk.Button(self.frame_analysis, text="Phân tích", command=self.analyze_image)
        self.analyze_button.pack(pady=5)

        # Nút quay lại
        btn_back = tk.Button(self.root, text="Quay lại", command=self.create_main_interface)
        btn_back.pack(pady=10)

        # Khung hiển thị cảm xúc
        self.frame_result = tk.Frame(self.root)
        self.frame_result.pack(pady=10)

        self.result_label = tk.Label(self.frame_result, text="Cảm xúc phân tích: ")
        self.result_label.pack(pady=5)

    def create_internet_analysis(self):
        self.clear_window()

        # Khung chọn mạng xã hội
        self.frame_social = tk.Frame(self.root, width=400, height=200)
        self.frame_social.pack(pady=10)

        tk.Label(self.frame_social, text="Chọn mạng xã hội:").pack(pady=5)

        btn_fb = tk.Button(self.frame_social, text="Facebook", command=lambda: self.fetch_comments("Facebook"))
        btn_fb.pack(pady=5)

        btn_tiki = tk.Button(self.frame_social, text="Tiki", command=lambda: self.fetch_comments("Tiki"))
        btn_tiki.pack(pady=5)

        btn_sendo = tk.Button(self.frame_social, text="Sen Đỏ", command=lambda: self.fetch_comments("Sen Đỏ"))
        btn_sendo.pack(pady=5)

        # Khung phân tích
        self.frame_analysis = tk.Frame(self.root, width=400, height=200)
        self.frame_analysis.pack(pady=10)

        self.analyze_button = tk.Button(self.frame_analysis, text="Phân tích", command=self.analyze_internet)
        self.analyze_button.pack(pady=5)

        # Nút quay lại
        btn_back = tk.Button(self.root, text="Quay lại", command=self.create_main_interface)
        btn_back.pack(pady=10)

        # Khung hiển thị cảm xúc
        self.frame_result = tk.Frame(self.root)
        self.frame_result.pack(pady=10)

        self.result_label = tk.Label(self.frame_result, text="Cảm xúc phân tích: ")
        self.result_label.pack(pady=5)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.result_label.config(text="Ảnh đã tải lên!")

    def fetch_comments(self, platform):
        self.result_label.config(text=f"Bình luận từ {platform}: 'Tuyệt vời!'")

    def analyze_image(self):
        self.result_label.config(text="Cảm xúc phân tích: Vui vẻ")

    def analyze_internet(self):
        self.result_label.config(text="Cảm xúc phân tích: Hài lòng")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = EmotionAIApp(root)
    root.mainloop()