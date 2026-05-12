def linear_search(v, key):
    """
    Caută key în lista v (lungime 5).
    Returnează indicele primei apariții sau -1 dacă nu există.
    """
    for i in range(len(v)):
        if v[i] == key:
            return i
    return -1