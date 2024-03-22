n = int(input("Enter the number of terms in the Fibonacci sequence: "))

a, b = 0, 1
sequence = []

if n >= 1:
    sequence.append(a)
if n >= 2:
    sequence.append(b)

for i in range(2, n):
  
    next_term = a + b
    sequence.append(next_term)

    a, b = b, next_term

print(f"Fibonacci sequence up to {n} terms: {sequence}")
