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




# 딕셔너리는 리스트나, 딕셔너리를 value에 넣을 수 있다.
# {
#     key : [List],
#     key2 : {Dict},
# }

capitalps = {
    "France": "Paris",
    "Germany": "Berlin",
}


# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}


travle_log = [
    {
        "Country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
]



# 연습문제
# "Steak"를 출력하려면 어떻게 해야할까?

# 보기
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: {}},
}

print(order["main"][2][0])
