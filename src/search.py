def search(v, key):
    """
    Caută elementul key în vectorul v de lungime 5.
    Returnează indicele elementului dacă este găsit, sau -1 dacă nu este găsit.

    Parametri:
        v (list[int]): vector de numere întregi, cu lungimea 5
        key (int): elementul căutat

    Returnează:
        int: indicele lui key în v, sau -1 dacă key nu se află în v
    """
    if not isinstance(v, list) or len(v) != 5:
        raise ValueError("Vectorul trebuie să fie o listă de lungime 5")

    for i in range(len(v)):       # S1: iterare prin vector
        if v[i] == key:           # D1: decizie — element găsit?
            return i              # S2: returnează indicele
    return -1                     # S3: element negăsit
