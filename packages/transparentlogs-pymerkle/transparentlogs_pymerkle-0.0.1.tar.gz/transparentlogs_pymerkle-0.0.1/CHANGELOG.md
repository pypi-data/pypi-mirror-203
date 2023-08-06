# CHANGELOG

All notable changes to this project will be documented in this file.

## 4.0.0 2023-03-06

### Added

- `verify_inclusion`
- `InvalidChallengeError` when requesting a proof for invalid parameters
- `append_entry` method
- `find_leaf` method

### Changed

- Access root hash as `.root`
- Return hash on append
- Simplify proof serialization
- Remove `created_at` field from proof
- Remove `NoPathException`
- Remove proof json utilities
- Rename `Proof` to `MerkleProof`
- Rename proof header to metadata
- Remove node serialization
- Rename `generate_consistency_proof` to `prove_consistency`
- Rename `generate_audit_proof` to `prove_inclusion`
- Remove tree serialization, representation and stringification
- Remove tree comparison operators
- Remove uuid from proof and tree objects
- Remove file encryption
- Remove md5 from supported hash algorithms
- Remove `root_hash` property

## 3.0.0 2022-05-21

This is the first documented release version, following 2.0.2. The result of
a major refactoring, it introduces significant breaking changes to the API. Here
we list only a few of the most striking ones.

### Added

- `get_root_hash` public method

### Changed

- Raise `InvalidProof` in case of verification failure
- Attach verification to the proof object
- Remove validator object
- Remove no raw-bytes mode
- Always include commitments to proofs
- Rename `update` to `append_leaf`
- Uniformly apply snake case to public method names
- Remove `InvalidChallengeError`
- Remove proof verification receipt
- Rename `validateProof` to `verify_proof`
