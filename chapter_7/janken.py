# 変数の宣言
num = 1
you = 0
key = ""

# 10回繰り返す
while num <= 10:
    print (num, "回目")
    print ("あなたが出すのは？(「1=グー 2=チョキ \
3=パー」の後にEnterを押す)")
# 文字の入力
    key = input()
# 文字が1、2、3だった場合
    if (key == "1" or key == "2" or key == "3"):
        you = int(key)
# 数字をじゃんけんの手に置き換える
        if you == 1:
            you_no_te = "グー"
        elif you == 2:
            you_no_te = "チョキ"
        elif you == 3:
            you_no_te = "パー"

        print (you_no_te)
        num += 1
    else:
        print ("1〜3の数字を入力してください！")
