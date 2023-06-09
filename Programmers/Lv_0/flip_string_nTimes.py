"""
문자열 여러번 뒤집기

<문제 설명>
문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다. 
queries의 원소는 [s, e] 형태로, my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다. 
my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.

<제한 사항>
1. my_string은 영소문자로만 이루어져 있습니다.
2. 1 ≤ my_string의 길이 ≤ 1,000
3. queries의 원소는 [s, e]의 형태로 0 ≤ s ≤ e < my_string의 길이를 만족합니다.
4. 1 ≤ queries의 길이 ≤ 1,000

<입출력 예시>
  - 입력:
    my_string = "rermgorpsam", queries = [[2, 3], [0, 7], [5, 9], [6, 10]]
    
  - 출력:
    result = "programmers"
"""

# 내가 작성한 코드
def solution(my_string, queries):
    for start, end in queries:
        my_string = my_string[:start] + my_string[start:end+1][::-1] + my_string[end+1:]
    return my_string