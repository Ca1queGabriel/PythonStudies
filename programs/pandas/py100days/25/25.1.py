# with open("../resources/weather_data.csv") as data_file:
    # data = data_file.readlines()
    # print(data)
#
# import csv
#
# with open("../resources/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     next(data)
#     temperatures = []
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

data = pd.read_csv("../../../../resources/weather_data.csv")