"""
접미사 배열

<문제 설명>
어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
문자열 my_string이 매개변수로 주어질 때, my_string의 모든 접미사를 사전순으로 정렬한 문자열 배열을 return 하는 solution 함수를 작성해 주세요.


<제한 사항>
my_string은 알파벳 소문자로만 이루어져 있습니다.
1 ≤ my_string의 길이 ≤ 100

<입출력 예시>
  - 입력:
    my_string = "banana"
    
  - 출력:
    result = ["a", "ana", "anana", "banana", "na", "nana"]
"""

# 내가 작성한 코드
def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])
    answer.sort()
    return answer

print(solution("banana"))