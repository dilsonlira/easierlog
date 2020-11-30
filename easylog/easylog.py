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

    argument = command[len(function_name) + 1:-1].strip()

    if argument == 'None':
        return

    file_name = path.split('/')[-1]
    marker = f'{file_name} (line {line_number}) in {scope}'

    type_ = type(expression).__name__

    if type_ == 'str':
        expression = f'\'{expression}\''

    argument_string = f'({type_}) {argument} = {expression}'

    for char in ['\'', '\"']:
        if argument.startswith(char) and argument.endswith(char):
            # argument is a string literal

            argument_string = argument
            break

    print(f'[{marker}] {argument_string}')


if __name__ == '__main__':
    pass
