import random

class Product:
    def __init__(self, code, name, saleP, costM, stockL, monthlyUnitsM):
        self.code = code
        self.name = name
        self.saleP = saleP
        self.costM = costM
        self.stockL = stockL
        self.monthlyUnitsM = monthlyUnitsM 

    def simulateMonthlySales(self):
        unitsM = random.randint(self.monthlyUnitsM - 10, self.monthlyUnitsM + 10 )
        unitsS = random.randint(0,unitsM)
        stockL +=  unitsM - unitsS

    def stockS(self, month):
        stockS = f"Product Code: {self.code}\nProduct Name: {self.name}\n"
        stockS += f"Sale Price: {self.saleP}\nManufacture Cost: {self.costM}\n"

        totalUnitsS = 0
        totalUnitsM = 0
        profit = 0
 
        for month in range(1, month +1):
            unitsS = self.simulateMonthlySales()
            tatalUnitsS += unitsS
            total_units_manufactured += self.monthlyUnitsM
            profit += (unitsS * self.saleP) - (self.unitsM * self.costM)
            stockStatement += f"Month {month}: Stock Level = {self.stockL}, Units Sold = {unitsS}\n"

        stockStatement += f"Total Units Sold: {totalUnitsS}\n"
        stockStatement += f"Total Units Manufactured: {totalUnitsM}\n"
        stockStatement += f"Net Profit/Loss: {profit}\n"

        return stockStatement 
    
    


        