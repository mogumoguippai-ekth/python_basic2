# 任意の行数と列数の九九表を出力します。


def some_kuku_table():
    rows = int(input("行数を入力してください: "))
    cols = int(input("列数を入力してください: "))


    # 二重ループを使って九九表を生成する
    for i in range(1, rows + 1):           # 1から入力行数までをiに取得する
        for j in range(1, cols + 1):       # 1から入力列数までをjに取得する
            result = i * j
            print(f"{i * j}", end=" ")  # i*jをスペースでつなげる
        print()   # 各段の終わりに改行

# 関数を実行する
some_kuku_table()
