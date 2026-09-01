#!/usr/bin/env python3
"""fix_docx_fonts.py — política tipográfica da edição unificada (equivalente --fix-fonts do word_guard):
corpo/títulos em Times New Roman; headings nível 1-2 em preto. stdlib puro (zipfile+re)."""
import re, shutil, sys, zipfile

path = sys.argv[1]
tmp = path + ".tmp"
with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
    for item in zin.namelist():
        data = zin.read(item)
        if item == "word/styles.xml":
            s = data.decode("utf-8")
            s = re.sub(r'w:ascii="[^"]*" w:hAnsi="[^"]*"', 'w:ascii="Times New Roman" w:hAnsi="Times New Roman"', s)
            s = re.sub(r'w:cs="[^"]*" w:eastAsia="[^"]*"', 'w:cs="Times New Roman" w:eastAsia="Times New Roman"', s)
            s = re.sub(r'w:color w:val="0F4761"', 'w:color w:val="000000"', s)
            s = re.sub(r'w:color w:val="2E74B5"', 'w:color w:val="000000"', s)
            data = s.encode("utf-8")
        elif item == "word/theme/theme1.xml":
            s = data.decode("utf-8")
            s = re.sub(r'<a:latin typeface="[^"]*"', '<a:latin typeface="Times New Roman"', s)
            data = s.encode("utf-8")
        zout.writestr(item, data)
shutil.move(tmp, path)
print("fix_docx_fonts ✓", path)
