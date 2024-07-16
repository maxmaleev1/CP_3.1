import pytest
from src.utils import loading_file, filtering_list, sorting_list_date, get_data, get_card_inf, get_money, get_main
import os
from config import ROOT_DIR


operations = [
    {"id": 1, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000000"},
    {"id": 2, "state": "CANCELED", "date": "2018-02-01T00:00:00.000000"},
    {"id": 3, "state": "EXECUTED", "date": "2018-03-01T00:00:00.000000"},
    {"id": 4, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000001"}
]

operation = {
"operationAmount": {'amount': '21344.35', 'currency': {'name': 'руб.'}}
}

@pytest.fixture
def operations_fixture():
    return operations

@pytest.fixture
def operation_fixture():
    return operation

test_path = os.path.join(ROOT_DIR, 'tests', 'test_operations.json')

def test_loading_file():
    assert loading_file(test_path) == []

def test_filtering_list(operations_fixture):
    assert len(filtering_list(operations_fixture)) == 3

def test_sorting_list_date(operations_fixture):
    assert [i["id"] for i in sorting_list_date(operations_fixture)] == [3, 2, 4, 1]

def test_get_data():
    assert get_data("2019-08-26T10:50:58.294041") == '26.08.2019'

def test_get_card_inf():
    assert get_card_inf("Visa Classic 7756673469642839") == "Visa Classic 7756 67** **** 2839"
    assert get_card_inf("Счет 35383033474447895560") == "Счет **5560"

def test_get_money(operation_fixture):
    assert get_money(operation_fixture) == '21344.35 руб.'