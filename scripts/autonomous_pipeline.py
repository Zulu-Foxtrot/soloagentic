#!/usr/bin/env python3
# SoloAgentic Otonom İçerik Pipeline - Windows Uyumlu Python Script
# Hermes cronjob tarafından çalıştırılır.

import os
import sys
import subprocess
import datetime

PROJECT_DIR = r"C:\Users\zafer\solopreneur-ai-hub"

def run_cmd(cmd, cwd=None):
    """Komut çalıştır, çıktıyı döndür."""
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, shell=True)
    return result.returncode, result.stdout, result.stderr

def main():
    print(f"[{datetime.datetime.now()}] SoloAgentic pipeline başladı...")
    
    # 1. Python içerik motorunu çalıştır
    code, out, err = run_cmd("python generate_post.py", cwd=PROJECT_DIR)
    if code != 0:
        print(f"HATA (generate_post.py): {err}")
        return 1
    print(out.strip())
    
    # 2. Git değişiklik kontrolü
    code, out, err = run_cmd("git status --porcelain", cwd=PROJECT_DIR)
    if code != 0:
        print(f"HATA (git status): {err}")
        return 1
    
    if not out.strip():
        print(f"[{datetime.datetime.now()}] Yeni içerik yok, çıkılıyor.")
        return 0
    
    # 3. Git konfigürasyonu
    run_cmd('git config user.name "hermes-cron[bot]"', cwd=PROJECT_DIR)
    run_cmd('git config user.email "hermes-cron@soloagentic.local"', cwd=PROJECT_DIR)
    
    # 4. Commit ve push
    code, out, err = run_cmd("git add -A", cwd=PROJECT_DIR)
    if code != 0:
        print(f"HATA (git add): {err}")
        return 1
    
    commit_msg = f"Auto: Daily content update {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}"
    code, out, err = run_cmd(f'git commit -m "{commit_msg}"', cwd=PROJECT_DIR)
    if code != 0:
        print(f"HATA (git commit): {err}")
        return 1
    
    code, out, err = run_cmd("git push origin main", cwd=PROJECT_DIR)
    if code != 0:
        print(f"HATA (git push): {err}")
        return 1
    
    print(f"[{datetime.datetime.now()}] Pipeline başarıyla tamamlandı. Site güncelleniyor...")
    return 0

if __name__ == "__main__":
    sys.exit(main())