print("あなたの名前を入力してください：")
input_lin = input()
print(f"こんにちは、{input_lin}さん！")

print("あなたの好きなジョジョは何部ですか：")
input_prin = input()
print(f"こんにちは、{input_prin}部が好きなんですね！")

print("あなたの好きなジョジョは何部ですか：")
input_prin = input()

part_names = {
    "1": "ファントムブラッド",
    "2": "戦闘潮流", 
    "3": "スターダストクルセイダース",
    "4": "ダイヤモンドは砕けない",
    "5": "黄金の風"
}

if input_prin in part_names:
    print(f"第{input_prin}部「{part_names[input_prin]}」が好きなんですね！")
else:
    print(f"こんにちは、{input_prin}部が好きなんですね！")
