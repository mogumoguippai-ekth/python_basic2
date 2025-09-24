"""
スペース区切りで入力された整数群において、
合計値、最大値、最小値、平均値の4つの統計量を
1つの統計量につき専用関数を持つ
計算アプリを実装する
"""

def calculate_sum(numbers):  # 整数のリストから合計値を計算する
    
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_max(numbers):  # 整数のリストから最大値を計算する
        
    maximum = numbers[0]  # 最初の要素を初期最大値とする
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def calculate_min(numbers):  # 整数のリストから最小値を計算する
            
    minimum = numbers[0]  # 最初の要素を初期最小値とする
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def calculate_average(numbers):  # 整数のリストから平均値を計算する

    total = calculate_sum(numbers)
    count = 0
    for _ in numbers:
        count += 1
    
    return total // count  # 商のみ表示(小数点以下切り捨て)


def main():  # 入力されたデータから統計量を計算して表示する

    data_str = input("データを入力してください(スペース区切り) > ")
    
    numbers = [int(x) for x in data_str.split()]  # 文字列をスペースで分割し、各要素を整数に変換してリストに格納する

    total_value = calculate_sum(numbers)
    max_value = calculate_max(numbers)
    min_value = calculate_min(numbers)
    avg_value = calculate_average(numbers)

    print(f"合計値: {total_value}")
    print(f"最大値: {max_value}")
    print(f"最小値: {min_value}")
    print(f"平均値: {avg_value}")

if __name__ == "__main__":
    main()  #関数を実行する
