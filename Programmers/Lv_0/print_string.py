"""
문자열 출력하기(완료자 수 10,368명, 정답률 64%)

<문제 설명>
문자열 str이 주어질 때, str을 출력하는 코드를 작성해보세요.

<제한 사항>
- 1 <= length of str <= 1,000,000
- str에는 공백이 없으며, 첫째 줄에 한 줄로만 주어집니다.
"""

# 작성한 코드
string = input()
if 1 <= len(string) <= 1000000:
    print(string)
else:
    print("It will not print more than 1,000,000 lengths.")