from katalytic.pkg import get_version

__version__, __version_info__ = get_version(__name__)


def map_dict_keys(f, data, *, condition=None):
    if not callable(f):
        raise TypeError(f'<f> expects a function. Got {f!r}')
    elif not isinstance(data, dict):
        raise TypeError(f'<data> expects a dict. Got {data!r}')
    elif not(condition is None or callable(condition)):
        raise TypeError(f'<condition> expects None or a function. Got {condition!r}')

    if condition is None:
        return {f(k): v for k, v in data.items()}
    else:
        return {f(k) if condition(k) else k: v for k, v in data.items()}


def map_dict_values(f, data, *, condition=None):
    if not callable(f):
        raise TypeError(f'<f> expects a function. Got {f!r}')
    elif not isinstance(data, dict):
        raise TypeError(f'<data> expects a dict. Got {data!r}')
    elif not(condition is None or callable(condition)):
        raise TypeError(f'<condition> expects None or a function. Got {condition!r}')

    if condition is None:
        return {k: f(v) for k, v in data.items()}
    else:
        return {k: f(v) if condition(v) else v for k, v in data.items()}


def sort_dict_by_keys(data, *, key=None, reverse=False):
    """key is the "metric" to sort by, not the dict's key"""
    if not isinstance(data, dict):
        raise TypeError(f'<data> expects a dict. Got {data!r}')
    elif not(key is None or callable(key)):
        raise TypeError(f'<key> expects None or a function. Got {key!r}')
    elif not isinstance(reverse, bool):
        raise TypeError(f'<reverse> expects True or False. Got {reverse!r}')

    if key is None:
        return dict(sorted(data.items(), reverse=reverse))
    else:
        return dict(sorted(data.items(), key=lambda kv: key(kv[0]), reverse=reverse))


def sort_dict_by_values(data, *, key=None, reverse=False):
    """key is the "metric" to sort by, not the dict's key"""
    if not isinstance(data, dict):
        raise TypeError(f'<data> expects a dict. Got {data!r}')
    elif not(key is None or callable(key)):
        raise TypeError(f'<key> expects None or a function. Got {key!r}')
    elif not isinstance(reverse, bool):
        raise TypeError(f'<reverse> expects True or False. Got {reverse!r}')

    if key is None:
        return dict(sorted(data.items(), key=lambda kv: kv[1], reverse=reverse))
    else:
        return dict(sorted(data.items(), key=lambda kv: key(kv[1]), reverse=reverse))
