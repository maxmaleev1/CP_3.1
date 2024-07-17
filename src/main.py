from utils import sorting_list_date, filtering_list, loading_file, get_data, get_card_inf, get_money

def main(num_operations=5):
    '''Главная функция с заданным счетчиком количества выдаваемых денежных операций
    '''
    sorted_list = sorting_list_date(filtering_list(loading_file('operations.json')))
    for operation in sorted_list:
        if num_operations == 0:
            break
        print(get_data(operation['date']), operation["description"])
        if operation["description"] != 'Открытие вклада':
            print(get_card_inf(operation['from']) + ' -> ', end='')
        print(get_card_inf(operation['to']))
        print(get_money(operation) + '\n')
        num_operations -= 1


if __name__ == "__main__":
    main()