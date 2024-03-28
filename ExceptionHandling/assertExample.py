try:
    n = int(input("Enter a even number: "))

    assert n % 2 == 0, "Invalid Number"

except AssertionError as obj:
    print(obj)

print("After Assertion")