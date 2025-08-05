import os
import shutil

reports_dir = "reports"


if not os.path.exists(reports_dir):
    os.mkdir(reports_dir)
    print(f"Directory '{reports_dir}' created.")
else:
    print(f"Directory '{reports_dir}' already exists.")

txt_files = [f for f in os.listdir() if f.endswith(".txt") and os.path.isfile(f)]

for txt_file in txt_files:
    print(f"Moving file: {txt_file}")
    shutil.move(txt_file, os.path.join(reports_dir, txt_file))
