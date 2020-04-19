if __name__ == "__main__":
    with open("hightemp.txt","r") as f:
        lines_list = f.readlines()
    column1_list = [line.split("\t")[0] for line in lines_list]
    column1_set = {line.split("\t")[0] for line in lines_list}
    column1_num_dict = {column : column1_list.count(column) for column in column1_set}
    [print("{}の出現頻度:{}".format(i[0],i[1])) for i in sorted(column1_num_dict.items(), key=lambda x: x[1], reverse=True)]