import cv2
import numpy as np

#membaca citra digital dari komputer
citra1 = cv2.imread("D:/Berkas Penting/Tugas Kuliah/Code/Py/image processing/green-screen2.jpg")

#membaca channel warna BGR dan menyimpannya ke dalam variabel terpisah
b = citra1[:,:,0]
g = citra1[:,:,1]
r = citra1[:,:,2]

#menyimpan jumlah baris dan jumlah kolom dari citra
jum_baris = len(citra1)
jum_kolom = len(citra1[0])

#menyiapkan citra baru dengan nilai 0
citra_subtraction = np.zeros((jum_baris, jum_kolom, 3))
subtract_value = 255

#menghitung nilai pixel grayscale
for i in range(jum_baris):
    for j in range(jum_kolom):
        citra_subtraction[i, j, 1] = b[i, j] - 0
        citra_subtraction[i, j, 1] = g[i, j] - 0
        citra_subtraction[i, j, 1] = r[i, j] - 0
        
        if (citra_subtraction[i, j, 0] > 0):
            citra_subtraction[i, j, 0] = citra_subtraction[i, j, 0]
        
        if (citra_subtraction[i, j, 1] > 0):
            citra_subtraction[i, j, 1] = 0
        
        if (citra_subtraction[i, j, 2] > 0):
             citra_subtraction[i, j, 2] = citra_subtraction[i, j, 2]

citra_subtraction = citra_subtraction.astype(np.uint8)

cv2.imshow("empty car", citra1)
cv2.imshow("subtract", citra_subtraction)

cv2.waitKey()