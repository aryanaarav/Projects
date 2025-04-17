# SimpleCalculator.jl

# Function to add two numbers
function add(x, y)
    return x + y
end

# Function to subtract two numbers
function subtract(x, y)
    return x - y
end

# Function to multiply two numbers
function multiply(x, y)
    return x * y
end

# Function to divide two numbers
function divide(x, y)
    if y == 0
        println("Error: Cannot divide by zero!")
        return NaN # Not-a-Number
    else
        return x / y
    end
end

# Function for exponentiation
function power(x, y)
    return x ^ y
end

# Function for modulo
function modulo(x, y)
    if y == 0
        println("Error: Cannot perform modulo by zero!")
        return NaN
    else
        return x % y
    end
end

println("Welcome to the Enhanced Simple Calculator with History!")
global memory = nothing # Initialize memory as global
history = []   # Initialize an empty list to store history

while true
    println("\nEnter an operation (+, -, *, /, ^, %, 'm' for memory, 'c' to clear memory, 'h' for history, or 'q' to quit:")
    operation = readline()

    if operation == "q"
        println("Goodbye!")
        break
    elseif operation == "m"
        if memory === nothing
            println("Memory is currently empty.")
        else
            println("Memory value: $memory")
        end
        continue # Go to the next iteration of the loop
    elseif operation == "c"
        global memory = nothing # Explicitly use the global memory
        println("Memory cleared.")
        continue
    elseif operation == "h"
        if isempty(history)
            println("Calculation history is empty.")
        else
            println("--- Calculation History ---")
            for (index, (num1, op, num2, res)) in enumerate(history)
                println("[$index]: $num1 $op $num2 = $res")
            end
            println("-------------------------")
        end
        continue
    elseif operation in ["+", "-", "*", "/", "^", "%"]
        local num1 # Declare num1 as local within this block
        if memory !== nothing # Access the global memory (no 'global' needed here for reading)
            println("Use memory value ($(memory)) for the first number? (y/n)")
            use_memory_input = lowercase(readline())
            if use_memory_input == "y"
                num1 = memory # Assign the global memory value to the local num1
            else
                println("Enter the first number:")
                num1 = parse(Float64, readline())
            end
        else
            println("Enter the first number:")
            num1 = parse(Float64, readline())
        end

        println("Enter the second number:")
        num2_str = readline()

        try
            local num2 = parse(Float64, num2_str) # Declare num2 as local
            local result # Declare result as local

            if operation == "+"
                result = add(num1, num2)
            elseif operation == "-"
                result = subtract(num1, num2)
            elseif operation == "*"
                result = multiply(num1, num2)
            elseif operation == "/"
                result = divide(num1, num2)
            elseif operation == "^"
                result = power(num1, num2)
            elseif operation == "%"
                result = modulo(num1, num2)
            end

            println("Result: $num1 $(operation) $num2 = $result")

            # Store the calculation in history
            push!(history, (num1, operation, num2, result))

            println("Store this result in memory? (y/n)")
            store_memory_input = lowercase(readline())
            if store_memory_input == "y"
                global memory = result # Explicitly update the global memory
                println("Result stored in memory.")
            end

        catch e
            println("Invalid input. Please enter numbers only.")
        end
    else
        println("Invalid operation. Please enter +, -, *, /, ^, %, 'm', 'c', 'h', or 'q'.")
    end
end
