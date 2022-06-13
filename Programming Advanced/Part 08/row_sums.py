# Add row items of a matrix,Then add item to the row
def row_sums(my_matrix: list):
    for i in range(len(my_matrix)):
        sum = 0
        # Get the item of the row
        for j in range(len(my_matrix[i])):
            # Add row items
            sum += my_matrix[i][j]
            if j == len(my_matrix[i])-1:
                # When all row item summed
                # Append the sum to the matrix row
                my_matrix[i].append(sum)
                # Reset the sum to calculate another row
                sum = 0


if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)
