import pytest

from tictactoe.core import Table


def test_table_init():
    """Test Table initialization"""
    Table(2)
    Table(3)


@pytest.mark.xfail
def test_table_init_failing():
    """Test failing Table initialization"""
    Table(-1)
    Table(0)
    Table(1)


def test_table_win():
    """Test Table.win()"""
    table = Table(3)
    table.play(0, 0)
    table.play(1, 1)
    table.play(1, 0)
    table.play(2, 1)
    table.play(2, 0)
    assert table.detect_win() == 1
