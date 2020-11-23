#!/usr/bin/env python

from inspect import currentframe, getouterframes


def log(expression):
    """Prints name and current value of variable or expression"""

    if expression is None:
        return

    try:
        current_frame = currentframe()
        function_name = current_frame.f_code.co_name
        outer_frame = getouterframes(current_frame)[1]
        path, line_number, scope, code = outer_frame[1:5]

    finally:
        del current_frame
        del outer_frame

    command = code[0].strip()

    expression = command[len(function_name) + 1:-1].strip()

    if expression == 'None':
        return

    file_name = path.split('/')[-1]
    marker = f'{file_name} (line {line_number}) in {scope}'

    value = eval(expression)
    type_ = type(value).__name__

    if type_ == 'str':
        value = f'\'{value}\''

    expression_string = f'({type_}) {expression} = {value}'

    for char in ['\'', '\"']:
        if expression.startswith(char) and expression.endswith(char):
            # expression is a string literal

            expression_string = expression
            break

    print(f'[{marker}] {expression_string}')


if __name__ == '__main__':
    log('testing log')
