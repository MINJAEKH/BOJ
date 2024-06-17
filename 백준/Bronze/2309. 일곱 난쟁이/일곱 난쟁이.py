def find_dwarf(heights : list) :
    remainder = sum(heights) - 100

    for i in range(9) :
        for j in range(i+1, 9) :
            if remainder == heights[i] + heights[j] :
                heights.remove(heights[i]) 
                heights.remove(heights[j-1]) #i번째 인덱스를 제거 후 인덱스 -1 
                return "\n".join(map(str, sorted(heights)))

heights = [int(input()) for _ in range(9)]
print(find_dwarf(heights))