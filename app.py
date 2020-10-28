# test project, app.py
# Emily Bacatan 10/23/2020

from flask import Flask
from flask import render_template, request

app = Flask(__name__)

#loan calculator
#Loan amount (A)
#Number of periodic payments (n) = payments per year * number of years
#Periodic interest rate (i) = annual rate / number of payment periods
#
#Discount Factor (D) = ((( 1 + i ) ^n ) - 1 ) / ( i ( 1+ i) ^n)
#
#
#A = $100,000
#n = 360 (30 years * 12 monthly payments)
#i = .005 (.06 / 12 monthly payments)
#D=166.7916 (((1+.005)^360)-1)/(.005(1+.005)^360))
#Loan payment (P) = A / D = $599.55 (in this case monthly payment)

class Loan:
    def __init__(self, loanAmount, numberYears, annualRate):
        self.loanAmount = loanAmount
        self.annualRate = annualRate
        self.numberOfPmts = numberYears * 12 #monthly pmts
        self.periodicIntRate = self.annualRate / 12
        self.discountFactor = 0.0
        self.loanPmt = 0
        
    def getDiscountFactor(self):
        return self.discountFactor
    
    def calculateDiscountFactor(self):
        self.discountFactor = (((1.0 + self.periodicIntRate) ** self.numberOfPmts) - 1.0) / (self.periodicIntRate * (1.0 + self.periodicIntRate) ** self.numberOfPmts)
        
    def calculateLoanPmt(self):
        self.calculateDiscountFactor()
        self.loanPmt = self.loanAmount / self.getDiscountFactor()
        
    def getLoanPmt(self):
        return self.loanPmt
        
        



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mnthlyPmt', methods=['POST'])
def mnthlyPmt():
    if request.method == 'POST':
        form = request.form
        loanAmt = float(form['loanAmt'])
        numberYears = float(form['lengthOfLoan'])
        annualRate = float(form['intRate'])

        loan = loan(loanAmt, numberYears, annualRate)

        loan.calculateLoanPmt()

        mnthlyLoanPmt = loan.getLoanPmt()

        print(mnthlyLoanPmt)

        return render_template('index.html', mnthlyPmt = mnthlyLoanPmt)
    return render_template('index.html')  

if __name__ == '__main__':
    app.run(debug=True)
