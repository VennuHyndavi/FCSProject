from flask import Flask, render_template, redirect, request, session
from keras.models import load_model
from PIL import Image
from keras.preprocessing import image
import numpy as np
import cv2
import os
import aes1
import bf
import steganography
import binascii, os



import MySQLdb 
db = MySQLdb.connect("localhost", "root", "Apurva*123*", "fcsproject")
print("Connected")


UPLOAD_FOLDER = 'static/'

#__name__ = __main__S
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'randomstring'

uid=""
aes_key = os.urandom(32)
b_key = "some random key"

@app.route('/home')
def home():
    #return redirect('/')
	cursor = db.cursor()
	try:
		cursor.execute("SELECT * FROM users")
		results = cursor.fetchall()
		print(results)
		return render_template("home.html",results=results)
	except:
		print ("here")
		return render_template("home.html")

@app.route('/')
def default():
    return redirect('/login')

@app.route('/login' , methods= ['POST','GET'])
def login():
	if request.method == 'POST':
		data = request.form
		uname = data.get("uname")
		pswd = data.get("login_password")
		cursor = db.cursor()
		cursor.execute("SELECT * FROM users")
		results = cursor.fetchall()
		for res in results:
			if uname==res[1] and pswd==res[2]:
				print("success")
				session["uname"]=uname
				session["uid"]=res[0]
				return redirect("/home")
		return redirect('/login')
	return render_template("login.html")

@app.route('/signup' , methods= ['POST','GET'])
def signup():
	if request.method == 'POST':
		print("in post")
		data = request.form
		uname = data.get("uname")
		pswd = data.get("login_password")
		print(uname,pswd)
		pswd_confirm = data.get("login_password_confirm")
		cursor = db.cursor()
		try:
			stmt=' insert into users(uname,pswd) values(%s,%s)'
			cursor.execute(stmt,(uname,pswd))
			db.commit()
		except (MySQLdb.Error, MySQLdb.Warning) as e:
			print(e)
		return redirect('/login')
	print("in get")
	return render_template("signup.html")

@app.route('/logout')
def logout():
   session.pop('uname', None)
   return redirect('/login')

@app.route('/encrypt' , methods= ['POST','GET'])
def encrypt():
	if request.method == 'POST':
		data = request.form
		msg = data.get("msg")
		f=request.files['myimage']
		imgfile=os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
		print(f)
		#b_key = "some random key"
		b_ct = bf.encryption(b_key, msg)
		print("\nBlow fish cipher text ",b_ct)

		#aes_key = os.urandom(32)  # 256-bit random encryption key
		aes_ct = aes1.encrypt_AES_GCM(b_ct, aes_key)
		print("\nAES cipher text ", aes_ct)

		steg_msg1 = aes_ct[0].decode("latin-1")
		steg_msg2 = aes_ct[1].decode("latin-1")
		steg_msg3 = aes_ct[2].decode("latin-1")
		steg_input = steg_msg1+"000000"+steg_msg2+"000000"+steg_msg3
		steganography.encode_text(steg_input)

		rname = data.get("rname")
		
		return render_template("encrypt.html",name=f.filename,img=imgfile)
	return render_template("encrypt.html",name="",img="")

@app.route('/decrypt' , methods= ['POST','GET'])
def decrypt():
	if request.method == 'POST':
		f=request.files['myimage']
		imgfile=os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
		steg_out = steganography.decode_text(f.filename)
		steg_array = steg_out.split("000000")
		aes_dt_ip = (steg_array[0].encode("latin-1"),steg_array[1].encode("latin-1"),steg_array[2].encode("latin-1"))

		aes_dt = aes1.decrypt_AES_GCM(aes_dt_ip, aes_key)

		b_dt = bf.decrypt(b_key,aes_dt)
		print("\nDecrypted message: ",b_dt.decode("latin-1"))
		return render_template("decrypt.html",msg = b_dt.decode("latin-1"))
	return render_template("decrypt.html",msg="")

if __name__ == '__main__':
	app.run(debug = True)