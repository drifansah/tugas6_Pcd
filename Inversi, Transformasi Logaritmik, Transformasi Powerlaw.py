#import library
import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt

#membaca gambar
img = imageio.imread("vespa.jpg")
#mendapatkan resolusi dan type  gambar
#dipake diperulangan

img_height = img.shape[0]#tinggi gambar
img_width = img.shape[1]#lebar gambar
img_channel = img.shape[2]#banyaknya channel setiap pixel
img_type = img.dtype #type gambar

#Inversi
#Membuat variabel img_inversi
img_inversi = np.zeros(img.shape, dtype=np.uint8)

#Membuat fungsi untuk inversi grayscale
img_inversi = np.zeros(img.shape, dtype=np.uint8) #membuat variable untuk inversi sesuai type data 

def inversi_grayscale(nilai): #untuk menyatakan fungsi inversi grayscale 
    for y in range(0, img_height): #memberikan interval range untuk variabel y sebagai ketinggian
        for x in range(0, img_width): #memberikan interval range untuk variabel x sebagai lebar gambar
            red = img[y][x][0] #memberikan nilai piel untuk red
            green = img[y][x][1] #memberikan nilai pixel untuk green
            blue = img[y][x][2] #memberikan nilai pixel untuk blue
            gray = (int(red) + int(green) + int(blue)) / 3 #rumus untuk merubah gambar original menjadi grayscale 
            gray = nilai - gray #rumus untuk menentukan hasil yang ditampilkan 
            img_inversi[y][x] = (gray, gray, gray) #mnampilkan hasil dari prubahan
def inversi_rgb(nilai):#untuk menyatakan fungsi inversi rgb
    for y in range(0, img_height): #memberikan interval range untuk variabel y sebagai ketinggian
        for x in range(0, img_width):#memberikan interval range untuk variabel x sebagai lebar gambar
            red = img[y][x][0]#menentukan variable untuk red x,y
            red = nilai - red #menentukan hasil red yang dikurangi nilai untuk inversi 
            green = img[y][x][1]#menentukan variable untuk green x,y
            green = nilai - green#menentukan hasil green yang dikurangi nilai untuk inversi 
            blue = img[y][x][2]#menentukan variable untuk blue x,y
            blue = nilai - blue#menentukan hasil bllue yang dikurangi nilai untuk inversi 
            img_inversi[y][x] = (red, green, blue)#menampilkan hasil output dari perubahan

#Menampilkan hasil inversi
inversi_grayscale(255) #menampilkan nilai pixel inversi grayscale
plt.imshow(img_inversi) #menampilkan gambar hasil inversi 
plt.title("Inversi Grayscale") #memasukkan judul untuk gambar
plt.show()#mnampilkan keseluruhan gambar yang akan ditampilkan di window

inversi_rgb(255) #menampilkan nilai pixel rgb hasil inversi
plt.imshow(img_inversi)#menamopilkan gambar hasil dari inversi rgb 
plt.title("Inversi RGB") #mmasukkan judul gambar yang akan ditampilkan 
plt.show()#menampilkan keseluruhan gambar yang akan ditampilkan di windows

#Log
#Membuat variabel img_log untuk menampung hasil
img_log = np.zeros(img.shape, dtype=np.uint8)#membuat variable untuk log sesuai type data 
#Mendefinisikan fungsi untuk log
def log(c):#fungsi log
    for y in range(0, img_height):#perulangan dari 0 hingga img_height
        for x in range(0, img_width):#perulangan 0 hingga img_widht
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(c * np.log(gray + 1))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_log[y][x] = (gray, gray, gray)
#Menampilkan hasil log
log(30)
plt.imshow(img_log)
plt.title("Log")
plt.show()

#inversi & log
img_inlog = np.zeros(img.shape, dtype=np.uint8) #membuat variable img_inlog untuk menampung hasil
def inlog(c): #mendifinisikan fungsi untuk inversi inlog
    for y in range(0, img_height):#memberikan nilai interval range untuk variabel y sebagai ketinggian gambar
        for x in range(0, img_width):#memberikan nilai interrval range untuk variable x sebagai lebar gambar 
            red = img[y][x][0] #memberikan nilai piel untuk red
            green = img[y][x][1] #memberikan nilai pixel untuk green
            blue = img[y][x][2] #memberikan nilai pixel untuk blue
            gray = (int(red) + int(green) + int(blue)) / 3 #rumus untuk merubah gambar original menjadi grayscale 
            gray = int(c * np.log(255 - gray + 1))#rumus untuk invers log 
            if gray > 255: #penentuan gray menggunakan fungsi if
                gray = 255 #nilai untuk gray 
            if gray < 0:#penentuan nilai gray  menggunakan fungsi if
                gray = 0#nilai untuk gray 
            img_inlog[y][x] = (gray, gray, gray) #hasil yang keluar sebagai output
            
inlog(30) #nilai inlog yang di tampilkan 
plt.imshow(img_inlog)#penampilan hasil gambar inversi log 
plt.title("Inversi & Log")#memasukkan atau memberikan judul pada gambar yang akan ditampilkan 
plt.show()#menampilkan keseluruhan gambar pada windows

img_nthpower = np.zeros(img.shape, dtype=np.uint8) #membuat variable img_nthPower untuk menampung hasil

def nthpower(c, y): #mendefinisikan fungsi x,y untuk nth power
    thc = c / 100 #penentuan nilai thc
    thy = y / 100 #penentuan nilai thy
    for y in range(0, img_height): #memberikan interval range untuk variable y sebagai ketinggian gambar
        for x in range(0, img_width): #memberikan interval range  untuk variable y sebagai lebar gambar
            red = img[y][x][0] #memberikan nilai piel untuk red
            green = img[y][x][1] #memberikan nilai pixel untuk green
            blue = img[y][x][2] #mclsemberikan nilai pixel untuk blue
            gray = (int(red) + int(green) + int(blue)) / 3 #rumus untuk merubah gambar original menjadi grayscale 
            gray = int(thc * pow(gray, thy)) #rumus untuk nth powr
            if gray > 255: #penentuan nilai untuk gray menggunakan fungsi if
                gray = 255 #nilai gray
            if gray < 0: #penentuan nilai untuk gray menggunakan fungsi if
                gray = 0 #nilai gray
            img_nthpower[y][x] = (gray, gray, gray) #hasil gambar yang akan ditampilkan 
        
nthpower(50, 100) #nilai nth yang akan ditampilkan 
plt.imshow(img_nthpower) #penampilan gambar hasil nth power
plt.title("Nth Power")#untuk memasukkan judul pada gambar yang akan di tampilkan 
plt.show() #menampilkan keseluruhan gambar hasil nth power yang ditampilkan di window 

#nth root power
img_nthrootpower = np.zeros(img.shape, dtype=np.uint8) #membuat variable img_nthrootpower

def nthrootpower(c, y): #mendefinisikan fungsi untuk nth root power
    thc = c / 100 #penentuan nilai thc
    thy = y / 100 #pnentuan nilai thy
    for y in range(0, img_height): #memberikan interval range untuk variable y sebagai ketinggian  gambar
        for x in range(0, img_width): #memberikan interval range untuk variasi x sebagai lebar gambar
            red = img[y][x][0] #memberikan nilai piel untuk red
            green = img[y][x][1] #memberikan nilai pixel untuk green
            blue = img[y][x][2] #memberikan nilai pixel untuk blue
            gray = (int(red) + int(green) + int(blue)) / 3 #rumus untuk merubah gambar original menjadi grayscale 
            gray = int(thc * pow(gray, 1./thy)) #rumus untuk nth root power
            if gray > 255:#menentukan nilai gray menggunakan fungsi if
                gray = 255 #nilai gray yang harus ditampilkan
            if gray < 0:#menentukan nilai gray menggunakan fungsi ig
                gray = 0 #nilai yang harus ditampilkan 
            img_nthpower[y][x] = (gray, gray, gray) #hasil gambar yang akan ditampilkan 

nthrootpower(50, 100) #nilai nth root power
plt.imshow(img_nthrootpower)#menampilkan gambar hasil nthrootpower
plt.title("Nth Root Power")#memasukkan judul pada gambar yang akan dita,pilkan
plt.show()#menampilkan keseluruhan gambar hasil yang akan ditampilkan di windows

