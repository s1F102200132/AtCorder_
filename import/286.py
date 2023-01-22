N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
B = A.copy()
 
for i, j in zip(range(P-1, Q),range(R-1, S)):
    B[i] = A[j]
    B[j] = A[i]
print(*B)

#unpack
def foo(i, j, k):
    print(f"i = {i}, j= {j}, k= {k}")

L = ['Hello', 'World', 'Python']
foo(*L)

print(*range(0,5))
