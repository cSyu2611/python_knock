import re

if __name__ == "__main__":
    with open("025.txt", "r") as f, open("026.txt", "w") as rslt:
        raw_text = f.read()
        result = re.sub("\'{1,}","",raw_text)
        rslt.write(result)