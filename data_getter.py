import requests
import country_code_getter
from collections import defaultdict, OrderedDict
import datetime
import copy


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
    country = None

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
                response = requests.get(url)
                raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'all countries today[total recovered]' or command == '2':
                url = 'https://api.thevirustracker.com/free-api?countryTotals=ALL'
                response = requests.get(url)
                raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'specific country today' or command == '3':
                url, country = get_country_specific_url('https://api.thevirustracker.com/free-api?countryTotal=')
                if url is not None:
                    response = requests.get(url)
                    raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'world full time line' or command == '4':
                url = 'https://thevirustracker.com/timeline/map-data.json'
                response = requests.get(url)
                raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'specific country timeline' or command == '5':
                url, country = get_country_specific_url('https://api.thevirustracker.com/free-api?countryTimeline=')
                if url is not None:
                    response = requests.get(url)
                    raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'all countries timeline[cases]' or command == '6':
                url = 'https://thevirustracker.com/timeline/map-data.json'
                response = requests.get(url)
                raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'all countries today[total deaths]' or command == '7':
                url = 'https://api.thevirustracker.com/free-api?countryTotals=ALL'
                response = requests.get(url)
                raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'all countries today[total cases]' or command == '8':
                url = 'https://api.thevirustracker.com/free-api?countryTotals=ALL'
                response = requests.get(url)
                raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'all countries today[new deaths]' or command == '9':
                url = 'https://api.thevirustracker.com/free-api?countryTotals=ALL'
                response = requests.get(url)
                raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'all countries today[new cases]' or command == '10':
                url = 'https://api.thevirustracker.com/free-api?countryTotals=ALL'
                response = requests.get(url)
                raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'all countries timeline[deaths]' or command == '11':
                url = 'https://thevirustracker.com/timeline/map-data.json'
                response = requests.get(url)
                raw_data = response.json()

    # ==================================================================================== #

            elif command.lower() == 'all countries timeline[recovered]' or command == '12':
                url = 'https://thevirustracker.com/timeline/map-data.json'
                response = requests.get(url)
                raw_data = response.json()

        return raw_data, country


def get_country_specific_url(partial_url):

    # get country codes
    country_codes = country_code_getter.get_country_codes()
    countries = []
    for item in country_codes.keys():
        countries.append(item)

    country = input('What is the name of the country: ')
    country_accepted = False

    # make sure if someone typed us or america the program would still work
    if country.lower() == 'america' or country.lower() == 'us':
        code = 'US'
        url = partial_url + code
        return url, country.upper()

    elif country.lower() != 'america' or country.lower() != 'us':
        for c in countries:
            if country.lower() in c:
                country_accepted = True
                # if the country is in the data base but spelled in a different way
                country = c

        if country_accepted:
            code = country_codes[country.lower()]
            url = partial_url + code
            return url, country.title()

    else:
        print('Sorry the country you are looking for is unknown\n')


def return_data_for_specific_month(dictionary):

    # get available months
    months_codes = {'1': 'january', '2': 'february', '3': 'march', '4': 'april', '5': 'may', '6': 'june',
                    '7': 'july', '8': 'august', '9': 'september', '10': 'october', '11': 'november', '12': 'december'}
    months = []
    for v in dictionary.values():
        dates = v[0]
        for date in dates:
            date = date.split('/')
            month = date[0]
            months.append(month)

    # remove duplicates from list
    for i in months:
        num = months.count(i)
        for _ in range(num-1):
            months.remove(i)

    # get input
    print('which month do you want the graph to represent the available months are:\n')
    for m in months:
        print(f'{months_codes[m]} ({m})')

    input_month = input('\n')

    # if someone rights january instead of 1
    if len(input_month) > 2:
        good_input = False
        for k, v in months_codes.items():
            if input_month.lower() == v:
                input_month = k
                good_input = True
                break
    # if someone writes   1   with space around it
    elif input_month.strip() in months_codes.keys():
        good_input = True
    else:
        good_input = False

    # check validity of input
    if not good_input:
        print('invalid month please try again and enter a valid month')
        return None

    else:
        # make a copy of the dict
        return_dict = {k: v for k, v in dictionary.items()}
        months_in_dict_values = []

        for k, v in copy.deepcopy(return_dict).items():
            # we use deep copy in order to copy the list in the dict
            date_list = v[0]

            # if country doesnt have data for the specific month remove it
            for d in date_list:
                if d.split('/')[0] not in months_in_dict_values:
                    months_in_dict_values.append(d.split('/')[0])

            if input_month not in months_in_dict_values:
                return_dict.pop(k)

            # remove data out of the range if the input month data
            else:
                index_subtracter = 0
                for i, m in enumerate(date_list):
                    if m.split('/')[0] != input_month:
                        return_dict[k][0].pop(i - index_subtracter)
                        return_dict[k][1].pop(i - index_subtracter)
                        # if an item is popped the index of the item after it becomes its index
                        # so we need to subtract 1 from the index in order not to change the index of
                        # each item
                        index_subtracter += 1

        # remove the keys with empty values (lists)
        for k, v in copy.deepcopy(return_dict).items():
            if v == ([], []):
                return_dict.pop(k)

        return return_dict


def return_data(raw_data_and_country, command):

    # get country codes
    country_codes = country_code_getter.get_country_codes()
    countries = []
    for item in country_codes.keys():
        countries.append(item)

    raw_data = raw_data_and_country[0]
    country = raw_data_and_country[1]

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

            x = []
            y = []
            for main_v in json_result.values():
                for k in main_v:
                    if k == 'title':
                        x.append(main_v[k])
                    elif k == 'total_recovered':
                        y.append(main_v[k])

            # put the results in increasing order
            result_dict = dict(zip(x, y))
            sorted_res_dict = {k: v for k, v in sorted(result_dict.items(), key=lambda i: i[1])}

            x = []
            y = []
            for k, v in sorted_res_dict.items():
                x.append(k)
                y.append(v)

            return x, y

    # ==================================================================================== #

        elif command.lower() == 'specific country today' or command == '3':
            # transform into a dict
            json_result = raw_data['countrydata']
            json_result = json_result[0]

            # remove unwanted data
            json_result.pop('info')

            x, y = list(json_result.keys()), list(json_result.values())
            return x, y, country

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
            # transform into a list
            json_result = raw_data
            # get country name
            country_name = json_result['countrytimelinedata'][0]['info']['title']

            # remove unwanted data
            json_result.pop('countrytimelinedata')
            json_result.pop['timelineitems'][0].pop('stat')

            # transform into dict
            json_result = json_result['timelineitems'][0]

            # sort dict according to date
            sorted_json_result = {k: v for k, v in sorted(json_result.items(), key=lambda unsorted_dict: datetime.datetime.strptime(unsorted_dict[0], '%m/%d/%y'))}

            new_daily_cases_y = []
            new_daily_deaths_y = []
            total_cases_y = []
            total_recoveries_y = []
            total_deaths_y = []
            x_date = []
            for main_k, main_v in sorted_json_result.items():
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
                        y_cases_int = dictionary[k]
                        all_countries_timeline_cases_dict[country_name].append(date)
                        all_countries_timeline_cases_dict[country_name].append(y_cases_int)

            # sort according to date
            sorted_all_countries_timeline_cases_dict = {}
            for k, v in all_countries_timeline_cases_dict.items():
                tup_list = []
                sorted_list = []
                for i, item in enumerate(v):
                    if i % 2 == 0:
                        date = item
                    else:
                        num = item
                        tup = (date, num)
                        tup_list.append(tup)

                # sort the tuple in increasing date
                tup_list.sort(key=lambda t: t[0])
                # change back to normal list
                for i in tup_list:
                    for i2 in i:
                        sorted_list.append(i2)
                # append in new dict
                sorted_all_countries_timeline_cases_dict[k] = sorted_list

            # put x and y in 2 separate lists
            result_dict = {}
            x_list = []
            y_list = []
            for k in sorted_all_countries_timeline_cases_dict.keys():
                unsorted_list = sorted_all_countries_timeline_cases_dict[k]
                for i, item in enumerate(unsorted_list):
                    if i % 2 == 0:
                        x_list.append(item)
                    else:
                        y_list.append(item)
                result_dict[k] = (x_list, y_list)
                x_list = []
                y_list = []
            print(result_dict)
            # sort the data in most latest cases order
            sorted_result_dict = {k: v for k, v in sorted(result_dict.items(), key=lambda i: i[1][1][-1])}

            before_final_dict = return_data_for_specific_month(sorted_result_dict)

            # get data by chunks instead of displaying all data at once (first 50 most cases, second most 50 cases...)
            chunk_data = list(before_final_dict.items())
            chunk_data_list = []
            if len(chunk_data) <= 50:
                final_dict = before_final_dict
            else:
                for _ in range(len(chunk_data) // 50):
                    lst = []
                    for chunk in chunk_data:
                        if len(lst) <= 50:
                            lst.append(chunk)



            # if we don't put None it will only return the keys
            return sorted_result_dict, None

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


if __name__ == '__main__':
    com = get_command()
    r_data = get_response(com)
    data = return_data(r_data, com)
    for i in data:
        print(i)

