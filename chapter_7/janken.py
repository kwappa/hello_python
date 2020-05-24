# 乱数のモジュールをインポート
import random

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
        num += 1
# 数字をじゃんけんの手に置き換える
        if you == 1:
            you_no_te = "グー"
        elif you == 2:
            you_no_te = "チョキ"
        elif you == 3:
            you_no_te = "パー"

# 整数の乱数を1〜3の範囲で発生させる
        pc = random.randint(1, 3)
# 乱数で出た数字をじゃんけんの手に置き換える
        if pc == 1:
            pc_no_te = "グー"
        elif pc == 2:
            pc_no_te = "チョキ"
        elif pc == 3:
            pc_no_te = "パー"

# あなたの手とパソコンの手の表示
        print ("あなたが出したのは……", you_no_te, "でした")
        print ("パソコンが出したのは……", pc_no_te, "でした")

    else:
        print ("1〜3の数字を入力してください！")
