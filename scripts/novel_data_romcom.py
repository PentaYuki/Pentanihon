# -*- coding: utf-8 -*-
"""Tổng hợp Tiểu thuyết 1 — ROMCOM (13 Chương, 13 Bài Shinkanzen, 314 Từ vựng)."""

from novel_data_romcom_a import ROMCOM_META, ROMCOM_CHAPTERS_A
from novel_data_romcom_b import ROMCOM_CHAPTERS_B

ROMCOM_NOVEL = {
    **ROMCOM_META,
    "chapters": ROMCOM_CHAPTERS_A + ROMCOM_CHAPTERS_B,
}
