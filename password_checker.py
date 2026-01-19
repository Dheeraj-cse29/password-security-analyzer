import hashlib
import math
import re
import requests

HIBP_API_URL = "https://api.pwnedpasswords.com/range/"

def calculate_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"[0-9]", password): charset += 10
    if re.search(r"[^a-zA-Z0-9]", password): charset += 32
    if charset == 0:
        return 0
    return round(len(password) * math.log2(charset), 2)

def check_breach(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]

    response = requests.get(HIBP_API_URL + prefix)
    if response.status_code != 200:
        return None

    hashes = response.text.splitlines()
    for h in hashes:
        hash_suffix, count = h.split(":")
        if hash_suffix == suffix:
            return int(count)
    return 0

def strength_label(entropy):
    if entropy < 40:
        return "WEAK ❌"
    elif entropy < 60:
        return "MODERATE ⚠️"
    else:
        return "STRONG ✅"

def main():
    print("\n🔐 Password Security Analyzer\n")
    password = input("Enter password to analyze: ")

    entropy = calculate_entropy(password)
    breach_count = check_breach(password)

    print("\n--- Analysis Report ---")
    print(f"Password Length : {len(password)}")
    print(f"Entropy         : {entropy} bits")
    print(f"Strength        : {strength_label(entropy)}")

    if breach_count is None:
        print("Breach Status   : Unable to check breaches")
    elif breach_count > 0:
        print(f"Breach Status   : FOUND in {breach_count} breaches ⚠️")
    else:
        print("Breach Status   : NOT FOUND ✅")

    print("\nSecurity Recommendations:")
    if len(password) < 12:
        print("✔ Increase password length (12+ characters)")
    if not re.search(r"[^a-zA-Z0-9]", password):
        print("✔ Add special characters")
    if breach_count and breach_count > 0:
        print("✔ Do not reuse breached passwords")

if __name__ == "__main__":
    main()
