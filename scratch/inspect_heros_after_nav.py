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
    
    # Find </header> of the menu (the first one)
    header_end = content.find("</header>")
    if header_end != -1:
        after_header = content[header_end + len("</header>"):]
        # Find the first tag that opens a block - usually <section> or <header> or <div class="relative bg-primary...">
        match = re.search(r"<(section|header|div)[^>]*>", after_header, re.IGNORECASE)
        if match:
            tag_start = match.start()
            # print the first 400 chars starting from this tag
            print(f"\n=================== {f_name} ===================")
            print(after_header[tag_start:tag_start+600].strip())
            print("==================================================")
        else:
            print(f"\n!!! No section tag found after </header> in {f_name}")
    else:
        print(f"\n!!! No </header> found in {f_name}")
