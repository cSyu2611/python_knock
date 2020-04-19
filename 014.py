import sys

if __name__ == "__main__":
    if(len(sys.argv)==3):
        filename, N = sys.argv[1], int(sys.argv[2])
        with open(filename, "r") as f:
            lines_list = f.readlines()
        print("".join(lines_list[0:N]), end="")
    else:
        print("引数が足りてネェ！！")
        print("python 014.py 開くファイル名 表示したい行数")