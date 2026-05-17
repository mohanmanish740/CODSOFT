first_number_value = float(input("Enter first number: "))
second_number_value = float(input("Enter second number: "))


operation_choice_symbol = input("Enter operation (+, -, *, /): ")

if operation_choice_symbol == "+":
    calculation_result_output = first_number_value + second_number_value

elif operation_choice_symbol == "-":
    calculation_result_output = first_number_value - second_number_value

elif operation_choice_symbol == "*":
    calculation_result_output = first_number_value * second_number_value

elif operation_choice_symbol == "/":
    if second_number_value != 0:
        calculation_result_output = first_number_value / second_number_value
    else:
        calculation_result_output = "Error: Division by zero!"

else:
    calculation_result_output = "Invalid operation!"


print("Result:", calculation_result_output)