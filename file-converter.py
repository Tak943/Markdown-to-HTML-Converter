import markdown
import sys

if len(sys.argv) != 4:
    print("正しい引数を入力してください")
    print("引数の形:")
    print("python3 file-converter.py markdown 入力ファイル 出力先ファイル")
    sys.exit(1)

inputpath = sys.argv[2]
outputpath = sys.argv[3]

with open(inputpath, "r", encoding="utf-8") as f:
    md_text = ""
    while True:
        line = f.readline()
        if line == "":
            break
        md_text += line


with open(outputpath, "w", encoding="utf-8") as f:
    md = markdown.Markdown()
    f.write(md.convert(md_text))