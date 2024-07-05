from pdfminer.high_level import extract_text
from pathlib import Path
import os

source = Path("Hello.pdf")
text = extract_text(source)
lines = text.split("\n")
# 空行や不要な空白を除外し、トリムした後に再度空要素を除外
filtered_lines = [line.strip() for line in lines if line.strip()]

print(filtered_lines)
for line in filtered_lines:
    if line == "Hello":
        print("ok")#    os.rename("Hello.pdf", "jjj.pdf")

