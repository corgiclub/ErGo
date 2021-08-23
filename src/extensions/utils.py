def regex_equal(keywords) -> str:
    return '|'.join(('^'+k+'$' for k in keywords))


