"""
등차수열의 특정 항만 더하기

<문제 설명>
두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다. 첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때, 
이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.

<제한 사항>
1. 1 ≤ a ≤ 100
2. 1 ≤ d ≤ 100
3. 1 ≤ included의 길이 ≤ 100
4. included에는 true가 적어도 하나 존재합니다.

<입출력 예시>
  - 입력:
    a = 3, d = 4, included = [true, false, false, true, true]
    
  - 출력:
    37
"""

# 내가 작성한 코드
def solution(a, d, included):
    if a > 100 or d > 100 or len(included) > 100:
        return
    else:
        answer = 0
        for i, element in enumerate(included):
            An = a + d*i # 등차수열의 일반항 공식
            if element: # True 일때만
              answer += An # 결과에 해당 항의 값을 더한다
            else:
              continue
        return answer
    