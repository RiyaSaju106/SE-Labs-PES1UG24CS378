
import re
import pytest
import string
from hypothesis import given, strategies as st

from processor import parse_member_id, total_fine, shelf_code


# 1. parse_member_id() - Valid and invalid inputs

valid_member_ids = st.tuples(
    st.text(alphabet=string.ascii_letters, min_size=1),
    st.integers(min_value=0)
).map(lambda x: f"{x[0]}-{x[1]}")


@given(valid_member_ids)
def test_parse_member_id_valid(value):
    member_type, number = value.split("-")
    assert parse_member_id(value) == (member_type.upper(), int(number))


@given(st.one_of(st.text(), st.none()))
def test_parse_member_id_invalid(value):
    if isinstance(value, str) and re.fullmatch(r"[A-Za-z]+-[0-9]+", value):
        assert parse_member_id(value) == (
            value.split("-")[0].upper(),
            int(value.split("-")[1])
        )
    else:
        with pytest.raises(ValueError):
            parse_member_id(value)


# 2. total_fine() - Valid and invalid inputs

valid_days = st.lists(
    st.integers(min_value=0, max_value=10000),
    min_size=1
).map(lambda days: ",".join(map(str, days)))


@given(valid_days)
def test_total_fine_valid(value):
    expected = sum(
        max(int(day) - 14, 0) * 2
        for day in value.split(",")
    )
    assert total_fine(value) == expected


@given(st.one_of(st.text(), st.none()))
def test_total_fine_invalid(value):
    if isinstance(value, str) and re.fullmatch(r"[0-9]+(,[0-9]+)*", value):
        expected = sum(
            max(int(day) - 14, 0) * 2
            for day in value.split(",")
        )
        assert total_fine(value) == expected
    else:
        with pytest.raises(ValueError):
            total_fine(value)


# 3. shelf_code() - Valid and invalid inputs

valid_titles = st.lists(
    st.text(alphabet=string.ascii_letters, min_size=1),
    min_size=2
).map(" ".join)


@given(valid_titles)
def test_shelf_code_valid(value):
    words = value.split()
    expected = (words[0][0] + words[1][0]).upper()
    assert shelf_code(value) == expected


@given(st.one_of(st.text(), st.none()))
def test_shelf_code_invalid(value):
    if isinstance(value, str) and len(value.split()) >= 2:
        words = value.split()
        expected = (words[0][0] + words[1][0]).upper()
        assert shelf_code(value) == expected
    else:
        with pytest.raises(ValueError):
            shelf_code(value)
