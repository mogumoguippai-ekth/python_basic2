"""
N面サイコロをM回振ったときの結果を表示する
N, M は正の整数とする
N, M はユーザーからの入力を利用すること
"""

import random

# ユーザーからサイコロの面の数 (N) を入力してもらう
while True:
    try:
        n = int(input("サイコロの面の数は?: "))
        if n > 0:
            break
        else:
            print("正の整数を入力してください。")
    except ValueError:
        print("無効な入力です。正の整数を入力してください。")


# ユーザーから振る回数 (M) を入力してもらう
while True:
    try:
        m = int(input("何回振りますか?: "))
        if m > 0:
            break
        else:
            print("正の整数を入力してください。")
    except ValueError:
        print("無効な入力です。正の整数を入力してください。")


# M回サイコロを振る
results = []
for _ in range(m):
    roll = random.randint(1, n)  # 1からNまでのランダムな整数を生成
    results.append(roll)


# 結果を表示する
print(results)
