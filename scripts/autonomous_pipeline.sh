#!/bin/bash
# SoloAgentic Otonom İçerik Pipeline Script
# Bu script Hermes cronjob tarafından çalıştırılır.

set -e

PROJECT_DIR="C:/Users/zafer/solopreneur-ai-hub"
cd "$PROJECT_DIR"

echo "[$(date)] SoloAgentic pipeline başladı..."

# 1. Python içerik motorunu çalıştır
python generate_post.py

# 2. Değişiklik var mı kontrol et
if git diff --quiet && git diff --staged --quiet; then
    echo "[$(date)] Yeni içerik yok, çıkılıyor."
    exit 0
fi

# 3. Git konfigürasyonu (Actions bot olarak)
git config user.name "hermes-cron[bot]"
git config user.email "hermes-cron@soloagentic.local"

# 4. Tüm değişiklikleri ekle ve commit et
git add -A
git commit -m "Auto: Daily content update $(date +'%Y-%m-%d %H:%M')"

# 5. Push et (GitHub Pages deploy tetikler)
git push origin main

echo "[$(date)] Pipeline başarıyla tamamlandı. Site güncelleniyor..."