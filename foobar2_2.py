def solution(xs):
    # Your code here
    num_zeros = 0
    num_negatives = 0
    smallest_negative = -1001
    product = 1


    for i in range(len(xs)):
        if(xs[i] == 0):
            num_zeros+=1
            continue
        if(xs[i] < 0):
            num_negatives+=1
            if(xs[i] > smallest_negative):
                smallest_negative = xs[i]
        product *= xs[i]
            
    if((num_zeros) >= (len(xs)-1)):
        if(num_negatives % 2 == 1 or num_zeros == len(xs)):
            return str(0)
        else:
            return str(product)
    else:
        if(num_negatives %2 == 1):
            return str(product/smallest_negative)
        else:
            return str(product)
    # negArr = 0
    # product = 1
    # for number in xs:
    #     if number < 0:
    #         negArr+=1
    # xs.sort()
    # if not xs:
    #     return 0
    # if len(xs)==1:
    #     return xs[0]
    # while 0 in xs:xs.remove(0)
    # if negArr%2 !=0:
    #     xs.pop(negArr-1)
    # for x in xs:
    #     product *=x
    # if len(xs)==0:
    #     return str(0)
    # else:
    #     return str(product)
tests = [[-100],[100],[0]]
test2 = []
for i in range(50):
    test2.append(1000)
for i in range(len(tests)):
   print(solution(tests[i]))
print(solution(test2))