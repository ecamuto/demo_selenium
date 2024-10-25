
class SoftAssert:
    def __init__(self):
        self.errors = []

    def assert_equal(self, actual, expected, message=""):
        try:
            assert actual == expected, message
        except AssertionError as e:
            self.errors.append(str(e))

    def assert_true(self, condition, message=""):
        try:
            assert condition, message
        except AssertionError as e:
            self.errors.append(str(e))

    def assert_false(self, condition, message=""):
        try:
            assert not condition, message
        except AssertionError as e:
            self.errors.append(str(e))

    def assert_in(self, member, container, message=""):
        try:
            assert member in container, message
        except AssertionError as e:
            self.errors.append(str(e))

    def assert_all(self):
        if self.errors:
            raise AssertionError('\n'.join(self.errors))