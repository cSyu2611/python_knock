import json

if __name__ == "__main__":
    with open("jawiki-country.json","r", encoding="utf-8") as f:
        for line in f:
            tmp = json.loads(line)
            if tmp["title"]=="イギリス":
                text = json.loads(line)["text"]
                print(text)

    with open("020.txt","w") as tf:
        tf.write(text)