# 
# Name Luis GIL
# Date 09/06/24
# Sales Tax Programming Project
# COSC 2409 DNT
#

# Variable declarations

# Constants for the state and county tax rates
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025
# Get the amount of the purchase.
purchase_amount = float(input("Enter the purchase ammount: "))
# Calculate the state sales tax.
state_tax = purchase_amount * STATE_TAX_RATE
# Calculate the county sales tax.
county_tax = purchase_amount * COUNTY_TAX_RATE
# Calculate the total tax.
total_tax = state_tax + county_tax
# Calculate the total of the sale.
total_sale = purchase_amount + total_tax
# Print information about the sale.
print(f"Purchase Amount: ${purchase_amount:.2f}")
print(f"State Tax: ${state_tax:.2f}")
print(f"County Tax: ${county_tax:.2f}")
print(f"Total Tax: ${total_tax:.2f}")
print(f"Total Sales: ${total_sales:.2f}")