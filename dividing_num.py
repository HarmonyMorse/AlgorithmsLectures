# We'll say that a positive int divides itself if every digit in the number divides into the number evenly.
# So for example 128 divides itself since 1, 2, and 8 all divide into 128 evenly.
# And we'll say that 0 does not divide into anything evenly, so no number with a digit 0 divides itself.
# Write a function to determine if a number divides itself.

# U.P.E.R.
# Understand
#     Input: a positive int
#     Output: boolean
#     Bad data?: no
# Plan
#     Loop over each digit in num (while the current number is not < 10)
#         if the digit is 0, return False
#         get the right most digit of num using %
#         get remainder of num divided by the digit
#         if it is not 0, return False
#         remove the last digit from the number using // 10 (integer division)
#     return True

def divides_self(num):
    while True:
        pass

print(divides_self(128))    # True
print(divides_self(12))     # True
print(divides_self(120))    # False
