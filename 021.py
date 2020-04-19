if __name__ == "__main__":
    with open("020.txt","r") as f:
        lines_list = f.readlines()
    [print(line, end="") for line in lines_list if "[[Category:" in line]