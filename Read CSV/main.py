# with open("weather_data.csv") as data_file:
#     data = data_file.readline()
#     print(data)

# 위처럼 하지 말고 아래처럼 해보자
import csv

# 이렇게 해도 데이터를 읽는데 굉장히 번거롭다.
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)



