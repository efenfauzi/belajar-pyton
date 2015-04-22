""" 
Belajar matematika sederhana
Rumus Bangun Ruang 
"""

__author__ = "Fendi Dwi Fauzi (efenfauzi)"
__website__ = "$efenfauzi.com $"
__date__ = "$Date: 2015/04/20 $"
__copyright__ = "Opensource"
__license__ = "Python"

"""KUBUS
Luas salah satu sisi = rusuk x rusuk   
Luas Permukaan Kubus = 6 x rusuk x rusuk
Keliling Kubus = 12 x rusuk
Volume Kubus = rusuk x rusuk x rusuk ( rusuk 3 )
"""
def luas_kubus():
	luas = 6*rusuk*rusuk
	return
def keliling_kubus():
	keliling = 12*rusuk
	return
def volume_kubus():
	volume = rusuk*rusuk*rusuk
	return


"""BALOK"
Luas Permukaan Balok = 2 x {(pxl) + (pxt) + (lxt)}
Diagonal Ruang = Akar dari (p kuadrat + l kuadrat + t kuadrat)
Keliling Balok = 4 x (p + l + t)
Volume Balok = p x l x t (sama dengan kubus, tapi semua rusuk kubus sama panjang).
"""
def luas_balok():
	luas = 2*((p*l)+(p*t)+(l*t))
	return luas
def keliling_balok():
	keliling = 4*(p+l+t)
	return keliling
def volume_balok():
	volume = p*l*t
	return volume
def diagonal_balok():
	diagonal = (p**2+l**2+t**2)**0.5
	return diagonal

"""BOLA
Luas Bola = 4 x  x jari-jari x jari-jari, atau 4 x phi x r2
Volume Bola = 4/3 x phi x jari-jari x jari-jari x jari-jari 
"""
def luas_bola():
	luas = 4*22/7*r**2
	return luas
def volume_bola():
	volume = 4/3*22/7*r**3
	return volume

"""TABUNG
Volume = luas alas x tinggi, atau luas lingkaran x t
Luas = luas alas + luas tutup + luas selimut, atau ( 2 x phi x r x r) + phi x d x t)
"""
def luas_tabung():
	luas = 2*(22/7*r**2)+(22/7*(r+r)*t)
	return luas
def volume_tabung():
	volume = 22/7*r**2*t
	return volume

"""KERUCUT
Volume = 1/3 x phi x r x r x t
Luas = luas alas + luas selimut
"""
def luas_kerucut():
	luas = (22/7*r**2)+(22/7*(r+r)*t)
	return luas
def volume_kerucut():
	volume = 1/3*22/7*r**3
	return volume

"""LIMAS
Volume = 1/3 luas alas tinggi sisi
Luas = luas alas + jumlah luas sisi tegak
"""
def luas_limas():
	luas = 4*(1/2*alas*tinggi)+2*(p+l) #jika limas alasnya persegi panjang
	return luas
def volume_limas():
	volume = 1/3*(p*l*t)
	return volume


def menu(str):
	return str


#test balok
p, l,  t = 16,10,8
print "Balok test"
print "luas: ", luas_balok() , "volume: ", volume_balok()
print "keliling: ", keliling_balok() , "diagonal: ", diagonal_balok()


#test tabung
r, t = 7, 10
print "TABUNG test"
print "luas: ", luas_tabung() , "volume: ", volume_tabung()



