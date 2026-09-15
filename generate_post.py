import os
import datetime

# Otonom İçerik Üretici - SoloAgentic Hub
# Bu script, solopreneur ve AI ajanları nişinde otonom makaleler üretir ve siteye ekler.

OUTPUT_DIR = "C:/Users/zafer/solopreneur-ai-hub"
POSTS_DIR = os.path.join(OUTPUT_DIR, "posts")

os.makedirs(POSTS_DIR, exist_ok=True)

def generate_article():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    title = f"Autonomous AI Workflows for Solopreneurs: Daily Briefing ({today})"
    filename = f"workflow-briefing-{today}.html"
    filepath = os.path.join(POSTS_DIR, filename)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | SoloAgentic</title>
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
            <h1>{title}</h1>
            <p><em>Published on {today} by SoloAgentic Autonomous Engine</em></p>
            <hr style="border:0; border-top:1px solid var(--border); margin: 1.5rem 0;">
            <p>As the solopreneur economy accelerates in 2026, leveraging autonomous agent stacks has moved from a competitive edge to a baseline requirement. Solo founders are now orchestrating background pipelines that handle everything from multi-source research to automated content and code deployment.</p>
            <h3>Key Takeaway of the Day</h3>
            <p>Instead of doing manual repetitive tasks, structure your workflows into modular agent scripts running via local cron jobs or background terminal sessions. This guarantees zero human friction and maximum operational leverage.</p>
            <p>Stay tuned for our next automated briefing update.</p>
        </div>
    </div>
</body>
</html>
"""
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"[SUCCESS] Otonom içerik üretildi: {filepath}")

if __name__ == "__main__":
    generate_article()
