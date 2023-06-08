"""
배열 만들기 5

<문제 설명>
문자열 배열 intStrs와 정수 k, s, l가 주어집니다. intStrs의 원소는 숫자로 이루어져 있습니다.
배열 intStrs의 각 원소마다 s번 인덱스에서 시작하는 길이 l짜리 부분 문자열을 잘라내 정수로 변환합니다. 
이때 변환한 정수값이 k보다 큰 값들을 담은 배열을 return 하는 solution 함수를 완성해 주세요.

<제한 사항>
0 ≤ s < 100
1 ≤ l ≤ 8
10^(l - 1) ≤ k < 10^l
1 ≤ intStrs의 길이 ≤ 10,000
    s + l ≤ intStrs의 원소의 길이 ≤ 120

<입출력 예시>
  - 입력:
    intStrs = ["0123456789","9876543210","9999999999999"], k = 50000, s = 5, l = 5
    
  - 출력:
    result = [56789, 99999]
"""

# 내가 작성한 코드
def solution(intStrs, k, s, l):
    answer = []
    for element in intStrs:
        if int(element[s:s+l]) > k:
            answer.append(int(element[s:s+l]))
    return answer