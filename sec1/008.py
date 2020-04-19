def cipher(string):
    return "".join([chr(219-ord(i)) if i.islower() else i for i in list(string)])

if __name__ == "__main__":
    print(cipher("ogasawara"))
    print(cipher(cipher("ogasawara")))