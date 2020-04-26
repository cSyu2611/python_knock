import re

if __name__ == "__main__":
    with open("020.txt","r") as f:
        lines_list = f.readlines()
    matched_list = [re.findall("(={2,})(.+?)(={2,})",line)[0] for line in lines_list if re.findall("(={2,})(.+?)(={2,})",line)]
    [print("セクション名: {}, レベル: {}".format(x[1],len(x[0])-1)) if x[0]==x[2] else print("始端と終端の=の数が違う") for x in matched_list]
