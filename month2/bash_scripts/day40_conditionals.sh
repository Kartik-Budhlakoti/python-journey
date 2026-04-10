#!/bin/bash


# iterating over the list
for fruit in apple banana mango orange; do 
    echo "Fruit: $fruit"
done
# using range
for i in {1..5}; do
    echo "NUmber : $i"
done

echo "Python files inn project directory : " # Using week1 cause currently it has more .py files
for file in /home/kartik007/Desktop/python-new/python-journey/week1/*.py; do
    if [ -f "$file" ]; then
        filename=$(basename "$file") # basename is used to strip the directorypath from the file
        echo "  $filename"
    fi
done

count=1
while [ $count -le 7 ]; do # value or length of count should be 7 as in 1-7
    echo "Count : $count"
    count=$((count + 1)) # incrementing value of count and resending it to the while condition
done

# while loop reading a file line by line
# create a test file first
echo -e "line one\nline two\nline three" > /tmp/test_lines.txt

while IFS= read -r line; do
    echo "Read: $line"
done < /tmp/test_lines.txt

# Loop with break and continue
for i in {1..10}; do
    if [ $i -eq 3 ]; then
        continue
    fi
    if [ $i -eq 7 ]; then
        break
    fi
    echo "i : $i"
done
