#Histogram
#import library
import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt

#membaca gambar
img = imageio.imread("vespa.jpg")
#mendapatkan resolusi dan type  gambar
img_height = img.shape[0] #untuk mendapatkan ukuran lebar dari gambar
img_width = img.shape[1] #untuk mendapatkan ukuran tinggi dari gambar
img_channel = img.shape[2] #untuk mendapatkan resolusi gambar
img_grayscale = np.zeros(img.shape, dtype=np.uint8) #membuat array berdasarkan bentuk dan tipe tertentu

for y in range(0, img_height): #memberikan interval range untuk tiggi
    for x in range(0, img_width): #memberikan interval range lebar
        red = img[y][x][0] #memberikan nilai piel untuk red
        green = img[y][x][1] #memberikan nilai pixel untuk green
        blue = img[y][x][2] #memberikan nilai pixel untuk blue
        gray = (int(red) + int(green) + int(blue)) / 3 #rumus untuk merubah gambar original menjadi grayscale 
        img_grayscale[y][x] = (gray, gray, gray) #menampilkan hasil yang akan ditampilkan
        
plt.imshow(img_grayscale)#menampilkan gambar yang sudah dilakukan perubahan
plt.title("Grayscale") #memberikan judul pada gambar yang akan ditampilkan
plt.show()# menampilkan gambar keseluruhan

#Menampilkan Histogram Gambar Grayscale
#Membuat variabel untuk menyimpan data gambar
#menampilkan histogram gambar grayscale
hg = np.zeros ((256)) #membuat variable untuk menyimpan data gambar

for x in range (0, 256): #memberikan interval range untuk x
    hg[x] = 0 #memberikan setiap nilai dalam array hg dengan 0

for y in range (0, img_height): #memberikan interval range  untuk y sebagai tinggi gambar
    for x in range(0, img_width): #memberkan interval range untuk x sebagai lebar gambar
        gray = img_grayscale[y][x][0] #mengisi nilai gray pada gambar
        hg[gray] += 1  #memasukkan nilai atau menghitung nilai dari gambar
#menampilkan histogram
#plt.figure(figsize=(20, 6)) #mllakukan objek yang mengandung semua elemen dari grafik
#plt.plot(hg, color="black", linewidth=2.0) #melakukan ploting 
#plt.show() #menampilkan gambar atau grafik

bins = np.linspace(0, 256, 100) # mengelompokkan data numerik menjadi beberapa bin agar sebaran data lebih mudah dipahami menggunakan  spasi secara merata dalam interval terettentu
plt.hist(hg, bins, color = "black", alpha = 0.5) #untuk membuat histogram grafik yang menunjukan distribusi frekuensi
plt.title ("Histogram") #memberikan judul pada gambar yang ditampilkan
plt.show() #menampilkan keseluruhan histogram yang dibuat 

#Menampilkan Histogram Gambar RGB
#Membuat variabel untuk menyimpan data gambar
hgr = np.zeros((256)) #membuat variabel red dengan nilai 256
hgg = np.zeros ((256)) #membuat variable green dengan nilai 256
hgb = np.zeros ((256)) #membuat variable blue dengan nilai 256
hgrgb = np.zeros ((768)) #membuat variable rgb dengan nilai 256
for x in range (0, 256): #untuk mengisi interval range setiap nilai dalam array hg dengan 0
    hgr[x] = 0 #mengisi nilai array hgred dengan 0
    hgg[x] = 0 #mengisi nilai array hggreen dengan 0
    hgb[x] = 0 #mengisi nilai array hgblue dengan 0

for x in range (0, 768) : #untuk mengisi interval range setiap nilai dalam array hg dengan 0
    hgrgb [x] = 0 #mengisi nilai array rgb dengan 0
for x in range (0, 256) : #mmberikan interval range untuk x
    hgr[x] = 0 #mengisi nilai array hgred dengan 0
    hgg[x] = 0 #mengisi nilai array hggreen dengan 0
    hgb[x] = 0 #mengisi nilai array hgblue dengan 0
for x in range (0, 768) : #membrikan interval range untuk x
    hgrgb [x] = 0 #mengisi nilai array rgb dengan 0
    
#th = int(256/64)
temp = [0]
for y in range(0, img.shape[0]): #memberikan interval range untuk y
    for x in range(0, img.shape[1]): #memberikan interval range untuk x
        red = int(img[y][x][0]) #menghitung nilai pixel red
        green = int(img[y][x][1]) #menghitung nilai pixel green
        blue = int(img[y][x][2]) #menghitung nilai pixel blue
        green = green + 256 #menghitung nilai pixel untuk green
        blue = blue + 512 #menghitung nilai pixel untuk blue
        #temp.append(green)
        hgrgb[red] += 1 #memberikan nilai hgrgbred
        hgrgb[green] += 1 #memberikan nilai hgrgbgreen
        hgrgb[blue] += 1 #memberikan nilai hgrgbblu

binsrgb = np.linspace(0, 768, 100) #mengelompokkan data numerik menjadi beberapa bin agar sebaran data lebih mudah dipahami menggunakan  spasi secara merata dalam interval terettentu
plt.hist(hgrgb, binsrgb, color="black", alpha=0.5)#untuk membuat histogram grafik yang menunjukan distribusi frekuensi
# plt.plot(hgrgb)
plt.title("Histogram Red Green Blue")#memberikan judul pada gambar yang akan ditampilkan
plt.show()#menampilkan keseluruhan gambar yang sudah dibuat

#Menampilkan Histogram
for y in range(0, img_height): #memberikan interval range untuk y
    for x in range(0, img_width): #memberikan interval range untuk x
        red = img[y][x][0] #menghitung nilai pixel red
        green = img[y][x][1] #menghitung nilai pixel green
        blue =img[y][x][2] #menghitung nilai pixel blue
        hgr[red] += 1 #memberikan nilai hgrgbred
        hgg[green] += 1 #memberikan nilai hgrgbgreen
        hgb[blue] += 1 #memberikan nilai hgrgbblu

bins = np.linspace(0, 256, 100) #mengelompokkan data numerik menjadi beberapa bin agar sebaran data lebih mudah dipahami menggunakan  spasi secara merata dalam interval terettentu
plt.hist(hgr, bins, color="red", alpha=0.5)#membuat grafik yang menunjukkan sebaran frekuensi red
plt.title("Histogram Red") #memberikan judul pada grafik yang akan ditampilkan
plt.show() #menampilkan gambar yang sudah dibuat

plt.hist(hgg, bins, color="green", alpha=0.5)#membuat grafik yang menunjukkan sebaran frekuensi green
plt.title("Histogram Green") #memberikan judul pada gambar 
plt.show()#menampilkan gambar secara menyeluruh yang telah dibuat

plt.hist(hgb, bins, color="blue", alpha=0.5)#membuat grafik yang menunjukkan sebaran frekuensi blue
plt.title("Histogram Blue")#memberikan judul pada gambar
plt.show()#menampilkan gambar secara menyeluruh yang telah dibuat


#Menampilkan Histogram Kumulatif
#menampilkan histogram komulatif
hgk = np.zeros((256)) #membuat variabl hgk dengan nilai 256
c = np.zeros((256)) #membuat variabl c dengan nilai 256

for x in range(0, 256): #memberikan interval rang untuk x
    hgk[x] = 0 #memasukkan nilai hgk dengan 0
    c[x] = 0  #memasukkan nilai c dengan 0

for y in range(0, img_height):#membuat interval range variabel y untuk nilai tinggi
    for x in range(0, img_width): #membuat interval range variabl x untuk nilai lebar
        gray = img_grayscale[y][x][0] #memberirkan nilai gray pada variabel x,y
        hgk[gray] += 1 #memasukkan nilai hgk untuk gray
                
c[0] = hgk[0]
for x in range(1, 256): #memberikan nilai range untuk variable x
     c[x] = c[x-1] + hgk[x] #rumus untuk melakukan perhitungan histogram

hmaxk = c[255] #nilai max histogram komulatif

for x in range(0, 256):#memberikan interval range untuk variable x 
    c[x] = 190 * c[x] / hmaxk #rumus untuk menentukan nilai max histogram komulatif

plt.hist(c, bins, color="black", alpha=0.5)#membuat grafik yang menunjukkan sebaran frekuensi blue
plt.title("Histogram Grayscale Kumulatif")#membuat atau memasukkan judul untuk histogram komulatif yang ditampilkan
plt.show()#menampilkan keseluruhan histogram yang sudah dibuat


#Menampilkan Histogram Hequalisasi
hgh = np.zeros((256)) #membuat variable untuk histogram hequalisasi
h = np.zeros((256))#membuat variabel untuk histogram 
c = np.zeros((256))#membuat variable untuk reoslusi 

for x in range(0, 256): #membuat interval variable untuk nilai x
    hgh[x] = 0 #memasukkan nilai array x untuk histogram hequaliisasi
    h[x] = 0 #memasukkan nilai aray x untuk histogram
    c[x] = 0 #memasukkan nilai array x untuk nilai resolusi channel

for y in range(0, img_height): #membuat interval range variable y untuk ketinggian gambar
    for x in range(0, img_width): #mmbuat interval range variable x untuk lebar gambar
        gray = img_grayscale[y][x][0] #memberikan nilai gray untuk variable x,y
        hgh[gray] += 1 #memasukkan nilai variabel untuk histogram hequalisasi
                
h[0] = hgh[0] #penentuan nilai histogram hequalisasi
for x in range(1, 256): #membuat interval range untuk nilai x
     h[x] = h[x-1] + hgh[x] #rumus penentuan histogram untuk variable x

for x in range(0, 256):#membuat interval range untuk nilai x
     h[x] = h[x] / img_height / img_width #penentuan histogram untuk variabl x ketinggian dan lebar

for x in range(0, 256):#membuat interval range untuk nilai x
    hgh[x] = 0
    
for y in range(0, img_height):#membuat interval range variable y untuk ketinggian gambar
    for x in range(0, img_width): #mmbuat interval range variable x untuk lebar gamba
        gray = img_grayscale[y][x][0]#memberikan nilai gray untuk variable x,y
        gray = h[gray] * 255 #menentukan nilai gray pada histogram 
        hgh[int(gray)] += 1 #memasukkan nilai gray pada histogram 

c[0] = hgh[0]
for x in range(1, 256): 
     c[x] = c[x-1] + hgh[x]

hmaxk = c[255]

for x in range(0, 256):
    c[x] = 190 * c[x] / hmaxk

plt.hist(c, bins, color="black", alpha=0.5) ##membuat grafik yang menunjukkan sebaran frekuensi
plt.title("Histogram Grayscale Hequalisasi") #memberikan judul pada histogram yang akan ditampilkan
plt.show() # menampilkan keseluruhan histogram yang sudah dibuat


