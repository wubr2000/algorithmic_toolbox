# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous_last_digit = 0
    current_last_digit  = 1

    for _ in range(n - 1):
        previous_last_digit, current_last_digit = current_last_digit, (previous_last_digit + current_last_digit) % 10

    return current_last_digit

# if __name__ == '__main__':
#     input = sys.stdin.read()
n = int(input())
print(get_fibonacci_last_digit_naive(n))
