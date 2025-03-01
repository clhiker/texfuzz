import re

import PyPDF2

info_list = ["Greek Letters", "Symbols of Type Ord", "Large OperatorsP",
             "Binary Operations", "Page Layout", "Relations",
             "Arrows", "Delimiters", "Every Time Insertions",
             "Accents", "Elementary Math Control Sequences", "Non-Italic Function Names",
             "Footnotes, Insertions, and Underlines", "Useful Parameters and Conversions",
             "Fills, Leaders and Ellipses", "TEX Fonts and Magnification",
             "Alignment Displays", "Boxes", "Overfull Boxes", "Indentation and Itemized Lists",
             "Headers, Footers, and Page Numbers", "Macro Definitions", "Advanced Macro Definition Commands",
             "Conditionals", "Dimensions, Spacing, and Glue", "Braces and Matrices", "Displayed Equations"]
info_dict = {}
# 打开PDF文件
with open('TeXRefCard.v1.5.pdf', 'rb') as file:
    # 创建一个PDF阅读器对象
    reader = PyPDF2.PdfReader(file)

    # 获取PDF的页数
    num_pages = len(reader.pages)

    # 逐页读取内容
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text = page.extract_text()
        # print(f"Page {page_num + 1}:\n{text}\n")
        lines = text.split('\n')
        # for i in range(len(lines)):
        i=0
        while i < len(lines):
            if lines[i] in info_list:
                key = lines[i]
                info_dict[key] = []
                i += 1
                while i < len(lines) and lines[i] not in info_list:
                    matches = re.findall(r'\\\w+(?=\s|$)', lines[i])
                    info_dict[key].extend(matches)
                    i += 1
                i -= 1
            i+=1

for key in info_dict.keys():
    print(f"{key}: {info_dict[key]}")
# for item in info_list:
#     if item not in info_dict:
#         print(item)

# Relations
# Accents
# TEX Fonts and Magnification
# Indentation and Itemized Lists
# Macro Definitions
# Advanced Macro Definition Commands
# Dimensions, Spacing, and Glue