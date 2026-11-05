#!/usr/bin/env python3
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
    stories = sorted([f for f in os.listdir(STORY_DIR) if f.startswith('story-')])
    return lessons, stories

def display_daily_dashboard():
    now = datetime.datetime.now()
    lessons, stories = get_study_status()
    print("=" * 60)
    print(f"🌸 PENTANIHONGO - LỊCH HỌC NHẬT NGỮ HÔM NAY ({now.strftime('%d/%m/%Y')}) 🌸")
    print("=" * 60)
    print(f"📚 Tổng số bài Shinkanzen Master N2 đã sẵn sàng: {len(lessons)}/25 bài")
    print(f"📖 Tổng số câu chuyện đã phát hành: {len(stories)} câu chuyện")
    print("-" * 60)
    print("💡 Lời dặn của chị gái:")
    print("   'Bé ngoan mỗi ngày dành 30 phút luyện 1 bài Shinkanzen và đọc 1 câu chuyện nhé!'")
    print("=" * 60)

if __name__ == '__main__':
    display_daily_dashboard()
