import glob
import os
import re
import textwrap

def detect_language(code_text):
    code = code_text.strip()
    
    # JSON
    if (code.startswith('{') and code.endswith('}')) or (code.startswith('[') and code.endswith(']')):
        if '"' in code and ':' in code:
            return 'json'
    
    # HTML / XML
    if re.search(r'</[a-zA-Z0-9]+>', code) or code.startswith('<?xml') or code.startswith('<ul') or code.startswith('<div'):
        return 'html'
    
    # Shell / Terminal output
    if code.startswith('$ ') or code.startswith('>>> ') or 'Traceback (most recent call last)' in code or '== ERROR:' in code or 'Function Performance' in code:
        if code.startswith('>>> '):
            return 'python'
        return 'text'
        
    # JavaScript
    if 'Handlebars' in code or 'function(' in code or 'const ' in code or 'var ' in code:
        return 'javascript'

    # Python indicators
    py_keywords = ['def ', 'class ', 'import ', 'from ', 'self.', 'return ', 'try:', 'except ', 'assert', 'raise ', 'elif ', 'print ', 'lambda ', '@', 'if ']
    for kw in py_keywords:
        if kw in code:
            return 'python'
            
    # Default to python if it looks like code
    return 'python'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Pattern to match <pre><code>...</code></pre> or <pre>...</pre>
    def replace_pre(match):
        inner = match.group(1)

        lang = detect_language(inner)
        if lang == 'python':
            inner = textwrap.dedent(inner)

        # strip inner <code> tags if present
        inner = re.sub(r'^<code>|</code>$', '', inner.strip(), flags=re.IGNORECASE)
        
        # Unescape HTML entities inside code
        inner = inner.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&quot;', '"')
        
        return f"\n\n```{lang}\n{inner}\n```\n\n"

    # Match <pre ...> ... </pre>
    new_content = re.sub(r'<pre[^>]*>(.*?)</pre>', replace_pre, content, flags=re.DOTALL | re.IGNORECASE)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    articles = glob.glob('/Users/durden/Documents/code/blog_2026/docs/articles/**/*.md', recursive=True)
    updated = 0
    for p in sorted(articles):
        if process_file(p):
            updated += 1

    print(f"Updated code blocks in {updated} articles.")

if __name__ == '__main__':
    main()
