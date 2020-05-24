# 全体のプログラム
# モジュールのインポート
from tkinter import *

# ウィンドウの作成
win = Tk()
cv = Canvas(win, width = 640, height = 480)
cv.pack()

# ゲームの初期化
ball_ichi_x = 300
ball_ichi_y = 150
ball_idou_x =  30
ball_idou_y = -30
ball_size = 10

# 画面の描画
def draw_screen():
    # 画面クリア
    cv.delete("all")
    # キャンバス（画面）の作成
    cv.create_rectangle(0, 0, 640, 480, fill = "white", width = 0)

# ボールを描く
def draw_ball():
    global ball_ichi_x, ball_ichi_y, ball_idou_x, ball_idou_y

    cv.create_oval(ball_ichi_x - ball_size, ball_ichi_y - ball_size,
        ball_ichi_x + ball_size, ball_ichi_y + ball_size,
        fill = "red")

# ボールの移動
def move_ball():
    global ball_ichi_x, ball_ichi_y, ball_idou_x, ball_idou_y

    # 左右の壁に当たったかの判定
    if (ball_ichi_x + ball_idou_x < 0 or ball_ichi_x + ball_idou_x > 640):
        ball_idou_x *= -1

    # 天井か床に当たったかの判定
    if (ball_ichi_y + ball_idou_y < 0 or ball_ichi_y + ball_idou_y > 480):
        ball_idou_y *= -1

    # ボールの位置を移動
    if (0 <= ball_ichi_x + ball_idou_x <= 640):
        ball_ichi_x = ball_ichi_x + ball_idou_x
    if (0 <= ball_ichi_y + ball_idou_y <= 480):
        ball_ichi_y = ball_ichi_y + ball_idou_y

# ゲームの繰り返し処理の指令
def game_loop():
    draw_screen()
    draw_ball()
    move_ball()
    win.after(50, game_loop)

# ゲームのメイン処理
game_loop()
win.mainloop()
