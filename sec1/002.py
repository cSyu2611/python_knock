if __name__ == "__main__":
    str_002_1, str_002_2 = "パトカー", "タクシー"
    print("".join([one + two for one, two in zip(str_002_1, str_002_2)]))
