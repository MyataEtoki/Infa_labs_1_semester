def twos_complement(n, bits=32):
    mask = (1 << bits) - 1
    if n < 0:
        n = ((abs(n) ^ mask) + 1)
    return bin(n & mask)


print(twos_complement(-123, 8))