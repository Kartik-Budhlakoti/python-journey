# !/bin/bash

greet(){
    local name=$1   #    $1 is the 1st argument passed to this function
    local age=$2   #    $2 is the 2nd argument passed to this function
    echo "Hello $name , you are $age years old"
}

# Calling a function
greet "kartik" 20
greet  "karma"  28

#  Function with return value (can only return numbers (exit codes))
#  to return string use echo
get_file_count() {
    local directory=$1
    local count=$(ls "$directory" | wc -l)
    echo "$count"
}
sher=$(get_file_count "/home/kartik007/Desktop/python-new/python-journey")
echo "Files in project: $sher"

echo "Script name : $0"  # $0 is the script name itself
echo "Number of arguments : $#"  # $# is the number of args
echo "All arguments: $@"    #  $@ is all arguments as list   

# always validate arguments at the start of a script
if [ $# -eq 0 ]; then
    echo "Usage: $0 <directory_path>"
    echo "Example: $0 /home/kartik007/Desktop"
    exit 1     #  exit with error code
fi

#  Now using argument safely
shera() {
    target_dir=$1
    if [ ! -d "$target_dir" ]; then
        echo "Error: $target_dir is not a valid directory"
        exit 1
    fi
}
shera "/home/kartik007/Desktop/python-new/python-journey/month2"
shera "/home/kartik007/Desktop/python-new/python-journey/README.md"

target_dir=$1
echo "Listing Python files in: $target_dir"
for file in "$target_dir"/*.py; do
    if [ -f "$file" ]; then
        size=$(wc -c < "$file")
        echo "  $(basename $file): $size bytes"
    fi
done
exit 0