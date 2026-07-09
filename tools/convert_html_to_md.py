"""
tools/convert_html_to_md.py
Parses Unity documentation HTML files, extracts the core content, 
and converts them into clean Markdown files for RAG.
"""

import os
import sys
import glob
from bs4 import BeautifulSoup
from markdownify import markdownify as md

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_DIR = os.path.join(project_root, "Unity_6_3_Archive")
TARGET_DIR = os.path.join(project_root, "Unity_6_3_Markdown")

def process_html_file(html_path):
    # Determine target path
    rel_path = os.path.relpath(html_path, SOURCE_DIR)
    md_rel_path = os.path.splitext(rel_path)[0] + ".md"
    target_path = os.path.join(TARGET_DIR, md_rel_path)
    
    # Skip if already exists
    if os.path.exists(target_path):
        return True
        
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            
        soup = BeautifulSoup(html_content, "html.parser")
        
        # Unity docs usually store the main text in <div class="content"> or <div class="section">
        # Let's try to find <div id="content-wrap"> -> <div class="content">
        main_content = None
        
        # Attempt 1: Standard Unity Docs format
        content_wrap = soup.find("div", id="content-wrap")
        if content_wrap:
            main_content = content_wrap.find("div", class_="content")
            
        # Attempt 2: Fallback to <main> or <article> if different format
        if not main_content:
            main_content = soup.find("main") or soup.find("article")
            
        # Attempt 3: Fallback to the whole body if we can't find specific sections
        if not main_content:
            main_content = soup.find("body") or soup
            
        # Convert to markdown
        md_text = md(str(main_content), heading_style="ATX", escape_asterisks=False)
        
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(md_text.strip())
            
        return True
    except Exception as e:
        print(f"Error processing {html_path}: {e}")
        return False

def main():
    print(f"Scanning for HTML files in {SOURCE_DIR}...")
    html_files = glob.glob(os.path.join(SOURCE_DIR, "**", "*.html"), recursive=True)
    total_files = len(html_files)
    
    print(f"Found {total_files} HTML files. Starting conversion to Markdown in {TARGET_DIR}...")
    
    # Optional: Since 39k files take a while, we'll print progress
    success_count = 0
    for i, file_path in enumerate(html_files):
        if process_html_file(file_path):
            success_count += 1
            
        if (i + 1) % 500 == 0:
            print(f"Progress: {i + 1}/{total_files} files converted...")
            
    print(f"Done! Successfully converted {success_count} files to {TARGET_DIR}")

if __name__ == "__main__":
    main()
