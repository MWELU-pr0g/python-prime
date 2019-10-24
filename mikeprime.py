def isPrime(n):
    if n <= 1:
        return False

    if n <= 3:
        return True

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True
