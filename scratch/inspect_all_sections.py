import os
import re

dir_path = r"c:\Users\nexus\OneDrive\Documentos\ProyectosWeb\avpcelespinar\avpcelespinar-template"
files = [f for f in os.listdir(dir_path) if f.endswith(".html")]

output_lines = []

for f_name in sorted(files):
    f_path = os.path.join(dir_path, f_name)
    with open(f_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We want to find all <section ...> tags
    sections = re.findall(r"<section\b[^>]*>", content, re.IGNORECASE)
    output_lines.append(f"=== {f_name} ({len(sections)} sections) ===")
    for idx, sec in enumerate(sections, 1):
        output_lines.append(f"  Section {idx}: {sec}")
    output_lines.append("")

with open("scratch/all_sections_classes.txt", "w", encoding="utf-8") as f_out:
    f_out.write("\n".join(output_lines))

print("Done! Written to scratch/all_sections_classes.txt")
