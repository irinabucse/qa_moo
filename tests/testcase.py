import unittest


class TestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(self):
        self.page.get_browser().maximize_window()

    @classmethod
    def tearDownClass(self):
        self.page.get_browser().close()