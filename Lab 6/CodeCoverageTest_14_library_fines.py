
import pytest

from library_fines import late_fine, can_borrow, renewal_status


# Tests for late_fine()

def test_student_returned_on_time():
    assert late_fine("student", 10, False) == 0


def test_faculty_returned_on_time():
    assert late_fine("faculty", 20, False) == 0


def test_guest_overdue():
    assert late_fine("guest", 16, False) == 10


def test_damaged_book():
    assert late_fine("student", 15, True) == 152


def test_fine_capped_at_200():
    assert late_fine("guest", 100, False) == 200


def test_unknown_member():
    with pytest.raises(ValueError, match="unknown member"):
        late_fine("visitor", 10, False)


def test_negative_days():
    with pytest.raises(ValueError, match="invalid days"):
        late_fine("student", -1, False)


# Tests for can_borrow()

def test_student_can_borrow():
    assert can_borrow(1, 0, "student") is True


def test_student_cannot_borrow_at_limit():
    assert can_borrow(3, 0, "student") is False


def test_faculty_can_borrow():
    assert can_borrow(5, 0, "faculty") is True


def test_faculty_cannot_borrow_at_limit():
    assert can_borrow(10, 0, "faculty") is False


def test_cannot_borrow_with_high_pending_fine():
    assert can_borrow(1, 101, "student") is False


# Tests for renewal_status()

def test_renewal_denied_due_to_reservation():
    assert renewal_status(0, True, 10) == "denied"


def test_renewal_limit_reached():
    assert renewal_status(2, False, 10) == "limit reached"


def test_renewal_overdue():
    assert renewal_status(1, False, -1) == "overdue"


def test_renewal_successful():
    assert renewal_status(0, False, 10) == "renewed"
