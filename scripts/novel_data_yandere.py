# -*- coding: utf-8 -*-
"""Tổng hợp Tiểu thuyết 2 — YANDERE ROMANCE (12 Chương, 12 Bài Shinkanzen, 233 Từ vựng)."""

from novel_data_yandere_a import YANDERE_META, YANDERE_CHAPTERS_A
from novel_data_yandere_b import YANDERE_CHAPTERS_B

YANDERE_NOVEL = {
    **YANDERE_META,
    "chapters": YANDERE_CHAPTERS_A + YANDERE_CHAPTERS_B,
}
