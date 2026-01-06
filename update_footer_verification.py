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

# Pattern 1: Add Google Business Profile link after the footer email
pattern1 = r'(<p class="aw-footer-email">[\s\S]*?</p>)'
replacement1 = r'''\1
                <p style="margin-top: 10px; font-size: 0.9rem;">
                    <a href="https://www.google.com/maps/search/?api=1&query=Urban+Design+%26+Remodel+West+Jordan+UT" target="_blank" rel="noopener" style="color: var(--text-light); text-decoration: none;">Google Business Profile</a>
                </p>'''

# Pattern 2: Add license verification in footer bottom
pattern2 = r'(<div class="aw-footer-bottom">[\s\S]*?</p>)\s*(</div>)'
replacement2 = r'''\1
            <p style="margin-top: 8px; font-size: 0.85rem; opacity: 0.8;">
                Utah Contractor License #10146123-5501 | Verified through the <a href="https://secure.utah.gov/llv/search/index.html" target="_blank" rel="nofollow noopener" style="color: inherit; text-decoration: underline;">Utah Division of Professional Licensing</a>
            </p>
        \2'''

# Update each file
for file_path in files_to_update:
    full_path = os.path.join(base_dir, file_path)
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Check if already updated
        if 'Google Business Profile' in content and 'Utah Contractor License #10146123-5501' in content:
            print(f"⊙ Already updated: {file_path}")
            continue
        
        # Apply pattern 1 (Google Business Profile)
        if 'Google Business Profile' not in content:
            content = re.sub(pattern1, replacement1, content)
        
        # Apply pattern 2 (License verification)
        if 'Utah Contractor License #10146123-5501' not in content:
            content = re.sub(pattern2, replacement2, content)
        
        if content != original_content:
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Updated: {file_path}")
        else:
            print(f"- No changes: {file_path}")
    else:
        print(f"✗ Not found: {file_path}")

print("\nFooter verification update complete!")
