"""
대소문자 바꿔서 출력하기

<문제 설명>
영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로, 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

<제한 사항>
1. 1 <= str의 길이 <= 20
  - str은 알파벳으로 이루어진 문자열이다.

<입출력 예시>
  - 입력:
    aBcDeFg
    
  - 출력:
    AbCdEfG
"""

# 내가 작성한 코드
string = input()
result = '' # 결과를 나타낼 빈 문자열
if 1 <= len(string) <= 20:
  for element in string: # 문자열의 한글자씩 순회하며
    if element.isupper(): # 각 글자들이 대문자라면
      result += element.lower() # 빈 문자열에 소문자로 변환해서 더하고
    else: # 아니라면
      result += element.upper() # 빈 문자열에 대문자로 변환해서 더한다.
  print(result)
else:
  print('out of range')