import requests
import time

def ambilDataGempaPgr3():
    print("## DATA GEMPA PGR3 ##")
    url = 'https://pgt.bmkg.go.id/login/sanglah_json'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        jsonData = response.json()
        data = jsonData[0]
        # print(data)
        if len(data['bulan']) == 1:
            bulan = '0'+ data['bulan']
        else:
            bulan = data['bulan']

        if len(data['tanggal']) == 1:
            tanggal = '0' + data['tanggal']
        else:
            tanggal = data['tanggal']
        jam = data["TIME"].replace(":","")
        id = data['tahun'] + bulan + tanggal +jam
        id_shakemap = data['idpublic'].replace("\n","")
        id_shakemap = id_shakemap.replace(" ","")
        return response.status_code , id,  data['gempabumi'] , data['lat'] , data['lon'] , id_shakemap
    else:
        print("Gagal Mengambil Data Gempa")
        return response.status_code, "" , "", "" , ""


def cekLokasi(lat,long):
    batasAtasLintang = -7;
    batasBawahLintang = -12;
    batasKiriBujur = 113.21;
    batasKananBujur = 117.31;
    if (batasBawahLintang <= float(lat) and batasAtasLintang >= float(lat) and float(long) >= batasKiriBujur and float(long) <= batasKananBujur):
        return "sesuai"
    else:
        return "tidak sesuai"


def kirimData(id, infogempa, tabel,id_shakemap=""):
    # url = 'http://182.23.56.142:90/geofisikaDNP/profileWeb/simpan_gempapgr3'
    # url = 'http://182.23.56.142:90/stageof-bali/web/simpan2'
    # url = 'https://stageof-bali.bmkg.go.id/web/simpan2'
    url = 'http://182.16.249.163/web/simpan2'
    dataKirim = id + "==" + infogempa+"=="+ id_shakemap +"=="+ tabel
    myobj = {'gempa': dataKirim}
    x = requests.post(url, data=myobj)
    if x.status_code == 200:
        print("DATA BERHASIL DIKIRIMKAN KE WEB SERVER")
        print(x.text)
        # print("=================================================================================")
        # print("")
    else:
        print("DATA GAGAL DIKIRIM KE SERVER")
        print(x.text)

def prosesDataGempaPgr3(id,infoGempa, lat,lon,id_shakemap=""):
    # BACA DATA GEMPA TERAKHIR
    gempaPgr3TerakhirTxt = open("GempaPgr3Terakhir.txt", "r")
    dataGempaPgr3Terakhir = gempaPgr3TerakhirTxt.readline()
    gempaPgr3TerakhirTxt.close()
    if dataGempaPgr3Terakhir == id:
        print("Tidak ada perubahan")
    else:
        print("Ada Perubahan")
        cek = cekLokasi(lat , lon) #cek apakah di wilayah bali atau tidak
        if cek == "sesuai":
            print("gempa berada di daerah Bali")
            tabel = "gempabali"
            kirimData(id,infoGempa,tabel,id_shakemap)
            tabel = "gempapgr3"
            kirimData(id,infoGempa,tabel)
            gempaPgr3TerakhirTxt = open("GempaPgr3Terakhir.txt", "w")
            gempaPgr3TerakhirTxt.write(id)
            gempaPgr3TerakhirTxt.close()
            print("data tersimpan pada" , gempaPgr3TerakhirTxt.name )
            print("")
        else:
            print("gempa TIDAK berada di daerah Bali")
            tabel = "gempapgr3"
            kirimData(id, infoGempa, tabel)
            gempaPgr3TerakhirTxt = open("GempaPgr3Terakhir.txt", "w")
            gempaPgr3TerakhirTxt.write(id)
            gempaPgr3TerakhirTxt.close()
            print("data tersimpan pada", gempaPgr3TerakhirTxt.name)
            print("")






