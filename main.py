import math


def karatsuba(x: int, y: int) -> int:
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = math.ceil(n / 2)

    high_x, low_x = divmod(x, 10 ** m)
    high_y, low_y = divmod(y, 10 ** m)

    z0 = karatsuba(low_x, low_y)
    z1 = karatsuba((low_x + high_x), (low_y + high_y))
    z2 = karatsuba(high_x, high_y)

    return (z2 * 10 ** (2 * m)) + ((z1 - z2 - z0) * 10 ** m) + z0


if __name__ == "__main__":
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = karatsuba(num1, num2)
    print(f"O resultado da multiplicação é: {resultado}")

