import re

if __name__ == "__main__":
    with open("020.txt","r") as f:
        lines_list = f.readlines()
    matched_list = [re.findall("\[{2,}(ファイル:|File:)(.+?)\|",line)[0] for line in lines_list if re.findall("\[{2,}(ファイル:|File:)(.+?)\|",line)]
    [print("{}".format(x[1])) for x in matched_list]
    print("結局どっからどこまでファイル名やねん")
