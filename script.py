# # Functions with Outputs

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"Result: {formatted_f_name} {formatted_l_name}"

# formatted_string = format_name("sean", "GUERRERO")

# print(formatted_string)
# print(format_name("sean", "GUERRERO"))


# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return "Leap year"
#       else:
#         return "Not leap year"
#     else:
#       return "Leap year"
#   else:
#     return "Not leap year"
  
# # TODO: Add more code here 👇
# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#   output = is_leap(year)
#   if output == "Leap year":
#     month_days[1] = 29
#     return month_days[month - 1]
#   return month_days[month - 1]
  
  
# #🚨 Do NOT change any of the code below 
# year = int(input()) # Enter a year
# month = int(input()) # Enter a month
# days = days_in_month(year, month)
# print(days)



def format_name(f_name, l_name):
    #Docstring
    """Take a first and last name and format it
      to return the title case version of the name"""
    #Return as an early exit
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"

formatted_string = format_name("sean", "GUERRERO")

print(formatted_string)
print(format_name("sean", "GUERRERO"))
