from app.restore_names import restore_names
from unittest import mock


@mock.patch("app.restore_names.restore_names")
def test_first_name_equal_to_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Black",
            "ful_name": "Bob Black"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Bob"
