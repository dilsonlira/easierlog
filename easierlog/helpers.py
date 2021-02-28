from inspect import currentframe, getouterframes


def get_frame_data():
    """Returns a dictionary with
        - a list of variables in the scope where log was called
        - a list of arguments passed in log function
        - the file name where log was called
        - the line number where log was called
        - the name of the function where log was called
    """

    try:
        current_frame = currentframe()
        log_function_name = getouterframes(current_frame)[1][3]
        outer_frame = getouterframes(current_frame)[2]
        caller, path, line_number, function_name, code = outer_frame[:5]

        if path == '<stdin>':
            # Invocation in a Python interactive shell
            return None

    finally:
        del current_frame
        del outer_frame

    caller_vars = caller.f_locals
    command = code[0].strip()
    arguments_string = command[len(log_function_name) + 1:-1].strip()
    arguments_list = [item.strip() for item in arguments_string.split(',')]
    file_name = path.split('/')[-1]

    data = {
        'caller_vars': caller_vars,
        'arguments_list': arguments_list,
        'file_name': file_name,
        'line_number': line_number,
        'function_name': function_name
    }

    return data


def make_header(frame_data):
    """Makes log header"""

    file_name = frame_data['file_name']
    line_number = frame_data['line_number']
    function_name = frame_data['function_name']

    header = f'{file_name} (line {line_number}) in {function_name}'

    return header


def make_body(variable_name, variable_value):
    """Makes log body"""

    variable_type = type(variable_value).__name__

    if variable_type == 'str':
        variable_value = f'\'{variable_value}\''

    log_body = f'({variable_type}) {variable_name} = {variable_value}'

    for char in ['\'', '\"']:
        if variable_name.startswith(char) and variable_name.endswith(char):
            # expression is a string literal

            log_body = variable_name
            break

    return log_body


def print_log(header, body):
    '''Makes and prints log_line'''

    log_line = f'[{header}] {body}'
    print(log_line)
