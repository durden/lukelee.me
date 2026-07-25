import glob
import os
import re
from datetime import datetime

SRC_DIR = "/Users/durden/Documents/code/syte/syte/articles"
DEST_DIR = "/Users/durden/Documents/code/blog_2026/docs/articles"

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text

def migrate():
    os.makedirs(DEST_DIR, exist_ok=True)
    articles = glob.glob(os.path.join(SRC_DIR, "*.md"))
    print(f"Found {len(articles)} articles to migrate.")

    converted_count = 0

    for filepath in sorted(articles):
        filename = os.path.basename(filepath)
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()

        if len(lines) < 3:
            print(f"Skipping {filename}: less than 3 lines")
            continue

        raw_date = lines[0].strip()
        raw_title = lines[1].strip()
        raw_category = lines[2].strip()

        # Parse date
        dt = None
        for fmt in ('%m-%d-%Y %H:%M:%S', '%m-%d-%Y'):
            try:
                dt = datetime.strptime(raw_date, fmt)
                break
            except ValueError:
                pass

        if dt:
            date_str = dt.strftime('%Y-%m-%d')
        else:
            date_str = raw_date

        category_slug = slugify(raw_category)
        target_dir = os.path.join(DEST_DIR, category_slug)
        os.makedirs(target_dir, exist_ok=True)

        target_file = os.path.join(target_dir, filename)

        # Body lines starting from line index 3
        body_lines = lines[3:]
        # Remove empty leading lines before body
        while body_lines and not body_lines[0].strip():
            body_lines.pop(0)

        body_content = "".join(body_lines)

        # Escape quotes in title if present
        title_escaped = raw_title.replace('"', '\\"')

        frontmatter = f"""---
title: "{title_escaped}"
date: {date_str}
categories:
  - {raw_category}
---

"""
        new_content = frontmatter + body_content

        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        converted_count += 1

    print(f"Successfully migrated {converted_count} articles to {DEST_DIR}.")

if __name__ == "__main__":
    migrate()
