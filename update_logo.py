#!/usr/bin/env python3
import os
import re

# Base directory
base_dir = "/Users/briansmith/Urban-Design"

# Files to update
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

# Pattern to find and replace
old_pattern = r'<a href="/" class="logo">Urban Design & <span>Remodel</span></a>'

def get_logo_path(file_path):
    """Determine the correct relative path to the logo based on file depth"""
    depth = file_path.count('/')
    if depth == 1:
        return "../images/logo.png"
    elif depth == 2:
        return "../../images/logo.png"
    else:
        return "images/logo.png"

# Update each file
for file_path in files_to_update:
    full_path = os.path.join(base_dir, file_path)
    if os.path.exists(full_path):
        logo_path = get_logo_path(file_path)
        new_logo = f'''<a href="/" class="logo">
                <img src="{logo_path}" alt="Urban Design & Remodel" style="height: 50px; width: auto;">
            </a>'''
        
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the logo
        updated_content = re.sub(old_pattern, new_logo, content)
        
        if content != updated_content:
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"✓ Updated: {file_path}")
        else:
            print(f"- Skipped (no match): {file_path}")
    else:
        print(f"✗ Not found: {file_path}")

print("\nLogo update complete!")
