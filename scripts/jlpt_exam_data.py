# -*- coding: utf-8 -*-
"""
Tổng hợp Toàn Bộ Hệ Thống Đề Thi Thử JLPT N2 Chuẩn (222 Câu Hỏi):
- 3 Đề Full JLPT N2 (言語知識：文字・語彙・文法 — 54 câu/đề = 162 câu)
- 3 Đề Ôn Tập Nhanh Theo Tiểu Thuyết (20 câu/đề = 60 câu)
"""

from jlpt_exam_data_1 import EXAM_1
from jlpt_exam_data_2 import EXAM_2
from jlpt_exam_data_3 import EXAM_3
from jlpt_exam_data_reviews import (
    EXAM_REVIEW_ROMCOM,
    EXAM_REVIEW_YANDERE,
    EXAM_REVIEW_ISEKAI,
)

ALL_EXAMS = [
    EXAM_1,
    EXAM_2,
    EXAM_3,
    EXAM_REVIEW_ROMCOM,
    EXAM_REVIEW_YANDERE,
    EXAM_REVIEW_ISEKAI,
]
