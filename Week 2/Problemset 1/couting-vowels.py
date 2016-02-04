s = 'azcbobobegghakl'
count = 0
vowels = set("a""e""i""o""u")
for vowel in s:
    if vowel in vowels:
         count += 1

print('Number of vowels: ' + str(count))
