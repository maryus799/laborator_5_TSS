def oracle_search(v, key):
    """
    Oracol independent — nu apelează linear_search.
    Folosește mecanismul nativ Python (index + excepție).
    """
    try:
        return v.index(key)
    except ValueError:
        return -1
