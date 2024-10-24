# Remove the private key so that it can pass the Pre-commit hook

private_key = """-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----"""

if __name__ == '__main__':
    print('Hello, World!')
