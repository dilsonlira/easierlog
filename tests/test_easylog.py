import pytest

from easylog import log

vars = [
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
    file_name = 'test_easylog.py'
    log_header = f'{file_name} (line {line_number}) in {function_name}'

    variable_type = type(variable_value).__name__
    if variable_type == 'str':
        variable_value = f'\'{variable_value}\''

    if variable_name is None:
        # string literal
        log_body = variable_value
    else:
        log_body = f'({variable_type}) {variable_name} = {variable_value}'

    log_line = f'[{log_header}] {log_body}\n'

    return log_line


@pytest.mark.parametrize('var', vars)
def test_vars(var, capfd):
    log(var)
    actual_output = capfd.readouterr().out
    expected_output = make_log_line('test_vars', 53, 'var', var)
    assert expected_output == actual_output


def test_literal_string(capfd):
    log('testing')
    actual_output = capfd.readouterr().out
    expected_output = make_log_line('test_literal_string', 60, None, 'testing')
    assert expected_output == actual_output


def test_empty_string(capfd):
    log('')
    actual_output = capfd.readouterr().out
    expected_output = make_log_line('test_empty_string', 67, None, '')
    assert expected_output == actual_output


def test_list_vars(capfd):
    log(vars)
    actual_output = capfd.readouterr().out
    expected_output = make_log_line('test_list_vars', 74, 'vars', vars)
    assert expected_output == actual_output


def test_many_variables(capfd):
    a = 1
    b = 4.3
    c = 'hello world'
    log(a, b, c)
    actual_output = capfd.readouterr().out
    log_lines = ''
    log_lines += make_log_line('test_many_variables', 84, 'a', a)
    log_lines += make_log_line('test_many_variables', 84, 'b', b)
    log_lines += make_log_line('test_many_variables', 84, 'c', c)
    assert actual_output == log_lines


def test_no_arguments(capfd):
    a = 1
    b = 4.3
    c = 'hello world'
    log()
    actual_output = capfd.readouterr().out
    log_lines = ''
    log_lines += make_log_line('test_no_arguments', 97, 'c', c)
    log_lines += make_log_line('test_no_arguments', 97, 'b', b)
    log_lines += make_log_line('test_no_arguments', 97, 'a', a)
    log_lines += make_log_line('test_no_arguments', 97, 'capfd', capfd)
    assert actual_output == log_lines
