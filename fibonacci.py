#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

def fibonacci_sequence(n):
    
    sequence = [] 
    a, b = 0, 1 
    for _ in range(n): 
        sequence.append(a)  
        a, b = b, a + b
    return sequence
          
                      
def main():
   while True:
    user_input = input("How many terms of the Fibonacci sequence do you want? ")

    # Validate input
    if not user_input.isdigit():
        print("Please enter a positive integer.")
    else:
        n = int(user_input)
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            # Calculate and print Fibonacci sequence
            a, b = 0, 1
            for _ in range(n):
                print(a, end=" ")
                a, b = b, a + b
            break    


if __name__ == "__main__":
    main()
