
def mod_inverse(a: int, m: int) -> int | None:
    """Return the modular inverse of a modulo m, or None if it doesn't exist."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  # No inverse if a and m are not coprime

def affine_encrypt(text: str, a: int, b: int) -> str:
    """Encrypt plaintext using the Affine Cipher."""
    if mod_inverse(a, 26) is None:
        raise ValueError("Key 'a' must be coprime with 26.")
    result = []
    for ch in text.upper():
        if ch.isalpha():
            x = ord(ch) - 65          # A → 0, B → 1, ...
            enc = (a * x + b) % 26
            result.append(chr(enc + 65))
        else:
            result.append(ch)         # keep spaces, punctuation
    return "".join(result)

def affine_decrypt(cipher: str, a: int, b: int) -> str:
    """Decrypt ciphertext using the Affine Cipher."""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("Key 'a' must be coprime with 26.")
    result = []
    for ch in cipher.upper():
        if ch.isalpha():
            y = ord(ch) - 65
            dec = (a_inv * (y - b)) % 26
            result.append(chr(dec + 65))
        else:
            result.append(ch)
    return "".join(result)

# ---- simple demo ----
if __name__ == "__main__":
    plaintext = "HELP"
    a, b = 5, 8          # sample keys (5 is coprime with 26)

    cipher = affine_encrypt(plaintext, a, b)
    print("Encrypted:", cipher)       # → RCLF

    decoded = affine_decrypt(cipher, a, b)
    print("Decrypted:", decoded)      # → HELP

