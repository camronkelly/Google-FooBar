def solution(x,y):
    # Your code here
   
    if(x == '1' and y == '1'):
        return '0'
    m = int(x)
    f = int(y)
    count = 0
    
    while(m > 1 or f > 1):
        if (m > f):
            temp = divmod(m,f)
            m = temp[1]
        else:
            temp = divmod(f,m)
            f = temp[1]
        
        count+=temp[0]
        
        if(temp[1]==0 and m != 1 and f != 1):
            return "impossible"
    return str(count-1)
print(solution('4','7'))
print(solution(7,4))
print(solution(7,7))
print(solution(1,7))
print(solution(7,1))
print(solution(2,4))
print(solution('1','1'))