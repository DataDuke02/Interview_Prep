word = "Infosys Interview".lower()
vowels = 0

for ch in word:
        if ch in "aeiou":
            vowels += 1
            
print(vowels)
