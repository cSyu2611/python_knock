import random

def func_009(string):
    return " ".join([i if len(i)<=4 else i[0]+"".join(random.sample(list(i[1:-1]),len(list(i[1:-1]))))+i[-1] for i in str_009.split()])

if __name__ == "__main__":
    str_009 = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(func_009(str_009))

    print("ここからお遊び")
    count = 1
    while(1):
        give_try = func_009(str_009)
        print(give_try)
        if(give_try == str_009):
            print("{}回目で元の文と一致！".format(count))
            break
        count += 1
    #まじで揃わんorz