if __name__ == "__main__":
    with open("col1.txt","r") as col1, open("col2.txt","r") as col2, open("013.txt","w") as f:
        col1_lines_list, col2_lines_list = col1.readlines(), col2.readlines()
        text_013 = "".join([col1_line.strip("\n")+"\t"+col2_line for col1_line, col2_line in zip(col1_lines_list, col2_lines_list)])
        f.write(text_013)