"""
tools/convert_html_to_md.py
Parses Unity documentation HTML files, extracts the core content, 
and converts them into clean Markdown files for RAG.
"""

import os
import sys
import glob
import argparse
from bs4 import BeautifulSoup
from markdownify import markdownify as md

def process_html_file(html_path, source_dir, target_dir):
    # Determine target path
    rel_path = os.path.relpath(html_path, source_dir)
    md_rel_path = os.path.splitext(rel_path)[0] + ".md"
    target_path = os.path.join(target_dir, md_rel_path)
    
    # Skip if already exists
    if os.path.exists(target_path):
        return True
        
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            
        soup = BeautifulSoup(html_content, "html.parser")
        
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
    parser = argparse.ArgumentParser(description="Convert HTML docs to Markdown")
    parser.add_argument("source_dir", help="Path to the source HTML directory")
    parser.add_argument("target_dir", help="Path to the target Markdown directory")
    args = parser.parse_args()

    source_dir = os.path.abspath(args.source_dir)
    target_dir = os.path.abspath(args.target_dir)

    print(f"Scanning for HTML files in {source_dir}...")
    html_files = glob.glob(os.path.join(source_dir, "**", "*.html"), recursive=True)
    total_files = len(html_files)
    
    if total_files == 0:
        print("No HTML files found.")
        return
        
    print(f"Found {total_files} HTML files. Starting conversion to Markdown in {target_dir}...")
    
    success_count = 0
    for i, file_path in enumerate(html_files):
        if process_html_file(file_path, source_dir, target_dir):
            success_count += 1
            
        if (i + 1) % 500 == 0:
            print(f"Progress: {i + 1}/{total_files} files converted...")
            
    print(f"Done! Successfully converted {success_count} files to {target_dir}")

if __name__ == "__main__":
    main()
