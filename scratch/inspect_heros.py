import os
import re

dir_path = r"c:\Users\nexus\OneDrive\Documentos\ProyectosWeb\avpcelespinar\avpcelespinar-template"
files = [f for f in os.listdir(dir_path) if f.endswith(".html")]

print(f"Found {len(files)} HTML files.")

for f_name in sorted(files):
    if f_name == "index.html":
        continue
    f_path = os.path.join(dir_path, f_name)
    with open(f_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Let's find everything from <body> to <main> or the first 50 lines after <body>
    body_match = re.search(r"<body[^>]*>(.*?)<main[^>]*>", content, re.DOTALL | re.IGNORECASE)
    if body_match:
        section_content = body_match.group(1).strip()
        # Find all sections or headers in this block
        first_section = re.search(r"<(section|header|div)[^>]*class=\"[^\"]*h-\[[^\"]*\"[^>]*>.*?</\1>", section_content, re.DOTALL | re.IGNORECASE)
        print(f"\n--- {f_name} (Inside body before main) ---")
        lines = section_content.splitlines()[:15]
        for line in lines:
            print(line)
    else:
        # Just show the first 20 lines after <body>
        body_start = content.find("<body")
        if body_start != -1:
            print(f"\n--- {f_name} (Body start) ---")
            print(content[body_start:body_start+800])
