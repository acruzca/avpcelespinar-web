import os
import re

dir_path = r"c:\Users\nexus\OneDrive\Documentos\ProyectosWeb\avpcelespinar\avpcelespinar-template"
files = [f for f in os.listdir(dir_path) if f.endswith(".html")]

output_lines = []

for f_name in sorted(files):
    if f_name == "index.html":
        continue
    f_path = os.path.join(dir_path, f_name)
    with open(f_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Let's find </header>
    header_end = content.find("</header>")
    if header_end != -1:
        after_header = content[header_end + len("</header>"):]
        # Find first container inside main, or first container after </header>
        # Let's check if there is a hero section that has a height or class or standard structure
        # We can search for the first tag after </header>
        match = re.search(r"<(section|header|div)[^>]*>", after_header, re.IGNORECASE)
        if match:
            tag_start = match.start()
            snippet = after_header[tag_start:tag_start+800].strip()
            output_lines.append(f"=== FILE: {f_name} ===")
            output_lines.append(snippet)
            output_lines.append("\n" + "="*50 + "\n")
        else:
            output_lines.append(f"=== FILE: {f_name} (No tags after </header>) ===")
    else:
        output_lines.append(f"=== FILE: {f_name} (No </header> found) ===")

with open("scratch/all_heroes_details.txt", "w", encoding="utf-8") as f_out:
    f_out.write("\n".join(output_lines))

print("Done! Output written to scratch/all_heroes_details.txt")
