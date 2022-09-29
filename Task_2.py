
testList = [1,1,1,1,2,2,2,3,3,3,4]

def Numbers(list):
    result = []

    for i in list:
        if (not result.__contains__(i)): #Проверяем повторения в списке 
            result.append(i)
    return result

print(Numbers(testList))