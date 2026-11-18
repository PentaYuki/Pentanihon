# 🎌 Pentanihon — Hệ Thống 3 Bộ Tiểu Thuyết Shinkanzen N2 &amp; Luyện Đề Chuẩn JLPT

<p align="center">
  <img src="https://img.shields.io/badge/JLPT-N2%20Master-red?style=for-the-badge&logo=japan" alt="JLPT N2" />
  <img src="https://img.shields.io/badge/3%20Novels-Romcom%20%7C%20Yandere%20%7C%20Isekai-b92b27?style=for-the-badge" alt="3 Light Novels" />
  <img src="https://img.shields.io/badge/Shinkanzen%20Goi-37%2F37%20Lessons%20(780%20Words)-green?style=for-the-badge" alt="100% Shinkanzen Vocabulary" />
  <img src="https://img.shields.io/badge/JLPT%20Exams-6%20Tests%20(222%20Questions)-364fc7?style=for-the-badge" alt="JLPT Mock Exams" />
  <img src="https://img.shields.io/badge/Daily-Stories%20Included-orange?style=for-the-badge" alt="Daily Stories" />
</p>

Chào mừng bạn đến với **Pentanihon** – hệ thống ôn luyện **JLPT N2** kết hợp giữa nền tảng **Shinkanzen Master N2 (Ngữ pháp • Từ vựng • Chữ Hán)** và phương pháp học nhập vai qua **3 Bộ Tiểu Thuyết Liên Hoàn (Romcom • Yandere Tâm Lý • Isekai)** phủ **100% toàn bộ 37 bài / 780 từ vựng Shinkanzen N2**, đi kèm **Trung tâm Đề Thi Chuẩn JLPT N2 (tự chấm điểm + giải thích chi tiết cả Đúng lẫn Sai)** dưới sự đồng hành nhắc nhở dịu dàng của **"Chị Yuki"**.

---

## 🌟 Những Điểm Nổi Bật Của Hệ Thống Mới

- 📖 **3 Bộ Tiểu Thuyết Tương Tác N2 ([`novel/index.html`](./novel/index.html)) — Phủ 100% 37/37 Bài Shinkanzen (780/780 Từ):**
  - **💕 Bộ 1 Romcom (13 chương — 314 từ — 65 câu quiz):** Chuyện tình hài lãng mạn nhà trọ chung Sakurazaka (Gia đình, Tính cách, Ẩm thực, Việc nhà, Sở thích, Du lịch, Trường học, Công việc, Truyền thông, Lễ hội, Đa nghĩa & Quán dụng 1).
  - **🖤 Bộ 2 Yandere Tâm Lý (12 chương — 233 từ — 60 câu quiz):** Tình yêu độc chiếm & tâm lý giằng xé (Cảm xúc, Sức khỏe, Máy tính, Hình sự, Động từ đa nghĩa, Từ đồng âm dễ nhầm, Phó từ & Quán dụng 2).
  - **⚔️ Bộ 3 Isekai Kiến Quốc (12 chương — 233 từ — 60 câu quiz):** Chuyển sinh dùng tri thức hiện đại lập quốc (Thiên nhiên, Kinh tế, Chính trị-Luật, Sinh thái, Khoa học AI, Số lượng, Không-Thời gian, Onomatopoeia & Toàn bộ Cấu tạo từ).
  - **Mỗi chương đều có:** Nhãn ghi rõ bài Shinkanzen chứa trong chương, dịch tiếng Việt từng đoạn & trọn chương, **bảng từ vựng kèm nghĩa đầy đủ ngay bên dưới mỗi chương**, phát âm MP3 + Web Speech, **lời nhắc nhẹ nhàng dễ thương của chị Yuki** và **5 câu trắc nghiệm giải thích cả Đúng & Sai**.
- 🎯 **Trung Tâm Đề Thi Chuẩn JLPT N2 ([`exam/index.html`](./exam/index.html)) — 6 Bộ Đề (222 Câu Hỏi):**
  - **3 Đề Full JLPT N2 言語知識（文字・語彙・文法）** chuẩn Mondai 1–9 (54 câu/55 phút) + **3 Đề Ôn Tập Nhanh Theo Bộ Truyện** (20 câu/bộ).
  - **Tự chấm điểm tự động** (quy đổi thang 60 + phân tích điểm từng Mondai) và **giải thích cặn kẽ cả khi em chọn ĐÚNG lẫn khi chọn SAI**, kèm link quay lại đúng chương truyện gốc.
- 🌸 **Lời Nhắc Nhẹ Nhàng Dễ Thương:** Từng chương truyện, đề thi và trang chủ đều có lời dặn dò ấm áp, hóm hỉnh từ chị Yuki giúp giảm áp lực ôn thi.
- ☕ **Series Dài Tập Nhật Ngữ (`story/`):** Giữ nguyên bộ truyện hàng ngày **「東京あおぞら物語」** tự động cập nhật bởi `.github/workflows/daily-story.yml`.

---

## 🗂️ Cấu Trúc Thư Mục Dự Án

```text
Pentanihon/
├── README.md                          # Trang chủ tổng quan dự án
├── index.html                         # Trang chủ web tương tác (3 Tiểu thuyết, JLPT Exam, Yuki Notes, Shinkanzen)
├── reader.html                        # Trình đọc Markdown đa năng
├── .github/workflows/
│   └── daily-story.yml                # GitHub Actions tự động xuất bản tập mới mỗi ngày
├── docs/                              # Cẩm nang tóm lược kiến thức N2 cốt lõi
│   ├── 01_Tu_Vung_Kanji_N2.md         # Tổng hợp phó từ, tiền tố, hậu tố, từ đồng nghĩa
│   ├── 02_Ngu_Phap_N2_Trong_Tam.md    # 120+ mẫu ngữ pháp phân loại theo cụm ý nghĩa
│   └── 03_Bi_Kip_Luyen_De_JLPT_N2.md  # Chiến thuật 55 phút Mondai 1–9 & mẹo tránh bẫy N2
├── novel/                             # 📖 3 Bộ Tiểu Thuyết Shinkanzen N2 (37 chương, 780 từ)
│   ├── index.html                     # Trình đọc 3 thể loại tương tác + Audio + Bảng nghĩa dưới chương + Quiz
│   ├── README.md                      # Mục lục 37 chương thuộc 3 bộ
│   ├── romcom/chuong-01..13.md        # Bộ 1 Romcom (13 chương)
│   ├── yandere/chuong-01..12.md       # Bộ 2 Yandere (12 chương)
│   └── isekai/chuong-01..12.md        # Bộ 3 Isekai (12 chương)
├── exam/                              # 🎯 Trung Tâm Đề Thi Chuẩn JLPT N2
│   ├── index.html                     # Giao diện Thi thật & Luyện tập, tự chấm điểm & giải thích Đúng/Sai
│   ├── exam-data.js                   # 6 Bộ đề (222 câu hỏi chuẩn N2)
│   └── README.md                      # Danh sách đề & bảng cấu trúc Mondai 1–9
├── shinkanzen/                        # Kho giáo trình nền tảng Shinkanzen Master N2
│   ├── README.md                      # Bản đồ hệ thống Shinkanzen × Tiểu thuyết × Thi thử
│   ├── ngu-phap/                      # ⛩️ Văn pháp (Phần 1: 26 bài, Phần 2 ★: 3 bài, Phần 3: 12 bài, Kính ngữ)
│   ├── tu-vung/                       # 📚 Từ vựng (37 bài / 780 từ + Flashcards + Audio MP3 + Link Tiểu thuyết)
│   └── kanji/                         # 🈷️ Chữ Hán (Step 1–3: 53 bài đủ 1.046 chữ + Challenge + 別冊1)
├── story/                             # Series Dài Tập: Tokyo Aozora Monogatari
└── scripts/                           # Công cụ tự động hóa build toàn bộ hệ thống
    ├── build_shinkanzen_all.py        # Orchestrator tổng hợp build Bunpou, Goi, Kanji, 3 Novels, 6 Exams & Manifest
    ├── build_novel.py                 # Sinh 3 tiểu thuyết tương tác & kiểm tra độ phủ 37/37 bài, 780/780 từ
    ├── build_exam.py                  # Sinh 6 đề thi thử JLPT N2 tự chấm điểm & giải thích Đúng/Sai
    ├── novel_data_{romcom,yandere,isekai}*.py  # Dữ liệu 3 bộ tiểu thuyết
    ├── jlpt_exam_data*.py             # Dữ liệu 222 câu hỏi thi thử JLPT N2
    └── daily_study_scheduler.py       # Script thống kê lịch học hàng ngày
```

---

## 🚀 Hướng Dẫn Build & Sử Dụng

### Build lại toàn bộ học liệu (Shinkanzen + 3 Tiểu thuyết + 6 Đề JLPT):
```bash
python3 scripts/build_shinkanzen_all.py
```

### Xem Dashboard Lịch Học Hôm Nay:
```bash
python3 scripts/daily_study_scheduler.py
```

---
> 🌸 *"Học mà có chút rung động của Romcom, chút hồi hộp của Yandere và tinh thần khám phá của Isekai thì hành trình chinh phục JLPT N2 sẽ nhẹ nhàng mà đáng nhớ hơn bao giờ hết. Chị Yuki luôn cổ vũ em nha!"* 💕
