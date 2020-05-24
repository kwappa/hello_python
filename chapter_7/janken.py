# Pythonジャンケンゲーム

# 乱数のモジュールをインポート
import random

# 強引な画面クリア
for i in range(50):
    print("\r")

# 変数の宣言
## 勝ち数、負け数、あいこの数を0にする
kachi = make = aiko = 0
try_again = 0
you = pc = 0

## プレイヤーの手とパソコンの手の変数が文字タイプであることを宣言
you_no_te = pc_no_te = ""

## キー入力の変数が文字タイプであることを宣言
key = ""

## 判定で表示するメッセージを決める
you_win = "あなたの勝ち"
pc_win = "あなたの負け"
hikiwake = "あいこ"
hantei = ""

# 10回繰り返し
num = 1
while num <= 10:

# キー入力
    print (num, "回目")
    print ("あなたが出すのは？(「1=グー 2=チョキ \
3=パー」の後にEnterを押す)")
    key = input()
    if (key == "1" or key == "2" or key == "3"):
        you = int(key)
        num += 1

# 入力チェック
        if you == 1:
            you_no_te = "グー"
        elif you == 2:
            you_no_te = "チョキ"
        elif you == 3:
            you_no_te = "パー"

# 整数の乱数を1〜3の範囲で発生させる
        pc = random.randint(1, 3)

# 乱数で出た数字をジャンケンの手に置き換える
        if pc == 1:
            pc_no_te = "グー"
        elif pc == 2:
            pc_no_te = "チョキ"
        elif pc == 3:
            pc_no_te = "パー"

# あなたの手とパソコンの手の表示
        print ("あなたが出したのは……", you_no_te, "でした")
        print ("パソコンが出したのは……", pc_no_te, "でした")

# 勝ち負けの判定
        if you == pc:               # プレイヤーとパソコンの手が同じだったら
            hantei = hikiwake       # 判定は引き分け
        if you == 1 and pc == 2:    # プレイヤーがグー、パソコンがチョキだったら
            hantei = you_win        # 判定はプレイヤーの勝ち
        if you == 1 and pc == 3:    # プレイヤーがグー、パソコンがパーだったら
            hantei = pc_win         # 判定はプレイヤーの負け
        if you == 2 and pc == 3:    # プレイヤーがチョキ、パソコンがパーだったら
            hantei = you_win        # 判定はプレイヤーの勝ち
        if you == 2 and pc == 1:    # プレイヤーがチョキ、パソコンがグーだったら
            hantei = pc_win         # 判定はプレイヤーの負け
        if you == 3 and pc == 1:    # プレイヤーがパー、パソコンがグーだったら
            hantei = you_win        # 判定はプレイヤーの勝ち
        if you == 3 and pc == 2:    # プレイヤーがパー、パソコンがチョキだったら
            hantei = pc_win         # 判定はプレイヤーの負け

# 勝ち負けの判定を表示
        print ("判定は……", hantei, "でした！")
        print ("\n")

# 勝ち・負け・あいこの回数を足す
        if hantei == you_win:
            kachi += 1
        if hantei == pc_win:
            make += 1
        if hantei == hikiwake:
            aiko += 1

# キー入力が「1〜3」以外だったときの処理
    else:
        print ("1〜3の数字を入力してください！")

# 最終結果の表示
print ("10回じゃんけんした結果は　あなたの", kachi, "勝", make, "敗", aiko, "引き分けでした")
