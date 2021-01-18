from inspect import currentframe, getouterframes


def get_frame_data(expression):
    """Get expression passed as argument and other necessary info"""

    try:
        current_frame = currentframe()
        function_name = getouterframes(current_frame)[1][3]
        outer_frame = getouterframes(current_frame)[2]
        caller, path, line_number, scope, code = outer_frame[:5]
        if path == '<stdin>':
            # Invocation in a Python interactive shell
            return None

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
    """Make log header"""

    file_name = frame_data['file_name']
    line_number = frame_data['line_number']
    scope = frame_data['scope']

    header = f'{file_name} (line {line_number}) in {scope}'

    return header


def make_body(frame_data):
    """Make log body"""

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
