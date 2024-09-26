def product_digit(n: int):
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product
while True:

   num = int(input("enter the number to be product: ? "))
   print(product_digit(num))   