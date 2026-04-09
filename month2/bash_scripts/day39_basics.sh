#!/bin/bash

echo "Hello World!!"

# Check for the indentations:-:-:-
name='Kartik'
echo ${name}
age=20

echo "Hello I am $name"
echo "I am $age years old"

pwd

current_dir=$(pwd)
current_date=$(date)
echo "I am in: $current_dir"
echo "Current date is: $current_date"

#  For arithmatic -  must use $(( )) for math
a=10
b=3
# echo $PATH
echo "Sum: $((a + b))"
echo "Difference: $((a - b))"
echo "Product: $((a * b))"
echo "Division: $((a / b))"
echo "Remainder: $((a % b))"

echo "What is your college name ? "
read college
echo "Oh! you are from $college college , Good for you."

# Differnt brackets to determine the length
name_length=${#name}
echo "Name length: $name_length"


