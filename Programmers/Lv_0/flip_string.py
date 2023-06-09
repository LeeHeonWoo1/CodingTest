"""
문자열 뒤집기

<문제 설명>
문자열 my_string과 정수 s, e가 매개변수로 주어질 때, my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을 return 하는 solution 함수를 작성해 주세요.

<제한 사항>
my_string은 숫자와 알파벳으로만 이루어져 있습니다.
1 ≤ my_string의 길이 ≤ 1,000
0 ≤ s ≤ e < my_string의 길이

<입출력 예시>
  - 입력:
    my_string = "Progra21Sremm3", s = 6, e = 12
    
  - 출력:
    result = "ProgrammerS123"
"""

# 내가 작성한 코드
def solution(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]