"""
주사위 게임 2

<문제 설명>
1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.

  - 세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
  - 세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) x (a^2 + b^2 + c^2 )점을 얻습니다.
  - 세 숫자가 모두 같다면 (a + b + c) x (a^2 + b^2 + c^2 ) x (a^3 + b^3 + c^3 )점을 얻습니다.
  
세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

<제한 사항>
a, b, c는 1이상 6이하의 정수입니다.

<입출력 예시>
  - 입력:
    a = 2, b = 6, c = 1
    
  - 출력:
    result = 9
    
"""

# 내가 작성한 코드
def solution(a, b, c):
  dice_list = [a, b, c] # 눈금 수들을 리스트화 하고
  non_dup_list = list(set(dice_list)) # 중복 제거한다.
  if len(non_dup_list) == 3: # 중복 제거 리스트의 길이 = 3 -> 모두 다른 수
    return a + b + c # 조건에 부합하는 값 return
  elif len(non_dup_list) == 2: # 중복 제거 리스트의 길이 = 2 -> 두 개는 같고, 나머지 하나는 다른 수
    for element in dice_list: # 중복 제거 전 리스트를 순회하면서
      if dice_list.count(element) == 2: # 해당 요소가 배열 안에 두개가 들어있다 -> 겹치는 수 -> a, b
        a = b = element # 겹치는 두 수를 a, b에 할당하고
        c = [x for x in non_dup_list if x != a][0] # c 할당 (중복 제거한 리스트에서 a와 b랑은 같지 않은 수. 리스트 컴프리헨션이라 뒤에 [0]까지 붙였다. )
        return (a + b + c)*(a**2 + b**2 + c**2) # 조건에 부합하는 값 return
  elif len(non_dup_list) == 1: # 중복 제거 리스트의 길이 = 1 -> 모두 같은 수 -> a = b = c = 중복 제거한 리스트의 값
    return (non_dup_list[0]*3)*(3*(non_dup_list[0]**2))*(3*(non_dup_list[0]**3)) # 조건에 맞게 return