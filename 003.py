import re

if __name__ == "__main__":
    str_003 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    # splitではなくre.splitで空白文字を指定できればもう少しマシなコードになりそう...
    print([len(i) if i[-1] not in {',','.'} else len(i)-1 for i in str_003.split()])