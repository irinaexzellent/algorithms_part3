import pytest

from two_bikes import buying_bikes


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ([1, 2, 4, 4, 6, 8], (3, 5)),
    ],
)
def test_buying_bikes(input, expected_result):
    assert buying_bikes(input) == expected_result
