# Cryptopals — Python Solutions

My implementations of the [Cryptopals Crypto Challenges](https://cryptopals.com/), written in Python.

The goal of this repository is to develop a deeper understanding of cryptography, cryptanalysis, and common security vulnerabilities by implementing attacks and cryptographic techniques from scratch.

## Objectives

- Understand fundamental cryptographic primitives.
- Implement encryption, encoding, and hashing algorithms.
- Explore common cryptographic vulnerabilities.
- Learn practical cryptanalysis techniques.
- Write clean, reusable, and tested Python code.

## Challenge Progress

| Set | Topic | Progress |
|---|---|---|
| Set 1 | Basics | ⬜ 0/8 |
| Set 2 | Block Crypto | ⬜ 0/8 |
| Set 3 | Block & Stream Crypto | ⬜ 0/8 |
| Set 4 | Stream Crypto and Randomness | ⬜ 0/8 |
| Set 5 | Diffie-Hellman and Friends | ⬜ 0/8 |
| Set 6 | RSA and DSA | ⬜ 0/8 |
| Set 7 | Hashes | ⬜ 0/8 |
| Set 8 | Abstract Algebra | ⬜ 0/8 |

## Requirements

### Python

- Python 3.11 or later
- Developed and tested using Python 3.12.3

### Dependencies

| Package | Version | Purpose |
|---|---|---|
| PyCryptodome | >= 3.20 | Cryptographic primitives |
| pytest | 9.2.0 | Automated testing |
| Ruff | 0.17.6 | Linting and code quality |
| setuptools | >= 68 | Package building |

### Development Environment

The project uses a Python virtual environment to isolate dependencies.

Create and activate the virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project and development dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Technologies

- Python 3
- PyCryptodome
- pytest
- Ruff

## Project Structure

```text
cryptopals-python/
├── data/
│   ├── set01/
│   ├── set02/
│   ├── set03/
│   ├── set04/
│   ├── set05/
│   ├── set06/
│   ├── set07/
│   └── set08/
│
├── src/
│   ├── cryptopals/
│   │   ├── __init__.py
│   │   ├── encoding.py
│   │   ├── xor.py
│   │   ├── aes.py
│   │   ├── padding.py
│   │   ├── hashing.py
│   │   └── utils.py
│   │
│   ├── set01/
│   │   ├── __init__.py
│   │   ├── challenge01.py
│   │   ├── challenge02.py
│   │   ├── challenge03.py
│   │   ├── challenge04.py
│   │   ├── challenge05.py
│   │   ├── challenge06.py
│   │   ├── challenge07.py
│   │   └── challenge08.py
│   │
│   ├── set02/
│   ├── set03/
│   ├── set04/
│   ├── set05/
│   ├── set06/
│   ├── set07/
│   └── set08/
│
├── tests/
│   ├── test_encoding.py
│   ├── test_xor.py
│   ├── test_aes.py
│   └── test_padding.py
│
├── README.md
├── pyproject.toml
├── .gitignore
└── LICENSE
```

- `src/cryptopals/`: Reusable cryptographic utilities shared across challenges.
- `src/set01/` - `src/set08/`: Individual challenge solutions organized by set.
- `tests/`: Unit tests for reusable functions and implementations.
- `data/`: Input files used by the challenges, organized by set.

## Running Solutions

Clone the repository:

```bash
git clone https://github.com/rustyapollo/cryptopals-python.git
cd cryptopals-python
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Run an individual challenge:

```bash
python -m set01.challenge01
```

Run tests:

```bash
pytest
```

Run the linter:

```bash
ruff check .
```

## Disclaimer

This repository is intended for educational purposes. The cryptographic implementations and attacks are designed to explore security concepts and should not be used as production security solutions.

## Reference

[The Cryptopals Crypto Challenges](https://cryptopals.com/)
