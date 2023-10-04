#!pip install pycrypto

from Crypto.Cipher import Blowfish
from Crypto import Random
from struct import pack

def encryption(input_key, input_text):
  bs = Blowfish.block_size
  key = bytes(input_key,'utf-8')
  iv = Random.new().read(bs)
  cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
  plaintext = bytes(input_text,'utf-8')
  plen = bs - divmod(len(plaintext),bs)[1]
  padding = [plen]*plen
  padding = pack('b'*plen, *padding)
  msg = iv + cipher.encrypt(plaintext + padding)
  return msg;

def decrypt(input_key,ciphertext):
  bs = Blowfish.block_size
  key=bytes(input_key,'utf-8')
  iv = ciphertext[:bs]
  ciphertext = ciphertext[bs:]
  cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
  msg = cipher.decrypt(ciphertext)
  last_byte = msg[-1]
  msg = msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]
  return msg
