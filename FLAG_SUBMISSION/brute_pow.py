import hashlib

prefix = "PUT_YOUR_PREFIX_HERE"

for i in range(100000000):
    attempt = prefix + str(i)
    digest = hashlib.sha256(hashlib.sha256(attempt.encode()).digest()).digest()
    bits = ''.join(f'{byte:08b}' for byte in digest)
    if bits.startswith('0'*23):
        print(f"Found: {attempt}")
        break
