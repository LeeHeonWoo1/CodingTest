"""
배열만들기 2

<문제 설명>
정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.

<제한 사항>
1 ≤ l ≤ r ≤ 1,000,000

<입출력 예시>
  - 입력:
    l = 5, r = 555
    
  - 출력:
    result = 	[5, 50, 55, 500, 505, 550, 555]
"""

# 내가 작성한 코드
def solution(l, r):
    answer = []
    a_func = lambda x : '5' in str(x) or '0' in str(x) 
    array = list(filter(a_func, range(l, r+1)))
        
    for element in array:
        if len(str(element).replace('5', '').replace('0', '')) == 0:
            answer.append(element)
            
    if len(answer) == 0:
        answer.append(-1)

    return answer