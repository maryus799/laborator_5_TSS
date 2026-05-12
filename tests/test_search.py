"""
Teste pentru funcția search(v, key)
===================================

Teste funcționale (black-box):
  - Partiționare în clase de echivalență
  - Analiza valorilor de frontieră

Teste structurale (white-box):
  - Statement coverage
  - Decision coverage
  - Condition coverage

Teste suplimentare pentru mutanți
"""

import unittest
from search import search


# ============================================================================
# 1. TESTE FUNCȚIONALE (BLACK-BOX)
# ============================================================================

class TestPartitionareClaseEchivalenta(unittest.TestCase):
    """
    Clase de echivalență identificate:
      CE1: key se află în vector → returnează indicele
      CE2: key NU se află în vector → returnează -1
      CE3: vectorul conține duplicate ale lui key → returnează primul indice
      CE4: vector invalid (lungime != 5) → ValueError
    """

    # CE1: key se află în vector
    def test_ce1_key_gasit_in_vector(self):
        self.assertEqual(search([10, 20, 30, 40, 50], 30), 2)

    # CE2: key NU se află în vector
    def test_ce2_key_negasit_in_vector(self):
        self.assertEqual(search([10, 20, 30, 40, 50], 99), -1)

    # CE3: duplicate — returnează primul indice
    def test_ce3_key_duplicat_returneaza_primul_indice(self):
        self.assertEqual(search([5, 3, 5, 5, 1], 5), 0)

    # CE4: vector invalid
    def test_ce4_vector_lungime_gresita(self):
        with self.assertRaises(ValueError):
            search([1, 2, 3], 1)

    def test_ce4_vector_gol(self):
        with self.assertRaises(ValueError):
            search([], 1)

    def test_ce4_vector_prea_lung(self):
        with self.assertRaises(ValueError):
            search([1, 2, 3, 4, 5, 6], 1)


class TestAnalizaValorilorDeFrontiera(unittest.TestCase):
    """
    Valori de frontieră identificate:
      VF1: key pe prima poziție (index 0)
      VF2: key pe ultima poziție (index 4)
      VF3: key pe poziție intermediară (index 2)
      VF4: valori extreme (numere foarte mari / foarte mici)
      VF5: vector cu toate elementele identice
      VF6: key = 0 (valoare de frontieră numerică)
      VF7: valori negative
    """

    # VF1: key pe prima poziție
    def test_vf1_key_pe_pozitia_0(self):
        self.assertEqual(search([7, 2, 3, 4, 5], 7), 0)

    # VF2: key pe ultima poziție
    def test_vf2_key_pe_pozitia_4(self):
        self.assertEqual(search([1, 2, 3, 4, 7], 7), 4)

    # VF3: key pe poziție intermediară
    def test_vf3_key_pe_pozitia_2(self):
        self.assertEqual(search([1, 2, 7, 4, 5], 7), 2)

    # VF4: valori extreme pozitive
    def test_vf4_valoare_foarte_mare(self):
        self.assertEqual(search([0, 0, 0, 0, 999999999], 999999999), 4)

    # VF4: valori extreme negative
    def test_vf4_valoare_foarte_mica(self):
        self.assertEqual(search([-999999999, 0, 0, 0, 0], -999999999), 0)

    # VF5: toate elementele identice, key prezent
    def test_vf5_toate_identice_key_prezent(self):
        self.assertEqual(search([3, 3, 3, 3, 3], 3), 0)

    # VF5: toate elementele identice, key absent
    def test_vf5_toate_identice_key_absent(self):
        self.assertEqual(search([3, 3, 3, 3, 3], 4), -1)

    # VF6: key = 0
    def test_vf6_key_zero_prezent(self):
        self.assertEqual(search([1, 0, 3, 4, 5], 0), 1)

    def test_vf6_key_zero_absent(self):
        self.assertEqual(search([1, 2, 3, 4, 5], 0), -1)

    # VF7: valori negative
    def test_vf7_valori_negative(self):
        self.assertEqual(search([-5, -3, -1, -4, -2], -1), 2)

    def test_vf7_key_negativ_absent(self):
        self.assertEqual(search([1, 2, 3, 4, 5], -1), -1)


# ============================================================================
# 2. TESTE STRUCTURALE (WHITE-BOX)
# ============================================================================

class TestStatementCoverage(unittest.TestCase):
    """
    Statement Coverage — fiecare instrucțiune executată cel puțin o dată.

    Instrucțiuni:
      S1: for i in range(len(v))
      S2: return i
      S3: return -1

    Două teste sunt suficiente:
      - un test unde key e găsit → acoperă S1, S2
      - un test unde key nu e găsit → acoperă S1, S3
    """

    def test_sc_key_gasit(self):
        """Acoperă S1 (iterare) + S2 (return i)"""
        self.assertEqual(search([10, 20, 30, 40, 50], 10), 0)

    def test_sc_key_negasit(self):
        """Acoperă S1 (iterare completă) + S3 (return -1)"""
        self.assertEqual(search([10, 20, 30, 40, 50], 99), -1)


class TestDecisionCoverage(unittest.TestCase):
    """
    Decision Coverage — fiecare decizie evaluată pe True și pe False.

    Decizii:
      D1: if v[i] == key → True (găsit) sau False (nu e egal)
      D2: for (implicit: mai sunt elemente?) → True (continuă) sau False (stop)

    Teste:
      - key găsit pe prima poziție → D1=True imediat
      - key negăsit → D1=False de 5 ori, D2=False la final
      - key găsit pe ultima poziție → D1=False de 4 ori, apoi D1=True
    """

    def test_dc_decizie_true_imediat(self):
        """D1 = True la prima iterație"""
        self.assertEqual(search([5, 1, 2, 3, 4], 5), 0)

    def test_dc_decizie_false_mereu(self):
        """D1 = False la fiecare iterație, D2 = False la final"""
        self.assertEqual(search([1, 2, 3, 4, 5], 99), -1)

    def test_dc_decizie_true_la_final(self):
        """D1 = False de 4 ori, apoi D1 = True"""
        self.assertEqual(search([1, 2, 3, 4, 5], 5), 4)


class TestConditionCoverage(unittest.TestCase):
    """
    Condition Coverage — fiecare condiție atomică ia valorile True și False.

    Condiția din decizia D1: v[i] == key
      - True: când v[i] este egal cu key
      - False: când v[i] nu este egal cu key

    Condiția implicită din for (i < len(v)):
      - True: mai sunt elemente de parcurs
      - False: s-au terminat elementele
    """

    def test_cc_conditie_egalitate_true(self):
        """v[i] == key este True"""
        self.assertEqual(search([1, 2, 3, 4, 5], 3), 2)

    def test_cc_conditie_egalitate_false(self):
        """v[i] == key este False pentru toate elementele"""
        self.assertEqual(search([1, 2, 3, 4, 5], 7), -1)

    def test_cc_conditie_for_true_si_false(self):
        """Bucla iterează (True) și apoi se termină (False) — key pe ultima poziție"""
        self.assertEqual(search([1, 2, 3, 4, 5], 5), 4)


# ============================================================================
# 3. TESTE SUPLIMENTARE PENTRU MUTANȚI
# ============================================================================

class TestMutanti(unittest.TestCase):
    """
    Teste suplimentare menite să omoare mutanți tipici:
      - Mutant: return i → return i+1 sau return i-1
      - Mutant: return -1 → return 0 sau return 1
      - Mutant: v[i] == key → v[i] != key
      - Mutant: range(len(v)) → range(len(v)-1) (nu verifică ultimul element)
      - Mutant: schimbarea operatorului de comparație (==, !=, <, >, <=, >=)
    """

    def test_mut_return_index_corect_pozitia_0(self):
        """Omoară mutantul return i+1 / return i-1 când key e pe poziția 0"""
        self.assertEqual(search([42, 1, 2, 3, 4], 42), 0)

    def test_mut_return_index_corect_pozitia_1(self):
        """Omoară mutantul return 0 / return i-1 când key e pe poziția 1"""
        self.assertEqual(search([1, 42, 3, 4, 5], 42), 1)

    def test_mut_return_index_corect_pozitia_3(self):
        """Omoară mutantul care ar schimba indicele returnat"""
        self.assertEqual(search([1, 2, 3, 42, 5], 42), 3)

    def test_mut_return_index_corect_pozitia_4(self):
        """Omoară mutantul range(len(v)-1) care ar sări peste ultimul element"""
        self.assertEqual(search([1, 2, 3, 4, 42], 42), 4)

    def test_mut_return_minus_1(self):
        """Omoară mutantul return -1 → return 0"""
        self.assertEqual(search([10, 20, 30, 40, 50], 999), -1)

    def test_mut_return_minus_1_diferit_de_1(self):
        """Omoară mutantul return -1 → return 1"""
        result = search([10, 20, 30, 40, 50], 999)
        self.assertNotEqual(result, 1)
        self.assertEqual(result, -1)

    def test_mut_operator_egalitate(self):
        """Omoară mutantul == → !="""
        # Dacă operatorul ar fi !=, ar returna 0 (primul element diferit de key)
        self.assertEqual(search([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(search([1, 2, 3, 4, 5], 6), -1)

    def test_mut_fiecare_pozitie_verificata(self):
        """Verifică explicit că fiecare poziție este testată corect"""
        v = [10, 20, 30, 40, 50]
        for i, val in enumerate(v):
            self.assertEqual(search(v, val), i)


if __name__ == "__main__":
    unittest.main()
