for _ in range(int(input())):
    n = int(input())
    dc = {"1":0,"0":0,"01":0}
    for i in range(n):
        st = set(list(input()))
        if len(st)==1:
            dc[st.pop()]+=1
        else:
            dc["01"]+=1
    a = ((dc["0"]-1)*dc["0"])//2
    b = ((dc["1"]-1)*dc["1"])//2
    c = a+b+dc["01"]
    c = (c-1)*(c)//2
    print(a+b+c)