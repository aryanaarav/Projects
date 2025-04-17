# Making a star pattern
# File: d:\Julia\aa.jl

# Define the number of rows for the pattern
height = 5

println("Simple Star Pattern (Right-Angled Triangle):")

# Loop from 1 up to the desired height
for i in 1:height
    # In each row 'i', print 'i' stars followed by a newline
    # The "^" operator repeats a string/character
    println("*" ^ i)
end

println("\nAnother Simple Pattern (Pyramid):")

# Loop for the pyramid pattern
for i in 1:height
    # Calculate leading spaces needed for centering
    num_spaces = height - i
    # Calculate the number of stars for this row (1, 3, 5, ...)
    num_stars = 2*i - 1

    # Create the spaces string
    spaces = " " ^ num_spaces
    # Create the stars string
    stars = "*" ^ num_stars

    # Concatenate spaces and stars, then print
    println(spaces * stars)
end