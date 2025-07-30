---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - math
  - data_security
  - code_snippet
---
Cryptography is the foundation of digital [[Data Security]], enabling privacy and secure communication over the internet.

Examples are implemented in [[Node.JS]] (using `crypto` module) and are written in [[JavaScript]].

Resources:
- [7 Cryptography Concepts EVERY Developer Should Know](https://www.youtube.com/watch?v=NuyzuNBFWxQ)
- https://fireship.io/lessons/node-crypto-examples/
## [[Hash]] (Chop and mix)

A hashing function takes an input of any length and outputs a fixed-length value, ensuring:

- The same input always produces the same output.
- It is computationally expensive to reverse the hash.
- It has a low [[probability]] of collisions.

### Create a Hash in Node.js

```javascript
const { createHash } = require('crypto');

function hash(str) {
    return createHash('sha256').update(str).digest('hex');
}

let password = 'hi-mom!';
const hash1 = hash(password);
console.log(hash1);

password = 'hi-mom';
const hash2 = hash(password);
console.log(hash1 === hash2 ? '✔️ Good password' : '❌ Password does not match');
```

## Salting

Salting strengthens hashes by appending a random string before hashing, preventing attacks using precomputed hash tables.

### Password Salt with Scrypt in Node.js

```javascript
const { scryptSync, randomBytes, timingSafeEqual } = require('crypto');

function signup(email, password) {
    const salt = randomBytes(16).toString('hex');
    const hashedPassword = scryptSync(password, salt, 64).toString('hex');
    users.push({ email, password: `${salt}:${hashedPassword}` });
}

function login(email, password) {
    const user = users.find(v => v.email === email);
    if (!user) return 'login fail!';
    
    const [salt, key] = user.password.split(':');
    const hashedBuffer = scryptSync(password, salt, 64);
    const match = timingSafeEqual(hashedBuffer, Buffer.from(key, 'hex'));
    return match ? 'login success!' : 'login fail!';
}

const users = [];
signup('foo@bar.com', 'pa$$word');
console.log(login('foo@bar.com', 'password'));
```

## HMAC (Hash-based Message Authentication Code)

HMAC combines a hash with a secret key, ensuring authenticity and integrity.

### HMAC in [[Node.js]]

```javascript
const { createHmac } = require('crypto');

const password = 'super-secret!';
const message = '🎃 hello jack';

const hmac = createHmac('sha256', password).update(message).digest('hex');
console.log(hmac);
```

## Symmetric Encryption

Symmetric encryption uses the same key to encrypt and decrypt data.

### Symmetric Encryption in Node.js

```javascript
const { createCipheriv, randomBytes, createDecipheriv } = require('crypto');

const message = 'i like turtles';
const key = randomBytes(32);
const iv = randomBytes(16);
const cipher = createCipheriv('aes256', key, iv);
const encryptedMessage = cipher.update(message, 'utf8', 'hex') + cipher.final('hex');

const decipher = createDecipheriv('aes256', key, iv);
const decryptedMessage = decipher.update(encryptedMessage, 'hex', 'utf-8') + decipher.final('utf8');
console.log(`Decrypted: ${decryptedMessage}`);
```

## Keypairs

Keypairs consist of a public key (shared) and a private key (kept secret) for secure communication.

### Generate an RSA Keypair in Node.js

```javascript
const { generateKeyPairSync } = require('crypto');

const { privateKey, publicKey } = generateKeyPairSync('rsa', {
  modulusLength: 2048,
  publicKeyEncoding: { type: 'spki', format: 'pem' },
  privateKeyEncoding: { type: 'pkcs8', format: 'pem' },
});

console.log(publicKey);
console.log(privateKey);
```

## Asymmetric Encryption

Asymmetric encryption encrypts with a public key and decrypts with a private key, securing communication over networks.

### RSA Encryption in Node.js

```javascript
const { publicEncrypt, privateDecrypt } = require('crypto');
const { publicKey, privateKey } = require('./keypair');

const secretMessage = 'Confidential message';
const encryptedData = publicEncrypt(publicKey, Buffer.from(secretMessage));
console.log(encryptedData.toString('hex'));

const decryptedData = privateDecrypt(privateKey, encryptedData);
console.log(decryptedData.toString('utf-8'));
```

## Signing

Signing verifies the authenticity of a message by hashing it and encrypting the hash with a private key.

### RSA Signing in Node.js

```javascript
const { createSign, createVerify } = require('crypto');
const { publicKey, privateKey } = require('./keypair');

const data = 'this data must be signed';
const signer = createSign('rsa-sha256');
signer.update(data);
const signature = signer.sign(privateKey, 'hex');
console.log(signature);

const verifier = createVerify('rsa-sha256');
verifier.update(data);
const isVerified = verifier.verify(publicKey, signature, 'hex');
console.log(isVerified);
```