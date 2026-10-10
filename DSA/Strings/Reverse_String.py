word = "hello"
rev = ""

for ch in word:
    rev = ch + rev
    
print(rev)

word1 = ["h","e","l","l","o"]

rev = []

for ch in range(len(word1) -1, -1, -1):
    rev.append(word1[ch])

result ="".join(rev)
print(result)