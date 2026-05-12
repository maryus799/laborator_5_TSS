# Linear Search — Testing Pipeline (L1–L5)

![CI Status](https://github.com/maryus799/laborator_5_TSS/actions/workflows/ci.yml/badge.svg)

## Descrierea proiectului

Acest repository conține implementarea și testarea completă a funcției `linear_search(v, key)` — o căutare liniară într-o listă de 5 numere întregi — realizată în cadrul laboratoarelor L1–L5 din cursul **Testarea Sistemelor Software**.

Funcția returnează indicele primei apariții a lui `key` în lista `v`, sau `-1` dacă `key` nu se află în listă.

Proiectul acoperă întregul ciclu de testare:
- **L1/L2** — teste funcționale (black-box) și structurale (white-box) în Java
- **L3** — reimplementare Python, coverage 100%, mutation testing cu cosmic-ray (96%)
- **L4** — random testing (1000 cazuri, seed=42), coverage 100%, mutation score 100%
- **L5** — pipeline CI/CD cu GitHub Actions care automatizează toate verificările

---

## Structura repository-ului

```
repo/
├── README.md
├── requirements.txt
├── pytest.ini
├── cosmic-ray.toml
├── src/
│   ├── linear_search.py        ← funcția testată (L4)
│   ├── search.py               ← funcția testată cu validare (L3)
│   └── oracle.py               ← oracol independent
├── tests/
│   ├── conftest.py
│   ├── test_black_box_white_box.py   ← teste L3 (black-box + white-box + mutanți)
│   └── test_random.py               ← teste L4 (1000 cazuri aleatoare)
└── .github/
    └── workflows/
        └── ci.yml              ← pipeline GitHub Actions
```

---

## Rulare locală a testelor

### Instalare dependențe

```bash
pip install -r requirements.txt
```

### Rulare teste

```bash
pytest tests/ -v
```

### Coverage cu branch coverage

```bash
coverage run --branch -m pytest tests/
coverage report -m
coverage html   # generează htmlcov/index.html
```

Pipeline-ul eșuează dacă branch coverage scade sub **80%**.

### Mutation testing

```bash
cosmic-ray init cosmic-ray.toml session.sqlite
cosmic-ray exec cosmic-ray.toml session.sqlite
cr-report session.sqlite
```

---

## Semnificația badge-ului

| Badge | Semnificație |
|-------|-------------|
| ![passing](https://img.shields.io/badge/CI-passing-brightgreen) | Toate testele trec, coverage ≥ 80% |
| ![failing](https://img.shields.io/badge/CI-failing-red) | Cel puțin un test a picat SAU coverage < 80% |

Badge-ul reflectă starea ultimului push pe orice branch. Se actualizează automat după fiecare rulare.

---

## Configurare notificări la eșec

Pentru a primi email când pipeline-ul eșuează:

1. Mergi în contul GitHub → **Settings → Notifications**
2. La secțiunea **Actions** → bifează **"Send notifications for failed workflows only"**
3. Asigură-te că ai adresa de email confirmată

Orice push care face pipeline-ul să eșueze va trimite automat un email de notificare.
