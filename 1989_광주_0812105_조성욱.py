
def palinFunc(word, a):
    if 3<= len(word[0]) <= 10:
        if word[0] == word[0][::-1]:
            print(f"#{a+1} 1")
        else:
            print(f"#{a+1} 0")
    

num = int(input())
wordList = []

for i in range(num):
    wordList.append(input().split("\n"))



for i in range(num):
    palinFunc(wordList[i] , i)
    



