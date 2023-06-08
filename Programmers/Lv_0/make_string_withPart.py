"""
부분 문자열 이어 붙여 문자열 만들기

<문제 설명>
길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다. 
parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다. 
각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

<제한 사항>
1 ≤ my_strings의 길이 = parts의 길이 ≤ 100
1 ≤ my_strings의 원소의 길이 ≤ 100
parts[i]를 [s, e]라 할 때, 다음을 만족합니다.
    0 ≤ s ≤ e < my_strings[i]의 길이

<입출력 예시>
  - 입력:
    my_strings = ["progressive", "hamburger", "hammer", "ahocorasick"], parts = [[0, 4], [1, 2], [3, 5], [7, 7]]
    
  - 출력:
    result = "programmers"
"""

# 내가 작성한 코드
def solution(my_strings, parts):
    answer = ''
    for i, part in enumerate(parts):
        answer += my_strings[i][part[0]:part[1]+1]
    return answer