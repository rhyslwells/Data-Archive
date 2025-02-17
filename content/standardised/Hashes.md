A hash is a fixed-size string of characters that is generated from input data of any size using a hash function. 

Hashes are used to ensure [[data integrity]] by providing a unique representation of the data, making it easy to detect any changes or alterations.

### Key Characteristics of Hashes:

1. **Deterministic**: The same input will always produce the same hash output.
2. **Fixed Size**: Regardless of the size of the input data, the output hash will always be of a fixed length (e.g., SHA-256 produces a 256-bit hash).
3. **Fast Computation**: Hash functions are designed to compute the hash value quickly.
4. **Pre-image Resistance**: It should be computationally infeasible to reverse-engineer the original input from its hash.
5. **Collision Resistance**: It should be difficult to find two different inputs that produce the same hash output.

### How Hashes are Used in Data Integrity:

6. **Data Verification**: When data is stored or transmitted, a hash of the data is generated and stored or sent along with it. When the data is later accessed, the hash is recalculated and compared to the original hash. If they match, the data is considered intact; if not, it indicates potential corruption or tampering.

7. **Digital Signatures**: Hashes are often used in digital signatures to ensure the authenticity and integrity of a message or document.

8. **Password Storage**: Instead of storing passwords in plain text, systems often store the hash of the password. When a user logs in, the system hashes the entered password and compares it to the stored hash.

### Example of Hashing:

For example, if we take the string "Hello, World!" and apply a hash function like SHA-256, it will produce a unique hash value:

- Input: "Hello, World!"
- Hash (SHA-256): `a591a6d40bf420404a011733cfb7b190d62c65bf0bcda190f4b6c3f0f3c3b8a`

If the input data changes even slightly (e.g., "Hello, World"), the hash will be completely different, making it easy to detect any alterations.

