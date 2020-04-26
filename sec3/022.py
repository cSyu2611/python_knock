import re

if __name__ == "__main__":
    with open("020.txt","r") as f:
        lines_list = f.readlines()
    [print(re.findall("\[{2,}Category:(.+?)\]{2,}", line)[0]) for line in lines_list if re.findall("\[\[Category:(.+?)\]\]", line)]