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
    dokkai = count_md_files(['doc-hieu/phan-1_luyen-ky-nang', 'doc-hieu/phan-2_thuc-chien'])
    choukai = count_md_files(['nghe-hieu'])
    novel_dir = os.path.join(WORKSPACE_DIR, 'novel')
    novel_chaps = len([f for f in os.listdir(novel_dir) if f.startswith('chuong-') and f.endswith('.md')]) if os.path.isdir(novel_dir) else 0

    stories = sorted([
        f for f in os.listdir(STORY_DIR)
        if (f.startswith('series-') or f.startswith('story-') or f.startswith('tap-')) and f.endswith('.md')
    ]) if os.path.isdir(STORY_DIR) else []

    counts = {
        'ngu-phap': bunpou,
        'tu-vung': goi,
        'kanji': kanji,
        'doc-hieu': dokkai,
        'nghe-hieu': choukai,
        'novel': novel_chaps,
    }
    return counts, stories


def display_daily_dashboard():
    now = datetime.datetime.now()
    counts, stories = get_study_status()
    total_lessons = sum(v for k, v in counts.items() if k != 'novel')
    print("=" * 64)
    print(f"🌸 PENTANIHONGO - LỊCH HỌC NHẬT NGỮ HÔM NAY ({now.strftime('%d/%m/%Y')}) 🌸")
    print("=" * 64)
    print(f"⛩️ Ngữ pháp (文法): {counts['ngu-phap']} bài (Phần 1-3 + Kính ngữ)")
    print(f"📚 Từ vựng (語彙):  {counts['tu-vung']}/37 bài + Flashcards Trắng Đen")
    print(f"🈷️ Chữ Hán (漢字):  {counts['kanji']}/53 bài (1.046 chữ chuẩn sách)")
    print(f"📖 Đọc hiểu (読解): {counts['doc-hieu']}/8 chuyên đề kỹ năng & thực chiến")
    print(f"🎧 Nghe hiểu (聴解): {counts['nghe-hieu']}/6 chương (TTS-ready + Furigana)")
    print(f"✨ Tổng tài liệu Shinkanzen 5 cuốn: {total_lessons} bài")
    print(f"📓 Tiểu thuyết tương tác N2 (novel/): {counts['novel']}/6 chương")
    print(f"📕 Tổng số tập Series Bầu Trời Xanh Tokyo: {len(stories)} tập")
    print("=" * 64)


if __name__ == "__main__":
    display_daily_dashboard()
