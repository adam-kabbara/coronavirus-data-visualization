from matplotlib import pyplot as plt
import mplcursors
import data_getter


def main():
    command = data_getter.get_command()
    raw_data = data_getter.get_response(command)
    data = data_getter.return_data(raw_data, command)

    if data is not None:

        if command.lower() == 'world wide today' or command == '1':
            x_data, y_data = data
            show_in_terminal(x_data, y_data)

            # graph part
            bars = plt.bar(x_data, y_data)
            plt.title('World wide today', fontsize=20)
            plt.tick_params(axis='x', rotation=45, labelsize=8)
            plt.tight_layout()

            # add number above each bar
            for rect in bars:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{int(height)}', ha='center', va='bottom',
                         fontsize=8)
            plt.show()

        # ==================================================================================== #

        elif command.lower() == 'all countries today[total recovered]' or command == '2':
            x_data, y_data = data
            x_cut = len(x_data) // 2
            y_cut = len(y_data) // 2
            x1, y1 = x_data[x_cut:], y_data[y_cut:]
            x2, y2 = x_data[:x_cut], y_data[:y_cut]

            fig1, ax1 = plt.subplots(figsize=(12, 4.5))
            fig2, ax2 = plt.subplots(figsize=(15, 5))

            bars1 = ax1.bar(x1, y1)
            ax1.tick_params(axis='x', rotation=90, labelsize=6)
            # if we created our own plt object instead of doing plt.title we do <objectname>.set_title
            ax1.set_title('Total recoveries of all countries from start till today', fontsize=20, c='green')

            bars2 = ax2.bar(x2, y2)
            ax2.tick_params(axis='x', rotation=90, labelsize=6)
            ax2.set_title('Total recoveries of all countries from start till today', fontsize=20, c='green')

            fig1.tight_layout()
            fig2.tight_layout(pad=1.8)

            # add number above each bar
            for rect in bars1:
                height = rect.get_height()
                ax1.text(rect.get_x() + rect.get_width() / 2.0, height + 10 ** 3, f'{int(height)}',
                         ha='center', va='bottom', fontsize=5, rotation=90, c='green')

            for rect in bars2:
                height = rect.get_height()
                ax2.text(rect.get_x() + rect.get_width() / 2.0, height + 1, f'{int(height)}', ha='center', va='bottom',
                         fontsize=5, rotation=90, c='green')

            plt.show()

        # ==================================================================================== #

        elif command.lower() == 'specific country today' or command == '3':
            x_data, y_data, country = data
            show_in_terminal(x_data, y_data)
            # graph part
            bars = plt.bar(x_data, y_data)
            plt.title(f'{country} today', fontsize=20)
            plt.tick_params(axis='x', rotation=45, labelsize=8)
            plt.tight_layout()
            # add number above each bar
            for rect in bars:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{int(height)}', ha='center', va='bottom',
                         fontsize=8)
            plt.show()

        # ==================================================================================== #

        elif command.lower() == 'world full time line' or command == '4':
            x_date_list, y_recovered_list, y_deaths_list, y_cases_list = data

            # make the lists equal in size
            mega_list = [x_date_list, y_cases_list, y_recovered_list, y_deaths_list]
            len_list = []
            for lst in mega_list:
                for lst2 in mega_list:
                    len_list.append(len(lst) == len(lst2))

            if not all(len_list):
                max_len = max(len(x_date_list), len(y_recovered_list), len(y_deaths_list), len(y_cases_list))
                min_len = min(len(x_date_list), len(y_recovered_list), len(y_deaths_list), len(y_cases_list))
                num_to_pop = max_len - min_len
                for lst in mega_list:
                    if len(lst) != min_len:
                        for _ in range(num_to_pop):
                            lst.pop()

            fig1, ax1 = plt.subplots()
            ax1.set_title('World timeline', fontsize=20)

            ax1.plot(x_date_list, y_recovered_list, c='green', label='recoveries')
            ax1.plot(x_date_list, y_cases_list, c='red', label='cases')
            ax1.plot(x_date_list, y_deaths_list, c='black', label='deaths')
            ax1.tick_params(axis='x', rotation=90, labelsize=7)

            fig1.legend(loc='upper left', ncol=3)
            fig1.tight_layout()
            plt.show()

        # ==================================================================================== #

        elif command.lower() == 'specific country timeline' or command == '5':
            country_name, x_date, new_daily_cases_y, new_daily_deaths_y, total_cases_y, total_recoveries_y, total_deaths_y = data

            fig1, ax1 = plt.subplots()
            ax1.set_title(f'{country_name} timline', fontsize=20)
            ax1.plot(x_date, total_recoveries_y, c='green', label='total recoveries')
            ax1.plot(x_date, total_deaths_y, c='black', label='total deaths')
            ax1.plot(x_date, new_daily_cases_y, c='red', label='new daily cases', linestyle='dashed')
            ax1.plot(x_date, new_daily_deaths_y, c='black', label='new daily deaths', linestyle='dashed')
            ax1.plot(x_date, total_cases_y, c='red', label='total cases')

            # show value
            mplcursors.cursor()

            ax1.tick_params(axis='x', rotation=90, labelsize=7)
            fig1.legend(loc='upper left', ncol=2, handletextpad=0.3, handlelength=1.5, labelspacing=0)
            fig1.tight_layout()
            plt.show()

# ==================================================================================== #

        elif command.lower() == 'all countries timeline[cases]' or command == '6':
            all_countries_timeline_cases_dict = data[0]
            print(all_countries_timeline_cases_dict)

def show_in_terminal(x_data, y_data):
    print('\n')
    for x, y in dict(zip(x_data, y_data)).items():
        print(f'{x} --> {y}')
    print('\n')


if __name__ == '__main__':
    main()
