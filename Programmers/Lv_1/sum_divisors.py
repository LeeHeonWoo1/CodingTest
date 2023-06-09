"""
약수 더하기

<문제 설명>
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

<제한 사항>
n은 0 이상 3000이하인 정수입니다.

<입출력 예시>
  - 입력:
    n = 12
    
  - 출력:
    return = 28
"""

# 내가 작성한 코드
def solution(n):
    if n != 0:
        divisor_list = [1, n] # 1과 자기 자신을 약수로 가짐은 자명하기에 기본적으로 1과 n을 넣고 시작
        for i in range(2, n): # 1과 n은 이미 들어있기에, 2부터 n-1번째까지
            if n%i == 0: # n을 범위에 있는 수로 나눠 나머지가 0이라면
                divisor_list.append(i) # divisor_list에 추가.
        return sum(list(set(divisor_list))) # 합을 return하되, 중복으로 인한 오류 방지
    else:
        return 0
    
# 컴프리헨션을 사용해도 될 것 같다.
def solution(n):
    return sum([x for x in range(1, n+1) if n%x==0 and n != 0])