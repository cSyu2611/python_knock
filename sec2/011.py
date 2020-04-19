if __name__ == "__main__":
    with open("hightemp.txt", "r") as f:
        raw_text= f.read()
    print("".join(raw_text).replace("\t"," "))