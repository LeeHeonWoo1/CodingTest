"""
접두사인지 확인하기

<문제 설명>
어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다. 예를 들어, "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"입니다.
문자열 my_string과 is_prefix가 주어질 때, is_prefix가 my_string의 접두사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.

<제한 사항>
1 ≤ my_string의 길이 ≤ 100
1 ≤ is_prefix의 길이 ≤ 100
my_string과 is_prefix는 영소문자로만 이루어져 있습니다.

<입출력 예시>
  - 입력:
    my_string = "banana", is_prefix = "ban"
    
  - 출력:
    result = 1
"""

# 내가 작성한 코드
def solution(my_string, is_prefix):
    prefix_array = []
    for i in range(len(my_string)):
        prefix_array.append(my_string[:i])
    
    if is_prefix in prefix_array:
        return 1
    else:
        return 0