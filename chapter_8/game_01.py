# ウィンドウを作るモジュールを読み込む
from tkinter import *

# ウィンドウの作成
win = Tk()
cv = Canvas(win, width = 640, height = 480)

# キャンバスの表示命令
cv.pack()

# ウインドウの表示命令
win.mainloop()
