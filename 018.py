with open("hightemp.txt", "r") as f:
    raw_text = f.readlines()

lines_list = [line.split("\t") for line in raw_text]
sorted_list = sorted(lines_list, key=lambda x: x[2], reverse=True)
[print("\t".join(i), end="") for i in sorted_list]