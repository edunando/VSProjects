valores = input().split()
a, b, c = valores
MaiorAB = (int(a)+int(b)+abs(int(a)-int(b)))/2

if int(c) > int(MaiorAB):
    print(int(c),"eh o maior")
else:
        print(int(MaiorAB),"eh o maior")

