import sys

if __name__ == "__main__":
    if(len(sys.argv)==3):
        filename, N = sys.argv[1], int(sys.argv[2])
        with open(filename, "r") as f:
            lines_list = f.readlines()
        print("".join(lines_list[-N:]), end="")
    else:
        print("引数が足りてネェ！！")
        print("python 015.py 開くファイル名 末尾から表示したい行数")