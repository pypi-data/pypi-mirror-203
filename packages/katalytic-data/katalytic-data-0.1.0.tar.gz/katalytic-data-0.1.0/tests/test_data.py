import pytest

from katalytic.data import map_dict_keys, map_dict_values, sort_dict_by_keys, sort_dict_by_values


class Test_map_dict_keys:
    @pytest.mark.parametrize('wrong_type', [[], set(), (), {}, 1, 1.0, True, None, False, 'string', object()])
    def test_mapping_is_not_a_function(self, wrong_type):
        with pytest.raises(TypeError):
            map_dict_keys(wrong_type, {})

    @pytest.mark.parametrize('wrong_type', [[], set(), (), 1, 1.0, True, None, False, 'string', object()])
    def test_not_a_dict(self, wrong_type):
        with pytest.raises(TypeError):
            map_dict_keys(lambda x: x, wrong_type)

    @pytest.mark.parametrize('wrong_type', [[], set(), (), {}, 1, 1.0, True, False, 'string', object()])
    def test_condition_is_not_a_function(self, wrong_type):
        with pytest.raises(TypeError):
            map_dict_keys(lambda x: x, {}, condition=wrong_type)

    def test_empty(self):
        assert map_dict_keys(lambda x: x, {}) == {}

    def test_simple_mapping(self):
        assert map_dict_keys(str.upper, {'a': 1, 'b': 2}) == {'A': 1, 'B': 2}

    def test_conditioned_mapping(self):
        data = {'a': 1, (0, 1): 2}
        expected = {'A': 1, (0, 1): 2}
        is_str = lambda x: isinstance(x, str)
        assert map_dict_keys(str.upper, data, condition=is_str) == expected


class Test_map_dict_values:
    @pytest.mark.parametrize('wrong_type', [[], set(), (), {}, 1, 1.0, True, None, False, 'string', object()])
    def test_mapping_is_not_a_function(self, wrong_type):
        with pytest.raises(TypeError):
            map_dict_values(wrong_type, {})

    @pytest.mark.parametrize('wrong_type', [[], set(), (), 1, 1.0, True, None, False, 'string', object()])
    def test_not_a_dict(self, wrong_type):
        with pytest.raises(TypeError):
            map_dict_values(lambda x: x, wrong_type)

    @pytest.mark.parametrize('wrong_type', [[], set(), (), {}, 1, 1.0, True, False, 'string', object()])
    def test_condition_is_not_a_function(self, wrong_type):
        with pytest.raises(TypeError):
            map_dict_values(lambda x: x, {}, condition=wrong_type)

    def test_empty(self):
        assert map_dict_values(lambda x: x, {}) == {}

    def test_simple_mapping(self):
        assert map_dict_values(str, {'a': 1, 'b': 2}) == {'a': '1', 'b': '2'}

    def test_conditioned_mapping(self):
        data = {'a': -1, (0, 1): 1}
        expected = {'a': '-1', (0, 1): 1}
        is_negative = lambda x: x < 0
        assert map_dict_values(str, data, condition=is_negative) == expected


class Test_sort_dict_by_keys:
    @pytest.mark.parametrize('wrong_type', [[], set(), (), 1, 1.0, True, None, False, 'string', object()])
    def test_not_a_dict(self, wrong_type):
        with pytest.raises(TypeError):
            sort_dict_by_keys(wrong_type)

    @pytest.mark.parametrize('wrong_type', [[], set(), (), {}, 1, 1.0, True, False, 'string', object()])
    def test_key_is_not_a_function(self, wrong_type):
        with pytest.raises(TypeError):
            sort_dict_by_keys({}, key=wrong_type)

    @pytest.mark.parametrize('wrong_type', [[], set(), (), {}, 1, 1.0, None, 'string', object()])
    def test_not_a_bool(self, wrong_type):
        with pytest.raises(TypeError):
            sort_dict_by_keys({}, reverse=wrong_type)

    def test_empty(self):
        assert sort_dict_by_keys({}) == {}

    def test_basic(self):
        out = sort_dict_by_keys({'b': 2, 'c': 1, 'a': 3})
        assert list(out.keys()) == ['a', 'b', 'c']

    def test_with_key(self):
        out = sort_dict_by_keys({'qwerty': 1, 'x': 3, 'asd': 2}, key=len)
        assert list(out.keys()) == ['x', 'asd', 'qwerty']

    def test_reversed(self):
        out = sort_dict_by_keys({'b': 2, 'c': 1, 'a': 3}, reverse=True)
        assert list(out.keys()) == ['c', 'b', 'a']

    def test_with_key_and_reversed(self):
        out = sort_dict_by_keys({'qwerty': 1, 'x': 3, 'asd': 2}, key=len, reverse=True)
        assert list(out.keys()) == ['qwerty', 'asd', 'x']



class Test_sort_dict_by_values:
    @pytest.mark.parametrize('wrong_type', [[], set(), (), 1, 1.0, True, None, False, 'string', object()])
    def test_not_a_dict(self, wrong_type):
        with pytest.raises(TypeError):
            sort_dict_by_values(wrong_type)

    @pytest.mark.parametrize('wrong_type', [[], set(), (), {}, 1, 1.0, True, False, 'string', object()])
    def test_key_is_not_a_function(self, wrong_type):
        with pytest.raises(TypeError):
            sort_dict_by_values({}, key=wrong_type)

    @pytest.mark.parametrize('wrong_type', [[], set(), (), {}, 1, 1.0, None, 'string', object()])
    def test_not_a_bool(self, wrong_type):
        with pytest.raises(TypeError):
            sort_dict_by_values({}, reverse=wrong_type)

    def test_empty(self):
        assert sort_dict_by_values({}) == {}

    def test_basic(self):
        out = sort_dict_by_values({'b': 2, 'c': 1, 'a': 3})
        assert list(out.values()) == [1, 2, 3]

    def test_with_key(self):
        out = sort_dict_by_values({'qwerty': 1, 'x': 3, 'asd': -2}, key=abs)
        assert list(out.values()) == [1, -2, 3]

    def test_reversed(self):
        out = sort_dict_by_values({'b': 2, 'c': 1, 'a': 3}, reverse=True)
        assert list(out.values()) == [3, 2, 1]

    def test_with_key_and_reversed(self):
        out = sort_dict_by_values({'qwerty': 1, 'x': 3, 'asd': -2}, key=abs, reverse=True)
        assert list(out.values()) == [3, -2, 1]
