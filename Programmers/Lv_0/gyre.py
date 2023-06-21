"""
정수를 나선형으로 배치하기

<문제 설명>
양의 정수 n이 매개변수로 주어집니다. n x n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.

<제한 사항>
1 ≤ n ≤ 30

<입출력 예시>
  - 입력:
    n = 4
    
  - 출력:
    result = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
"""

# 내가 작성한 코드
def solution(n):
    if n == 1:
        return [[1]]
    
    answer = [[0]*n for _ in range(n)] # n x n 크기의 2차원 배열 초기화
    
    x = 0 # x좌표
    y = 0 # y좌표
    way = 'r' # 우측이동
    
    for i in range(n**2): # n^2회 반복
        answer[x][y] = i + 1 # 1부터 값 할당 시작
        if way == 'r': # 오른쪽으로 이동할땐
            y += 1 # y좌표를 1씩 늘린다
            if y == n-1 or answer[x][y+1] != 0: # 끝 지점에 도달했거나 이미 값이 할당되어 있는 경우,
                way = 'd' # 아래로 방향 전환
        elif way == 'd': # 아래로 이동할땐
            x += 1 # x좌표를 하나씩 늘린다
            if x == n-1 or answer[x+1][y] != 0: # 마찬가지로 끝지점에 도달했거나 이미 값이 할당되어 있는 경우
                way = 'l' # 왼쪽으로 방향 전환
        elif way == 'l': # 왼쪽으로 이동할 땐
            y -= 1 # y좌표를 하나씩 줄이고
            if y == 0 or answer[x][y-1] != 0:
                way = 'u' # 위로 방향 전환
        elif way == 'u': # 위로 이동할 땐
            x -= 1 # x좌표를 하나씩 줄인다.
            if x == n-1 or answer[x-1][y] != 0:
                way = 'r'
                
    return answer