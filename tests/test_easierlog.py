import pytest

from easierlog.easierlog import log

var_list = [
    0,
    404,
    -23,
    3.14,
    0.7e-2,
    4.4e88,
    2j-3,
    '',
    'Always test your code!',
    'Verás que um filho teu não foge à luta',
    'さくらが恋しい',
    'أفضل التمور في العالم',
    'multi \n page \n string',
    'w' * 9999,
    True,
    [0, 1],
    (0, 1),
    {0, 1},
    {'zero': 0, 'one': 1},
    2 + 13,
    39 - 300,
    28 * 69,
    (4j - 1) / (7j + 99)
]


def make_log_line(function_name, line_number, variable_name, variable_value):
    file_name = 'test_easierlog.py'
    log_header = f'{file_name} (line {line_number}) in {function_name}'
    variable_type = type(variable_value).__name__
    if variable_type == 'str':
        if variable_value != 'No declared variables.':
            variable_value = f'\'{variable_value}\''

    if variable_name is None:
        # string literal
        log_body = variable_value
    else:
        log_body = f'({variable_type}) {variable_name} = {variable_value}'

    log_line = f'[{log_header}] {log_body}\n'

    return log_line


@pytest.mark.parametrize('var', var_list)
def test_vars(var, capfd):
    log(var)
    actual_output = capfd.readouterr().out
    expected_output = make_log_line('test_vars', 53, 'var', var)
    assert actual_output == expected_output


def test_literal_string(capfd):
    log('testing')
    actual_output = capfd.readouterr().out
    expected_output = make_log_line('test_literal_string', 60, None, 'testing')
    assert actual_output == expected_output


def test_empty_string(capfd):
    log('')
    actual_output = capfd.readouterr().out
    expected_output = make_log_line('test_empty_string', 67, None, '')
    assert actual_output == expected_output


def test_list_vars(capfd):
    log(var_list)
    actual_output = capfd.readouterr().out
    expected_output = make_log_line('test_list_vars', 74, 'var_list', var_list)
    assert actual_output == expected_output


def test_many_variables(capfd):
    a = 1
    b = 4.3
    c = 'hello world'
    log(a, b, c)
    fuction_name = 'test_many_variables'
    actual_output = capfd.readouterr().out
    expected_output = ''
    expected_output += make_log_line(fuction_name, 84, 'a', a)
    expected_output += make_log_line(fuction_name, 84, 'b', b)
    expected_output += make_log_line(fuction_name, 84, 'c', c)
    assert actual_output == expected_output


def test_no_args_with_vars(capfd):
    a = 1
    b = 4.3
    c = 'hello world'
    log()
    fuction_name = 'test_no_args_with_vars'
    actual_output = capfd.readouterr().out
    actual_list = [item + '\n' for item in actual_output[:-1].split('\n')]
    expected_list = []
    expected_list += [make_log_line(fuction_name, 98, 'a', a)]
    expected_list += [make_log_line(fuction_name, 98, 'b', b)]
    expected_list += [make_log_line(fuction_name, 98, 'c', c)]
    expected_list += [make_log_line(fuction_name, 98, 'capfd', capfd)]
    assert len(actual_list) == len(expected_list)
    assert set(actual_list) == set(expected_list)


def test_no_args_no_vars(capfd):
    def inner_function():
        log()
    inner_function()
    function_name = 'inner_function'
    no_vars_string = 'No declared variables.'
    actual_output = capfd.readouterr().out
    expected_output = make_log_line(function_name, 113, None, no_vars_string)
    assert actual_output == expected_output


def test_object(capfd):
    class MyClass:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return self.name

    my_object = MyClass('name')
    log(my_object)
    actual_output = capfd.readouterr().out
    expected_output = make_log_line('test_object', 131, 'my_object', my_object)
    assert actual_output == expected_output
