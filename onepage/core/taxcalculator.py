#The logic for calculating the output of a salary, by applying the relavent tax band to the input
import itertools

def calculateTaxedSalary(salary):
    output = 0
    band = ""
    if salary <= 12500 and salary >= 0:
        output = salary
        band = "Personal Allowance"
    elif salary >= 12501 and salary <= 50000:
        output = salary*0.8
        band = "Basic Rate"
    elif salary >= 50001 and salary <=150000:
        output= salary*0.6
        band = "Higher Rate"
    elif salary > 150000:
        output = salary*0.55
        band = "Additional Rate"
    return str("{:.2f}".format(output))
    
# A query class ( or model in django) to store the output data from salary calculator
class Query():

    def __init__(self,taxedsalary,band):
        self.id = id
        self.taxedsalary = taxedsalary
        self.band = band

