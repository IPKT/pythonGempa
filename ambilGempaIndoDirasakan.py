import requests
from xml.dom.minidom import parseString
from ambilGempaPgr3 import cekLokasi , kirimData

def ambilDataGempaIndoDirasakan (no):
    # baca disini bro https://nanonets.com/blog/parse-xml-files-using-python/
    url = 'https://data.bmkg.go.id/DataMKG/TEWS/gempadirasakan.xml'
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }
    response = requests.get(url, headers=headers)

    document = parseString(response.content)
    tanggal = document.getElementsByTagName("Tanggal")[no].firstChild.nodeValue
    jam = document.getElementsByTagName("Jam")[no].firstChild.nodeValue
    koordinat = document.getElementsByTagName("coordinates")[no].firstChild.nodeValue
    lintang = document.getElementsByTagName("Lintang")[no].firstChild.nodeValue
    bujur = document.getElementsByTagName("Bujur")[no].firstChild.nodeValue
    magnitude = document.getElementsByTagName("Magnitude")[no].firstChild.nodeValue
    kedalaman = document.getElementsByTagName("Kedalaman")[no].firstChild.nodeValue
    wilayah = document.getElementsByTagName("Wilayah")[no].firstChild.nodeValue
    # potensi = document.getElementsByTagName("Potensi")[no].firstChild.nodeValue
    dirasakan = document.getElementsByTagName("Dirasakan")[no].firstChild.nodeValue
    id = createIdGempaBesar(tanggal , jam)
    tanggal = tanggal.split(" ")
    abad = tanggal[2][:-2]
    tahun = tanggal[2].replace(abad,"")
    tanggal = tanggal[0]+"-"+tanggal[1]+"-"+tahun

    infoGempa = 'Info Gempa Mag:'+magnitude+" SR, " + tanggal +" "+ jam +", Lok:"+lintang+","+bujur+" ("+wilayah+"), Kedlmn:"+kedalaman+" :: Dirasakan: " + dirasakan

    sumberData = "bmkgpusat"
    lat = koordinat.split(",")[0]
    long = koordinat.split(",")[1]

    return response.status_code , id, infoGempa, lat, long

def createIdGempaBesar (tanggal, jam):
    jam = jam.replace(" WIB","")
    tahun = tanggal.split(" ")[2]
    bulan = tanggal.split(" ")[1]
    if (bulan == 'Des'):
        bulan = '12'
    elif (bulan == 'Dec'):
        bulan = '12'
    elif (bulan == 'Nov'):
        bulan = '11'
    elif (bulan == 'Jan'):
        bulan = '01'
    elif (bulan == 'Feb'):
        bulan = '02'
    elif (bulan == "Mar"):
        bulan = '03'
    elif (bulan == 'Apr'):
        bulan = '04'
    elif (bulan == 'May'):
        bulan = '05'
    elif (bulan == 'Mei'):
        bulan = '05'
    elif (bulan == 'Jun'):
        bulan = '06'
    elif (bulan == 'Jul'):
        bulan = '07'
    elif (bulan == 'Aug'):
        bulan = '08'
    elif (bulan == 'Agu'):
        bulan = '08'
    elif (bulan == 'Sep'):
        bulan = '09'
    elif (bulan == 'Oct'):
        bulan = '10'
    elif (bulan == 'Okt'):
        bulan = '10'
    tanggal = tanggal.split(" ")[0]
    jam = jam.replace(":","")
    id = tahun+bulan+tanggal+jam
    return id

def prosesDataGempaIndoDirasakan(id,infoGempa, lat,lon):
    cek = cekLokasi(lat, lon)  # cek apakah di wilayah bali atau tidak
    if cek == "sesuai":
        print("gempa dirasakan berada di daerah Bali")
        tabel = "gempabalidirasakan"
        kirimData(id, infoGempa, tabel)
        tabel = "gempaindodirasakan"
        kirimData(id, infoGempa, tabel)
    else:
        print("gempa dirasakan TIDAK berada di daerah Bali")
        tabel = "gempaindodirasakan"
        kirimData(id, infoGempa, tabel)
