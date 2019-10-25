
t=int(input())
for ll in range(t):
    n,m,k=map(int,input().split(' '))
    str1=input()
    str2=input()
    
    sub1 = [str1[i:i+k] for i in range(len(str1)-k+1)]
    sub2 = [str2[i:i+k] for i in range(len(str2)-k+1)]
    
    dict1 = {}
    dict2 = {}
    
    # Using dict as uses Hash values internally
    for s in sub1:
        try:
            dict1[s]+=1
        except:
            dict1[s]=1
            
    for s in sub2:
        try:
            dict2[s]+=1
        except:
            dict2[s]=1
    da =  (dict1,dict2) if len(dict1)<len(dict2) else (dict2,dict1)
    dc = {}
    
    for i in da[0].keys():
        try:
            dc[i] = da[0][i] + da[1][i]
        except:
            pass
    
    if len(dc)<1:
        print(-1)
    else:
        
        ans_list = [i for i, value in enumerate(dc.values()) if value == max(dc.values())] 
        
        if len(ans_list)==1:
            print(list(dc.keys())[ans_list[0]])
            
        else:
            abc=list(dc.keys())
            min_string = abc[0]
            for i in abc:
                if min_string>i:
                    min_string=i
            print(min_string)
        
    
    
