num = 1
you = 0
key = ""
while num <= 10:
    print (num, "回目")
    print ("あなたが出すのは？(「1=グー 2=チョキ \
3=パー」の後にEnterを押す)")
    key = input()
    if (key == "1" or key == "2" or key == "3"):
        you = int(key)
        print (you)
        num += 1
    else:
        print ("1〜3の数字を入力してください！")
