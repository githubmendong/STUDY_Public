import sys
input = sys.stdin.readline

L = int(input())
A = int(input()) 
B = int(input()) 
C = int(input()) 
D = int(input()) 

if A % C == 0 :
    num1 = A//C
else :
    num1 = (A//C) + 1

if B % D == 0 :
    num2 = B//D

else :
    num2 = (B//D) + 1

num = max(num1, num2)

print(L - num)