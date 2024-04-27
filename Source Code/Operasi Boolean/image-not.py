import cv2
import numpy as np

#membaca citra digital dari komputer
citra1 = cv2.imread("E:/Documents/Jobs/UTY/Semester Ganjil 21-22/Pengolahan Citra Digital/Kode Program/gambar-hewan-bw.jpg")

#membaca channel warna BGR dan menyimpannya ke dalam variabel terpisah
b1 = citra1[:,:,0]
g1 = citra1[:,:,1]
r1 = citra1[:,:,2]

#menyimpan jumlah baris dan jumlah kolom dari citra
jum_baris = len(citra1)
jum_kolom = len(citra1[0])

#menyiapkan citra baru dengan nilai 0
citra_gray1 = np.zeros((jum_baris, jum_kolom))
citra_not = np.zeros((jum_baris, jum_kolom))

#menghitung nilai pixel grayscale
for i in range(jum_baris):
    for j in range(jum_kolom):
        # aktifkan ini jika ingin menggunakan citra grayscale 
        citra_gray1[i, j] = round(0.299 * r1[i, j] + 0.587 * g1[i, j] + 0.114 * b1[i, j])
        
        # thresholding untuk konversi grayscale ke biner
        if (citra_gray1[i, j] >= 128):
            citra_gray1[i, j] = 1
        else:
            citra_gray1[i, j] = 0

        citra_not[i, j] = 1 - citra_gray1[i, j]

        # aktifkan ini jika ingin menggunakan citra RGB
        # citra_not[i, j, 0] = 255 - b1[i, j]
        # citra_not[i, j, 1] = 255 - g1[i, j]
        # citra_not[i, j, 2] = 255 - r1[i, j]

# uint8 utk 8 bit
# citra_gray1 = citra_gray1.astype(np.uint8)
# citra_not = citra_not.astype(np.uint8)

cv2.imshow("empty car", citra_gray1)
cv2.imshow("subtract", citra_not)

cv2.waitKey()