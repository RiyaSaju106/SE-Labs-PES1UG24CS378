
import pytest

from library_fines import late_fine, can_borrow, renewal_status


# Branch tests for late_fine()

def test_unknown_member_branch():
    with pytest.raises(ValueError, match="unknown member"):
        late_fine("visitor", 10, False)


def test_negative_days_branch():
    with pytest.raises(ValueError, match="invalid days"):
        late_fine("student", -1, False)


def test_faculty_member_branch():
    assert late_fine("faculty", 31, False) == 1


def test_non_faculty_member_branch():
    assert late_fine("student", 15, False) == 2


def test_overdue_branch():
    assert late_fine("guest", 15, False) == 5


def test_not_overdue_branch():
    assert late_fine("guest", 14, False) == 0


def test_fine_cap_branch():
    assert late_fine("guest", 100, False) == 200


def test_fine_below_cap_branch():
    assert late_fine("student", 15, False) == 2


def test_damaged_book_branch():
    assert late_fine("student", 14, True) == 150


def test_undamaged_book_branch():
    assert late_fine("student", 14, False) == 0


# Branch tests for can_borrow()

def test_pending_fine_exceeds_limit():
    assert can_borrow(0, 101, "student") is False


def test_pending_fine_within_limit():
    assert can_borrow(0, 100, "student") is True


def test_faculty_borrowing_branch():
    assert can_borrow(9, 0, "faculty") is True


def test_faculty_limit_branch():
    assert can_borrow(10, 0, "faculty") is False


def test_non_faculty_borrowing_branch():
    assert can_borrow(2, 0, "student") is True


def test_non_faculty_limit_branch():
    assert can_borrow(3, 0, "student") is False


# Branch tests for renewal_status()

def test_reservation_branch():
    assert renewal_status(0, True, 10) == "denied"


def test_no_reservation_branch():
    assert renewal_status(0, False, 10) == "renewed"


def test_renewal_limit_branch():
    assert renewal_status(2, False, 10) == "limit reached"


def test_below_renewal_limit_branch():
    assert renewal_status(1, False, 10) == "renewed"


def test_overdue_renewal_branch():
    assert renewal_status(1, False, -1) == "overdue"


def test_not_overdue_renewal_branch():
    assert renewal_status(1, False, 0) == "renewed"
