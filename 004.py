if __name__ == "__main__":
    str_004 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    pointed_nums = [0,4,5,6,7,8,14,15,18]
    pointed_nums2 = 12

    # 内包表記で完結
    split_list = str_004.split()
    ans_dict = {str(i+1) : str(split_list[i][0]) if i in pointed_nums else str(split_list[i][0:2]) for i in range(len(split_list))}
    print(ans_dict)

    print("ちょっと気持ち悪いので修正")
    ans_dict[str(pointed_nums2)]='Mg'
    print(ans_dict)
