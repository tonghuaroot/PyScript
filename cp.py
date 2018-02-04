import sys

source_file = sys.argv[1] # 源文件
dst_file = sys.argv[2] # 目标文件
with open(source_file, mode="rb") as f1,\
    open(dst_file, mode="wb") as f2:
    #data = f1.read()
    #f2.write(data)

    for data in f1:
        f2.write(data)
