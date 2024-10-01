#Assignment 2

#Task 1

while True:
    try:
        a, b, c = map(int, input("Enter three whole numbers separated by spaces: ").split())
        break
    except ValueError:
        print("Please enter three whole numbers separated by spaces.")
    
print (f"The largest number is {max(a, b, c)}.")

#Task 2

while True:
    try:
        a, b, c = map(int, input("Enter three whole numbers separated by spaces: ").split())
        break
    except ValueError:
        print("Please enter three whole numbers separated by spaces.")

print (f"The smallest number is {min(a, b, c)}. The largest number is {max(a, b, c)}.")