def sort_percentages(percentages):
    # Using Python's built-in sort function to sort the percentages array
    percentages.sort()
    return percentages

def main():
    # Initializing an empty array to store 10th class percentages
    percentages = []

    # Getting input for 10 students' percentages
    for i in range(10):
        percentage = float(input(f"Enter percentage for student {i + 1}: "))
        percentages.append(percentage)

    print("\nOriginal percentages array:", percentages)

    # Sorting the percentages array
    sorted_percentages = sort_percentages(percentages)
    
    print("\nSorted percentages array:", sorted_percentages)

if __name__ == "__main__":
    main()
