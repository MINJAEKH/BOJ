word = input()

suffix_list = []
for i in range(len(word)) :
    suffix_list.append(word[i:])

suffix_list.sort()
print(*suffix_list, sep = '\n')