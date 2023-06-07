"""
주사위 게임 3

<문제 설명>
1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

    1. 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 x p점을 얻습니다.
    2. 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 x p + q)2 점을 얻습니다.
    3. 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) x |p - q|점을 얻습니다.
    4. 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q x r점을 얻습니다.
    5. 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
    
네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

<제한 사항>
a, b, c, d는 1 이상 6 이하의 정수입니다.

<입출력 예시>
  - 입력:
    a = 2, b = 2, c = 2, d = 2
    
  - 출력:
    result = 2222
"""

# 내가 작성한 코드
def solution(a, b, c, d):
    dice_list = [a, b, c, d] # 입력받는 인자로 배열 생성
    non_dup_list = list(set(dice_list)) # 중복 제거
    if len(non_dup_list) == 1: # 중복 제거한 리스트의 길이가 1 => 눈금이 모두 똑같은 경우
        return 1111 * non_dup_list[0] # 조건에 맞는 결과값 return
    elif len(non_dup_list) == 2: # 중복 제거한 리스트의 길이가 2 => 3개가 동일하고 1개만 다르거나, 2개씩 동일하거나.
        for element in dice_list:
            if dice_list.count(element) == 3: # 3개가 겹치는 경우엔, 그 요소를
                p = element # p로 정의하고, 
                q = [x for x in non_dup_list if x != p][0] # 나머지 한 요소를 q로 정의하여
                return (10*p+q)**2 # 조건에 맞는 결과값 return
            elif dice_list.count(element) == 2: # 2개씩 겹치는 경우도 동일하게 진행
                p = element
                q = [x for x in non_dup_list if x != p][0]
                return (p + q)*(abs(p-q))
    elif len(non_dup_list) == 3: # 중복 제거한 리스트의 길이가 3 => 2개가 겹치고 나머지 두 수는 다른 경우.
        for element in dice_list: 
            if dice_list.count(element) == 2: # 겹치는 요소를 제외한 
                new_list = [x for x in non_dup_list if x != element] # 나머지 요소들을 가지고
                return new_list[0]*new_list[1] # 조건에 맞는 결과값 return
    else: # 네 눈금이 모두 다르다면,
        return min(dice_list) # 네 눈금 중 최소값을 return