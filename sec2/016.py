import sys, math

if __name__ == "__main__":
    if(len(sys.argv)==3):
        filename, N = sys.argv[1], int(sys.argv[2])
        with open(filename, "r") as f:
            lines_list = f.readlines()
        [print("".join(lines_list[i:i+N])+"\n\n") for i in range(0,len(lines_list),N)]
        
    else:
        print("引数が足りてネェ！！")
        print("python 016.py 開くファイル名 分割行数")