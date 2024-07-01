# 파이썬 딕셔너리는 실제 사전(딕셔너리)와 비슷하게 동작한다.
# 모든 딕셔너리는 다음과 같이 정의할 수 있다.
# {key : value}

programming_dictionaries = {
    "Bug" : "An error  in program that prevents the program from running as expected",
    "Function" : "A piece of code that you can easily call over and over again",
}

print(programming_dictionaries["Bug"])

# Adding new items to dictionary.
ç["Loop"] = "The action of doding something over and over again"

print(programming_dictionaries["Loop"])

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionaries = {}

# Loop through a dictionary
for key in programming_dictionaries:
    print(key)
    print(programming_dictionaries[key])
