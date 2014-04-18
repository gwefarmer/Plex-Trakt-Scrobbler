def setdefault(d, defaults, func=None):
    for key, value in defaults.items():
        if func and not func(key, value):
            continue

        d.setdefault(key, value)


def parse_credentials(value):
    if type(value) is dict:
        return value

    if hasattr(value, '__iter__') and len(value) == 2:
        return {
            'username': value[0],
            'password': value[1]
        }

    return value


def has_attribute(obj, name):
    try:
        object.__getattribute__(obj, name)
        return True
    except AttributeError:
        return False


def update_attributes(obj, dictionary, keys):
    if not dictionary:
        return

    for key in keys:
        if key not in dictionary:
            continue

        if getattr(obj, key) is not None:
            continue

        setattr(obj, key, dictionary[key])
