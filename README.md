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

## Technologies

- Python 3
- PyCryptodome
- pytest

## Project Structure

- `set01/` - `set08/`: Challenge solutions organized by set.
- `src/cryptopals/`: Reusable cryptographic utilities.
- `tests/`: Unit tests.
- `data/`: Challenge input files.

## Running Solutions

Clone the repository:

```bash
git clone https://github.com/rustyapollo/cryptopals-python.git
cd cryptopals-python
```

Install the project:

```bash
python -m pip install -e ".[dev]"
```

Run an individual challenge:

```bash
python set01/challenge01.py
```

Run tests:

```bash
pytest
```

## Disclaimer

This repository is intended for educational purposes. The cryptographic implementations and attacks are designed to explore security concepts and should not be used as production security solutions.

## Reference

[The Cryptopals Crypto Challenges](https://cryptopals.com/)
