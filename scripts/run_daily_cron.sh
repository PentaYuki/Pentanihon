#!/bin/bash
# Script tự động chạy lúc 09:00 sáng hàng ngày trên máy Mac
cd /Users/gooleseswsq1gmail.com/Documents/PentaNihonGo || exit 1
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"

echo "=== Running Daily Story Automation at $(date) ===" >> /tmp/pentanihon_cron.log
git pull --rebase origin main >> /tmp/pentanihon_cron.log 2>&1
python3 scripts/generate_daily_story.py >> /tmp/pentanihon_cron.log 2>&1
python3 scripts/daily_study_scheduler.py >> /tmp/pentanihon_cron.log 2>&1

git add story/ README.md index.html
if git diff --staged --quiet; then
    echo "No changes to commit today." >> /tmp/pentanihon_cron.log
else
    git commit -m "feat(daily-story): tự động phát hành tập mới lúc 09:00 sáng [skip ci]" >> /tmp/pentanihon_cron.log 2>&1
    git push origin main >> /tmp/pentanihon_cron.log 2>&1
    echo "Pushed new episode successfully at $(date)!" >> /tmp/pentanihon_cron.log
fi
