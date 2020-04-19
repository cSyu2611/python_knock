if __name__ == "__main__":
    str_001 = "stressed"
    # 方法１：スライスでやる方法
    print(str_001[::-1])
    # 方法２：文字列のreversed object→リスト化→区切り文字なしで結合 いらんな。
    print(''.join(list(reversed(str_001))))