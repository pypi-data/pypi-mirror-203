# pymerkle

**Merkle-tree cryptography**

[![Build Status](https://travis-ci.com/fmerg/pymerkle.svg?branch=master)](https://travis-ci.com/github/fmerg/pymerkle)
[![codecov](https://codecov.io/gh/fmerg/pymerkle/branch/master/graph/badge.svg)](https://codecov.io/gh/fmerg/pymerkle)
[![Docs Status](https://readthedocs.org/projects/pymerkle/badge/?version=latest)](http://pymerkle.readthedocs.org)
[![PyPI version](https://badge.fury.io/py/pymerkle.svg)](https://pypi.org/project/pymerkle/)
![Python >= 3.6](https://img.shields.io/badge/python-%3E%3D%203.6-blue.svg)

Documentation found at **[pymerkle.readthedocs.org](http://pymerkle.readthedocs.org/)**.

This library provides a Merkle-tree implementation in Python. It supports
multiple combinations of hash functions and encding schemas with defense against
second-preimage attack enabled.

## Install

```bash
pip3 install pymerkle
```

## Usage

```python
from pymerkle import MerkleTree, verify_inclusion, verify_consistency

tree = MerkleTree()

# Populate tree with some entries
for data in [b'foo', b'bar', b'baz', b'qux', b'quux']:
    tree.append_entry(data)

# Prove and verify inclusion of `bar`
proof = tree.prove_inclusion(b'bar')
verify_inclusion(b'bar', tree.root, proof)

# Save current state
sublength = tree.length
subroot = tree.root

# Append further entries
for data in [b'corge', b'grault', b'garlpy']:
    tree.append_entry(data)

# Prove and verify previous state
proof = tree.prove_consistency(sublength, subroot)
verify_consistency(subroot, tree.root, proof)
```

## Security

This is currently a prototype requiring security review. However, some steps have
been made to this direction:

### Defense against second-preimage attack

This consists in the following standard technique:

- Upon computing the hash of a leaf, prepend its data with `0x00`.
- Upon computing the hash of an interior node, prepend the hashes of its
  children with `0x01`.

Refer [here](./tests/test_defense.py) to see how to perform second preimage
attack against the present implementation.


### Defense against CVE-2012-2459 DOS

Contrary to the [bitcoin](https://en.bitcoin.it/wiki/Protocol_documentation#Merkle_Trees)
specification for Merkle-trees, lonely leaves are not duplicated while the tree is growing.
Instead, when appending new leaves, a bifurcation node is created at the rightmost branch.
As a consequence, the present implementation should be invulnerable to the DOS attack reported as
[CVE-2012-2459](https://nvd.nist.gov/vuln/detail/CVE-2012-2459) (see also
[here](https://github.com/bitcoin/bitcoin/blob/bccb4d29a8080bf1ecda1fc235415a11d903a680/src/consensus/merkle.cpp)
for explanation).

## Tree structure

The topology turns out to be that of a binary [Sakura tree](https://keccak.team/files/Sakura.pdf).

## Development

```commandline
pip3 install -r requirements-dev.txt
```

### Tests

```commandline
./test.sh [pytest options]
```

to run tests against the limited set of encoding schemas UTF-8, UTF-16 and
UTF-32. To run tests against all possible combinations of hash algorithms and
encoding schemas, run

```commandline
./test.sh --extended
```

## Documentation

**[pymerkle.readthedocs.org](http://pymerkle.readthedocs.org/)**.

### Build locally

Documentation is built with
[`sphinx`](https://www.sphinx-doc.org/en/master/index.html):

```commandline
pip3 install -r requirements-doc.txt
```

Once installed, build docs with

```commandline
./build-docs.sh [--help]
```

and browse at

```
docs/target/build/html/index.html
```

to view them.
