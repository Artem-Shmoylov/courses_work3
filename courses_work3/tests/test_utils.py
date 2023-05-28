import os

import pytest

from courses_work3.src import utils


def test_load_operations():
    with pytest.raises(FileNotFoundError):
        utils.load_operations('operations')


def test_coding_sender():
    assert utils.coding_sender("Maestro 1308795367077170") == "Maestro 1308 79** **** 7170"


def test_coding_to():
    assert utils.coding_to("Счет 18889008294666828266") == "Счет **8266"

def test_last_executed_op():
    assert isinstance(utils.last_executed_op(utils.load_operations("/home/artem/PycharmProjects/courses_work3/courses_work3/src/operations.json")), list) == True
