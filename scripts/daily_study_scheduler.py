# -*- coding: utf-8 -*-
import os
import datetime

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHINKANZEN_DIR = os.path.join(WORKSPACE_DIR, 'shinkanzen')
STORY_DIR = os.path.join(WORKSPACE_DIR, 'story')


def count_md_files(rel_subdirs, exclude_readme=True):
    total = 0
    for sub in rel_subdirs:
        target = os.path.join(SHINKANZEN_DIR, sub)
        if not os.path.isdir(target):
            continue
        for f in os.listdir(target):
            if not f.endswith('.md'):
                continue
            if exclude_readme and f == 'README.md':
                continue
            total += 1
    return total


def get_study_status():
    bunpou = count_md_files(['ngu-phap/phan-1', 'ngu-phap/phan-2', 'ngu-phap/phan-3', 'ngu-phap'])
    goi = count_md_files(['tu-vung/phan-1', 'tu-vung/phan-2'])
    kanji = count_md_files(['kanji/step-1', 'kanji/step-2', 'kanji/step-3'])
    novel_chaps = 0
    for genre in ('romcom', 'yandere', 'isekai'):
        gdir = os.path.join(WORKSPACE_DIR, 'novel', genre)
        if os.path.isdir(gdir):
            novel_chaps += len([f for f in os.listdir(gdir) if f.startswith('chuong-') and f.endswith('.md')])

    stories = sorted([
        f for f in os.listdir(STORY_DIR)
        if (f.startswith('series-') or f.startswith('story-') or f.startswith('tap-')) and f.endswith('.md')
    ]) if os.path.isdir(STORY_DIR) else []

    counts = {
        'ngu-phap': bunpou,
        'tu-vung': goi,
        'kanji': kanji,
        'novel': novel_chaps,
        'exam': 6,
    }
    return counts, stories


def display_daily_dashboard():
    now = datetime.datetime.now()
    counts, stories = get_study_status()
    total_shinkanzen = counts['ngu-phap'] + counts['tu-vung'] + counts['kanji']
    print("=" * 64)
    print(f"🌸 PENTANIHONGO - LỊCH HỌC NHẬT NGỮ HÔM NAY ({now.strftime('%d/%m/%Y')}) 🌸")
    print("=" * 64)
    print(f"⛩️ Ngữ pháp (文法):   {counts['ngu-phap']} bài (Phần 1-3 + Kính ngữ)")
    print(f"📚 Từ vựng (語彙):    {counts['tu-vung']}/37 bài + Flashcards 780 từ")
    print(f"🈷️ Chữ Hán (漢字):    {counts['kanji']}/53 bài (1.046 chữ chuẩn sách)")
    print(f"📖 3 Bộ Tiểu thuyết:  {counts['novel']}/37 chương (Romcom • Yandere • Isekai)")
    print(f"🎯 Đề thi JLPT N2:    {counts['exam']} đề chuẩn (222 câu tự chấm & giải thích)")
    print(f"✨ Tổng Shinkanzen:   {total_shinkanzen} bài nền tảng")
    print(f"📕 Series Aozora:     {len(stories)} tập")
    print("💌 Chị Yuki nhắc nhẹ: Hôm nay đọc 1 chương tiểu thuyết + 5 câu trắc nghiệm nha em~ 🌸")
    print("=" * 64)


if __name__ == "__main__":
    display_daily_dashboard()
