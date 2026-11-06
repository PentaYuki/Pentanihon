#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PentaNihon Daily Study Scheduler & Story Automation
Quản lý lịch học 25 bài Shinkanzen và tạo câu chuyện mỗi ngày.
"""
import os
import datetime

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHINKANZEN_DIR = os.path.join(WORKSPACE_DIR, 'shinkanzen')
STORY_DIR = os.path.join(WORKSPACE_DIR, 'story')

def get_study_status():
    lessons = sorted([d for d in os.listdir(SHINKANZEN_DIR) if d.startswith('bai-')])
    notes_count = sum(1 for d in lessons if os.path.exists(os.path.join(SHINKANZEN_DIR, d, 'lesson-note.md')))
    stories = sorted([f for f in os.listdir(STORY_DIR) if (f.startswith('series-') or f.startswith('story-') or f.startswith('tap-')) and f.endswith('.md')])
    return lessons, notes_count, stories

def display_daily_dashboard():
    now = datetime.datetime.now()
    lessons, notes_count, stories = get_study_status()
    print("=" * 60)
    print(f"🌸 PENTANIHONGO - LỊCH HỌC NHẬT NGỮ HÔM NAY ({now.strftime('%d/%m/%Y')}) 🌸")
    print("=" * 60)
    print(f"📚 Tổng số bài Shinkanzen Master N2 đã sẵn sàng: {len(lessons)}/25 bài")
    print(f"📝 Sổ tay ghi chú bài học (Lesson Notes) hoàn chỉnh: {notes_count}/25 bài")
    print(f"📖 Tổng số tập Series Bầu Trời Xanh Tokyo đã phát hành: {len(stories)} tập")
    print("-" * 60)
    print("💡 Lời dặn của chị Yuki:")
    print("   'Bé cưng mỗi ngày nhớ xem 5 phút Lesson Note, luyện 1 bài Shinkanzen và theo dõi 1 tập phim Tokyo nhé!'")
    print("=" * 60)

if __name__ == '__main__':
    display_daily_dashboard()
