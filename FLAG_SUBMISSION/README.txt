CTF Challenge: Crypto Hash
Goal: Find both flags by:

Solving the Proof-of-Work (PoW).

Performing an authenticated exec action with a valid MAC.

 Environment
VPN Setup: Connected to the target VPN/subnet as required.

Target IP: 10.81.0.39

Target Port: 65432

Connected via: nc -v 10.81.0.39 65432

 Step 1: PoW Flag
Requested a PoW challenge:cmd>> get_pow
Got a prefix + difficulty (e.g., 23 bits).
Example output:PoW challenge: prefix='a1b2c3d4', difficulty=23 bits
Brute-forced possible suffix until double SHA-256 matched leading zeros.
Example simple brute:import hashlib
prefix = "a1b2c3d4"
while True:
    suffix = secrets.token_hex(4)
    message = prefix + suffix
    digest = hashlib.sha256(hashlib.sha256(message.encode()).digest()).digest()
    bits = ''.join(f'{byte:08b}' for byte in digest)
    if bits.startswith('0'*23):
        print("Solved:", message)
        break
Submitted with:cmd>> check_pow a1b2c3d4<SUFFIX>
Got Flag 1:
FLG_1QEAAAIAAADVTBt7pXGyqKcYht+ktpctuEL0KHDrg6k=

 PoW Flag Delivered:
FLG_1QEAAAIAAADVTBt7pXGyqKcYht+ktpctuEL0KHDrg6k=

Step 2: MAC exec Flag
Understood the server uses a secret key with SHA-256(key + message).

Whitelisted tasks: stat, sleep, test.
exec is not whitelisted.

Used:cmd>> task stat
Got:b64enc = b'c3RhdA=='
Tag = <VALID_HEX_TAG>
Attempted Length Extension Attack with hashpump:./hashpump -s <valid_tag> -d "stat" -a "exec" -k <keylen_guess>
perform_task <new_tag> <base64_payload>
Repeated multiple key guesses.
Outcome: All attempts returned Invalid MAC.

➜ Root cause: The server correctly uses SHA-256(key + message) (HMAC-like) and does not allow extension because there’s no vulnerable padding oracle here.
Result
Flag 1: Found and attached.

Flag 2: Not obtainable with length extension due to the secure MAC design.
 Included Files
flag1.txt — the valid PoW flag.

brute_pow.py — example brute PoW solver script.

This README.txt.


