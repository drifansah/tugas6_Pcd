#IMPORT LIBRARY
import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt

#membaca gambar
img = imageio.imread("vespa.jpg")

#mendapatkan resolusi dan type  gambar
img_height = img.shape[0]#tinggi gambar
img_width = img.shape[1]#lebar gambar
img_channel = img.shape[2]#banyaknya channel setiap pixel
img_type = img.dtype #type gambar

#Membuat variabel dengan resolusi dan tipe yang sama seperti gambar
img_flip_horizontal = np.zeros(img.shape, img_type)#berfungsi untuk memberikan bentuk dan tipe menjadi horizontal
img_flip_vertical = np.zeros(img.shape, img_type)#berfungsi untuk memberikan bentuk dan tipe gambar vertikal

#Membalik gambar secara horizontal
for y in range(0, img_height): #memberikan interval rang untuk height ketika dibalikkan secara horizontal
    for x in range (0, img_width): #memberikan interval range untuk width ketika dibalikkan secara horizontal
        for c in range (0, img_channel): #memberikan interval range untuk resolusi ketika dibalikkan secara horizontal
            img_flip_horizontal[y][x][c] = img[y][img_width -1-x ][c] #rumus yang digunakan untuk membalikkan secara horizomtal dengan ketetapan resolusi

#Membalik gambar secara vertical
for y in range(0, img_height): #memberikan interval rang untuk height ketika dibalikkan secara vertical
    for x in range(0, img_width):#memberikan interval range untuk width ketika dibalikkan secara vertical
        for c in range(0, img_channel): #memberikan interval range untuk resolusi ketika dibalikkan secara vertikal
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c]  #rumus yang digunakan untuk membalikkan secara vertikal

#Menampilkan hasil balik gambar
plt.imshow (img_flip_horizontal) #melakukan penampilan gambar secara horizontal
plt.title ("flip Horizontal")#memberikan title atau judul pada gambar yang ditampilkan
plt.show () #menampilkan gambar serta judul secara keseluruhan
plt.imshow(img_flip_vertical) #melakukan penampilan gambar flip vertical 
plt.title("flip Vertical") #memberikan judul atau title pada gambar yang akan di tampilkan
plt.show()#menampilkan gambar serta judul dari hasil flip secara vertikal
