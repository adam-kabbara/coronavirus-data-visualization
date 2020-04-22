import requests
import country_code_getter
from collections import defaultdict
import datetime


def get_data(url):
    try:
        res = requests.get(url)
        return res.json()
    except requests.exceptions.ConnectionError:
        print('error getting the data. please connect to wifi and try again')


def get_command():
    command = input('''What data do you want:
            - world wide today (1)
            - all countries today[total recovered] (2)
            - specific country today (3)
            - world full time line (4)
            - specific country timeline (5)
            - all countries timeline[cases] (6)
            - all countries today[total deaths] (7)
            - all countries today[total cases] (8)
            - all countries today[new deaths] (9)
            - all countries today[new cases] (10)
            - all countries timeline[deaths] (11)
            - all countries timeline[recovered] (12)\n\n''')

    return command


def get_response(command):

    raw_data = None
    commands = ['world wide today', 'all countries today[total recovered]', 'specific country today', 'world full time line',
                'specific country timeline', 'all countries timeline[cases]', 'all countries today[total deaths]',
                'all countries today[total cases]', 'all countries today[new deaths]', 'all countries today[new cases]',
                'all countries timeline[deaths]', 'all countries timeline[recovered]', '1', '2', '3', '4',
                '5', '6', '7', '8', '9', '10', '11', '12']
    if command is not None:
        if command.lower() not in commands:
            print('unknown command. please enter a valid command')

        else:
            if command.lower() == 'world wide today' or command == '1':
                url = 'https://api.thevirustracker.com/free-api?global=stats'
                try:
                    response = requests.get(url)
                except requests.exceptions.ConnectionError:
                    print('error getting the data. please connect to wifi and try again')
                else:
                    raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'all countries today[total recovered]' or command == '2':
                url = 'https://api.thevirustracker.com/free-api?countryTotals=ALL'
                try:
                    response = requests.get(url)
                except requests.exceptions.ConnectionError:
                    print('error getting the data. please connect to wifi and try again')
                else:
                    raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'specific country today' or command == '3':
                url = get_country_specific_url('https://api.thevirustracker.com/free-api?countryTotal=')
                if url is not None:
                    try:
                        response = requests.get(url)
                    except requests.exceptions.ConnectionError:
                        print('error getting the data. please connect to wifi and try again')
                    else:
                        raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'world full time line' or command == '4':
                url = 'https://thevirustracker.com/timeline/map-data.json'
                try:
                    response = requests.get(url)
                except requests.exceptions.ConnectionError:
                    print('error getting the data. please connect to wifi and try again')
                else:
                    raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'specific country timeline' or command == '5':
                url = get_country_specific_url('https://api.thevirustracker.com/free-api?countryTimeline=')
                if url is not None:
                    try:
                        response = requests.get(url)
                    except requests.exceptions.ConnectionError:
                        print('error getting the data. please connect to wifi and try again')
                    else:
                        raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'all countries timeline[cases]' or command == '6':
                url = 'https://thevirustracker.com/timeline/map-data.json'
                try:
                    response = requests.get(url)
                except requests.exceptions.ConnectionError:
                    print('error getting the data. please connect to wifi and try again')
                else:
                    raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'all countries today[total deaths]' or command == '7':
                url = 'https://api.thevirustracker.com/free-api?countryTotals=ALL'
                try:
                    response = requests.get(url)
                except requests.exceptions.ConnectionError:
                    print('error getting the data. please connect to wifi and try again')
                else:
                    raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'all countries today[total cases]' or command == '8':
                url = 'https://api.thevirustracker.com/free-api?countryTotals=ALL'
                try:
                    response = requests.get(url)
                except requests.exceptions.ConnectionError:
                    print('error getting the data. please connect to wifi and try again')
                else:
                    raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'all countries today[new deaths]' or command == '9':
                url = 'https://api.thevirustracker.com/free-api?countryTotals=ALL'
                try:
                    response = requests.get(url)
                except requests.exceptions.ConnectionError:
                    print('error getting the data. please connect to wifi and try again')
                else:
                    raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'all countries today[new cases]' or command == '10':
                url = 'https://api.thevirustracker.com/free-api?countryTotals=ALL'
                try:
                    response = requests.get(url)
                except requests.exceptions.ConnectionError:
                    print('error getting the data. please connect to wifi and try again')
                else:
                    raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'all countries timeline[deaths]' or command == '11':
                url = 'https://thevirustracker.com/timeline/map-data.json'
                try:
                    response = requests.get(url)
                except requests.exceptions.ConnectionError:
                    print('error getting the data. please connect to wifi and try again')
                else:
                    raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'all countries timeline[recovered]' or command == '12':
                url = 'https://thevirustracker.com/timeline/map-data.json'
                try:
                    response = requests.get(url)
                except requests.exceptions.ConnectionError:
                    print('error getting the data. please connect to wifi and try again')
                else:
                    raw_data = response.json()

        return raw_data


def get_country_specific_url(partial_url):

    # get country codes
    country_codes = country_code_getter.country_codes
    countries = []
    for item in country_codes.keys():
        countries.append(item)

    country = input('What is the name of the country: ')
    country_accepted = False

    for c in countries:
        if country.lower() in c:
            country_accepted = True
            # if the country is in the data base but spelled in a different way
            country = c

    if country_accepted:
        code = country_codes[country.lower()]
        url = partial_url + code
        return url

    # make sure if someone typed us or america the program would still work
    elif country.lower() == 'america' or country.lower() == 'us':
        code = 'US'
        url = partial_url + code
        return url

    else:
        print('Sorry the country you are looking for is unknown\n')


def return_data(raw_data, command):

    try:
        requests.get('http://google.com')
    except requests.exceptions.ConnectionError:
        print('error getting the data. please connect to wifi and try again')
    else:

        # get country codes
        country_codes = country_code_getter.get_country_codes()
        countries = []
        for item in country_codes.keys():
            countries.append(item)

        if raw_data is not None:
            if command.lower() == 'world wide today' or command == '1':
                # transform into a dict
                json_result = raw_data['results']
                json_result = json_result[0]

                # remove unwanted data
                json_result.pop('source')

                x, y = list(json_result.keys()), list(json_result.values())
                return x, y

# ==================================================================================== #

        elif command.lower() == 'all countries today[total recovered]' or command == '2':
            # transform into a dict
            json_result = raw_data['countryitems']
            json_result = json_result[0]
            print(raw_data)

            x = []
            y = []
            for main_v in json_result.values():
                for k in main_v:
                    if k == 'title':
                        x.append(main_v[k])
                    elif k == 'total_recovered':
                        y.append(main_v[k])
            return x, y

# ==================================================================================== #

        elif command.lower() == 'specific country today' or command == '3':
            # transform into a dict
            json_result = raw_data['countrydata']
            json_result = json_result[0]

            # remove unwanted data
            json_result.pop('info')

            x, y = list(json_result.keys()), list(json_result.values())
            return x, y

# ==================================================================================== #

        elif command.lower() == 'world full time line' or command == '4':
            # transform into a list
            json_result = raw_data['data']

            # remove unwanted data
            json_result.pop()

            x_date = {}
            y_recovered_dict = defaultdict(float)
            y_deaths_dict = defaultdict(float)
            y_cases_int = defaultdict(float)

            # this is the starting date
            date = '1/22/20'
            prev_date = '1/22/20'

            # we use a list to append all the dicts in it and sort the data according to the date
            # so we get clean data cause the data in the api is not completely sorted correctly
            # example they go from 3/13/20 to 4/17/20
            json_result.sort(key=lambda dictionary_for_sort: datetime.datetime.strptime(dictionary_for_sort['date'], '%m/%d/%y'))

            for dictionary in json_result:
                for k in dictionary.keys():
                    if k == 'date':
                        if dictionary[k] not in x_date:
                            x_date[dictionary[k]] = []
                        date, prev_date = dictionary[k], date

                    elif k == 'cases':
                        if date == prev_date:
                            y_cases_int[k] += int(dictionary[k])
                        else:
                            y_append = y_cases_int.copy()
                            x_date[prev_date].append(y_append)
                            y_cases_int.clear()
                            y_cases_int[k] += int(dictionary[k])

                    elif k == 'deaths':
                        if date == prev_date:
                            y_deaths_dict[k] += int(dictionary[k])
                        else:
                            y_append = y_deaths_dict.copy()
                            x_date[prev_date].append(y_append)
                            y_deaths_dict.clear()
                            y_deaths_dict[k] += int(dictionary[k])

                    elif k == 'recovered':
                        if date == prev_date:
                            y_recovered_dict[k] += int(dictionary[k])
                        else:
                            y_append = y_recovered_dict.copy()
                            x_date[prev_date].append(y_append)
                            y_recovered_dict.clear()
                            y_recovered_dict[k] += int(dictionary[k])

            # transform data into lists
            y_recovered_list = []
            y_deaths_list = []
            y_cases_list = []
            x_date_list = []
            for main_k, main_v in x_date.items():
                x_date_list.append(main_k)
                for i in main_v:
                    for k, v in i.items():
                        if k == 'cases':
                            y_cases_list.append(int(v))
                        elif k == 'deaths':
                            y_deaths_list.append(int(v))
                        elif k == 'recovered':
                            y_recovered_list.append(int(v))

            return x_date_list, y_recovered_list, y_deaths_list, y_cases_list
# ==================================================================================== #

        elif command.lower() == 'specific country timeline' or command == '5':
            # transform into a dict
            json_result = raw_data
            # get country name
            country_name = json_result['countrytimelinedata'][0]['info']['title']
            # remove unwanted data
            json_result.pop('countrytimelinedata')
            # transform into better dict
            json_result = json_result['timelineitems'][0]
            json_result.pop('stat')

            new_daily_cases_y = []
            new_daily_deaths_y = []
            total_cases_y = []
            total_recoveries_y = []
            total_deaths_y = []
            x_date = []
            for main_k, main_v in json_result.items():
                x_date.append(main_k)
                for k in main_v.keys():
                    if k == 'new_daily_cases':
                        new_daily_cases_y.append(main_v[k])
                    elif k == 'new_daily_deaths':
                        new_daily_deaths_y.append(main_v[k])
                    elif k == 'total_cases':
                        total_cases_y.append(main_v[k])
                    elif k == 'total_recoveries':
                        total_recoveries_y.append(main_v[k])
                    elif k == 'total_deaths':
                        total_deaths_y.append(main_v[k])

            return country_name, x_date, new_daily_cases_y, new_daily_deaths_y, total_cases_y, total_recoveries_y, total_deaths_y

# ==================================================================================== #

        elif command.lower() == 'all countries timeline[cases]' or command == '6':
            # transform into a list
            json_result = raw_data['data']

            # remove unwanted data
            json_result.pop()

            # starter values
            country_name = 'china'
            date = '1/22/20'
            all_countries_timeline_cases_dict = {}

            for dictionary in json_result:
                for k in dictionary.keys():
                    if k == 'countrycode':
                        for country_k, country_v in country_codes.items():
                            if country_v == dictionary[k]:
                                country_name = country_k

                        if country_name not in all_countries_timeline_cases_dict:
                            all_countries_timeline_cases_dict[country_name] = []

                    elif k == 'date':
                        date = dictionary[k]

                    elif k == 'cases':
                        # make sure all countries start at x = 0
                        y_cases_int = dictionary[k]
                        all_countries_timeline_cases_dict[country_name].append(date)
                        all_countries_timeline_cases_dict[country_name].append(y_cases_int)

            # if we don't put None it will only return the keys
            return all_countries_timeline_cases_dict, None

# ==================================================================================== #

        elif command.lower() == 'all countries today[total deaths]' or command == '7':
            # transform into a dict
            json_result = raw_data['countryitems']
            json_result = json_result[0]

            x = []
            y = []
            for main_v in json_result.values():
                for k in main_v:
                    if k == 'title':
                        x.append(main_v[k])
                    elif k == 'total_deaths':
                        y.append(main_v[k])
            return x, y

# ==================================================================================== #

        elif command.lower() == 'all countries today[total cases]' or command == '8':
            # transform into a dict
            json_result = raw_data['countryitems']
            json_result = json_result[0]

            x = []
            y = []
            for main_v in json_result.values():
                for k in main_v:
                    if k == 'title':
                        x.append(main_v[k])
                    elif k == 'total_cases':
                        y.append(main_v[k])
            return x, y

# ==================================================================================== #

        elif command.lower() == 'all countries today[new deaths]' or command == '9':
            # transform into a dict
            json_result = raw_data['countryitems']
            json_result = json_result[0]

            x = []
            y = []
            for main_v in json_result.values():
                for k in main_v:
                    if k == 'title':
                        x.append(main_v[k])
                    elif k == 'total_new_deaths_today':
                        y.append(main_v[k])
            return x, y

# ==================================================================================== #

        elif command.lower() == 'all countries today[new cases]' or command == '10':
            # transform into a dict
            json_result = raw_data['countryitems']
            json_result = json_result[0]

            x = []
            y = []
            for main_v in json_result.values():
                for k in main_v:
                    if k == 'title':
                        x.append(main_v[k])
                    elif k == 'total_new_cases_today':
                        y.append(main_v[k])
            return x, y

# ==================================================================================== #

        elif command.lower() == 'all countries timeline[deaths]' or command == '11':
            # transform into a list
            json_result = raw_data['data']

            # remove unwanted data
            json_result.pop()

            # starter values
            country_name = 'china'
            date = '1/22/20'
            all_countries_timeline_deaths_dict = {}

            for dictionary in json_result:
                for k in dictionary.keys():
                    if k == 'countrycode':
                        for country_k, country_v in country_codes.items():
                            if country_v == dictionary[k]:
                                country_name = country_k

                        if country_name not in all_countries_timeline_deaths_dict:
                            all_countries_timeline_deaths_dict[country_name] = []

                    elif k == 'date':
                        date = dictionary[k]

                    elif k == 'deaths':
                        # make sure all countries start at x = 0
                        y_cases_int = dictionary[k]
                        all_countries_timeline_deaths_dict[country_name].append(date)
                        all_countries_timeline_deaths_dict[country_name].append(y_cases_int)

            # if we don't put None it will only return the keys
            return all_countries_timeline_deaths_dict, None

# ==================================================================================== #

        elif command.lower() == 'all countries timeline[recovered]' or command == '12':
            # transform into a list
            json_result = raw_data['data']

            # remove unwanted data
            json_result.pop()

            # starter values
            country_name = 'china'
            date = '1/22/20'
            all_countries_timeline_recovered_dict = {}

            for dictionary in json_result:
                for k in dictionary.keys():
                    if k == 'countrycode':
                        for country_k, country_v in country_codes.items():
                            if country_v == dictionary[k]:
                                country_name = country_k

                        if country_name not in all_countries_timeline_recovered_dict:
                            all_countries_timeline_recovered_dict[country_name] = []

                    elif k == 'date':
                        date = dictionary[k]

                    elif k == 'recovered':
                        # make sure all countries start at x = 0
                        y_cases_int = dictionary[k]
                        all_countries_timeline_recovered_dict[country_name].append(date)
                        all_countries_timeline_recovered_dict[country_name].append(y_cases_int)

            # if we don't put None it will only return the keys
            return all_countries_timeline_recovered_dict, None


command = get_command()
r_data = get_response(command)
data = return_data(r_data, command)

