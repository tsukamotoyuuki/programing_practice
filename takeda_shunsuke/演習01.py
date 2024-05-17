print("1から100の間で数値を入力してください")
nenrei=int(input())
if nenrei <= 19:
    print("未成年です。地方自治体によっては医療費が¥200 のところも。")
elif nenrei <= 59:
    print("成年です。飲酒・喫煙は控えめに。")
elif nenrei <= 100:
    print("定年後も元気 100%で過ごしてください。")

if nenrei > 100:
    print("100以下を入力して下さい")

