import matplotlib.pyplot as Grafik
import numpy as np
import random

veriler = np.loadtxt('./cancerData.txt', delimiter=',', usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9))
k = [2, 3, 4, 5, 6, 7, 8]
merkez_noktalari = np.zeros(len(k))
veri_sayisi = veriler.shape[0]


def k_means():
    for i in k:
        merkez_noktasi = np.zeros([i, 9])
        for j in range(i):
            random_1 = random.randint(1, int(veri_sayisi / 2))
            random_2 = random.randint(int(veri_sayisi / 2), veri_sayisi - 1)
            merkez_noktasi[j] = np.average(veriler[random_1:random_2], axis=0)
        uzaklik = np.zeros([veri_sayisi, i])
        gecici_merkez_noktais = np.zeros(merkez_noktasi.shape)
        while np.sum(merkez_noktasi - gecici_merkez_noktais) != 0:
            gecici_merkez_noktais[:, :] = merkez_noktasi[:, :]

            for j in range(i):
                uzaklik[:, j] = np.linalg.norm((veriler - merkez_noktasi[j]), axis=1)
                classification = np.argsort(uzaklik, axis=1)
                classification = np.delete(classification, np.arange(1, i), 1)
                arrange = np.reshape(np.argsort(classification, axis=0), veriler.shape[0])
                data1 = 0
                potential = 0
                for j in range(veriler.shape[0] - 1):
                    if classification[arrange[j]] != classification[arrange[j + 1]]:
                        data2 = j + 1
                        merkez_noktasi[classification[arrange[j]]] = np.average(veriler[arrange[data1:data2]], axis=0)
                        potential += np.sum(np.square(
                            np.linalg.norm(veriler[arrange[data1:data2]] - merkez_noktasi[classification[arrange[j]]], axis=1)))
                        data1 = data2
                merkez_noktasi[classification[arrange[j - 1]]] = np.average(veriler[arrange[data1:veriler.shape[0]]], axis=0)
                potential += np.sum(np.square(
                    np.linalg.norm(veriler[arrange[data1:veriler.shape[0]]] - merkez_noktasi[classification[arrange[j - 1]]],
                                   axis=1)))
            merkez_noktalari[k.index(i)] = potential
            print(k.index(i))
k_means()
Grafik.bar(k, merkez_noktalari, color='red',)
Grafik.ylim(min(merkez_noktalari)*0.80,max(merkez_noktalari)*1.1)
Grafik.xlabel('K')
Grafik.ylabel('L(K)')
Grafik.title('K-ortalama algoritmasi')
Grafik.show()