# 🎌 Pentanihon - Cẩm Nang Ôn Luyện JLPT N2 & Kể Chuyện Mỗi Ngày

<p align="center">
  <img src="https://img.shields.io/badge/JLPT-N2%20Master-red?style=for-the-badge&logo=japan" alt="JLPT N2" />
  <img src="https://img.shields.io/badge/Shinkanzen-25%20Lessons%20Complete-green?style=for-the-badge" alt="Shinkanzen 25 Lessons" />
  <img src="https://img.shields.io/badge/Daily-Stories%20Included-orange?style=for-the-badge" alt="Daily Stories" />
  <img src="https://img.shields.io/badge/Hiragana-100%25%20Annotated-blue?style=for-the-badge" alt="Hiragana Annotated" />
  <img src="https://img.shields.io/badge/Audio--Ready-TTS%20Metadata-purple?style=for-the-badge" alt="Audio Ready" />
</p>

Chào mừng bạn đến với **Pentanihon** – dự án học tiếng Nhật toàn diện được thiết kế đặc biệt cho kỳ thi **JLPT N2**, kết hợp phương pháp học giáo trình kinh điển **Shinkanzen Master** và phương pháp học cảm xúc qua **Truyện kể mỗi ngày (Storytelling)** dưới sự đồng hành của **"Người chị gái dễ thương"**.

---

## 🌟 Những Điểm Nổi Bật Của Dự Án

- 🌸 **Đồng hành cùng Chị Gái Dễ Thương:** Giọng văn chỉ bảo ân cần, hóm hỉnh, phân tích sắc thái tâm lý người Nhật, mẹo nhớ đời và chỉ điểm các cạm bẫy trắc nghiệm hay gặp.
- 🔤 **Phiên âm Hiragana 100%:** Mọi chữ Hán trong câu ví dụ, hội thoại nghe, bài đọc hiểu và đề thi trắc nghiệm đều được chú thích Hiragana `漢字（かんじ）` để người học đọc mượt mà, không bị khựng lại.
- 🎧 **Dữ liệu Nghe sẵn sàng cho Tool Audio (TTS-Ready):** Toàn bộ file kịch bản nghe đều có cấu trúc trường rõ ràng (`track_id`, `speakers: ["Narrator", "Man", "Woman"]`) giúp dễ dàng lập trình bot đọc audio hoặc tích hợp ứng dụng di động.
- 📖 **Storytelling Mỗi Ngày (`story/`):** Những mẩu chuyện ngắn giàu cảm xúc về đời sống Tokyo, góc phố mùa thu, chuyến tàu đêm... lồng ghép khéo léo các điểm ngữ pháp N2, có kèm bài tập đọc hiểu và bài học nhân sinh.
- ⏰ **Tự Động Hóa & Đặt Lịch:** Tích hợp script [**`daily_study_scheduler.py`**](./scripts/daily_study_scheduler.py) và **GitHub Actions Workflow** tự động chạy lịch học mỗi ngày.

---

## 🗂️ Cấu Trúc Thư Mục Dự Án

```text
Pentanihon/
├── README.md                          # Trang chủ tổng quan dự án
├── .github/workflows/
│   └── daily-story.yml                # GitHub Actions tự động chạy lịch học mỗi ngày
├── docs/                              # Cẩm nang tóm lược kiến thức N2 cốt lõi
│   ├── 01_Tu_Vung_Kanji_N2.md         # Tổng hợp phó từ, tiền tố, hậu tố, từ đồng nghĩa
│   ├── 02_Ngu_Phap_N2_Trong_Tam.md    # 120+ mẫu ngữ pháp phân loại theo cụm ý nghĩa
│   └── 03_Chien_Thuat_Doc_Hieu_N2.md  # Kỹ thuật bẻ khóa bài đọc và 4 loại bẫy kinh điển
├── shinkanzen/                        # Trọn bộ 25 bài giáo trình Shinkanzen Master N2
│   ├── README.md                      # Bảng Tracker theo dõi tiến độ học tập 25 bài
│   ├── bai-01/                        # Bài 01: Thời điểm & Trình tự (時間・時)
│   │   ├── ngu-phap.md                # Cấu trúc, cách dùng, ví dụ có Hiragana
│   │   ├── tu-vung.md                 # Từ vựng, collocations, giải thích cặn kẽ
│   │   ├── kanji.md                   # Chữ Hán Shinkanzen, âm On/Kun, từ ghép
│   │   ├── nghe.md                    # Script đối thoại nghe hiểu (TTS-ready)
│   │   ├── doc-hieu.md                # Bài đọc ngắn, phân tích câu & loại suy đáp án
│   │   └── luyen-tap.md               # Trắc nghiệm, bài tập dấu sao (★), đáp án
│   ├── bai-02/                        # Bài 02: Phạm vi & Giới hạn (範囲・起点)
│   └── ... (đến bai-25/)              # Đầy đủ trọn bộ từ Bài 01 đến Bài 25!
├── story/                             # Chuyên mục Mỗi Ngày Một Câu Chuyện
│   ├── README.md                      # Mục lục và hướng dẫn học qua truyện kể
│   ├── story-01_tiem_banh_mua_thu.md  # Tiệm bánh mì mùa thu & Cuộc gặp định mệnh
│   ├── story-02_chuyen_tau_dem.md     # Chuyến tàu đêm & Tấm vé đến ngày mai
│   └── story-03_quan_ca_phe_ngay_mua.md# Quán cà phê ngày mưa & Chiếc ô bỏ quên
└── scripts/
    └── daily_study_scheduler.py       # Script quản lý tiến độ và lịch học hàng ngày
```

---

## 🗺️ Lộ Trình Ôn Luyện Shinkanzen N2 Chuẩn 25 Bài

| Chặng | Danh sách bài | Trọng tâm kiến thức |
| :--- | :--- | :--- |
| **Chặng 1: Nền tảng** | Bài 01 - 08 | Thời điểm, trình tự, phạm vi, liên quan, đối chiếu và tiêu chuẩn đánh giá |
| **Chặng 2: Nâng cao** | Bài 09 - 16 | Nguyên nhân sâu xa, mục đích, nhượng bộ, điều kiện giả định và biểu cảm |
| **Chặng 3: Thực chiến** | Bài 17 - 25 | Phán đoán khẳng định, bắt buộc, kính ngữ thương mại và tổng duyệt đề thi |

👉 Chi tiết từng bài và bảng checklist học tập có thể xem tại: [**`shinkanzen/README.md`**](./shinkanzen/README.md)

---

## ☕ Góc Truyện Kể Hàng Ngày (`story/`)

Mỗi ngày mở một câu chuyện ngắn:
1. Đọc văn bản tiếng Nhật có phiên âm Hiragana.
2. Cảm nhận bản dịch tiếng Việt giàu cảm xúc.
3. Ôn lại cấu trúc ngữ pháp N2 xuất hiện tự nhiên trong bài.
4. Trả lời câu hỏi đọc hiểu và lắng nghe lời dặn dò dịu dàng của chị gái.

👉 Khám phá danh sách truyện tại: [**`story/README.md`**](./story/README.md)

---

## 🚀 Hướng Dẫn Sử Dụng & Tự Động Hóa

### Chạy Dashboard Lịch Học:
```bash
python3 scripts/daily_study_scheduler.py
```

### Kích hoạt GitHub Actions:
Workflow tự động được lên lịch chạy vào lúc **07:00 sáng mỗi ngày (giờ Việt Nam)**, hoặc bạn có thể vào tab **Actions** trên GitHub và nhấn **Run workflow** bất cứ lúc nào.

---

## 💖 Lời Nhắn Từ Chị Gái
> *"Học một ngôn ngữ mới cũng như trồng một mầm cây vậy, mỗi ngày tưới một chút nước kiên trì thì nhất định sẽ nở hoa thơm ngát. Chúc bé của chị ôn thi thật tốt và luôn vững tin vào chính mình nha!"*
