from .config import Ergo


def regex_equal(keywords) -> str:
    return '|'.join(('^'+k+'$' for k in keywords))


def regex_ergo(keywords) -> str:
    command = Ergo().call
    return '|'.join(('^'+command+k+'$' for k in keywords))
