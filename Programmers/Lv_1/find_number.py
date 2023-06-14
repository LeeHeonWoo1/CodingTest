"""
나머지가 1이 되는 수 찾기

<문제 설명>
자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.

<제한 사항>
3 ≤ n ≤ 1,000,000

<입출력 예시>
  - 입력:
    n = 10
    
  - 출력:
    result = 3
"""

# 내가 작성한 코드
def solution(n):
    temp_list = []
    for i in range(1, n):
        if n%i == 1:
            temp_list.append(i)
    return min(temp_list) # 문제는 통과했지만, 시간 복잡도를 고려했을 때 좋지 않은 선택

# 다른 풀이
def solution1(n):
    return [x for x in range(1, n) if n%x == 1][0]