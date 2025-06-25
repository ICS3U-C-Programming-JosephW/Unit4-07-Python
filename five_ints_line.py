#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: May 3, 2025
# This program displays five
# integers per line with a
# loop and an if statement.


# Define the main function.
def main():
    # Use a for loop to iterate over
    # the integer range of 1000 to 2000.
    for counter in range(1000, 2001):
        # Display and format the
        # integer without a newline.
        print(f"{counter} ", end="")
        # Check if five integers have
        # been displayed on the line.
        if (counter - 999) % 5 == 0:
            # Display a newline to
            # introduce a new line.
            print()


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
