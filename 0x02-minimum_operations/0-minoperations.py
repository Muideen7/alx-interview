def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
            operations += factor
        else:
            factor += 1

    if n > 1:
        operations += n

    return operations
