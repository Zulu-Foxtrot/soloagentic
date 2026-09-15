import os
import datetime
import re

# SoloAgentic Profesyonel Otonom İçerik Motoru v3.0
# Dinamik okuma süresi, kod blokları, adım adım rehberler ile tam donanımlı makaleler üretir.

OUTPUT_DIR = "C:/Users/zafer/solopreneur-ai-hub"
POSTS_DIR = os.path.join(OUTPUT_DIR, "posts")
os.makedirs(POSTS_DIR, exist_ok=True)

def count_words(text):
    """HTML etiketlerini temizleyip kelime sayar."""
    clean = re.sub(r'<[^>]+>', '', text)
    return len(clean.split())

def calculate_read_time(text):
    """Ortalama 200 kelime/dk hızıyla okuma süresi hesaplar."""
    words = count_words(text)
    mins = max(1, round(words / 200))
    return f"{mins} min read"

ADVANCED_TOPICS = [
    {
        "title": "Architecting a 24/7 Autonomous AI Agent Pipeline for Solo Founders",
        "slug": "architecting-24-7-autonomous-ai-pipeline",
        "category": "Architecture & Stacks",
        "intro": "In 2026, building a solo business no longer means working 16 hours a day. By structuring multi-agent runtimes with local background processes, founders are achieving unprecedented leverage. Here is the complete architectural breakdown of a production-grade autonomous agent pipeline you can deploy today on zero-cost infrastructure.",
        "sections": [
            {
                "h2": "1. The Core Philosophy: Agents Over Scripts",
                "text": "Traditional automation tools like basic webhook triggers or linear scripts fall short when dealing with ambiguity, retries, and decision-making. A true agentic architecture separates concerns into specialized roles:",
                "code": None,
                "bullet_points": [
                    "<strong>Research Agent:</strong> Crawls APIs, RSS feeds, and web sources; normalizes data into structured JSON.",
                    "<strong>Synthesis Agent:</strong> Takes raw data, applies LLM reasoning (summarization, classification, insight extraction), outputs actionable briefs.",
                    "<strong>Deployment Agent:</strong> Commits generated artifacts (Markdown, HTML, code) to Git, triggers CI/CD, posts to social APIs."
                ]
            },
            {
                "h2": "2. Local Orchestration Layer: Zero-Cost Runtime",
                "text": "To keep operational costs at absolute zero, leverage your existing hardware (or a cheap VPS). The stack is remarkably simple:",
                "code": """# scheduler.py - Minimal cron replacement using schedule library
import schedule
import time
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_agent(agent_name):
    logging.info(f'Starting {agent_name}...')
    result = subprocess.run(['python', f'agents/{agent_name}.py'], capture_output=True, text=True)
    if result.returncode != 0:
        logging.error(f'{agent_name} failed: {result.stderr}')
    else:
        logging.info(f'{agent_name} completed successfully.')

# Define your agent schedule
schedule.every().day.at("06:00").do(run_agent, 'research_agent')
schedule.every().day.at("06:30").do(run_agent, 'synthesis_agent')
schedule.every().day.at("07:00").do(run_agent, 'deployment_agent')

if __name__ == "__main__":
    logging.info("Orchestrator started. Waiting for jobs...")
    while True:
        schedule.run_pending()
        time.sleep(60)""",
                "bullet_points": [
                    "Run this as a background systemd service (Linux) or NSSM service (Windows) for true 24/7 uptime.",
                    "Each agent script is independent — swap, debug, or scale individually."
                ]
            },
            {
                "h2": "3. Error Handling & Self-Healing Loops",
                "text": "The hardest part of autonomous systems isn't the happy path—it's failure recovery. A robust agentic loop must include validation gates. If an API call fails, a build errors out, or an LLM hallucinates, the supervisor captures the traceback, applies a patch, and retries safely.",
                "code": """# supervisor.py - Wrapper for resilient execution
import json
import traceback
from tenacity import retry, stop_after_attempt, wait_exponential

class AgentSupervisor:
    def __init__(self, agent_func, max_retries=3):
        self.agent_func = agent_func
        self.max_retries = max_retries

    @retry(wait=wait_exponential(multiplier=1, min=2, max=10), stop=stop_after_attempt(3))
    def execute_with_retry(self, *args, **kwargs):
        try:
            result = self.agent_func(*args, **kwargs)
            self._validate_output(result)
            return result
        except Exception as e:
            logging.error(f"Attempt failed: {e}\\n{traceback.format_exc()}")
            raise

    def _validate_output(self, output):
        # Custom validation logic per agent
        if not output or (isinstance(output, dict) and not output.get('success')):
            raise ValueError("Invalid output structure")""",
                "bullet_points": [
                    "Use <code>tenacity</code> for exponential backoff retries.",
                    "Implement <code>_validate_output</code> per agent to catch silent failures (empty files, malformed JSON).",
                    "Log everything to a rotating file handler for post-mortem debugging."
                ]
            },
            {
                "h2": "4. Monetization & Practical ROI",
                "text": "When your administrative and content generation overhead drops by 80%, your focus shifts purely to high-leverage product decisions and community engagement. That is how solo founders cross the $1M revenue threshold with zero full-time employees. This pipeline isn't just a toy—it's the operating system of a modern one-person business.",
                "code": None,
                "bullet_points": [
                    "<strong>Affiliate Revenue:</strong> Embed tracking links in generated content for tools you genuinely use (Make, n8n, hosting, LLM APIs).",
                    "<strong>Digital Products:</strong> Package your refined agent scripts as a 'Solo Founder Automation Kit' ($49-$99).",
                    "<strong>High-Ticket Services:</strong> Use the pipeline output as a portfolio to sell 'Custom AI Automation Setup' ($1,500+)."
                ]
            }
        ]
    },
    {
        "title": "Mastering Local LLMs and Python Scripts for Zero-Cost Operations",
        "slug": "mastering-local-llms-python-scripts",
        "category": "Development & Code",
        "intro": "Relying entirely on paid cloud APIs can drain a solopreneur's budget during heavy iterative testing. Combining lightweight Python automation with local execution environments provides an unbreakable, private, and lightning-fast operational stack. Here is how to build it.",
        "sections": [
            {
                "h2": "1. Why Local-First Execution Wins",
                "text": "Cloud rate limits, token costs, and privacy concerns make cloud-only setups risky for background processing that runs thousands of times per month. Running lightweight scripts combined with smart caching layers eliminates unpredictable expenses and gives you full data sovereignty.",
                "code": None,
                "bullet_points": [
                    "No per-token billing — run 10k or 10M inferences for the same electricity cost.",
                    "Zero latency variance — critical for tight automation loops.",
                    "Full offline capability — your agents work on a plane, in a bunker, anywhere."
                ]
            },
            {
                "h2": "2. Setting Up a Local LLM Server (Ollama + Python)",
                "text": "The fastest way to get a production-grade local LLM running is Ollama. It handles model quantization, GPU acceleration, and exposes an OpenAI-compatible API.",
                "code": """# 1. Install Ollama (one-liner)
curl -fsSL https://ollama.com/install.sh | sh

# 2. Pull a coding-optimized model (4-bit quantized, ~4GB VRAM/RAM)
ollama pull codellama:7b-instruct-q4_K_M

# 3. Python client (openai-compatible)
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # dummy key
)

def local_llm_call(prompt, model="codellama:7b-instruct-q4_K_M"):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=2048
    )
    return response.choices[0].message.content

# Usage in your agent
result = local_llm_call("Write a Python script that scrapes HN front page and summarizes top 5 posts.")""",
                "bullet_points": [
                    "Swap models instantly: <code>ollama pull llama3.1:8b</code> for general reasoning.",
                    "Use <code>ollama serve</code> as a systemd service for background persistence."
                ]
            },
            {
                "h2": "3. Designing Resilient Python Agent Scripts",
                "text": "When writing scripts intended to run autonomously 24/7, every file operation, network call, and LLM interaction must be verified. Never assume success; verify before proceeding to the next pipeline stage.",
                "code": """import hashlib
import json
from pathlib import Path
from typing import Dict, Any

class AgentOutput:
    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def write_verified(self, filename: str, content: str, expected_hash: str = None) -> bool:
        filepath = self.output_dir / filename
        
        # 1. Write to temp file first (atomic write)
        temp_path = filepath.with_suffix('.tmp')
        temp_path.write_text(content, encoding='utf-8')
        
        # 2. Verify content hash if provided
        if expected_hash:
            actual_hash = hashlib.sha256(content.encode()).hexdigest()
            if actual_hash != expected_hash:
                temp_path.unlink(missing_ok=True)
                raise ValueError(f"Hash mismatch for {filename}")
        
        # 3. Verify file exists and is readable
        if not temp_path.exists() or temp_path.stat().st_size == 0:
            raise IOError(f"File write failed for {filename}")
        
        # 4. Atomic replace
        temp_path.replace(filepath)
        return True

    def read_verified(self, filename: str) -> str:
        filepath = self.output_dir / filename
        if not filepath.exists():
            raise FileNotFoundError(f"Required input {filename} missing")
        return filepath.read_text(encoding='utf-8')""",
                "bullet_points": [
                    "Atomic writes prevent corruption if the process is killed mid-write.",
                    "Content hashing catches silent data corruption.",
                    "Explicit verification turns 'hope it works' into 'proven it works'."
                ]
            },
            {
                "h2": "4. Integrating with GitHub Pages & Actions for Free Hosting",
                "text": "Static sites hosted on GitHub Pages offer infinite scalability with zero maintenance. Your Python agents generate Markdown or HTML, commit changes automatically, and trigger instant deployments via GitHub Actions — all free for public repos.",
                "code": """# .github/workflows/deploy.yml
name: Deploy SoloAgentic
on:
  push:
    branches: [main]
  workflow_dispatch:
  schedule:
    - cron: '0 6 * * *'  # Daily at 06:00 UTC

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install deps
        run: pip install -r requirements.txt
      - name: Run Content Pipeline
        run: python generate_post.py
      - name: Configure Git
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
      - name: Commit & Push if changed
        run: |
          git add -A
          git diff --staged --quiet || git commit -m "Auto: Content update $(date +'%Y-%m-%d')"
          git push""",
                "bullet_points": [
                    "The cron trigger in Actions runs your pipeline daily even if you never touch the repo.",
                    "Git history becomes your content audit trail — zero database needed.",
                    "Custom domain support (CNAME) for professional branding at zero cost."
                ]
            }
        ]
    }
]

def generate_deep_post():
    today = datetime.datetime.now()
    topic_index = today.day % len(ADVANCED_TOPICS)
    topic = ADVANCED_TOPICS[topic_index]
    
    date_str = today.strftime("%Y-%m-%d")
    filename = f"{topic['slug']}-{date_str}.html"
    filepath = os.path.join(POSTS_DIR, filename)
    
    sections_html = ""
    full_text_for_readtime = topic['intro']
    
    for sec in topic["sections"]:
        full_text_for_readtime += " " + sec.get("text", "")
        if sec.get("bullet_points"):
            full_text_for_readtime += " " + " ".join(sec["bullet_points"])
        
        section_html = f"<h2>{sec['h2']}</h2>\n<p>{sec['text']}</p>"
        
        if sec.get("code"):
            section_html += f'\n<pre><code>{sec["code"]}</code></pre>\n'
        
        if sec.get("bullet_points"):
            bullets = "".join([f"<li>{bp}</li>" for bp in sec["bullet_points"]])
            section_html += f"<ul>{bullets}</ul>"
        
        sections_html += section_html + "\n"
    
    read_time = calculate_read_time(full_text_for_readtime)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{topic['title']} | SoloAgentic</title>
    <style>
        :root {{
            --bg: #0d1117;
            --card-bg: #161b22;
            --text: #c9d1d9;
            --accent: #58a6ff;
            --border: #30363d;
            --muted: #8b949e;
            --code-bg: #0d1117;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            line-height: 1.7;
            margin: 0;
            padding: 0;
        }}
        .container {{
            max-width: 900px;
            margin: 3rem auto;
            padding: 0 1.5rem;
        }}
        .card {{
            background-color: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 2.5rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }}
        h1 {{
            color: #ffffff;
            font-size: 2.2rem;
            margin-bottom: 0.5rem;
            line-height: 1.3;
        }}
        h2 {{
            color: var(--accent);
            font-size: 1.4rem;
            margin-top: 2.5rem;
            border-bottom: 1px solid var(--border);
            padding-bottom: 0.5rem;
        }}
        p {{
            margin-bottom: 1.2rem;
            font-size: 1.05rem;
        }}
        .meta {{
            color: var(--muted);
            font-size: 0.9rem;
            margin-bottom: 2rem;
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            align-items: center;
        }}
        .badge {{
            background: #1f6feb33;
            color: var(--accent);
            padding: 0.2rem 0.6rem;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: 600;
        }}
        a {{
            color: var(--accent);
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .back {{
            margin-bottom: 1.5rem;
            display: inline-block;
            font-weight: 500;
        }}
        pre {{
            background: var(--code-bg);
            border: 1px solid var(--border);
            border-radius: 6px;
            padding: 1.5rem;
            overflow-x: auto;
            margin: 1.5rem 0;
        }}
        code {{
            font-family: 'Fira Code', 'Consolas', monospace;
            font-size: 0.9rem;
            line-height: 1.5;
        }}
        pre code {{
            background: none;
            padding: 0;
        }}
        ul {{
            padding-left: 1.5rem;
            margin: 1rem 0;
        }}
        li {{
            margin-bottom: 0.5rem;
        }}
        footer {{
            text-align: center;
            padding: 3rem;
            color: var(--muted);
            font-size: 0.9rem;
            border-top: 1px solid var(--border);
            margin-top: 4rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <a class="back" href="../index.html">&larr; &nbsp;Back to SoloAgentic Hub</a>
        <div class="card">
            <div class="meta">
                <span class="badge">{topic['category']}</span>
                <span>Published on {date_str}</span>
                <span>•</span>
                <span>{read_time}</span>
            </div>
            <h1>{topic['title']}</h1>
            <p style="font-size: 1.2rem; color: #ffffff; margin-top: 1rem; font-weight: 400;">{topic['intro']}</p>
            <hr style="border:0; border-top:1px solid var(--border); margin: 2rem 0;">
            
            {sections_html}

            <hr style="border:0; border-top:1px solid var(--border); margin: 2.5rem 0;">
            <p><strong>About SoloAgentic:</strong> We document real-world, zero-cost autonomous architectures for solo founders building high-leverage digital businesses.</p>
        </div>
    </div>
    <footer>
        <p>&copy; 2026 SoloAgentic. Powered by Hermes Agent & Autonomous Systems.</p>
    </footer>
</body>
</html>
"""
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"[SUCCESS] Profesyonel makale üretildi: {filepath} | Okuma Süresi: {read_time}")
    return topic, filename, date_str

def update_index(topic, filename, date_str):
    index_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_link = f'<li><a href="posts/{filename}"><strong>{topic["title"]}</strong> <span style="color: #8b949e; font-size: 0.9rem;">({date_str})</span></a></li>'
    
    if filename not in content:
        content = content.replace("<ul>", f"<ul>\n                {new_link}")
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("[SUCCESS] index.html güncellendi!")

if __name__ == "__main__":
    top, fn, dt = generate_deep_post()
    update_index(top, fn, dt)