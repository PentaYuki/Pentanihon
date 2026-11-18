# -*- coding: utf-8 -*-
"""Tổng hợp Tiểu thuyết 3 — ISEKAI FANTASY (12 Chương, 12 Bài Shinkanzen, 233 Từ vựng)."""

from novel_data_isekai_a import ISEKAI_META, ISEKAI_CHAPTERS_A
from novel_data_isekai_b import ISEKAI_CHAPTERS_B

ISEKAI_NOVEL = {
    **ISEKAI_META,
    "chapters": ISEKAI_CHAPTERS_A + ISEKAI_CHAPTERS_B,
}
