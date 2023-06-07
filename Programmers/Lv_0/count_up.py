"""
카운트 업

<문제 설명>
정수 start와 end가 주어질 때, start부터 end까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

<제한 사항>
0 ≤ start ≤ end ≤ 50

<입출력 예시>
  - 입력:
    start = 3, end = 10
    
  - 출력:
    result = [3, 4, 5, 6, 7, 8, 9, 10]
"""

# 내가 작성한 코드
def solution(start, end):
    return list(range(start, end+1))