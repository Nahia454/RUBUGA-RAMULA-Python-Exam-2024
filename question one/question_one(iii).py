def calculate_operations(num1, num2):
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    
    if num2 != 0:
        quotient_result = num1 / num2
    else:
        quotient_result = "Error: Division by zero"
    
    return {
        "sum": sum_result,
        "difference": difference_result,
        "product": product_result,
        "quotient": quotient_result
    }
result = calculate_operations(15, 5)
print("Sum:", result["sum"])
print("Difference:", result["difference"])
print("Product:", result["product"])
print("Quotient:", result["quotient"])




