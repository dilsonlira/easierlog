#!/usr/bin/env python

from contextlib import suppress

from helpers import get_frame_data, make_header, make_body


def log(expression):
    """Prints name and current value of variable or expression"""

    if expression is None:
        return

    frame_data = get_frame_data(expression)

    for variable_name, variable_value in frame_data['caller_vars'].items():

        if isinstance(variable_value, str):
            assignment_line = f'{variable_name} = \"{variable_value}\"'
        else:
            assignment_line = f'{variable_name} = {variable_value}'

        with suppress(SyntaxError):
            exec(assignment_line)

    log_header = make_header(frame_data)

    log_body = make_body(frame_data)

    print(f'[{log_header}] {log_body}')


if __name__ == '__main__':
    pass
