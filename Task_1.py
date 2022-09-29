def getMultipliers(digit):
    result = []
    cicle = True

    while(cicle):
        for i in range(2, 10):
            if (str(digit / i).split(".")[1] == "0" and not result.__contains__(i)):
                result.append(i)
                if (digit / i > 9):
                    digit /= i
                    break
                else:
                    result.append(int(digit / i))
                    cicle = False
                    break
    return result

print(getMultipliers(25))