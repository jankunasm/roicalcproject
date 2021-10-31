class RoiCalculator:


    def __init__(self):
        self.value = 0


    def InfoInpInc(self):
        while True:
            try:
                input1 = int(float(input("Please enter your Total Monthly Income from the property.: ")))
                self.value += input1
                break
            except ValueError:
                print("Pleaase enter a valid number instead.")

    def InfoInpExp(self):
        while True:
            try:
                input2 = int(float(input("Please enter your Total Monthly Expenses from the property.: ")))
                self.value += input2
                break
            except ValueError:
                print("Pleaase enter a valid number instead.")

    def InfoInpTotInv(self):
        while True:
            try:
                input3 = int(float(input("Please enter your Total Investment on the property.: ")))
                self.value += (input3)
                break
            except ValueError:
                print("Pleaase enter a valid number instead.")


income = RoiCalculator()

expenses = RoiCalculator()

total_inv = RoiCalculator()


def run():

    income.InfoInpInc()
    expenses.InfoInpExp()
    cash_flow = income.value - expenses.value
    print(f"Your Monthly Cash Flow is: ${cash_flow}. ")
    annual_cash_flow = cash_flow * 12
    total_inv.InfoInpTotInv()
    roi= annual_cash_flow / total_inv.value
    finalcalc= roi * 100
    print(f"Your Total Monthly Income is: ${income.value}. ")
    print(f"Your Total Monthly Expenses are: ${expenses.value}. ")
    print(f"Your Total Investment in this property is: ${total_inv.value}. ")
    print(f"Your Return on Investment on this property is {finalcalc}%.")

run()