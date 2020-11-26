import unittest

def calculateTaxedSalary(salary):
    temp = salary
    print("1 temp is " + str(temp))
    output=0
    bands = [
        [12500, 1.0, "Personal Allowance"], 
        [37500, 0.8, "Basic Rate"], 
        [100000, 0.6, "Higher Rate"], 
        [0,0.55, "Additional Rate"]
        ]
    amountTaxedPerBand =[]
    i=0
    while i < len(bands):
        if temp > bands[i][0]:
            maxoutputFromBand = bands[i][0]*bands[i][1]
            output += (bands[i][0]*bands[i][1])
            temp -= bands[i][0]
            amountTaxedString = "Amount taxed in band: " + bands[i][2] + " is: " + str(bands[i][0] - (bands[i][0]*bands[i][1]))
            amountTaxedPerBand.append(amountTaxedString)
            print (amountTaxedPerBand[i])
            i += 1
        else:
            output += (temp*(bands[i][1]))
            break
    output = "{:.2f}".format(output)  
    print("Estimated take-home pay is " + str(output))  
    return output

            


class TaxCalcTest(unittest.TestCase):

    def test_allbands(self):
        self.assertEqual(calculateTaxedSalary(200000), '102500.00')

if __name__ == '__main__':
    unittest.main()

