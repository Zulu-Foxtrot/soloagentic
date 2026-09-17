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

# Research-based content generation for Solopreneur Automation
# Trend 1: Seat Apocalypse (SaaS vs Agentic)
# Trend 2: Decision Fatigue (Architecture over Tools)
# Trend 3: AI Cost Management (Local-First vs API)

ADVANCED_TOPICS = [
    {
        "title": "The Seat Apocalypse: Why Solopreneurs are Fleeing SaaS for Agentic Automation",
        "slug": "seat-apocalypse-saas-to-agentic",
        "category": "Strategy",
        "intro": "Per-seat pricing is dying. In 2026, the leanest solo businesses are replacing 5+ SaaS tools with single-agent pipelines. Here is the architectural shift behind this exodus and how you can reclaim your margin.",
        "sections": [
            {"h2": "1. The Cost of Connectivity", "text": "Every API integration you pay for adds to your 'operational tax'. When you use Zapier or Make, you pay for the convenience of not thinking. The agentic model flips this: you build the thinking layer yourself (via LLM reasoning), and pay only for the compute."},
            {"h2": "2. Blueprint: From SaaS Stack to Agentic Loop", "text": "Instead of a 10-node Zapier flow, use a single Python agent that monitors your inbox, processes tasks, and updates your CRM. It's not about 'connecting' apps anymore; it's about delegating decisions.", "code": "def agentic_loop():\n    # Simplified agent logic\n    email = fetch_inbox()\n    decision = reason(email)\n    execute(decision)"}
        ]
    },
    {
        "title": "Decision Fatigue: Building Operational Boundaries in an AI World",
        "slug": "decision-fatigue-automation",
        "category": "Strategy",
        "intro": "The biggest threat to a solo founder isn't a lack of tools—it's having too many choices. Automation should protect your time, not steal it through maintenance.",
        "sections": [
            {"h2": "1. Constrained Stacks", "text": "The winning strategy in 2026 is simple: Fewer tools, deeper configurations. Pick your orchestration layer (n8n or pure Python) and stick to it."},
            {"h2": "2. The 'Human-in-the-loop' Buffer", "text": "Never automate the irreversible. Keep humans in the loop for decisions that involve money, reputation, or long-term strategy."}
        ]
    },
    {
        "title": "AI Cost Management: The $0/Month Operational Blueprint",
        "slug": "ai-cost-management",
        "category": "Development & Code",
        "intro": "Unexpected API bills are the new 'SaaS bloat'. Here is how to keep your AI costs flat as you scale your solopreneur business.",
        "sections": [
            {"h2": "1. Local-First Execution", "text": "By running small models (Ollama/Llama 3.1) locally for triage and using high-end cloud models (Claude 3.5/GPT-4o) only for high-judgment work, you can slash your API costs by 90%."},
            {"h2": "2. Verification Layers", "text": "Stop re-running failed agent loops. Implement robust error handling to ensure your agent doesn't burn tokens on recursive failures.", "code": "from tenacity import retry\n@retry(stop=stop_after_attempt(3))\ndef efficient_call():\n    # your agent logic here"}
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