if __name__ == "__main__":
    with open("hightemp.txt", "r") as f, open("col1.txt","w") as col1, open("col2.txt","w") as col2:
        lines_list = f.readlines()
        col1_text, col2_text = "\n".join([line.split("\t")[0] for line in lines_list]), "\n".join([line.split("\t")[1] for line in lines_list])
        col1.write(col1_text)
        col2.write(col2_text)
