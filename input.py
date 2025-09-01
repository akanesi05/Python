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

items_imges = {
    "剣" : "http://paiza.jp/learning/images/sword.png",
    "盾" : "http://paiza.jp/learning/images/shield.png",
    "回復薬" : "http://paiza.jp/learning/images/potion.png",
    "クリスタル" : "http://paiza.jp/learning/images/crystal.png"
}

# アイテムの並び順リスト
items_orders = ["剣", "盾", "回復薬", "クリスタル"]

# ここから下を記述しよう
for item_name in items_orders:
    print( <img src='URL'><br>items_imges[item_name])
    print(item_name)
class MenuItem:
    pass
