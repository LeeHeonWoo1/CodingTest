"""
간단한 논리 연산

<문제 설명>
boolean 변수 x1, x2, x3, x4가 매개변수로 주어질 때, 다음의 식의 true/false를 return 하는 solution 함수를 작성해 주세요.

(x1 ∨ x2) ∧ (x3 ∨ x4)

<제한 사항>


<입출력 예시>
  - 입력:
    x1 = false, x2 = true, x3 = true, x4 = true
    
  - 출력:
    result = true
    
"""

# 내가 작성한 코드
def solution(x1, x2, x3, x4):
    return (x1 or x2) and (x3 or x4) # 문제에서 제시한 조건 = (x1 논리합 x2) 논리곱 (x3 논리합 x4), 논리합 = or, 논리곱 = and