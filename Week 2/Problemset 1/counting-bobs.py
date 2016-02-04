s = 'azcbobobegghakl'
count = 0
for l, _ in enumerate(s): #i here is the index, equal to "i in range(len(s))"
    if s[l:l+3] == 'bob': #Check the current char + the next three chars.
        count += 1
print('Number of times bob occurs is: ' + str(count))

count = 0
for l, _ in enumerate(s):
    if s[l:l+3] == 'bob':
        count += 1
print('Number of times bob occurs is: ' + str(count)
return('This is the end of the function')
