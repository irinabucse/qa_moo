import pytest


class Login(object):
    @pytest.fixture
    def good(request):
        return {
            'username': 'irinabucse.qa@gmail.com',
            'password': 'test12345'
        }
