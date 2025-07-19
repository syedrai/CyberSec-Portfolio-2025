# Crypto Hash Challenge — Writeup

## Overview

This challenge tested two main skills:
1. Solving a custom Proof-of-Work to get the first flag.
2. Exploiting a MAC verification for a hidden `exec` task to get the second flag.

---

## How I got Flag 1

- Connected to the provided server using `nc`.
- Requested a Proof-of-Work challenge using `get_pow`.
- Brute-forced the challenge with a custom `brute_pow.py` script.
- Found a valid hash with the required leading zero bits.
- Submitted it using `check_pow` — server confirmed and gave me:
FLG_1QEAAAIAAADVTBt7pXGyqKcYht+ktpctuEL0KHDrg6k=
## Why I couldn’t get Flag 2

I attempted a hash length extension attack using `hashpump`:
- I generated valid `task` tags for `stat` and tried to extend them to `exec`.
- Tried different key lengths and padding.
- Rebuilt payloads manually and with `hashpump`.

But the server MAC used `SHA-256(secret || message)` which is resistant to length extension because the secret is **prepended** not appended. This means Merkle–Damgård tricks don’t work here — so no realistic exploit.

---

## Key Takeaway

- The PoW was simple and solvable with brute force.
- The MAC design was secure — so Flag 2 was impossible to extract with any practical method.

I learned about Merkle–Damgård weaknesses, hashpump, PoW brute force, and secure MAC design.
