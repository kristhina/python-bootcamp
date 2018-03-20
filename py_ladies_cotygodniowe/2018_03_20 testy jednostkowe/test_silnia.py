import pytest
from app.silnia import silnia


def test_silnia():
    assert silnia(0) == 1
    assert silnia(1) == 1
    assert silnia(2) == 2
    assert silnia(5) == 120

    with pytest.raises(ValueError):
        silnia(-1)