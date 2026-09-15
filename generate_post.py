import os
import datetime

# SoloAgentic Otonom Makale Fabrikası
OUTPUT_DIR = "C:/Users/zafer/solopreneur-ai-hub"
POSTS_DIR = os.path.join(OUTPUT_DIR, "posts")
os.makedirs(POSTS_DIR, exist_ok=True)

TOPICS = [
    {
        "title": "How to Automate Client Onboarding with AI Agents",
        "slug": "automate-client-onboarding-ai-agents",
        "content": "Client onboarding is one of the highest friction points for solo founders. By deploying a simple multi-agent pipeline using Python and local LLMs, you can automatically ingest new client forms, generate custom project scopes, and set up the entire workspace within seconds."
    },
    {
        "title": "The Zero-Cost Tech Stack Behind Successful Solopreneurs",
        "slug": "zero-cost-tech-stack-solopreneurs",
        "content": "You don't need an expensive software stack to run a profitable solo business. Combining open-source tools like GitHub Pages, local cron orchestration, and free-tier API endpoints allows solo operators to run entire digital businesses with zero operational cost."
    },
    {
        "title": "Why Autonomous Cron Jobs Are Better Than Traditional SaaS",
        "slug": "autonomous-cron-jobs-vs-saas",
        "content": "Instead of paying for multiple automation subscriptions, solo founders are shifting towards lightweight cron scripts running locally or on inexpensive VPS nodes. Complete data ownership, zero platform lock-in, and absolute customizability."
    }
]

def generate_new_post():
    today = datetime.datetime.now()
    day_index = today.day % len(TOPICS)
    topic = TOPICS[day_index]
    
    date_str = today.strftime("%Y-%m-%d")
    filename = f"{topic['slug']}-{date_str}.html"
    filepath = os.path.join(POSTS_DIR, filename)
    
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
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }}
        .container {{
            max-width: 800px;
            margin: 3rem auto;
            padding: 0 1rem;
        }}
        .card {{
            background-color: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 6px;
            padding: 2rem;
        }}
        h1 {{ color: #ffffff; }}
        a {{ color: var(--accent); text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .back {{ margin-bottom: 1rem; display: inline-block; }}
    </style>
</head>
<body>
    <div class="container">
        <a class="back" href="../index.html">&larr; Back to Home</a>
        <div class="card">
            <h1>{topic['title']}</h1>
            <p><em>Published on {date_str} by SoloAgentic Autonomous Engine</em></p>
            <hr style="border:0; border-top:1px solid var(--border); margin: 1.5rem 0;">
            <p>{topic['content']}</p>
            <h3>Execution Blueprint</h3>
            <p>1. Define your repetitive trigger event.<br>
               2. Write a lightweight Python script or prompt sequence.<br>
               3. Schedule via background cron or agentic runtime.<br>
               4. Review outputs weekly.</p>
            <p>Stay tuned for our next automated briefing update.</p>
        </div>
    </div>
</body>
</html>
"""
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"[SUCCESS] Yeni otonom makale oluşturuldu: {filepath}")
    return topic, filename, date_str

def update_index(topic, filename, date_str):
    index_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_link = f'<li><a href="posts/{filename}">{topic["title"]} ({date_str})</a></li>'
    
    if new_link not in content:
        content = content.replace("<ul>", f"<ul>\n                {new_link}")
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("[SUCCESS] index.html güncellendi!")

if __name__ == "__main__":
    top, fn, dt = generate_new_post()
    update_index(top, fn, dt)
