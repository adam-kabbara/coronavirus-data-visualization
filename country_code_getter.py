import requests
import bs4


def get_country_codes():
    url = 'https://thevirustracker.com/api'
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('error getting the data. please connect to wifi and try again')
    else:
        page = bs4.BeautifulSoup(response.content, 'html.parser')

        table = page.find(id='indexpage')
        raw_table_data = table.get_text().split('\n')

        raw_data = []
        # remove blank lines
        for item in raw_table_data:
            if item != '':
                raw_data.append(item.strip())

        for item in raw_data:
            if item == '':
                raw_data.pop(raw_data.index(item))

        # remove unwanted words
        num_of_country_word = raw_data.count('Country Statistics Code')
        num_of_counry_word = raw_data.count('Counry Title')
        num_of_timeline_word = raw_data.count('Country Timeline Code')

        for _ in range(num_of_country_word):
            raw_data.remove('Country Statistics Code')
        for _ in range(num_of_counry_word):
            raw_data.remove('Counry Title')
        for _ in range(num_of_timeline_word):
            raw_data.remove('Country Timeline Code')

        # clean country codes
        for item in raw_data:
            if 'Stats' in item:
                index = raw_data.index(item)
                raw_data.pop(index)
                code = item[:2]
                raw_data.insert(index, code)

        # transform into a dict
        country_names = []
        country_code = []
        for item in raw_data:
            if len(item) > 2:
                country_names.append(item.lower())

            else:
                country_code.append(item)

        clean_data = dict(zip(country_names, country_code))
        return clean_data

