import re

if __name__ == "__main__":
    with open("020.txt","r") as f:
        lines_list = f.readlines()
    [print(line.strip("[[Category:")[0:-3]+"\n", end="") for line in lines_list if "[[Category:" in line]
        # print(re.match(r"[[]{2}Category:(\.*)[[]{2}",line), end="")