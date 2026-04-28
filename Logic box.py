print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option: ")
    print("1 Generate a Pattern")
    print("2 Analyze a Range of Numbers")
    print("3 Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        n = int(input("No of rows for the pattern: "))
        print("Pattern: ")
        for i in range(1, n + 1):
            print("*" * i)

    elif choice == 2:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        for i in range(start, end + 1):  # fixed to include 'end'
            if i % 2 == 0:
                print(f"even {i}")
            else:
                print(f"odd {i}")
        total = sum(range(start, end + 1))
        print(f"Sum of all numbers from {start} to {end} is: {total}")

    elif choice == 3:
        print("Exiting the program, GOOD BYE!")
        break

    else:
        print("Invalid Choice, Please Try Again!")
