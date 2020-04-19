import re

if __name__ == "__main__":
    with open("020.txt","r") as f:
        lines_list = f.readlines()
    [print(re.findall("={2}(.*)={2}",line)) for line in lines_list if re.findall("={2}(.*)={2}",line)]