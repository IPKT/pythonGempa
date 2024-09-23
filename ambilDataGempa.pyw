import time

from ambilGempaPgr3 import ambilDataGempaPgr3 , prosesDataGempaPgr3
from ambilGempaIndoM5 import ambilDataGempaIndoM5 , prosesDataGempaIndoM5
from  ambilGempaIndoDirasakan import ambilDataGempaIndoDirasakan , prosesDataGempaIndoDirasakan

print("===================================================================================================")
# AMBIL DATA GEMPA PGR3
response, id, infoGempa, lat, lon = ambilDataGempaPgr3()
if response == 200:
    print(id, lat, lon, infoGempa)
    prosesDataGempaPgr3(id, infoGempa,lat,lon)
else:
    print("Gagal Diproses")
    print("")

print("===================================================================================================")

#AMBIL DATA GEMPA INDO M5
print("## DATA GEMPA INDO M5 ##")
response, id, infoGempa, lat, lon = ambilDataGempaIndoM5(0)
if response == 200:
    print(id, lat, lon, infoGempa)
else:
    print("Gagal Diproses")
    print("")
gempaPgr3TerakhirTxt = open("GempaIndoM5Terakhir.txt", "r")
dataGempaPgr3Terakhir = gempaPgr3TerakhirTxt.readline()
gempaPgr3TerakhirTxt.close()
if dataGempaPgr3Terakhir == id:
    print("Tidak ada perubahan")
else:
    print("Ada Perubahan")
    print("")
    for a in range(-3,1):
        response, id, infoGempa, lat, lon = ambilDataGempaIndoM5(-a)
        if response == 200:
            print(id, lat, lon, infoGempa)
            prosesDataGempaIndoM5(id, infoGempa, lat, lon)
            gempaIndoM5Terakhir = open("GempaIndoM5Terakhir.txt", "w")
            gempaIndoM5Terakhir.write(id)
            gempaIndoM5Terakhir.close()
            print("data tersimpan pada ",gempaIndoM5Terakhir.name)
            print("")
        else:
            print("Gagal Diproses")
            print("")

print("===================================================================================================")

# AMBIL DATA GEMPA INDO DIRASAKAN
print("## DATA GEMPA INDO DIRASAKAN ##")
response, id, infoGempa, lat, lon = ambilDataGempaIndoDirasakan(0)
if response == 200:
    print(id, lat, lon, infoGempa)
else:
    print("Gagal Diproses")
    print("")
gempaIndoDirasakanTerakhirTxt = open("GempaIndoDirasakanTerakhir.txt", "r")
dataGempaIndoDirasakanTerakhir = gempaIndoDirasakanTerakhirTxt.readline()
gempaIndoDirasakanTerakhirTxt.close()
if dataGempaIndoDirasakanTerakhir == id:
    print("Tidak ada perubahan")
else:
    print("Ada Perubahan")
    print("")
    for a in range(-14,1):
        response, id, infoGempa, lat, lon = ambilDataGempaIndoDirasakan(-a)
        if response == 200:
            print(id, lat, lon, infoGempa)
            prosesDataGempaIndoDirasakan(id, infoGempa, lat, lon)
            gempaIndoDirasakanTerakhirTxt = open("GempaIndoDirasakanTerakhir.txt", "w")
            gempaIndoDirasakanTerakhirTxt.write(id)
            gempaIndoDirasakanTerakhirTxt.close()
            print("data tersimpan pada ",gempaIndoDirasakanTerakhirTxt.name)
            print("")
        else:
            print("Gagal Diproses")
            print("")

print("===================================================================================================")

time.sleep(10)