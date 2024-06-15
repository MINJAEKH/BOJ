'''
1. Test case 개수 받기
2. T만큼 이진수로 변환할 숫자 입력받기
3. for 문 
    1) 이진수로 변환 (str)
    2) 1의 위치 찾아서 리스트로 반환 (int)
    3) (int -> str 변환 후) join 함수로 문자열로 변환 
'''
# 위치 일일이 찾기
T = int(input()) # 테스트 케이스 개수 
number_list =[int(input())for _ in range (T)]

def find_positions(n) :
    binary = bin(n)[2:] #str
    positions = [i for i in range(len(binary)) if binary[-i-1] == '1'] #위치가 낮은 것부터
    result = " ".join(map(str, positions))
    return result

for n in number_list :
    print(find_positions(n))