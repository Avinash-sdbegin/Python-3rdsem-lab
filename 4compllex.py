c1 = complex(input("Enter the real part of first complex number: ")) + complex(input("Enter the imaginary part of first complex number: ")) * 1j
c2 = complex(input("Enter the real part of second complex number: ")) + complex(input("Enter the imaginary part of second complex number: ")) * 1j
sum = c1 + c2
diff = c1 - c2

print("The sum of the two complex numbers is:", sum)
print("The difference of the two complex numbers is:", diff)
print("The product of the two complex numbers is:", c1 * c2)