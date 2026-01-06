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

# Pattern to find header logo and add inline style
# Matches <a href="/" class="logo">\n (whitespace) <img ...>
pattern = r'(<a href="/" class="logo">\s*<img src="[^"]*logo\.png" alt="Urban Design & Remodel")(\s*>)'
replacement = r'\1 style="height: 50px; width: auto;"\2'

# Update each file
for file_path in files_to_update:
    full_path = os.path.join(base_dir, file_path)
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply replacement
        # We only want to target the one inside the header link
        if 'class="logo"' in content:
            updated_content = re.sub(pattern, replacement, content)
            
            # Check if it was already updated to avoid duplication or if style is already there
            if 'style="height: 50px; width: auto;"' in updated_content and content != updated_content:
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"✓ Fixed header logo in: {file_path}")
            elif 'style="height: 50px;' in content:
                 print(f"- Already has style: {file_path}")
            else:
                 # Try a more loose pattern if the exact one failed
                 alt_pattern = r'(<a href="/" class="logo">\s*<img src="[^"]*")'
                 updated_content = re.sub(alt_pattern, r'\1 style="height: 50px; width: auto;"', content)
                 if content != updated_content:
                    with open(full_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    print(f"✓ Fixed header logo (alt match) in: {file_path}")
                 else:
                    print(f"- No match found in: {file_path}")
        else:
             print(f"- No logo class found in: {file_path}")
    else:
        print(f"✗ Not found: {file_path}")

print("\nHeader logo fix complete!")
