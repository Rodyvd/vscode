import jwt

def decode_jwt_insecure(token):
    # Insecure: Disabling signature verification
    decoded = jwt.decode(token, verify=False)  # Noncompliant
    print("Decoded token (insecure):", decoded)

def decode_jwt_insecure_with_options(token, key):
    # Insecure: Disabling signature verification using options
    decoded = jwt.decode(token, key, options={"verify_signature": False})  # Noncompliant
    print("Decoded token with options (insecure):", decoded)

def main():
    token = "your.jwt.token.here"
    key = "your-secret-key"

    decode_jwt_insecure(token)
    decode_jwt_insecure_with_options(token, key)

if __name__ == "__main__":
    main()
