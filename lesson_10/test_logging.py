import pytest

from homework_10 import log_event
from datetime import datetime


@pytest.mark.parametrize("user, status, date",
[
    ("Edward", "success", datetime.now().time()),
    ("Andy", "expired", datetime.now().time()),
    ("Mary", "failed", datetime.now().time())
])

def test_logging(user: str, status: str, date: datetime):
    log_event(user, status, date)
    with open('login_system.log', 'r') as log_file:
        content = log_file.read()
        lines = content.splitlines()
        last_line: str = lines[len(lines) - 1]
        assert str(date) in last_line and user in last_line and status in last_line
