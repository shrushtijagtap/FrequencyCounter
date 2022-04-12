# i/p: 111223333
# o/p: 312243

def pattern(str):
    op_str=[]
    temp=None
    for i in str:
        if i!=temp:
            temp = i
            count=0

            for j in range(i, len(str)):
                if str[j]==temp:
                    count+=1
                else:
                    break

            op_str.append(count)
            op_str.append(temp)

    return op_str


str = "111223333"
print(pattern(str))
