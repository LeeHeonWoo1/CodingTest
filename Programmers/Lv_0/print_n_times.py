"""
문자열 반복해서 출력하기

<문제 설명>
문자열 str과 정수 n이 주어집니다.
str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

<제한 사항>
1. 1 <= str <= 10
2. 1 <= n <= 5

<입출력 예시>
  - 입력:
    string 5
    
  - 출력:
    stringstringstringstringstring
"""

# 내가 작성한 코드
str, n = input().strip().split(' ')
n = int(n)

if 1 <= len(str) <= 10 and 1 <= n <= 5:
  print(str*n)
else:
  print('out of range')