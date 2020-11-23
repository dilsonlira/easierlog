from re import match

import pytest

from easylog import log

expressions = [
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

log_pattern = r'^\[(.+)\]\s(.+)'
marker_pattern = r'\w+\.py\s\(line\s\d+\)\sin\s.+'
expression_pattern = r'\(\w+\)\s\w+\s=\s.+'


@pytest.mark.parametrize('expression', expressions)
def test_expressions(expression, capfd):
    log(expression)
    output, _ = capfd.readouterr()
    marker_content, expression_eval = match(log_pattern, output).groups()
    assert match(marker_pattern, marker_content) is not None
    assert match(expression_pattern, expression_eval) is not None


def test_literal_string(capfd):
    log('testing')
    output, _ = capfd.readouterr()
    marker_content, expression_eval = match(log_pattern, output).groups()
    assert isinstance(expression_eval, str)
    assert match(marker_pattern, marker_content) is not None


def test_multiline_literal_string(capfd):
    log('testing \n multiple \n line \n strings')
    output, _ = capfd.readouterr()
    marker_content, expression_eval = match(log_pattern, output).groups()
    assert isinstance(expression_eval, str)
    assert match(marker_pattern, marker_content) is not None


def test_empty_string(capfd):
    log('')
    output, _ = capfd.readouterr()
    marker_content, expression_eval = match(log_pattern, output).groups()
    assert isinstance(expression_eval, str)
    assert match(marker_pattern, marker_content) is not None
