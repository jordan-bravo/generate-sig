import hashlib

print("")

api_key = raw_input("Enter API key: ")
api_secret = raw_input("Enter API secret: ")
nonce = 1234567890

sig = hashlib.sha256(api_key + api_secret + str(nonce)).hexdigest()

print("")
print("sig: %s" % sig)
