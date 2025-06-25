# Factorial function
def factorial(n):
    """Tính giai thừa của một số nguyên n."""
    if n < 0:
        raise ValueError("Giai thừa không xác định cho số âm.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result