def checkPrimeNumber(data):
    if (data.isnumeric() != True or int(data) < 0):
        return "Provided data is of the string type, or it is negative!"
    else:
        checkSum = 0
        for i in range(1, int(data)+1):
            if int(data) % i == 0:
                checkSum += 1
                if checkSum >= 3:
                    return "Provided number is not a prime numebr."
        if checkSum == 2:
            return "Provided number is a prime number."
        else:
            return "Provided number is not a prime number."