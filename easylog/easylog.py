#!/usr/bin/env python

from inspect import currentframe, getouterframes


def log(expression):
    """Prints name and current value of variable or expression"""

    def get_frame_data(expression):

        try:
            current_frame = currentframe()
            function_name = getouterframes(current_frame)[1][3]
            outer_frame = getouterframes(current_frame)[2]
            caller, path, line_number, scope, code = outer_frame[:5]

        finally:
            del current_frame
            del outer_frame

        caller_vars = caller.f_locals
        command = code[0].strip()
        expression_passed = command[len(function_name) + 1:-1].strip()
        file_name = path.split('/')[-1]

        data = {
            'evaluation': expression,
            'caller_vars': caller_vars,
            'expression_passed': expression_passed,
            'file_name': file_name,
            'line_number': line_number,
            'scope': scope
        }

        return data

    def make_header(frame_data):

        file_name = frame_data['file_name']
        line_number = frame_data['line_number']
        scope = frame_data['scope']

        header = f'{file_name} (line {line_number}) in {scope}'

        return header

    def make_body(frame_data):

        expression = frame_data['expression_passed']
        evaluation = frame_data['evaluation']

        expression_type = type(evaluation).__name__

        if expression_type == 'str':
            evaluation = f'\'{evaluation}\''

        log_body = f'({expression_type}) {expression} = {evaluation}'

        for char in ['\'', '\"']:
            if expression.startswith(char) and expression.endswith(char):
                # expression is a string literal

                log_body = expression
                break

        return log_body

    if expression is None:
        return

    _frame_data = get_frame_data(expression)

    for caller_variable_name, caller_variable_value \
            in _frame_data['caller_vars'].items():

        if isinstance(caller_variable_value, str):
            caller_variable_assignment_line = \
                f'{caller_variable_name} = \"{caller_variable_value}\"'
        else:
            caller_variable_assignment_line = \
                f'{caller_variable_name} = {caller_variable_value}'

        try:
            exec(caller_variable_assignment_line)
        except BaseException:
            pass

    log_header = make_header(_frame_data)
    log_body = make_body(_frame_data)

    print(f'[{log_header}] {log_body}')


if __name__ == '__main__':
    pass
