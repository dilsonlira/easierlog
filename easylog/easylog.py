#!/usr/bin/env python

from helpers import get_frame_data, make_header, make_body, print_log


def log(*variables):
    """Prints name and value of variables passed"""

    frame_data = get_frame_data()

    if frame_data is None:
        shell_error_message = '''
        This function does not work in Python interactive shell.
        Try it inside a Python file.
        '''
        print(shell_error_message)
        return

    log_header = make_header(frame_data)

    if variables:
        variable_names = frame_data['arguments_list']
        variable_values = variables

        for name, value in zip(variable_names, variable_values):
            log_body = make_body(name, value)
            print_log(log_header, log_body)
    else:
        for name, value in frame_data['caller_vars'].items():

            log_body = make_body(name, value)

            is_dunder = name.startswith('__') and name.endswith('__')
            is_function = hasattr(value, '__call__')

            if not is_dunder and not is_function:
                print_log(log_header, log_body)


if __name__ == '__main__':
    pass
