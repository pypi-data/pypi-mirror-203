import pytest
from katalytic.checks import is_collection, is_primitive


class Test_is_primitive:
    @pytest.mark.parametrize('correct_type', [1, 1.0, True, False, 'string', None])
    def test_True(self, correct_type):
        assert is_primitive(correct_type)

    @pytest.mark.parametrize('wrong_type', [[], set(), (), {}, object()])
    def test_False(self, wrong_type):
        assert not is_primitive(wrong_type)


class Test_is_collection:
    @pytest.mark.parametrize('correct_type', [[], set(), (), {}])
    def test_True(self, correct_type):
        assert is_collection(correct_type)

    @pytest.mark.parametrize('wrong_type', [1, 1.0, True, False, 'string', None, object()])
    def test_False(self, wrong_type):
        assert not is_collection(wrong_type)
