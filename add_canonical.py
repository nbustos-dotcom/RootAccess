import os
import re

# Base URL for your site
BASE_URL = "https://nbustos-dotcom.github.io/RootAccess"

# Directory containing your HTML files — change this if needed
HTML_DIR = os.path.dirname(os.path.abspath(__file__))

files_updated = 0
files_skipped = 0

for filename in os.listdir(HTML_DIR):
    if not filename.endswith(".html"):
        continue

    filepath = os.path.join(HTML_DIR, filename)

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if canonical tag already exists
    if 'rel="canonical"' in content:
        print(f"SKIPPED (already has canonical): {filename}")
        files_skipped += 1
        continue

    # Build the canonical URL for this file
    if filename == "index.html":
        canonical_url = f"{BASE_URL}/"
    else:
        canonical_url = f"{BASE_URL}/{filename}"

    canonical_tag = f'  <link rel="canonical" href="{canonical_url}" />\n'

    # Insert after <head> tag
    new_content = re.sub(r'(<head>)', r'\1\n' + canonical_tag, content, count=1)

    if new_content == content:
        print(f"WARNING - could not find <head> in: {filename}")
        continue

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"UPDATED: {filename} → {canonical_url}")
    files_updated += 1

print(f"\nDone! {files_updated} files updated, {files_skipped} files skipped.")
