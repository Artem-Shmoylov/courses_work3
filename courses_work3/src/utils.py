import json

from courses_work3.src.classes import Operation
from datetime import datetime


def load_operations(filename):
    with open(filename, 'r') as file:
        operations_json = json.load(file)
        operations_list = []
        for operation in operations_json:
            try:
                operations_list.append(
                    Operation(
                        operation['id'],
                        operation['state'],
                        datetime.strptime(operation['date'].strip(), '%Y-%m-%dT%H:%M:%S.%f'),
                        operation['operationAmount'],
                        operation['description'],
                        operation['from'],
                        operation['to']))
            except KeyError:
                continue
    operations_sorted = sorted(operations_list, key=lambda op: op.date, reverse=True)

    return operations_sorted


def coding_sender(sender):
    sender_ = sender.split(' ')
    result = ''
    for elem in sender_:
        if not elem.isdigit():
            result += elem + " "
        else:
            result += elem[0:4] + " " + elem[4:6] + "** **** " + elem[-4:]
    return result


def coding_to(to):
    to_ = to.split(' ')
    result = ''
    for elem in to_:
        if not elem.isdigit():
            result += elem + " "
        else:
            result += "**" + elem[-4:]
    return result


def last_executed_op(operations):
    executed = 0
    ops_to_print = []
    for operation in operations:
        if operation.state == 'EXECUTED':
            executed += 1
            op = f'{operation.date:%d.%m.%Y}  {operation.description}\n'
            op = op + f'{coding_sender(operation.sender)} ---> {coding_to(operation.to)}\n'
            op = op + f'{operation.operationAmount["amount"]} {operation.operationAmount["currency"]["name"]}\n'
            ops_to_print.append(op)
        else:
            continue

        if executed == 5:
            return ops_to_print
