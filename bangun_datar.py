""" 
Belajar matematika sederhana
Rumus Bangun Datar 
"""

__author__ = "Fendi Dwi Fauzi (efenfauzi)"
__website__ = "$efenfauzi.com $"
__date__ = "$Date: 2015/04/20 $"
__copyright__ = "Opensource"
__license__ = "Python"


"""1# Persegi
Keliling : 4 x sisi
Luas : sisi x sisi (s2)"""
def luas_persegi():
	luas = sisi*sisi
	return luas
def keliling_persegi():
	keliling = sisi*4
	return keliling


"""2# Persegi Panjang
Keliling : 2 x (p+l)
Luas : panjang x lebar"""
def luas_persegipanjang():
	luas = panjang*lebar
	return luas
def keliling_persegipanjang():
	keliling = 2*(panjang+lebar)
	return keliling

"""3# Segitiga
Keliling : AB+BC+AC
Luas : 0.5 x alas x tinggi"""
def luas_segitiga():
	luas = 0.5*alas*tinggi
	return luas
def keliling_segitiga():
	sisimiring = ((alas**2)+(tinggi**2))**0.5
	keliling = alas+tinggi+sisimiring
	return keliling 

"""4# Jajar Genjang
Keliling: AB+BC+CD+AD
Luas: alas x tinggi
misalnkan panjang = alas
alas = AB = At + tB """
def luas_jajargenjang():
	luas = alas*tinggi
	return luas
def keliling_jajargenjang():
	sisimiring = (((alas-alastB)**2)+(tinggi**2))**0.5
	keliling = (2*alas)+(2*sisimiring)
	return keliling


"""5# Trapesium  sembarang
Keliling : AB+BC+CD+DA
Luas: 0.5 x jumlah sisi sejajar x tinggi"""
def luas_trapesium():
	luas = alas*tinggi
	return luas
def keliling_trapesium():
	keliling = (2*alas)+(2*sisimiring)
	return keliling

"""6# Layang-layang
Keliling: 2(AB+BC)
Luas: 0.5 x d1 x d2"""
def luas_layanglayang():
	luas = 0.5*diagonal1*diagonal2
	return luas
def keliling_layanglayang():
	keliling = (2*alas)+(2*sisimiring)
	return keliling


"""7# Belah ketupat
Keliling : 4 x s
Luas: 0.5 x d1 x d2"""
def luas_belahketupat():
	luas = 0.5*diagonal1*diagonal2
	return luas
def keliling_belahketupat():
	keliling = 4*sisi
	return keliling

"""8# Lingkaran
Keliling : phi x D
Luas: phi x r x r"""
def luas_lingkaran():
	luas = 22/7*r**2
	return luas
def keliling_lingkaran():
	keliling = 22/7*(r+r)
	return keliling


#Program Utama
def menu(str):
	print "============================="
	print "|Menghitung Luas dan Keliling|"
	print "|        BANGUN DATAR        |"
	print "|     1. Persegi             |"
	print "|     2. Persegi panjang     |"
	print "|     3. Segitiga            |"
	print "|     4. Jajar Genjang       |"
	print "|     5. Trapesium           |"
	print "|     6. Layang-layang       |"
	print "|     7. Belah Ketupat       |"
	print "|     8. Lingkaran           |"
	print "============================="
	print "by efenfauzi (efenfauzi.com)"
	print str
	print "\n"*3



ulangi = 0
while (ulangi<=1):
	menu("------------------")
	pilihan = int(input("Pilihan : "))
	if pilihan == 1:
		print ("Luas dan Keliling Persegi")
		sisi = int(input("Masukan sisi persegi: "))
		print "Luas", luas_persegi()
		print "Keliling", keliling_persegi()
		print "\n"*5
		menu("Mau Coba Lagi [Y/N]?")
		ulangi = raw_input().upper()
		if ulangi == "Y":
			menu("")
		else:
			exit()

	elif pilihan == 2:
		print ("Luas dan Keliling Persegi Panjang")
		panjang = int(input("Masukan Panjang: "))
		lebar = int(input("Masukan Lebar: "))
		print "Luas", luas_persegipanjang()
		print "Keliling", keliling_persegipanjang()
		print "\n"*5
		print "Mau Coba Lagi [Y/N]?"
		ulangi = raw_input().upper()
		if ulangi == "Y":
			menu()
		else:
			exit()

	elif pilihan == 3:
		print ("Luas dan Keliling Segitga")
		alas = int(input("Masukan Alas: "))
		tinggi = int(input("Masukan Tinggi: "))
		print "Luas", luas_segitiga()
		print "Keliling", keliling_segitiga()
		print "\n"*5
		print "Mau Coba Lagi [Y/N]?"
		ulangi = raw_input().upper()
		if ulangi == "Y":
			menu()
		else:
			exit()

	elif pilihan == 4:
		print ("Luas dan Keliling Jajar Genjang")
		alas = int(input("Masukan Alas (AB): "))
		tinggi = int(input("Masukan tinggi: "))
		alastB = int(input("Masukan Alas tB: "))
		print "Luas", luas_jajargenjang()
		print "Keliling", keliling_jajargenjang()
		print "\n"*5
		print "Mau Coba Lagi [Y/N]?"
		ulangi = raw_input().upper()
		if ulangi == "Y":
			ulangi ==1
			menu()
		else:
			exit()


	else:
		print ("Pilihan salah, Mau Coba Lagi [Y/N]?")
		ulangi = raw_input().lower()
		if ulangi == "Y":
			ulangi ==1
			menu()
		else:
			exit()
	break


