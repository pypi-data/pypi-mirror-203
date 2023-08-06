"""
Merkle-proof machinery
"""

import os
import json
from time import time

from pymerkle_logsTransparentes.hashing import HashEngine


class InvalidProof(Exception):
    """
    Raised when a merkle-proof is found to be invalid
    """
    pass


def verify_inclusion(data, target, proof):
    """
    Verifies the provided merkle-proof of inclusion for the given data against
    the provided root hash.

    :param data: entry to verify
    :type data: str or bytes
    :param target: root hash during proof generation
    :type target: str or bytes
    :param proof: proof of inclusion
    :type proof: MerkleProof
    :raises InvalidProof: if the proof is invalid
    """
    engine = HashEngine(**proof.get_metadata())

    if isinstance(target, str):
        target = target.encode(proof.encoding)

    offset = proof.offset

    if proof.path[offset][1] != engine.hash_entry(data):
        raise InvalidProof("Path not based on provided entry")

    if target != engine.hash_path(offset, proof.path):
        raise InvalidProof("Path failed to resolve")


def verify_consistency(subroot, target, proof):
    """
    Verifies the provided merkle-proof of consistency for the given state
    against the provided root hash.

    :param subroot:
    :type subroot: str or bytes
    :param target: root during proof generation
    :type target: str or bytes
    :raises InvalidProof: if the proof is invalid
    :param proof: proof of consistency
    :type proof: MerkleProof
    """
    engine = HashEngine(**proof.get_metadata())

    if isinstance(subroot, str):
        subroot = subroot.encode(proof.encoding)

    if isinstance(target, str):
        target = target.encode(proof.encoding)

    offset = proof.offset

    principals = [(-1, value) for (_, value) in proof.path[:offset + 1]]
    if subroot != engine.hash_path(offset, principals):
        raise InvalidProof("Path not based on provided state")

    if target != engine.hash_path(offset, proof.path):
        raise InvalidProof("Path failed to resolve")


class MerkleProof:
    """
    :param algorithm: hash algorithm
    :type algorithm: str
    :param encoding: encoding scheme
    :type encoding: str
    :param security: defense against 2-nd preimage attack
    :type security: bool
    :param offset: starting position for hashing during verification
    :type offset: int
    :param path: path of hashes
    :type path: list[(+1/-1, bytes)]
    """

    def __init__(self, algorithm, encoding, security, offset, path,
                 timestamp=None):
        self.algorithm = algorithm
        self.encoding = encoding
        self.security = security
        self.timestamp = timestamp or int(time())
        self.offset = offset
        self.path = path


    def get_metadata(self):
        """
        .. note:: These are parameters required for configuring the hashing
            machinery during proof verification

        :rtype: dict
        """
        return {'algorithm': self.algorithm, 'encoding': self.encoding,
                'security': self.security}


    def serialize(self):
        """
        :rtype: dict
        """
        timestamp = self.timestamp
        algorithm = self.algorithm
        encoding = self.encoding
        security = self.security
        offset = self.offset
        path = [[sign, value.decode(self.encoding)] for (sign, value) in
                self.path]

        return {
            'metadata': {
                'timestamp': timestamp,
                'algorithm': algorithm,
                'encoding': encoding,
                'security': security,
            },
            'offset': offset,
            'path': path,
        }


    @classmethod
    def deserialize(cls, proof):
        """
        :rtype: MerkleProof
        """
        metadata = proof['metadata']
        encoding = metadata['encoding']
        path = [(sign, value.encode(encoding)) for [sign, value] in
                proof['path']]
        offset = proof['offset']

        return cls(**metadata, path=path, offset=offset)
