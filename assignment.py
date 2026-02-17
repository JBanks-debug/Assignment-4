# =========================================================
# Jermaine Banks
# GitHub: JBanks-debug
# Assignment Due: 2/20/26
# =========================================================


# ========================================
# Step 1: Collatz Sequence
# ========================================

def collatz_sequence(n):
    sequence = []
    steps = 0

    while n != 1:
        sequence.append(n)

        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        steps += 1

    sequence.append(1)
    return sequence, steps


# ========================================
# Step 2: Prime Number Checker
# ========================================

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# ========================================
# Step 3: Multiplication Table
# ========================================

def multiplication_table():
    table = []

    for i in range(1, 6):
        row = []
        for j in range(1, 6):
            row.append(i * j)
        table.append(row)

    return table


# ========================================
# Step 4: Factorial
# ========================================

def factorial(n):
    if n < 0:
        return None

    result = 1

    while n > 0:
        result *= n
        n -= 1

    return result


# ========================================
# Step 5: List Statistics
# ========================================

def calculate_statistics(numbers):
    total = 0
    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        total += num

        if num > largest:
            largest = num

        if num < smallest:
            smallest = num

    average = total / len(numbers)

    return {
        "sum": total,
        "average": average,
        "min": smallest,
        "max": largest
    }
