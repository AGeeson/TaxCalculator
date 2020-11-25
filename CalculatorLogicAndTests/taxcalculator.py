#The logic for calculating the output of a salary, by applying the relavent tax band to the input

def calculateTaxedSalary(salary):
    output = 0
    if salary <= 12500 and salary >= 0:
        output = salary
    elif salary >= 12501 and salary <= 50000:
        output = salary*0.8
    elif salary >= 50001 and salary <=150000:
        output= salary*0.6
    elif salary > 150000:
        output = salary*0.55
    return str("{:.2f}".format(output))
    


