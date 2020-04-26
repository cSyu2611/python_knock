import re

if __name__ == "__main__":
    str_003 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    #method 1
    print("".join([str(len(j)) for j in [i.strip(", .") for i in str_003.split()]]))
    #method 2
    print("".join([str(len(i)) if i[-1] not in {',','.'} else str(len(i)-1) for i in str_003.split()]))