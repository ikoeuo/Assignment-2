from Assignment2 import Product 


def main():
    code = int(input("Enter Product Code (100-10000): \n"))
    name = input("Enter Product Name: \n")
    saleP = float(input("Enter Product Sale Price, must be greater than 0: \n"))
    costM = float(input("Enter Product Manufacture Cost, must be greater than 0: \n"))
    stockL = int(input("Enter Stock Level, must be greater than 0: \n"))
    monthlyUnitsM = int(input("Enter Monthly Units Manufactured, must be greater than or equal to 0: \n"))

    print(f'\nProduct code: {code}')
    print(f'Product Name: {name}')
    print(f'\nSale Price: {saleP} CAD')
    print(f'Manufacture Cost: {costM} CAD')
    print(f'Monthly Production: {monthlyUnitsM} units (Approx.)\n')

    if 100 <= code <= 10000 and saleP > 0 and costM > 0 and stockL > 0 and monthlyUnitsM >= 0:
        product1 = Product(code, name, saleP, costM, stockL, monthlyUnitsM)
        months = 12  

        stockStatement = product1.stockS(months)
        print(f"\nPredicted Stock Statement for the Next {months} Months: ")
        print(stockStatement)

    else:
        print("Invalid input. Please make sure all input values are within the specified ranges.")


main()