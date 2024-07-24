N = int(input())

str_list = [input() for _ in range(N)]
str_unique = list(set(str_list))

str_unique.sort(key = lambda x : x)
str_unique.sort(key=len)

for word in str_unique :
    print(word)