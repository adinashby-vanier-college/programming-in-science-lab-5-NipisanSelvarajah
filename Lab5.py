# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                result += "*" 
            else: 
                result += " " 
        result += "\n"
    return result.strip()

# def hollow_square(n):
#     result = ""
#     for i in range(n):
#         if i == 0 or i == n - 1:
#             result += "*" * n  + "\n"
#         else: 
#             result += "*" + " " * (n-2) + "*" + "\n"
        
#     return result.strip()

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    for i in range(n):
        for j in range(1, 2 + i):
            result += str(j) 
           # result = result.rstrip()
        result += "\n"
    
    #print(result)
    return result.rstrip()


# # Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    sum = 0
    i= 0
    while i <= n:
        sum += i
        i += 1
    return sum

# # Example for n = 4:
# #    *
# #   ***
# #  *****
# # *******
def centered_star_pyramid(n):
    result = ""
    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "*" * (1 + 2 * i)
        result += spaces + stars + "\n"
    return result.rstrip()

# n = 4
# result = ""
# for i in range(n):
#     for j in range(1, 2 + i):
#         result += str(j) 
#            # result = result.rstrip()
#     result += "\n"
    
# print(result)