# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------


# TODO: 구구단
# ----------------------------------------------------------------
"""
문제
N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

출력
출력형식과 같게 N*1부터 N*9까지 출력한다.
"""

n = int(input())
for i in range(1, 10):
    print(n, '*', i, '=', n * i)
# ----------------------------------------------------------------


# TODO: A+B-3
# ----------------------------------------------------------------
"""
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 A+B를 출력한다.
"""

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(a + b)

# ----------------------------------------------------------------


# TODO: 합
# ----------------------------------------------------------------
"""
문제
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

출력
1부터 n까지 합을 출력한다.
"""
n = int(input())  # 5
s = 0  # 0
for i in range(n + 1):  # i(1, 2,...) n(2, 3, ...)
    s += i  # skip      # s <- i(1, 2,...)
print(s)  # s(1 + 2 + 3 + 4,...)

# ----------------------------------------------------------------


# TODO: 영수증
# ----------------------------------------------------------------
"""
문제
준원이는 저번 주에 살면서 처음으로 코스트코를 가 봤다. 
정말 멋졌다. 그런데, 몇 개 담지도 않았는데 수상하게 높은 금액이 나오는 것이다! 
준원이는 영수증을 보면서 정확하게 계산된 것이 맞는지 확인해보려 한다.

영수증에 적힌,
구매한 각 물건의 가격과 개수
구매한 물건들의 총 금액을 보고,
구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.

입력`
첫째 줄에는 영수증에 적힌 총 금액 $X$가 주어진다.
둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 $N$이 주어진다.
이후 $N$개의 줄에는 각 물건의 가격 $a$와 개수 $b$가 공백을 사이에 두고 주어진다.

출력
구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes를 출력한다.
일치하지 않는다면 No를 출력한다.
"""

# -> 첫째 줄에는 영수증에 적힌 총 금액 x가 주어진다.
t = int(input())  # 영수증 최종 금액 # 26000
# -> 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다.
s = int(input())  # 수량 # 4
n = 0

# -> 이후 N개의 줄에는 각 물건의 가격 a와 b가 공백을 사이에 두고 주어진다.
for i in range(s):
    # range(시작숫자, 종료숫자, step)
    a, b = map(int, input().split())  # (20000, 5)...(30000, 2)...(10000, 6)...(5000, 8)
    n += a * b
print("Yes" if t == n else "No")

# ----------------------------------------------------------------


# TODO: 빠른 A+B
# ----------------------------------------------------------------
"""
문제
본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.

C++을 사용하고 있고 cin/cout을 사용하고자 한다면, cin.tie(NULL)과 sync_with_stdio(false)를 둘 다 적용해 주고, endl 대신 개행문자(\n)를 쓰자.
    단, 이렇게 하면 더 이상 scanf/printf/puts/getchar/putchar 등 C의 입출력 방식을 사용하면 안 된다.
Java를 사용하고 있다면, Scanner와 System.out.println 대신 BufferedReader와 BufferedWriter를 사용할 수 있다. 
    BufferedWriter.flush는 맨 마지막에 한 번만 하면 된다.
-> Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.
        단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.
또한 입력과 출력 스트림은 별개이므로, 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다. 테스트케이스를 하나 받은 뒤 하나 출력해도 된다.

입력
첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.

출력
각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.
"""

# 문제에서 input() 대신 sys.stdin.readline을 사용을 권함
import sys

inp = int(input())  # 5
for i in range(inp):
    a, b = map(int, sys.stdin.readline().split())
    # a, b = map(int, input().split())
    # a와 b를 한줄에서 입력 받고 sys.stdin.readline().split()을 통해 라인 입력 받는다.
    # 근데 잘 안쓴다네... 가볍게만 보자!
    print(a + b)

# ----------------------------------------------------------------


# TODO: 별 찍기 -1
# ----------------------------------------------------------------
"""
문제
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
*
**
***
****
*****
"""
a: int = input()
b: str = ""
c: int = 0
for i in range(a):
    b = "*"
    c = b + i
    print(c)

a: int = input()
print(type(a))
a = int(input())
print(type(a))

a: int = int(input())
for i in range(1, (a + 1)):
    print("*" * i)

# ----------------------------------------------------------------


# TODO: 별 찍기 - 2
# ----------------------------------------------------------------
"""
문제
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.  
    *
   **
  ***
 ****
*****
"""
a: int = int(input())  # 값을 받습니다.
for i in range(1, (a + 1)):  # range(maxi+1)값 만큼 i 돌립니다.
    # print(f"{' '*(a+1-i)}{'*' * i}")
    print(' ' * (a - i) + '*' * i)  # 빈공간을 a - 4 만큼 출력합니다.

# ----------------------------------------------------------------


# TODO: A+B - 5 (삼항연산자)
# ----------------------------------------------------------------
"""
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
입력의 마지막에는 0 두 개가 들어온다.

출력
각 테스트 케이스마다 A+B를 출력한다.
"""
while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a + b)

    print("Null") if a == 0 and b == 0 else print(a + b)

# ----------------------------------------------------------------


# TODO: A+B - 4
# ----------------------------------------------------------------
"""
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 A+B를 출력한다.
"""
while 1:
    try:  # 변수 A, B에 int형이 들어간다면, A+B값 출력
        a, b = map(int, input().split())
        print(a + b)
    except:  # try에 대한 에러가 발생하면 while멈춘다.
        break

# ----------------------------------------------------------------


# TODO: 더하기 사이클
# ----------------------------------------------------------------
"""
문제
0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다.  0 < a > 99
먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. if a < 10  --> 0a
그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 

다음 예를 보자.
26부터 시작한다.  #26
2+6 = 8이다. 새로운 수는 68이다. # 2608 68 
6+8 = 14이다. 새로운 수는 84이다. # 6814 84
8+4 = 12이다. 새로운 수는 42이다. # 8412 42
4+2 = 6이다. 새로운 수는 26이다.  # 4206 26
위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.

출력
첫째 줄에 N의 사이클 길이를 출력한다.
1. 55
2. 5+5 = 10 -> 5510 --> 50
3. 5+0 = 05 -> 5005 --> 05
4. 0+5 = 05 -> 0505 --> 55
"""

# ------------------------------ -> 무슨 개소리인지 모르겠다.. 주말에 한번 보도록하자
# ------------------------------ -> 무슨 개소리인지 모르겠다.. 주말에 한번 보도록하자
# ------------------------------ -> 무슨 개소리인지 모르겠다.. 주말에 한번 보도록하자
# ------------------------------ -> 무슨 개소리인지 모르겠다.. 주말에 한번 보도록하자
# ------------------------------ -> 무슨 개소리인지 모르겠다.. 주말에 한번 보도록하자
# ------------------------------ -> 무슨 개소리인지 모르겠다.. 주말에 한번 보도록하자
# ------------------------------ -> 무슨 개소리인지 모르겠다.. 주말에 한번 보도록하자
n: int = int(input())  # 55
key: int = n  # key
cnt: int = 0
print(type(key, type(n)))

while 1:
    cnt += 1  # 사이클 수 증가
    sum = n // 10 + n % 10  # (sum = 5 + 5)
    n = n % 10 * 10 + sum % 10
    if n == key:  # num에서 입력된 n과 똑같은 숫자가 나오면 멈춤
        break
print(cnt)

input_num = int(input())
num = input_num
cnt = 0
while True:
    sum_num = (num // 10) + (num % 10)
    new_num = ((num % 10) * 10) + (sum_num % 10)
    cnt += 1
    if new_num == input_num:
        break
    num = new_num
print(cnt)

# ----------------------------------------------------------------


# TODO: 개수 세기
# ----------------------------------------------------------------
"""
문제
총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 정수가 공백으로 구분되어져있다. 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.

출력
첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.
"""
# 정수의 개수n 정수nlist를 찾는 정수 v
n: int = int(input())
n_list = list(map(int, input().split()))
v = int(input())

print(n_list.count(v))  # 입력으로 주어진 n_list중 v가 몇개인지 출력한다.
# count : 매개변수로 입력된 값이 리스트안에 몇개 있는지 세어 반환

# ----------------------------------------------------------------


# TODO: X보다 작은 수
# ----------------------------------------------------------------
"""
문제
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 
이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)

둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 
주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

출력
X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다.
X보다 작은 수는 적어도 하나 존재한다.
"""

a, b = map(int, input().split())
num = list(map(int, input().split()))  # 리스트를 담는디

for i in range(a):  # a횟수만큼 돌린다
    if num[i] < b:  # 만약 num배열에 i값이 b보다 작다면 프린터한다
        # 배열값은 [] 괄호로 찾는다
        print(num[i], end=" ")

# ----------------------------------------------------------------


# TODO: 최소, 최대
# ----------------------------------------------------------------
"""
문제
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

출력
첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
"""

# min, max 함수를 자주 사용한다
# sort 함수를 사용한다. 정렬의 기본함수
a: int = int(input())  # input 함수를 통해 입력을 받고 int를 통해 정수형으로 변환
array: list = list(map(int, input().split()))
print(min(array), max(array))

# 풀이 2 정렬을 사용한 방법
a: int = int(input())  # input 함수를 통해 입력을 받고 int를 통해 정수형으로 변환
array: list = list(map(int, input().split()))
array.sort()  # 오름차순으로 정렬한다
print(array[0], array[-1])  # 처음과 마지막을 출력한다. 그러면 구해지는듯..

# ----------------------------------------------------------------


# TODO: 최댓값
# ----------------------------------------------------------------
"""
문제
9개의 서로 다른 자연수가 주어질 때, 
이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수

3, 29, 38, 12, 57, 74, 40, 85, 61

이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

입력
첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

출력
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.
"""
# 9개의 자연수가 하나씩 차례대로 입력되면 어디에 저장되는 공간이 필요하다.
# 저장된 공간에서의 최댓값과 몇 번째로 저장되었는지에 출력이 필요하다.
num_list = []
for i in range(9):
    num_list.append(int(input()))  # num_list 값 넣기
print(max(num_list))
print(num_list.index(max(num_list)) + 1)  # 최대값 출력하기

# ----------------------------------------------------------------


# TODO: 과제 안 내신 분..?
# ----------------------------------------------------------------
"""
문제
X대학 M교수님은 프로그래밍 수업을 맡고 있다. 
교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.

교수님이 내준 특별과제를 28명이 제출했는데,
그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

입력
입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다.
출석번호에 중복은 없다.

출력
출력은 2줄이다. 
1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 
2번째 줄에선 그 다음 출석번호를 출력한다.
"""
student = [False for i in range(30)]
# student 리스트를 선언하여 인덱스 0~29번 값 False로 초기화
# 파이썬 리스트 특정 값으로 초기화 하는 방법
# == student = [False] * 30
for i in range(28):
    number = int(input())
    student[number - 1] = True
# 과제를 제출한 28명 학생의 출석번호를 입력,
# 입력받은 출석 번호 -1에 해당하는 인덱스의 값을 True로 선언한다.
for i in range(30):
    if not student[i]:
        print(i + 1)
# student리스트의 값 모두 확인하여, 값이 True가 아닌 경우 해당 인덱스 +1를 출력
# 인덱스(i)가 0부터 시작하기 때문에, 가장 작은 번호부터 출력한다는 출력 조건 또한 만족한다.
# 생각보다 난이도가 있는 문제네............................................

# ----------------------------------------------------------------


# TODO: 숫자의 개수
# ----------------------------------------------------------------
"""
문제
세 개의 자연수 A, B, C가 주어질 때,
A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고,
계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

입력
첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. 
A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.

출력
첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다. 
마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 
1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.
"""

x: int = int(input()) * int(input()) * int(input())
for i in range(0, 10):
    print(str(x).count(str(i)))

# 다른 방식
a: int = int(input())
b: int = int(input())
c: int = int(input())
d_list: list = list(str(a * b * c))
for i in range(0, 10):
    print(d_list.count(str(i)))

# ----------------------------------------------------------------


# TODO:숫자의 합
# ----------------------------------------------------------------
"""
문제
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

출력
입력으로 주어진 숫자 N개의 합을 출력한다.
"""
a = int(input())
n = list(input())
sum = 0
for i in n:
    sum += int(i)
print(sum)
# ----------------------------------------------------------------


# TODO: 팩토리얼
# ----------------------------------------------------------------
"""
문제
0보다 크거나 같은 정수 N이 주어진다.
이때, N!을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

출력
첫째 줄에 N!을 출력한다.
"""
n = int(input())

result = 1
if n > 0:
    for i in range(1, n + 1):
        result *= i
print(result)
# ----------------------------------------------------------------


# TODO: 나머지
# ----------------------------------------------------------------
"""
문제
두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 
예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

입력
첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 
이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.

출력
첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.
//
각 수를 42로 나눈 나머지는 1, 2, 3, 4, 5, 6, 7, 8, 9, 10이다.
모든 수를 42로 나눈 나머지는 0이다.
각 수를 42로 나눈 나머지는 39, 40, 41, 0, 1, 2, 40, 41, 0, 1이다. 서로 다른 값은 6개가 있다.
"""
n = []

for _ in range(10):
    a = int(input())
    b = a % 42
    n.append(b)
s = set(n)
print(len(s))
# ----------------------------------------------------------------
a: int = int(input())
b: int = int(input())
print(a + b)

# TODO: 김염원의 나머지
# ----------------------------------------------------------------
"""
문제
두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다.
예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

입력
첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 
이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.

출력
첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.
"""
n = []

for _ in range(10):
    a = int(input())
    b = a % 42
    n.append(b)
s = set(n)

# ----------------------------------------------------------------


# TODO: 평균
# ----------------------------------------------------------------
"""
문제
만종이는 기말고사를 망쳤다. 만종이는 점수를 조작해서 집에 가져가기로 했다. 
일단 만종이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 
그리고 나서 모든 점수를 점수/M*100으로 고쳤다.

예를 들어, 만종이의 최고점이 70이고, 
수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.

세준이의 성적을 위의 방법대로 새로 계산했을 때,
새로운 평균을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 시험 본 과목의 개수 N이 주어진다.
값은 1000보다 작거나 같다. 둘째 줄에 세준이의 현재 성적이 주어진다.
이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.

출력
첫째 줄에 새로운 평균을 출력한다. 
실제 정답과 출력값의 절대오차 또는 상대오차가 10-2 이하이면 정답이다.
"""

a: int = int(input())
b: list = list(map(int, input().split()))
c: max = max(list)

# ----------------------------------------------------------------

# TODO: OX 퀴즈
# ----------------------------------------------------------------
"""
문제
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, 
X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 
예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고,
길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.

출력
각 테스트 케이스마다 점수를 출력한다.
"""

a: int = int(input())  # for문 최댓값 설정
for _ in range(a):  # 받는 값 없이 a 만큼 루프
    b: list = list(input())  # 입력받을 리스트문
    score: int = 0  # 카운트 값
    sum_score: int = 0  # 입력 받을 점수
    for i in b:  # 리스트 b 에서 탐색합니다.
        if i == '0':  # 조건문
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)

a: int = int(input())
for _ in range(a):
    b: list = list(input())
    score: int = 0
    sum_score: int = 0
    for i in b:
        if i == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)

# ----------------------------------------------------------------


# TODO: 평균은 넘겠지
# ----------------------------------------------------------------
"""
문제
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

입력
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 
이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
"""
count: int = int(input())
for _ in range(count):
    count2: list = list(map(int, input().split()))
    avg = sum(count2[1:]) / count2[0]
    cnt = 0
    for score in count2[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수
    rate = cnt / count2[0] * 100
    print(f'{rate:.3f}%')

# ----------------------------------------------------------------


# TODO: 아스키 코드
# ----------------------------------------------------------------
"""
문제
알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

입력
알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.

출력
입력으로 주어진 글자의 아스키 코드 값을 출력한다.
"""
a = input()
print(ord(a))
# ----------------------------------------------------------------


# TODO: 알파벳 찾기
# ----------------------------------------------------------------
"""
문제
알파벳 소문자로만 이루어진 단어 S가 주어진다. 
각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

출력
각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, 
... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 
단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.
"""
S = input()
arr = list(range(97, 123))

for i in arr:
    print(S.find(chr(i)))
# ----------------------------------------------------------------


# TODO: 행렬 덧셈
# TODO:
# ----------------------------------------------------------------
"""
문제
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

입력
첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

출력
첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.
"""
n, m = map(int, input().split())
a, b = [], []
for i in [a, b]:
    for j in range(n):
        i.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]
    print(*a[i])
# ----------------------------------------------------------------

# TODO: 문자열 반복
# ----------------------------------------------------------------
"""
문제
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

출력
각 테스트 케이스에 대해 P를 출력한다.
"""

t = int(input())
for i in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)
# ----------------------------------------------------------------


# TODO: 피보나치 수 5
# ----------------------------------------------------------------
"""
문제
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 
그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 n번째 피보나치 수를 출력한다.

 피보나치 함수를 정의해 사용한다.
• n이 0일때는 0, n이 1일때는 1이므로 n<=1 일때는 n을 반환한다.
• 피보나치 수는 앞의 두 피보나치 수의 합이다.
• 따라서, n번째 피보나치 수는 (n-1)과 (n-2)의 합이 된다.
"""


def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)  # 앞 두 수의 합


n = int(input())
print(fibo(n))

# ----------------------------------------------------------------


# TODO: 덩치
# ----------------------------------------------------------------
"""
문제
우리는 사람의 덩치를 키와 몸무게, 이 두 개의 값으로 표현하여 그 등수를 매겨보려고 한다. 
어떤 사람의 몸무게가 x kg이고 키가 y cm라면 이 사람의 덩치는 (x, y)로 표시된다.
두 사람 A 와 B의 덩치가 각각 (x, y), (p, q)라고 할 때 x > p 
그리고 y > q 이라면 우리는 A의 덩치가 B의 덩치보다 "더 크다"고 말한다. 
예를 들어 어떤 A, B 두 사람의 덩치가 각각 (56, 177), (45, 165) 라고 한다면 A의 덩치가 B보다 큰 셈이 된다. 
그런데 서로 다른 덩치끼리 크기를 정할 수 없는 경우도 있다. 
예를 들어 두 사람 C와 D의 덩치가 각각 (45, 181), (55, 173)이라면 몸무게는 D가 C보다 더 무겁고, 
키는 C가 더 크므로, "덩치"로만 볼 때 C와 D는 누구도 상대방보다 더 크다고 말할 수 없다.

N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해진다. 
만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다.
이렇게 등수를 결정하면 같은 덩치 등수를 가진 사람은 여러 명도 가능하다.
아래는 5명으로 이루어진 집단에서 각 사람의 덩치와 그 등수가 표시된 표이다.

이름	(몸무게, 키)	덩치 등수
A	(55, 185)	2
B	(58, 183)	2
C	(88, 186)	1
D	(60, 175)	2
E	(46, 155)	5
위 표에서 C보다 더 큰 덩치의 사람이 없으므로 C는 1등이 된다. 
그리고 A, B, D 각각의 덩치보다 큰 사람은 C뿐이므로 이들은 모두 2등이 된다. 
그리고 E보다 큰 덩치는 A, B, C, D 이렇게 4명이므로 E의 덩치는 5등이 된다. 
위 경우에 3등과 4등은 존재하지 않는다. 
여러분은 학생 N명의 몸무게와 키가 담긴 입력을 읽어서 각 사람의 덩치 등수를 계산하여 출력해야 한다.

입력
첫 줄에는 전체 사람의 수 N이 주어진다. 
그리고 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.

출력
여러분은 입력에 나열된 사람의 덩치 등수를 구해서 그 순서대로 첫 줄에 출력해야 한다. 
단, 각 덩치 등수는 공백문자로 분리되어야 한다.
"""
n = int(input())
data = []
ans = []
for i in range(n):
    a, b = map(int, input().split())
    data.append((a, b))

for i in range(n):
    count = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:  # 몸무게와 키 모두 자신보다 큰 사람의 수를 센다
            count += 1
    ans.append(count + 1)
for d in ans:
    print(d, end=" ")
# ----------------------------------------------------------------


# TODO: 단어 공부
# ----------------------------------------------------------------
"""
문제
알파벳 대소문자로 된 단어가 주어지면,
이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 
주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
"""
# 1.
words = input().upper()
unique_words = list(set(words))
# 입력받은 문자열에서 중복값을 제거
# 입력 받은 문자열 중 중복 되는 요소는 set 함수를 이용해서 제거했다.
# 요소만 남긴 리스트는 unique_words라는 벼수에 선언
cnt_list = []
for x in unique_words:
    cnt = words.count(x)
    cnt_list.append(cnt)
# count 숫자를 리스트에 append
# 입력받은 문자열에 같은 알파벳이 몇 개 있는지 숫자 카운트 해서 cnt_list 리스트에 추가한다.
if cnt_list.count(max(cnt_list)) > 1:
    # count 숫자 최대값이 중복되면
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])
# 숫자 리스트에서 알파벳이 사용된 개수 중 가장 큰 수를 찾고서 해당 숫자가 1보다 크면 물음표에 출력한다.
# 최댓값이 하나라면 숫자 리스트에서 가장 큰 수의 위치를 index함수로 찾고서 unique_words리스트에 같은 인덱스에 위치한 문자열 출력
# ----------------------------------------------------------------


# TODO:엄청난 부자2
# ----------------------------------------------------------------
"""
문제
갑부 최백준 조교는 동전을 최소로 바꾸는데 성공했으나 김재홍 조교가 그 돈을 발견해서 최백준 조교에게 그 돈을 나누자고 따진다.
그 사실이 전 우주로 알려지자 우주에 있던 많은 생명체들이 자신들에게 돈을 분배해 달라고 당장 달려오기 시작했다.
프로토스 중앙 우주 정부의 정책인, ‘모든 지적 생명체는 동등하다’라는 규칙에 입각해서 돈을 똑같이 분배하고자 한다.

한 생명체에게 얼마씩 돈을 줄 수 있는가?
또, 생명체들에게 동일하게 분배한 후 남는 돈은 얼마인가?

입력
첫째 줄에는 최백준 조교가 가진 돈 n과 돈을 받으러 온 생명체의 수 m이 주어진다. (1 ≤ m ≤ n ≤ 101000, m과 n은 10진수 정수)

출력
첫째 줄에 생명체 하나에게 돌아가는 돈의 양을 출력한다. 그리고 두 번째 줄에는 1원씩 분배할 수 없는 남는 돈을 출력한다.
"""

a, b = map(int, input().split())
print(a // b)
print(a % b)
# ----------------------------------------------------------------


# TODO: 별 찍기 - 3
#
# ----------------------------------------------------------------
"""
*****
****
***
**
*
"""
#   range(Start, end, step)
a: int = int(input())
for i in range(a, 0, -1):
    print("*" * i)
# ----------------------------------------------------------------


# TODO:명령 프롬프트
# ----------------------------------------------------------------
"""
문제
시작 -> 실행 -> cmd를 쳐보자. 
검정 화면이 눈에 보인다. 여기서 dir이라고 치면 그 디렉토리에 있는 서브디렉토리와 파일이 모두 나온다.
 이때 원하는 파일을 찾으려면 다음과 같이 하면 된다.

dir *.exe라고 치면 확장자가 exe인 파일이 다 나온다. 
"dir 패턴"과 같이 치면 그 패턴에 맞는 파일만 검색 결과로 나온다.
예를 들어, dir a?b.exe라고 검색하면 파일명의 첫 번째 글자가 a이고,
세 번째 글자가 b이고, 확장자가 exe인 것이 모두 나온다.
이때 두 번째 문자는 아무거나 나와도 된다.
예를 들어, acb.exe, aab.exe, apb.exe가 나온다.

이 문제는 검색 결과가 먼저 주어졌을 때,
패턴으로 뭘 쳐야 그 결과가 나오는지를 출력하는 문제이다
패턴에는 알파벳과 "." 그리고 "?"만 넣을 수 있다.
가능하면 ?을 적게 써야 한다.
 
그 디렉토리에는 검색 결과에 나온 파일만 있다고 가정하고, 파일 이름의 길이는 모두 같다.

입력
첫째 줄에 파일 이름의 개수 N이 주어진다.
둘째 줄부터 N개의 줄에는 파일 이름이 주어진다.
N은 50보다 작거나 같은 자연수이고 파일 이름의 길이는 모두 같고 길이는 최대 50이다.
파일이름은 알파벳 소문자와 '.' 로만 이루어져 있다.

출력
첫째 줄에 패턴을 출력하면 된다.
"""
N = int(input())
first_word = list(input())
first_word_len = len(first_word)

for i in range(N - 1):
    other_words = list(input())
    for j in range(first_word_len):
        if first_word[j] != other_words[j]:
            first_word[j] = '?'

print(''.join(first_word))

# ----------------------------------------------------------------


# TODO: 정수 N개의 합
# ----------------------------------------------------------------
"""
문제
정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.

작성해야 하는 함수는 다음과 같다.
Python 2, Python 3, PyPy, PyPy3: def solve(a: list) -> int
a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
리턴값: a에 포함되어 있는 정수 n개의 합 (정수)
"""


def solve(a):
    return sum(a)


# ----------------------------------------------------------------


# TODO: 분산 처리
# ----------------------------------------------------------------
"""
문제
재용이는 최신 컴퓨터 10대를 가지고 있다.
어느 날 재용이는 많은 데이터를 처리해야 될 일이 생겨서 각 컴퓨터에 1번부터 10번까지의 번호를 부여하고, 
10대의 컴퓨터가 다음과 같은 방법으로 데이터들을 처리하기로 하였다.

1번 데이터는 1번 컴퓨터, 2번 데이터는 2번 컴퓨터, 3번 데이터는 3번 컴퓨터, ... ,
10번 데이터는 10번 컴퓨터, 11번 데이터는 1번 컴퓨터, 12번 데이터는 2번 컴퓨터, ...

총 데이터의 개수는 항상 ab개의 형태로 주어진다. 
재용이는 문득 마지막 데이터가 처리될 컴퓨터의 번호가 궁금해졌다. 
이를 수행해주는 프로그램을 작성하라.

입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 
그 다음 줄부터 각각의 테스트 케이스에 대해 정수 a와 b가 주어진다. (1 ≤ a < 100, 1 ≤ b < 1,000,000)

출력
각 테스트 케이스에 대해 마지막 데이터가 처리되는 컴퓨터의 번호를 출력한다.
"""

# ?


# ----------------------------------------------------------------


# TODO:대소문자 바꾸기
# ----------------------------------------------------------------
"""
문제
영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 영어 소문자와 대문자로만 이루어진 단어가 주어진다. 단어의 길이는 최대 100이다.

출력
첫째 줄에 입력으로 주어진 단어에서 대문자는 소문자로, 소문자는 대문자로 바꾼 단어를 출력한다.
"""
a = input()
print(a.swapcase())
# ----------------------------------------------------------------


# TODO:학점계산
# ----------------------------------------------------------------
"""
문제
어떤 사람의 C언어 성적이 주어졌을 때, 평점은 몇 점인지 출력하는 프로그램을 작성하시오.

A+: 4.3, A0: 4.0, A-: 3.7
B+: 3.3, B0: 3.0, B-: 2.7
C+: 2.3, C0: 2.0, C-: 1.7
D+: 1.3, D0: 1.0, D-: 0.7
F: 0.0

풀이
딕셔너리를 이용해 풀었다.
딕셔너리는 사전처럼 2개의 요소를 하나로 묶어 표현한 자료형이다.
"""
dic = {'A+': '4.3', 'A0': '4.0', 'A-': '3.7',
       'B+': '3.3', 'B0': '3.0', 'B-': '2.7',
       'C+': '2.3', 'C0': '2.0', 'C-': '1.7',
       'D+': '1.3', 'D0': '1.0', 'D-': '0.7',
       'F': '0.0'}
grade = input()
print(dic[grade])

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
# TODO:
# ----------------------------------------------------------------
"""

"""

# ----------------------------------------------------------------
