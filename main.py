from matplotlib import pyplot as plt
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
            print(x_data)
            print(y_data)



def show_in_terminal(x_data, y_data):
    print('\n')
    for x, y in dict(zip(x_data, y_data)).items():
        print(f'{x} --> {y}')
    print('\n')

if __name__ == '__main__':
    main()


