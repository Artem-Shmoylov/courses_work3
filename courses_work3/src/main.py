from utils import load_operations, last_executed_op

PATH_TO_OPERATIONS = 'operations.json'

operations = load_operations(PATH_TO_OPERATIONS)
executed_op = last_executed_op(operations)
for op in executed_op:
    print(op)
