from math import floor

print("ようこそ！")
print("電子レンジ　加熱量　計算機へ")
print("コンビニのお惣菜などをあなたの希望する、W数で加熱時間を計算します！")

while True:
    input_w = input("パッケージに表記されている [W]数を入力して下さい：")
    if int(input_w) > 0 and int(input_w) < 2000:
        break
    print("無効なW数です。")
    print("最初からやり直して下さい。")    

while True:
    input_time＿min = input(input_w + "Wを使用した場合の、加熱時間を入力して下さい（分）：")
    if int(input_time＿min) < 100 and int(input_time＿min) > -1:
        break
    print("無効な時間です")
    print("入力し直して下さい。")

while True:
    input_time_sec = input("(秒)：")
    if int(input_time_sec) == 0 or int(input_time_sec) < 60:
        break
    print("無効な時間です。")
    print("入力し直して下さい。")

w = int(input_w)
time_min = int(input_time＿min)
time_sec = int(input_time_sec)

total_tiem = time_min * 60 + time_sec

total_jour = w * total_tiem

while True:
    input_your_w = input("あなたが希望するW数を入力して下さい:")
    if int(input_your_w) > 0 and int(input_your_w) < 2000:
        break
    print("無効なW数です。")
    print("やり直して下さい")


your_w = int(input_your_w)

get_time = total_jour / your_w

get_min = get_time / 60

floor_min = floor(get_min)

get_sec = get_time % 60

floor_sec = floor(get_sec)


print("")
print(str(your_w) + "Wで加熱する場合、加熱時間は" + str(floor_min) + "分 " + str(floor_sec) + "秒です。")
print("")
