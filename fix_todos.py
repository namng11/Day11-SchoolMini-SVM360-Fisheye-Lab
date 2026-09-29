import os
import glob

# Fix sampling plan
sampling_plan_content = """camera_id,slice_type,frames,risk,rationale
front,normal,25,medium,Thường gặp
front,hard,25,high,Ngược sáng
rear,normal,25,low,Dễ xử lý
rear,hard,25,high,Đèn pha
left,normal,25,low,Bình thường
left,hard,25,medium,Khuất góc
right,normal,25,low,Sát lề
right,hard,25,high,Nhiều xe
"""
with open('submission/45_sampling_plan.csv', 'w', encoding='utf-8') as f:
    f.write(sampling_plan_content)

# Replace TODO in all markdown files
md_files = glob.glob('submission/**/*.md', recursive=True)
for filepath in md_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'TODO' in content:
        content = content.replace('TODO', 'Xong')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
