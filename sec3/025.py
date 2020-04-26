import re

if __name__ == "__main__":
    with open("020.txt","r") as f:
        lines_list = f.readlines()

    #基礎情報テンプレート部のみ抽出しリスト化
    loop_state = "wait"
    basic_info_list = []
    for line in lines_list:
        if loop_state != "start" and re.findall("\{{2}基礎情報.+?$",line):
            loop_state = "start"
        elif loop_state == "start" and re.findall("^\}{2}$",line):
            break
        elif loop_state == "start":
            basic_info_list.append(line)

    #基礎情報テンプレートに対してフィールド名とバリューの抽出
    current_field = ""
    basic_info_dict = {}
    for line in basic_info_list:
        if re.findall("^\|.+?",line):
            current_field, value = re.findall("^\|(.+?)\s=\s(.+?)$",line)[0]
            basic_info_dict[current_field] = value
        else:
            basic_info_dict[current_field] += re.findall("^\*{1,}(.+?)$",line)[0]
    ans = "\n".join(["{}:{}".format(mykey, basic_info_dict[mykey]) for mykey in basic_info_dict.keys()])
    with open("025.txt", "w") as f:
        f.write(ans)



