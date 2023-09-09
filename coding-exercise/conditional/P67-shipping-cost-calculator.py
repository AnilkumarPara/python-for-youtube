"""
Write a program that calculates the shipping cost for an online order based on the
total order value. Apply a 10% shipping fee if the order value is below $50;
otherwise, offer free shipping.
"""
total_order = float(input("Enter the total order value"))

if 0 < total_order < 50:
    print(f"shipping cost : ${total_order * 0.1}")
elif total_order >= 50:
    print("Shipping is free")
else:
    print("Invalid total order value, please re-enter again")
