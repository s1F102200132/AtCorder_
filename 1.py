S = input()
word = []
i = 0
while i < len(S):
    j = i + 1
    while j < len(S) and S[j].islower:
        j += 1
    word.append(S[i:j + 1])
    i = j +1
word.sort(key=str.lower)
print("".join(word))

    

