from prettytable import PrettyTable
import pwinput
import datetime
import re

#KUMPULAM DATA

password_admin = "admin"

data_karyawan = {
    1: {"Nama": "Anaida", "Jabatan": "CEO", "Departemen": "Direktur Utama", "Tanggal Masuk": datetime.date(2025, 1, 1), "Gaji": 50000000, "Email": "naida02@gmail.com", "Password": "123"},
    2: {"Nama": "Ghina Ghufrani", "Jabatan": "Manajer", "Departemen": "Teknologi", "Tanggal Masuk": datetime.date(2025, 1, 1), "Gaji": 15000000, "Email": "ghinaghufrani44@gmail.com", "Password": "123"},
    3: {"Nama": "Fika Nabila", "Jabatan": "Data Scientist", "Departemen": "Teknologi", "Tanggal Masuk": datetime.date(2025, 1, 1), "Gaji": 12000000, "Email": "nabilaa1331@gmail.com", "Password": "123"},
    4: {"Nama": "Cut Zahara", "Jabatan": "Manajer", "Departemen": "Produk", "Tanggal Masuk": datetime.date(2025, 1, 5), "Gaji": 15000000, "Email": "fhonnafhonna@gmail.com", "Password": "123"},
    5: {"Nama": "Nurul Maghfirah", "Jabatan": "Web Developer", "Departemen": "Teknologi", "Tanggal Masuk": datetime.date(2025, 1, 10), "Gaji": 8000000, "Email": "nurul2001@gmail.com", "Password": "123"},
    6: {"Nama": "Devi Auliani", "Jabatan": "Desainer UI/UX", "Departemen": "Produk", "Tanggal Masuk": datetime.date(2025, 1, 15), "Gaji": 8000000, "Email": "depipi55@gmail.com", "Password": "123"},
    7: {"Nama": "Suci Ramadhani", "Jabatan": "Mobile Developer", "Departemen": "Teknologi", "Tanggal Masuk": datetime.date(2025, 1, 15), "Gaji": 10000000, "Email": "suciramadhani01@gmail.com", "Password": "123"},
    8: {"Nama": "Hanifah Azzahra", "Jabatan": "Staff", "Departemen": "Pemasaran & Komunikasi", "Tanggal Masuk": datetime.date(2025, 1, 20), "Gaji": 5000000, "Email": "nifahanifah20@gmail.com", "Password": "123"},
    9: {"Nama": "Cut Aufia", "Jabatan": "Staff", "Departemen": "Konten Islami", "Tanggal Masuk": datetime.date(2025, 1, 20), "Gaji": 5000000, "Email": "aufiashadiqoh33@gmail.com", "Password": "123"}}

#FUNGSI LOGIN

def login():
    while True:
        print("Selamat datang di data karyawan.")
        print("Login sebagai:")
        print("1. Admin")
        print("2. Karyawan")

        try:
            peran = int(input("Masukkan pilihan (1/2): "))
            if peran == 1:
                return login_admin()
            elif peran == 2:
                return login_karyawan()
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Input tidak valid. Silahkan masukkan angka.")

def login_admin():
    password = pwinput.pwinput("Masukkan password admin: ")

    if password == password_admin:
        print("Login admin berhasil.")
        return True, True, None  #akses admin, status login, dan id_karyawan
    else:
        print("Password admin salah.")
        return False, False, None

def login_karyawan():
    try:
        id_karyawan = int(input("Masukkan ID karyawan: "))
        if id_karyawan in data_karyawan:
            password_karyawan = pwinput.pwinput("Masukkan password karyawan: ")

            if verifikasi_password(id_karyawan, password_karyawan):
                print("Login user berhasil.")
                return False, True, id_karyawan
            else:
                print("Password salah.")
                return False, False, None 
        else:
            print("ID user tidak ditemukan.")
            return False, False, None  #mengembalikan None jika ID tidak ditemukan
    except ValueError:
        print("Input tidak valid. Silahkan masukkan angka.")
        return False, False, None  #mengembalikan None jika input tdk valid
    
def verifikasi_password(id_karyawan, password_karyawan):
    password_tersimpan = data_karyawan[id_karyawan]["Password"] #password diambil dr kolom password

    if password_tersimpan == password_karyawan:  #memastikan passwordnya sama
        return True
    else:
        return False
    
#FUNGSI DI MENU ADMIN

def tampilkan_data_karyawan(data_karyawan, akses_admin=False):
    print("Data Karyawan :")
    table = PrettyTable()
    if akses_admin:
        table.field_names = ["ID", "Nama", "Jabatan", "Departemen", "Tanggal Masuk", "Gaji", "Email", "Password"]
    else:
        table.field_names = ["ID", "Nama", "Jabatan", "Departemen", "Email"]

    for id_karyawan, detail_karyawan in data_karyawan.items():
        if akses_admin:
            row = [id_karyawan, detail_karyawan["Nama"], detail_karyawan["Jabatan"], detail_karyawan["Departemen"], detail_karyawan["Tanggal Masuk"], detail_karyawan["Gaji"], detail_karyawan["Email"], detail_karyawan["Password"]]
        else:
            row = [id_karyawan, detail_karyawan["Nama"], detail_karyawan["Jabatan"], detail_karyawan["Departemen"], detail_karyawan["Email"]]
        table.add_row(row)

    table.align["ID"] = 'c'
    table.align["Nama"] = 'l'
    table.align["Jabatan"] = 'l'
    table.align["Departemen"] = 'l'
    table.align["Email"] = 'l'
    if akses_admin:
        table.align["Tanggal Masuk"] = 'c'
        table.align["Gaji"] = 'l'
        table.align["Password"] = 'l'
    print(table)

def cari_karyawan():
    while True:
        nama_dicari = input("Masukkan nama karyawan yang ingin dicari (ketik 'batal' untuk membatalkan): ").lower()
        if nama_dicari == "batal":
            return
        karyawan_ditemukan = []

        for id_karyawan, detail_karyawan in data_karyawan.items():
            if detail_karyawan["Nama"].lower() == nama_dicari:
                karyawan_ditemukan.append((id_karyawan, detail_karyawan))
        if karyawan_ditemukan:
            tampilkan_data_karyawan({id: detail for id, detail in karyawan_ditemukan}, akses_admin=True)
        else:
            print("Karyawan dengan nama tersebut tidak ditemukan.")

def tampilkan_info_departemen():
    departemen_grup = {} #dict untuk mengelompokkan anggota berdasarkan departemen
    print("Daftar Departemen:")
    for id_karyawan, detail_karyawan in data_karyawan.items():
        nama_departemen = detail_karyawan["Departemen"]
        if nama_departemen not in departemen_grup:
            departemen_grup[nama_departemen] = [] #membuat list baru jika departemen tsb sebelumnya tdk ada
        departemen_grup[nama_departemen].append((id_karyawan, detail_karyawan))

    for nama_departemen, anggota in departemen_grup.items():
        print(f"Informasi Departemen: {nama_departemen}")
        tabel = PrettyTable()
        tabel.field_names = ["ID", "Nama", "Jabatan", "Email"]
        for id_karyawan, detail_karyawan in anggota:
            tabel.add_row([id_karyawan, detail_karyawan["Nama"], detail_karyawan["Jabatan"], detail_karyawan["Email"]])
        print(tabel)
        print(f"Jumlah Anggota: {len(anggota)}")
        print("-" * 30)

def tambah_karyawan():
    while True:
        try:
            tambah_id = input("Masukkan nomor ID karyawan baru (ketik 'batal' untuk membatalkan): ")
            if tambah_id.lower() == "batal":
                return
            tambah_id = int(tambah_id)
            if tambah_id not in data_karyawan:
                break
            else:
                print("ID sudah ada.Masukkan ID yang berbeda.")
        except ValueError:
            print("ID harus berupa angka.")

    nama = input("Masukkan nama karyawan: ")
    jabatan = input("Masukkan jabatan: ")
    depatemen = input("Masukkan departemen: ")
    while True:
        tanggal_masuk = input("Masukkan tanggal masuk (YYYY-MM-DD): ")
        try:
            tanggal_masuk = datetime.datetime.strptime(tanggal_masuk, "%Y-%m-%d").date() # konversi string ke date
            break
        except ValueError:
            print("Format tanggal tidak valid. Gunakan YYYY-MM-DD.")
    while True:  # Loop validasi email
        email = input("Masukkan email: ")
        if not validasi_email(email):  # Panggil fungsi validasi email
            print("Format email tidak valid. Silakan coba lagi.")
        else:
            break  # Keluar dari loop jika email valid
    while True:
        gaji_str = input("Masukkan gaji: ")
        if gaji_str.isdigit():  # Periksa apakah semua karakter adalah digit
            gaji = int(gaji_str)
            break  # Jika ya, keluar dari loop
        else:
            print("Gaji harus berupa angka.")
    password_karyawan = input("Masukkan password: ")

    data_karyawan[tambah_id] = {"ID": tambah_id,"Nama": nama, "Jabatan": jabatan, "Departemen": depatemen, "Tanggal Masuk": tanggal_masuk, "Gaji": gaji, "Email": email, "Password": password_karyawan}
    print(f"{nama} berhasil ditambahkan.")
    tampilkan_data_karyawan(data_karyawan, akses_admin=True)

def validasi_email(email):
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" #regular expression untuk validasi email
    return re.match(regex, email)  #mengembalikan True jika cocok, False jika tidak

def ubah_data_karyawan():
    tampilkan_data_karyawan(data_karyawan, akses_admin=True)
    while True:
        try:
            ubah_id = (input("Masukkan nomor ID karyawan yang ingin diubah (ketik 'batal' untuk membatalkan): "))
            if ubah_id.lower() == "batal":
                return
            ubah_id = int(ubah_id)
            if ubah_id in data_karyawan:
                break #keluar dr while loop
            else:
                print("ID Karyawan tidak ditemukan.")
        except ValueError:
            print("ID harus berupa angka.")

    while True:
        kolom_data = input("Masukkan kolom yang ingin diubah: ").lower()

        for key in data_karyawan[ubah_id]:
            if kolom_data == key.lower():  #case-insensitive
                kolom_data = key
                break
        else:  #jika loop for selesai tanpa menemukan kolom yg sesuai
            print("Kolom tersebut tidak ditemukan dalam data karyawan.")
            continue  #kembali ke baris input kolom

        if kolom_data in data_karyawan[ubah_id]: 
            break  #keluar dr while loop

    while True: 
        if kolom_data == "Email":
            data_baru = input(f"Masukkan {kolom_data} baru: ")
            data_karyawan[ubah_id][kolom_data] = data_baru
            if not validasi_email(data_baru):  #jika tidak sesuai dgn format email
                print("Format email tidak valid. Silakan coba lagi.")
            else:
                break #keluar dari loop setelah email valid
        elif kolom_data == "Tanggal Masuk":
            data_baru = input(f"Masukkan {kolom_data} baru (YYYY-MM-DD): ")
            try:
                data_karyawan[ubah_id][kolom_data] = datetime.datetime.strptime(data_baru, "%Y-%m-%d").date() #validasi format tanggal
                break
            except ValueError:
                print("Format tanggal tidak valid. Gunakan YYYY-MM-DD.")
        else:
            data_baru = input(f"Masukkan {kolom_data} baru: ")
            data_karyawan[ubah_id][kolom_data] = data_baru
            break 

    print("Data berhasil diubah.")
    tampilkan_data_karyawan(data_karyawan, akses_admin=True)

def hapus_karyawan():
    tampilkan_data_karyawan(data_karyawan, akses_admin=True)
    while True:
        try:
            hapus_id = (input("Masukkan nomor ID karyawan yang ingin dihapus (ketik 'batal' untuk membatalkan): "))
            if hapus_id.lower() == "batal":
                return
            hapus_id = int(hapus_id)
            if hapus_id in data_karyawan: 
                konfirmasi = input(f"Apakah Anda yakin ingin menghapus karyawan dengan ID {hapus_id}? (y/n): ")
                if konfirmasi.lower() == "y":
                    del data_karyawan[hapus_id]
                    print(f"Karyawan dengan ID {hapus_id} berhasil dihapus.")
                    tampilkan_data_karyawan(data_karyawan, akses_admin=True)
                    break
                else:
                    print("Penghapusan dibatalkan.")
                    continue 
            else:
                print("Nomor ID tersebut tidak tersedia dalam data.")
        except ValueError:
            print("Input tidak valid. Masukkan angka atau 'batal'.")

def hitung_statistik_gaji(id_karyawan, data_karyawan):
    total_gaji = 0
    gaji_tertinggi = 0
    gaji_terendah = float('inf')  #inisialisasi dengan nilai tak hingga positif agar tersisa nilai terendah yg diinput
    jumlah_karyawan = len(data_karyawan)

    for id_karyawan, detail_karyawan in data_karyawan.items():
        gaji = detail_karyawan["Gaji"]
        total_gaji += gaji
        if gaji > gaji_tertinggi:
            gaji_tertinggi = gaji
        if gaji < gaji_terendah:
            gaji_terendah = gaji

    rata_rata_gaji = round(total_gaji / jumlah_karyawan) if jumlah_karyawan > 0 else 0 #menghasilkan 0 jika tidak ada karyawan
    return total_gaji, rata_rata_gaji, gaji_tertinggi, gaji_terendah

def tampilkan_statistik_gaji(data_karyawan):
    total, rata_rata, tertinggi, terendah = hitung_statistik_gaji(id_karyawan, data_karyawan)
    print("Berikut detail terkait statistik gaji karyawan:")

    tabel = PrettyTable()
    tabel.field_names = ["Statistik", "Nilai"]
    tabel.add_row(["Total Gaji", f"{total}"]) # Format dengan f-string
    tabel.add_row(["Rata-rata Gaji", f"{rata_rata}"])
    tabel.add_row(["Gaji Tertinggi", f"{tertinggi}"])
    tabel.add_row(["Gaji Terendah", f"{terendah}"])

    print(tabel)

#FUNGSI DI MENU KARYAWAN

def tampilkan_data_pribadi(data_karyawan, id_karyawan):
    if id_karyawan not in data_karyawan:
        print("ID karyawan tidak ditemukan.")
        return

    detail_karyawan = data_karyawan[id_karyawan]

    print("Data Pribadi Karyawan:")
    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Jabatan", "Departemen", "Tanggal Masuk", "Gaji", "Email", "Password"]
    table.add_row([id_karyawan, detail_karyawan["Nama"], detail_karyawan["Jabatan"], detail_karyawan["Departemen"], detail_karyawan["Tanggal Masuk"], detail_karyawan["Gaji"], detail_karyawan["Email"], detail_karyawan["Password"]])

    table.align["ID"] = 'c'
    table.align["Nama"] = 'l'
    table.align["Jabatan"] = 'l'
    table.align["Departemen"] = 'l'
    table.align["Tanggal Masuk"] = 'c'
    table.align["Gaji"] = 'c'
    table.align["Email"] = 'l'
    table.align["Password"] = 'l'
    print(table)

def ubah_password(id_karyawan):
    while True:
        password_lama = pwinput.pwinput("Masukkan password lama: ")
        if verifikasi_password(id_karyawan, password_lama):
            break
        else:
            print("Password lama salah.")

    while True:
        password_baru = pwinput.pwinput("Masukkan password baru: ")
        konfirmasi_password_baru = pwinput.pwinput("Konfirmasi password baru: ")
        if password_baru == konfirmasi_password_baru:
            data_karyawan[id_karyawan]["Password"] = password_baru  #menyimpan password baru
            print("Password berhasil diubah.")
            return
        else:
            print("Password baru dan konfirmasi password baru tidak cocok.")

# JALANKAN PROGRAM

keluar_program = False  #menambah variabel untuk menandai apakah user ingin keluar program
while not keluar_program:  #loop utama berjalan selama keluar_program bernilai False
    akses_admin, status_login, id_karyawan = login() #ikut mengembalikan id_karyawan agar id_karyawan bisa dipanggil di luar fungsi

    if status_login:
        while True:
            if akses_admin:
                #menu utama admin
                print("Berikut menu utama (Admin):")
                print("1. Menampilkan data karyawan")
                print("2. Mencari data karyawan")
                print("3. Menampilkan info departemen")
                print("4. Menambah karyawan")
                print("5. Mengubah data karyawan")
                print("6. Menghapus karyawan")
                print("7. Hitung statistik gaji")
                print("8. Logout")
            else:
                #menu utama karyawan
                print("Berikut menu utama (Karyawan):")
                print("1. Menampilkan data pribadi")
                print("2. Menampilkan data karyawan")
                print("3. Menampilkan info departemen")
                print("4. Ubah Password")
                print("5. Logout")

            try:
                pilihan = int(input("Masukkan menu yg ingin dijalankan: "))

                if akses_admin:
                    if pilihan == 1:
                        tampilkan_data_karyawan(data_karyawan, akses_admin=True)
                    elif pilihan == 2:
                        cari_karyawan()
                    elif pilihan == 3:
                        tampilkan_info_departemen()
                    elif pilihan == 4:
                        tambah_karyawan()
                    elif pilihan == 5:
                        ubah_data_karyawan()
                    elif pilihan == 6:
                        hapus_karyawan()
                    elif pilihan == 7:
                        tampilkan_statistik_gaji(data_karyawan)
                    elif pilihan == 8:
                        konfirmasi = input("Apakah Anda yakin ingin logout? (y/n): ")
                        if konfirmasi.lower() == "y":
                            status_login = False
                            print("Berhasil Logout.")
                            break
                        else:
                            print("Logout dibatalkan.")
                    else:
                        print("Pilihan tidak valid.")
                else: #menu untuk karyawan
                    if pilihan == 1:
                        tampilkan_data_pribadi(data_karyawan, id_karyawan)
                    elif pilihan == 2:
                        tampilkan_data_karyawan(data_karyawan, akses_admin=False)
                    elif pilihan == 3:
                        tampilkan_info_departemen()
                    elif pilihan == 4:
                        ubah_password(id_karyawan)
                    elif pilihan == 5:
                        konfirmasi = input("Apakah Anda yakin ingin logout? (y/n): ")
                        if konfirmasi.lower() == "y":
                            status_login = False
                            print("Berhasil Logout.")
                            break
                        else:
                            print("Logout dibatalkan.")
                    else:
                        print("Pilihan tidak valid.")
            except ValueError:
                print("Input tidak valid. Silahkan masukkan angka.")

        if not status_login:  #jika memilih logout
            while True:
                print("Pilih opsi:")
                print("1. Login Ulang")
                print("2. Keluar Program")
                try:
                    pilihan_logout = int(input("Masukkan pilihan: "))

                    if pilihan_logout == 1:
                        break  #kembali ke menu login utama
                    elif pilihan_logout == 2:
                        while True:  
                            konfirmasi = input("Apakah Anda yakin ingin keluar? (y/n): ")
                            if konfirmasi.lower() == "y":
                                print("Program selesai.")
                                exit()  #keluar dari program
                            elif konfirmasi.lower() == "n":
                                break  #kembali ke menu pilihan logout
                            else:
                                print("Pilihan tidak valid. Masukkan 'y' atau 'n'.")
                        break #kq   eluar dari loop pilihan logout
                    else:
                        print("Pilihan tidak valid.")

                except ValueError:
                    print("Input tidak valid. Silahkan masukkan angka.")
                        
    else:
        print("Login gagal. Silahkan coba lagi.")

