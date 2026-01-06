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

# Pattern to find and replace - remove inline styles from footer logo
pattern = r'(<img src="[^"]*logo\.png" alt="Urban Design & Remodel")(\s+style="[^"]*")?(\s*/?>)'

# Update each file
for file_path in files_to_update:
    full_path = os.path.join(base_dir, file_path)
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Remove inline styles from footer logo
        updated_content = re.sub(pattern, r'\1>', content)
        
        if content != updated_content:
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"✓ Updated: {file_path}")
        else:
            print(f"- No changes needed: {file_path}")
    else:
        print(f"✗ Not found: {file_path}")

print("\nFooter logo style cleanup complete!")
