import glob
import os
from datetime import datetime

SRC_DIR = "/Users/durden/Documents/code/blog_2026/docs/articles"

categories_map = {
    "programming-articles": "Programming Articles",
    "web-development": "Web Development",
    "talks": "Talks"
}

index_content = """---
icon: lucide/book-open
---

# Welcome to the Tech & Software Engineering Blog

This blog features 119 articles covering Python development, software engineering patterns, memory profiling, and conference talks.

## Categories

"""

for cat_slug, cat_title in categories_map.items():
    cat_dir = os.path.join(SRC_DIR, cat_slug)
    if not os.path.exists(cat_dir):
        continue
    
    files = glob.glob(os.path.join(cat_dir, "*.md"))
    articles = []
    
    for fpath in files:
        fname = os.path.basename(fpath)
        rel_path = f"articles/{cat_slug}/{fname}"
        
        with open(fpath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        title = fname
        date_str = ""
        for line in lines:
            if line.startswith("title:"):
                title = line.replace("title:", "").strip().strip('"')
            elif line.startswith("date:"):
                date_str = line.replace("date:", "").strip()
            elif line.strip() == "---" and date_str:
                break
                
        articles.append((date_str, title, rel_path))
    
    # Sort by date descending
    articles.sort(key=lambda x: x[0], reverse=True)
    
    index_content += f"### {cat_title} ({len(articles)})\n\n"
    for date_str, title, rel_path in articles:
        index_content += f"- **{date_str}** - [{title}]({rel_path})\n"
    index_content += "\n"

with open("/Users/durden/Documents/code/blog_2026/docs/index.md", "w", encoding="utf-8") as f:
    f.write(index_content)

print("Updated docs/index.md successfully!")
