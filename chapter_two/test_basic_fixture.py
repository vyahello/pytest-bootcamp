from chapter_one.operation import increment


def setup() -> None:
    print("basic setup - executes before every test")


def teardown() -> None:
    print("basic teardown - executes after every test")


def setup_module() -> None:
    print("module setup - executes once for a module")


def teardown_module() -> None:
    print("module teardown - executes once for a module")


def test_increment() -> None:
    print("running test_increment test")
    assert increment(2) == 3


class TestFixtures:
    def setup_class(cls) -> None:
        print("basic class setup - executes once before all tests")

    def teardown_class(cls) -> None:
        print("basic class teardown - executes once after all tests")

    def setup(self) -> None:
        print("basic setup - executed once before every test")

    def teardown(self) -> None:
        print("basic teardown - executed once after every test")

    def test_increment_in_class(self) -> None:
        print("running test_increment_in_class test")
        assert increment(4) == 5
