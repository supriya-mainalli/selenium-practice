import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_login(self):
        print("I m inside the login page")

    def test_dashboard(self):
        print("I m inside the dashboard page")

    def test_inventory(self):
        print("I m inside the inventory page")
