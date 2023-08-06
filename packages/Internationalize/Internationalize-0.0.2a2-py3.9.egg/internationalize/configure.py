import typing as tp

from . import _working_dict


def add_to_kw(keyword: str, data: tp.Dict[str, tp.Any]) -> None:
    """
    Add data to a keyword
    :param keyword: keyword to add to
    :param data: dictionary of [language, anything, str is suggested]
    """
    if keyword not in _working_dict:
        _working_dict[keyword] = data
        return

    dict_to_mutate = _working_dict[keyword]

    for language, baggage in data.items():
        if baggage not in dict_to_mutate:
            dict_to_mutate[language] = baggage
        else:
            dict_to_mutate[language].update(baggage)


def add(*data: tp.Dict[str, tp.Dict[str, tp.Any]]) -> None:
    """
    Add data to the working set.

    You can use it either like:

    .. code-block: python

        add({'hello': {'pl': 'Witaj', en: 'Welcome'})

    And as

    .. code-block: python

        add({'hello': {'pl': 'Witaj', en: 'Welcome'},
            {'bye': {'pl': 'Żegnaj', en': 'Goodbye'})


    :param data: a dictionary of [working keyword => dictionary[language, anything, str is suggested]]
    """
    for datum in data:
        for keyword, baggage in datum.items():
            add_to_kw(keyword, baggage)
