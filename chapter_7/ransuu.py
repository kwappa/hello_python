# 「乱数のテスト」
# 乱数のモジュールをインポート

import random

# 乱数を発生させる
r = 0
for i in range(10):
    r = random.randint(1, 6)
    print (r)
