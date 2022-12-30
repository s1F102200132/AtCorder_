N,T = map(int,input().split())
A = list(map(int,input().split()))
total_time = sum(A)
diff = T % total_time

for i, ai in enumerate(A):
    if diff < ai:
        print(i + 1,diff)
        exit()
    else:
        diff -= ai
            
    


