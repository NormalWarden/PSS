from base64 import b64encode, b64decode
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES


def getInitVectorAndKey():
	key = get_random_bytes(16) 
	cipher = AES.new(key, AES.MODE_CBC)
	initVector = b64encode(cipher.iv).decode('utf-8')
	key = b64encode(key).decode("utf-8")
	return initVector, key

def encryptWithInputData(text: str, initVector: str, key: str):
	data = str.encode(text)
	cipher = AES.new(b64decode(key), AES.MODE_CBC, b64decode(initVector))
	ct_bytes = cipher.encrypt(pad(data, AES.block_size))
	cipherText = b64encode(ct_bytes).decode('utf-8')
	return cipherText

def decrypt(cipherText: str, initVector: str, key: str):
	try:
		cipherText = b64decode(cipherText)
		cipher = AES.new(b64decode(key), AES.MODE_CBC, b64decode(initVector))
		sourceText = unpad(cipher.decrypt(cipherText), AES.block_size)
		return bytes.decode(sourceText)
	except (ValueError, KeyError) as e:
		return f"Incorrect decryption {e}"