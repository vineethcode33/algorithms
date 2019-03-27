def fibonacci(n):
    if n < 1:
        assert "Please give a number greater than 0"
    elif n == 1 or n == 2:
        return n-1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


if __name__ == "__main__":
    print(fibonacci(5))
