import os
import re

dir_path = r"c:\Users\nexus\OneDrive\Documentos\ProyectosWeb\avpcelespinar\avpcelespinar-template"
files = [f for f in os.listdir(dir_path) if f.endswith(".html")]

for f_name in sorted(files):
    f_path = os.path.join(dir_path, f_name)
    with open(f_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # search for classes like h-[...]
    height_classes = re.findall(r"h-\[\d+px\]", content)
    if height_classes:
        print(f"{f_name}: {height_classes}")
