import os
import pytest
from _pytest.fixtures import SubRequest


@pytest.fixture(scope='module', autouse=True)
def setup_dir(request: SubRequest) -> None:
    os.mkdir('test-dir', mode=0o777)

    def teardown_dir() -> None:
        os.rmdir('test-dir-1')

    request.addfinalizer(teardown_dir)


@pytest.mark.dir
def test_rename_dir() -> None:
    os.rename('test-dir', 'test-dir-1')
    assert os.path.basename('test-dir-1') == 'test-dir-1'


@pytest.mark.dir
def test_list_dir() -> None:
    assert os.listdir('test-dir-1') == []