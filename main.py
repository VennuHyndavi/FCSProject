import aes1
import bf
import steganography
import base64
import binascii, os
import time
import datetime

text = input("enter the message")
b_key = "some random key"
t1 = datetime.datetime.now()
b_ct = bf.encryption(b_key, text)
time_diff = datetime.datetime.now()-t1
print("\nBlow fish cipher text ",b_ct)
time_diff = datetime.datetime.now()-t1
execution_time = time_diff.total_seconds() * 1000
print("time taken...", execution_time)

aes_key = os.urandom(32)  # 256-bit random encryption key
aes_ct = aes1.encrypt_AES_GCM(b_ct, aes_key)
print("\nAES cipher text ", aes_ct)

steg_msg1 = aes_ct[0].decode("latin-1")
steg_msg2 = aes_ct[1].decode("latin-1")
steg_msg3 = aes_ct[2].decode("latin-1")
steg_input = steg_msg1+"000000"+steg_msg2+"000000"+steg_msg3
steganography.encode_text(steg_input)

#decryption
de_image = input("enter image name to decrypt:")
steg_out = steganography.decode_text(de_image)
steg_array = steg_out.split("000000")
aes_dt_ip = (steg_array[0].encode("latin-1"),steg_array[1].encode("latin-1"),steg_array[2].encode("latin-1"))

aes_dt = aes1.decrypt_AES_GCM(aes_dt_ip, aes_key)

b_dt = bf.decrypt(b_key,aes_dt)
print("\nDecrypted message: ",b_dt)