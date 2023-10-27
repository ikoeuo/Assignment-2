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
        self.stockL +=  self.monthlyUnitsM - unitsS

    def stockS(self, months):
        stockStatement = f"Product Code: {self.code}\nProduct Name: {self.name}\n"
        stockStatement += f"Sale Price: {self.saleP}\nManufacture Cost: {self.costM}\n"

        totalUnitsS = 0
        totalUnitsM = 0
        profit = 0
 
        for month in range(1, months + 1):
            unitsS = self.simulateMonthlySales()
            totalUnitsS += unitsS
            totalUnitsM += self.monthlyUnitsM
            profit += (unitsS * self.saleP) - (self.monthlyUnitsM * self.costM)
            stockStatement = f"\nMonth {month}: Stock Level = {self.stockL}, Units Sold = {unitsS}\n"
            
        stockStatement += f"Total Units Sold: {totalUnitsS}\n"
        stockStatement += f"Total Units Manufactured: {totalUnitsM}\n"
        stockStatement += f"Net Profit/Loss: {profit}\n"

        return stockStatement 
    
  