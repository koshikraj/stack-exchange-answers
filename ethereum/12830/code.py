import binascii

from web3.auto import w3
with open("/home/koshik/.ethereum/rinkeby/keystore/UTC--2018-06-10T05-43-22.134895238Z--9e63c0d223d9232a4f3076947ad7cff353cc1a28") as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(encrypted_key, 'koshik93')
print(binascii.b2a_hex(private_key))