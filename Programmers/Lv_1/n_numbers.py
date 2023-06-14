"""
x만큼 간격이 있는 n개의 숫자

<문제 설명>
함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 
다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

<제한 사항>
x는 -10000000 이상, 10000000 이하인 정수입니다.
n은 1000 이하인 자연수입니다.

<입출력 예시>
  - 입력:
    x = 2, n = 5
    
  - 출력:
    answer = [2,4,6,8,10]
"""

# 내가 작성한 코드
def solution(x, n):
    if x < 0:
        return [i for i in range(x*n, x+1, -x)][::-1]
    elif x == 0:
        answer = []
        for i in range(n):
            answer.append(0)
        return answer
    else:
        return [i for i in range(x, x*n+1, x)]
    
# 다른 사람의 풀이
def number_generation(x, n):
    return [i*x + x for i in range(n)]