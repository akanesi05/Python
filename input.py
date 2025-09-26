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
    print( img src='URL'><br>items_imges[item_name])
    print(item_name)
class MenuItem:
    pass

import sys
for line in sys.stdin.readlines():
    print(line.rstrip())

input_line = input().split()
del input_line[0]
#print(input_line)


for n in input_line:
     print(n)
     

# 1行目をスペースで分割してリスト化
data = input().split()

# 最初の要素が N（件数）
n = int(data[0])
print(n)
# 2番目以降が文字列データ
strings = data[1:]
print(strings)
# 改行区切りで出力
for s in strings:
    print(s)

input_line = input()
#print("XXXXXX")

for num in range(int(input_line)):
s=input().split()
del s[0]
print(*s)

if len(input_line)==3:
    print(input_line)
elif len(input_line)==2:
    print('0'+str(input_line))
elif len(input_line)==1:
    print('00'+str(input_line))
    

s = input()           # 例: 5 1
parts = s.split(' ')  # ['5', '1'] に分割
print(','.join(parts))  # → 5,1

a, b, c = map(int, input().split())
arr = list(map(int, input().split()))

total = 0
for num in arr[b-1:c]:   # b〜c番目の要素を取り出す
    total += num

print(total)

N = int(input())
lower = 1
upper = 10**9
divisors = []

for _ in range(N):
    op, x = input().split()
    x = int(x)
    if op == ">":
        lower = max(lower, x+1)
    elif op == "<":
        upper = min(upper, x-1)
    elif op == "/":
        divisors.append(x)

for num in range(lower, upper+1):
    ok = True
    for d in divisors:
        if num % d != 0:
            ok = False
            break
    if ok:
        print(num)
        break   # 最小の a を見つけたら終了

# ユーザーの名前を入力
print("あなたの名前を入力してください：")
input_lin = input()
print(f"こんにちは、{input_lin}さん！")

# 好きなジョジョの部を入力
print("あなたの好きなジョジョは何部ですか：")
input_prin = input()
print(f"こんにちは、{input_prin}部が好きなんですね！")

# もう一度好きなジョジョの部を入力
print("あなたの好きなジョジョは何部ですか：")
input_prin = input()

# ジョジョ各部の辞書
part_names = {
    "1": "ファントムブラッド",
    "2": "戦闘潮流", 
    "3": "スターダストクルセイダース",
    "4": "ダイヤモンドは砕けない",
    "5": "黄金の風"
}

# 入力が辞書にあれば正式名称で出力
if input_prin in part_names:
    print(f"第{input_prin}部「{part_names[input_prin]}」が好きなんですね！")
else:
    print(f"こんにちは、{input_prin}部が好きなんですね！")

# アイテム名と画像URLの辞書
items_imges = {
    "剣" : "http://paiza.jp/learning/images/sword.png",
    "盾" : "http://paiza.jp/learning/images/shield.png",
    "回復薬" : "http://paiza.jp/learning/images/potion.png",
    "クリスタル" : "http://paiza.jp/learning/images/crystal.png"
}

# アイテムの並び順リスト
items_orders = ["剣", "盾", "回復薬", "クリスタル"]

# アイテム名と画像URLを順に出力
for item_name in items_orders:
    print( img src='URL'><br>items_imges[item_name])  # ←この行は文法エラーです
    print(item_name)

# メニューアイテムのクラス定義（未実装）
class MenuItem:
    pass

# 標準入力から複数行を読み込んで出力
import sys
for line in sys.stdin.readlines():
    print(line.rstrip())

# 入力をスペース区切りでリスト化し、先頭要素を削除
input_line = input().split()
del input_line[0]
#print(input_line)

# 残りの要素を順に出力
for n in input_line:
     print(n)
     
# 1行目をスペースで分割してリスト化
data = input().split()

# 最初の要素が N（件数）
n = int(data[0])
print(n)
# 2番目以降が文字列データ
strings = data[1:]
print(strings)
# 改行区切りで出力
for s in strings:
    print(s)

# 入力を受け取る
input_line = input()
#print("XXXXXX")

# 入力値の回数分ループ
for num in range(int(input_line)):
    s=input().split()
    del s[0]
    print(*s)

# 入力値の長さによって出力を変える
if len(input_line)==3:
    print(input_line)
elif len(input_line)==2:
    print('0'+str(input_line))
elif len(input_line)==1:
    print('00'+str(input_line))
    
# 入力をカンマ区切りで出力
s = input()           # 例: 5 1
parts = s.split(' ')  # ['5', '1'] に分割
print(','.join(parts))  # → 5,1

# 3つの整数を入力し、配列を作成
a, b, c = map(int, input().split())
arr = list(map(int, input().split()))

# b〜c番目の要素の合計を計算
total = 0
for num in arr[b-1:c]:   # b〜c番目の要素を取り出す
    total += num

print(total)

# 条件に合う最小の値を探索
N = int(input())
lower = 1
upper = 10**9
divisors = []

for _ in range(N):
    op, x = input().split()
    x = int(x)
    if op == ">":
        lower = max(lower, x+1)
    elif op == "<":
        upper = min(upper, x-1)
    elif op == "/":
        divisors.append(x)

for num in range(lower, upper+1):
    ok = True
    for d in divisors:
        if num % d != 0:
            ok = False
            break
    if ok:
        print(num)
        break   # 最小の a を見つけたら終了
