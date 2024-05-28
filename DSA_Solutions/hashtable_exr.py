
nyc_weather = []
with open('C:/Users/admin/Downloads/nyc_weather.csv', 'r') as f:
    next(f)
    for line in f:
        token = line.split(',')
        temp = int(token[1])
        nyc_weather.append(temp)
    print(nyc_weather)

def first_wk_ave():
    first_wk_temp = nyc_weather[0:7]
    days = len(nyc_weather[0:7])
    total = sum(first_wk_temp)
    ave = total/days

    return ave

def max_temp():
    max_temp = max(nyc_weather)
    print(max_temp)




nyc_weda = {}
with open('C:/Users/admin/Downloads/nyc_weather.csv', 'r') as f:
    next(f)
    for line in f:
        token = line.split(',')
        key = token[0]
        temperature = int(token[1])
        nyc_weda[key] = temperature
    print(nyc_weda)

    for key, value in nyc_weda.items():
        if key == 'Jan 9':
            print(f"The temperature on Jan 9th was {value}")

        if key == 'Jan 4':
            print(f"The temperature on Jan 4th was {value}")


words_dict = {}
with open('C:/Users/admin/Downloads/poem.txt', 'r') as f:
    for line in f:
        words = line.split(' ')
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1

    print(words_dict)




