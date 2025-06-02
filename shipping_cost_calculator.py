# Sipping Cost Calculator

## Input package wiehgt and shipping
weight = float(input("Enter the package wieght in kilograms: "))
rate = float(input("Enter the shipping rate per kilograms: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display thee result
print(f"Shipping Cost: {shipping_cost} USD")
