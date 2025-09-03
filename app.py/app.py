import requests
print("MATERI 13 - JSON API")
print("-" *40)
kota = input("Masukkan Nama Kota: ")
# set target url ke api al-dhan
url ="https://api.aladhan.com/v1/timingsByCity/28-08-2025?city={kota}&country=Indonesia&method=5"
print(f"Target URL: {url}")
response = requests.get(url) # Http get (ambil data)
data_json = response.json() # ambil data sebagai format json
print("Jadwal Sholat:")
# buat data timings ke variable baru agar lebih ringkas 
jadwal_sholat = data_json["data"]["timings"]
print(f"-> Shubuh = {jadwal_sholat ["Fajr"]}")
print(f"-> Maghrib = {jadwal_sholat ["Maghrib"]}")
print(f"-> Isya = {jadwal_sholat ["Isha"]}")
