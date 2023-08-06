from typing import Dict, Any

from . import _working_dict


def get_for(keyword: str) -> Dict[str, Any]:
    """
    Provide a mapping of [language=>baggage] for given keyword

    :param keyword: a keyword to return for
    :return: a dictionary with entries
    :raises KeyError: mapping not found
    """

    return _working_dict[keyword]


def get(keyword: str, language: str) -> Any:
    """
    Provide an entry for given language and keyword

    :param keyword: a keyword to return for
    :param language: a language entry
    :return: a baggage given previously
    :raises KeyError: mapping not found
    """
    return _working_dict[keyword][language]
