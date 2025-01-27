import sys

T = int(sys.stdin.readline())

list_str = [] # 중복없는 리스트 받기
list_len = [] # 문자열 길이 저장하는 리스트트
for _ in range(T):
    word = sys.stdin.readline().strip()
    if word not in list_str: # 없을시 
        list_str.append(word) # 단어 추가
        list_len.append(len(word)) # 같은 위치에 길이값도 저장

M = max(list_len)

list_idx = [[] for _ in range(M + 1)] # 최대 단어 길이만큼의 이중 리스트 생성

for i in range(len(list_len)):
    list_idx[list_len[i]].append(list_str[i]) # 이중 리스트 안에 인덱스값 맞추어서 저장

for i in range(M + 1): # 이중 리스트 내부 정렬
    list_idx[i].sort()

for i in range(M + 1):
    for j in range(len(list_idx[i])):
        print(list_idx[i][j])

    
