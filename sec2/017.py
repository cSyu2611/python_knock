if __name__ == "__main__":
    with open("hightemp.txt","r") as f:
        lines_list = f.readlines()
    print({line.split("\t")[0] for line in lines_list})