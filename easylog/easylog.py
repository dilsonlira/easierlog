#!/usr/bin/env python

from helpers import get_frame_data, make_header, make_body


def log(expression):
    """Prints name and current value of variable or expression"""

    if expression is None:
        return

    frame_data = get_frame_data(expression)

    if frame_data is None:
        shell_error_message = '''
        This function does not work in Python interactive shell.
        Try it inside a Python file.
        '''
        print(shell_error_message)
        return

    log_header = make_header(frame_data)

    log_body = make_body(frame_data)

    print(f'[{log_header}] {log_body}')


if __name__ == '__main__':
    pass
