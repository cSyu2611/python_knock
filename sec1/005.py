def create_n_gram(seq, n):
    if type(seq) is str:
        seq_list = list(seq.strip(".").split())
    elif type(seq) is list:
        seq_list = seq
    else:
        print("unsupported type")
        return -1
    tango_ngram = ['-'.join(seq_list[i:i+n]) for i in range(len(seq_list)-n+1)]
    moji_ngram = [''.join(seq_list)[i:i+n] for i in range(len(''.join(seq_list))-n+1)]
    print("単語{}-gram: ".format(n),tango_ngram)
    print("文字{}-gram: ".format(n),moji_ngram)
    return 0
    
if __name__ == "__main__":
    create_n_gram("I am an NLPer.",2)
