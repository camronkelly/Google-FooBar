def solution(l, t):
    # Your code here
    start_index = -1
    end_index = -1
    running_count = 0
    for i in range(len(l)):
        running_count=l[i]
        start_index = i
        if(running_count == t):
            end_index = i
            break
        if(running_count > t):
            continue
        for j in range(i+1,len(l)):
            running_count+=l[j]
            if(running_count == t):
                end_index = j
                break
            if(running_count > t):
                break
        if(running_count == t):
            break
    if(running_count == t):
        return [start_index, end_index]
    else:
        return [-1,-1]

def solution2(l,t):
    sum = 0
    left_index = 0
    for right_index in range(len(l)):
        sum+=l[right_index]
        while(sum > t):
            sum-=l[left_index]
            left_index+=1
            #if left_index==right_index:
            #    break
        if(sum == t):
            return([left_index, right_index])
    return([-1,-1])

print(solution2([16],6))