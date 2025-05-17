# Nhận diện cảm xúc văn bản bằng Machine Learning

## Tổng quan

### Chủ đề
Nghiên cứu này tập trung vào việc **nhận diện cảm xúc** (Emotion Analysis) của văn bản tiếng Anh bằng các kỹ thuật học máy, sử dụng mạng nơ-ron hồi tiếp (LSTM, Bi-LSTM) với dữ liệu huấn luyện gồm các câu văn bản và nhãn cảm xúc tương ứng.

### Động lực & Ý nghĩa
- Phân tích cảm xúc văn bản hỗ trợ nhiều lĩnh vực: chăm sóc khách hàng, phân tích mạng xã hội, đánh giá sản phẩm, hỗ trợ phòng chống tự tử, v.v.
- Giúp các hệ thống AI hiểu sâu sắc hơn về trạng thái cảm xúc của con người, từ đó đưa ra các phản hồi phù hợp và kịp thời.

### Mục tiêu
- Xây dựng pipeline tiền xử lý dữ liệu văn bản, mã hóa dữ liệu, và huấn luyện mô hình mạng nơ-ron để phân loại cảm xúc.
- Phân loại các cảm xúc: **anger** (giận dữ), **fear** (sợ hãi), **joy** (vui), **love** (yêu), **sadness** (buồn), **surprise** (ngạc nhiên).

---

## Cấu trúc Dự án

```
emotion-analysis/
├── train.txt          # Dữ liệu huấn luyện: văn bản & nhãn cảm xúc
├── test.txt           # Dữ liệu kiểm thử
├── Emotion Analysis.ipynb  # Notebook Colab thực thi pipeline
├── requirements.txt   # Các thư viện cần thiết
└── README.md          # Tài liệu mô tả dự án
```

---

## Cài đặt Môi trường

### 1. Cài đặt Python và các thư viện
Khuyến nghị sử dụng Python >=3.8 và cài đặt các thư viện trong `requirements.txt`:

```bash
pip install -r requirements.txt
```

Các thư viện chính:
- pandas, numpy
- scikit-learn
- nltk
- seaborn, matplotlib
- tensorflow, keras

### 2. Chuẩn bị dữ liệu
- Tải file `train.txt` và `test.txt` (dạng CSV, phân cách `;`) vào thư mục dự án.

---

## Pipeline Xử lý & Huấn luyện Mô hình

### 1. Tiền xử lý dữ liệu
- Đọc dữ liệu huấn luyện và kiểm thử từ file txt.
- Chuyển đổi nhãn cảm xúc từ text sang số.
- Làm sạch văn bản: loại bỏ ký tự đặc biệt, chuyển về chữ thường, loại bỏ stopwords, và stemming.

### 2. Biểu diễn văn bản
- Ánh xạ mỗi từ sang chỉ số (one-hot encoding với vocab size = 10.000).
- Padding chuỗi để đảm bảo độ dài đầu vào đồng nhất cho model.

### 3. Xây dựng và huấn luyện mô hình
- Sử dụng **Sequential Model** với các lớp: Embedding, Bidirectional LSTM, Dense.
- Hàm loss: `categorical_crossentropy`, optimizer: `adam`.
- Chia tập huấn luyện/kiểm thử ngẫu nhiên (train/test split).
- Đánh giá mô hình trên tập kiểm thử.

### 4. Triển khai hàm nhận diện cảm xúc mới
- Hàm `suicide_avoider(x)` tiền xử lý và dự đoán cảm xúc cho 1 câu văn bản đầu vào.

---

## Hướng dẫn sử dụng

### Chạy notebook trên Google Colab
1. Tải notebook `Emotion Analysis.ipynb` lên Google Colab.
2. Upload dữ liệu `train.txt` và `test.txt` khi được yêu cầu.
3. Thực thi từng cell để hoàn tất pipeline và huấn luyện mô hình.
4. Sử dụng hàm `suicide_avoider(x)` để dự đoán cảm xúc cho văn bản mới.

### Ví dụ sử dụng:
```python
x = "I am very happy today!"
suicide_avoider(x)
# Output: person is in joy
```

---

**Tác giả:**  
- Team Name: _(nhóm 12)_  
- Affiliation: _(SGU_CNTT)_  

---
