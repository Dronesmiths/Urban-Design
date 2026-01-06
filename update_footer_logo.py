#!/usr/bin/env python3
import os
import re

# Base directory
base_dir = "/Users/briansmith/Urban-Design"

# Files to update (all pages except index.html which is already done)
files_to_update = [
    "contact/index.html",
    "about/index.html",
    "locations/south-jordan/index.html",
    "locations/herriman/index.html",
    "locations/riverton/index.html",
    "locations/draper/index.html",
    "locations/sandy/index.html",
    "locations/west-jordan/index.html",
    "services/accessible-bathroom-walk-ins/index.html",
    "services/index.html",
    "services/luxury-bathroom-renovation/index.html",
    "services/flooring-installation/index.html",
    "services/basement-finishing/index.html",
    "services/kitchen-remodeling/index.html",
    "services/custom-cabinetry/index.html"
]

def get_logo_path(file_path):
    """Determine the correct relative path to the logo based on file depth"""
    depth = file_path.count('/')
    if depth == 1:
        return "../images/logo.png"
    elif depth == 2:
        return "../../images/logo.png"
    else:
        return "images/logo.png"

# Pattern to find and replace the footer brand
pattern = r'<div class="aw-footer-brand">\s*<h3>Urban Design & <span>Remodel</span></h3>'

# Update each file
for file_path in files_to_update:
    full_path = os.path.join(base_dir, file_path)
    if os.path.exists(full_path):
        logo_path = get_logo_path(file_path)
        
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already updated
        if 'aw-footer-brand' in content and '<img src=' in content and 'logo.png' in content:
            # Check if it's in the footer brand section
            if re.search(r'<div class="aw-footer-brand">[\s\S]*?<img src=".*?logo\.png"', content):
                print(f"⊙ Already updated: {file_path}")
                continue
        
        # Create the replacement
        replacement = f'''<div class="aw-footer-brand">
                <img src="{logo_path}" alt="Urban Design & Remodel" style="height: 60px; width: auto; margin-bottom: 15px;">
                <h3 style="display: none;">Urban Design & <span>Remodel</span></h3>'''
        
        # Replace the pattern
        updated_content = re.sub(pattern, replacement, content)
        
        if content != updated_content:
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"✓ Updated: {file_path}")
        else:
            print(f"- No match found: {file_path}")
    else:
        print(f"✗ Not found: {file_path}")

print("\nFooter logo update complete!")
