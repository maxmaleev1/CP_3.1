import json
from datetime import datetime

def loading_file(json_file):
    '''Открывает джейсоновский файл с операциями'''
    with open(json_file, 'r', encoding="utf-8") as load_file:
        return json.load(load_file)

def filtering_list(load_file):
    '''Фильтрует файл с операциями по статусу выполненных'''
    filtered_list = list(filter(lambda x: len(x) and x['state'] == 'EXECUTED', load_file))
    return filtered_list

def sorting_list_date(filtered_list):
    '''Сортирует по дате от новых к старым'''
    sorted_list = sorted(filtered_list, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return sorted_list

def get_data(date_in_file):
    '''Преобразует дату в требуемый формат: 14.10.2018
    '''
    date_obj = datetime.strptime(date_in_file, '%Y-%m-%dT%H:%M:%S.%f')
    return datetime.strftime(date_obj, '%d.%m.%Y')

def get_card_inf(inf):
    '''Преобразует информацию о транзакциях в требуемый вид:
    "Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638"
    '''
    inf_s = inf.split()
    if inf_s[0] == 'Счет':
        return 'Счет **' + inf[-4:]
    else:
        card_name = ' '.join(inf_s[:-1])
        return card_name + ' ' + inf_s[-1][:4] + ' ' + inf_s[-1][4:6] + '** **** ' + inf_s[-1][-4:]

def get_money(operation):
    '''Передает из файла с операциями информацию о деньгах в требуемом виде: "82771.72 руб."
    '''
    return f'{operation["operationAmount"]['amount']} {operation["operationAmount"]['currency']["name"]}'