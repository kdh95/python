# 파이썬 함수
# 함수뒤에는 괄호 ()가 붙는다.
print("Hello") # print 함수
num_char = len("Hello")
print(num_char)

# 나만의 함수 만들기
def my_function():
    print("Hello")
    print("Bye")


my_function() # 함수 실행

# Defining Functions
# def my_function():
#     Do this
#     Then do this
#     Finally do this

# Calling Functions
# my_functions()


# DocStrings
def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    format_f_name = f_name.title()
    foramt_l_name = l_name.title()
    return f"Result : {format_f_name} {foramt_l_name}"
