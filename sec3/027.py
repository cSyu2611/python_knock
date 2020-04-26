import re

if __name__ == "__main__":
    with open("026.txt", "r") as f, open("027.txt", "w") as rslt:
        raw_text = f.read()
        result = re.sub("[\[\]]","",raw_text)
        rslt.write(result)