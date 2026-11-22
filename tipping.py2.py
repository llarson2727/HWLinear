from fitting_fxns import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.genfromtxt("tips.csv", delimiter=",", skip_header=1)

bill = data[:, 0]
tip = data[:, 1]
pct_tip = data[:, 6]

print(bill[:5])
print(tip[:5])
print(pct_tip[:5])

# Graph 1: Bill vs Tip

plt.scatter(bill, tip)
plt.xlabel("Bill ($)")
plt.ylabel("Tip ($)")
plt.title("Bill vs Tip")
# Fit a line to Bill vs Tip
popt, pcov = curve_fit(linear, bill, tip)

m = popt[0]
b = popt[1]

plt.plot(bill, linear(bill, m, b), color="red")

print_equation(m, b, "dollars", "dollars")
#y = 0.1822147334760305 dollar/dollar + -0.2922674321861712 dollars

plt.show()

plt.figure()
plt.scatter(bill, pct_tip)
plt.xlabel("Bill ($)")
plt.ylabel("PctTip (%)")
plt.title("Bill vs PctTip")

popt2, pcov2 = curve_fit(linear, bill, pct_tip)

m2=popt2[0]
b2=popt2[1]

plt.plot(bill, linear(bill, m2, b2), color="red")

print_equation(m2, b2, "percent", "dollars")

plt.show()

# percent tip inreases slightly as bill inreases
# the relationship is weak because the data is scattered
