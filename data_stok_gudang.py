#import library datetime untuk mendapatkan data tanggal/bulan hari ini
from datetime import datetime

#Data Stok barang hingga saat ini (awal stok di bulan januari)
STOK_BARANG = { "kode"          : [1,2,3,4,5,6],
                "nama"           : ["piring", "sendok", "garpu", "sabun", "sampo", "kabel"],
                "kategori"       : ["peralatan dapur", "peralatan dapur", "peralatan dapur", "peralatan mandi", "peralatan mandi", "kelistrikan"],
                "harga beli"     : [10000, 3000, 3000, 3500, 5000, 4000],
                "harga jual"     : [12000, 4000, 4000, 4500, 6000, 5000],
                "stok awal"      : [100, 180, 180, 300, 250, 40],
                "stok masuk"     : [61,12,12,60,60,10],
                "stok keluar"    : [9,0,0,0,0,50],
                "stok akhir"     : [162, 192, 192, 360, 310, 0],
                "status"         : ["ready", "ready", "ready", "ready", "ready", "out of stock"] 
                                                                    }

#Kamus/Dictionary histori/riwayat data stok barang per bulan di gudang toko Hendra_Toserba, 
#Stok akhir di bulan januari akan menjadi stok awal di bulan februari dst.
#Stok akhir = stok awal + stok masuk - stok keluar
HISTORI_STOK = {"januari"   : { "kode"          : [1,2,3,4,5,6],
                                "nama"           : ["piring", "sendok", "garpu", "sabun", "sampo", "kabel"],
                                "kategori"       : ["peralatan dapur", "peralatan dapur", "peralatan dapur", "peralatan mandi", "peralatan mandi", "kelistrikan"],
                                "harga beli"     : [10000, 3000, 3000, 3500, 5000, 4000],
                                "harga jual"     : [12000, 4000, 4000, 4500, 6000, 5000],
                                "stok awal"      : [100, 180, 180, 300, 250, 40],
                                "stok masuk"     : [40,12,12,60,60,0],
                                "stok keluar"    : [0,0,0,0,0,0],
                                "stok akhir"     : [140, 192, 192, 360, 310, 40],
                                "status"         : ["ready", "ready", "ready", "ready", "ready", "ready"]
                            },

                "februari" : {  "kode"           : [1,2,3,4,5,6],
                                "nama"           : ["Piring", "Sendok", "Garpu", "Sabun", "Sampo", "kabel"],
                                "kategori"       : ["Peralatan dapur", "Peralatan dapur", "Peralatan dapur", "Peralatan mandi", "Peralatan mandi", "Kelistrikan"],
                                "harga beli"     : [10000, 3000, 3000, 3500, 5000, 4000],
                                "harga jual"     : [12000, 4000, 4000, 4500, 6000, 5000],
                                "stok awal"      : [140, 192, 192, 360, 310, 40],
                                "stok masuk"     : [21,0,0,0,0,10],
                                "stok keluar"    : [9,0,0,0,0,50],
                                "stok akhir"     : [152, 192, 192, 360, 310, 0],
                                "status"         : ["ready", "ready", "ready", "ready", "ready", "out of stock"]
                            },

                "maret"    : {  "kode"          : [],
                                "nama"           : [],
                                "kategori"       : [],
                                "harga beli"     : [],
                                "harga jual"     : [],
                                "stok awal"      : [],
                                "stok masuk"     : [],
                                "stok keluar"    : [],
                                "stok akhir"     : [],
                                "status"         : [],
                            },

                "april"    : {  "kode"          : [],
                                "nama"           : [],
                                "kategori"       : [],
                                "harga beli"     : [],
                                "harga jual"     : [],
                                "stok awal"      : [],
                                "stok masuk"     : [],
                                "stok keluar"    : [],
                                "stok akhir"     : [],
                                "status"         : [],
                            },
                
                "mei"      : {  "kode"          : [],
                                "nama"           : [],
                                "kategori"       : [],
                                "harga beli"     : [],
                                "harga jual"     : [],
                                "stok awal"      : [],
                                "stok masuk"     : [],
                                "stok keluar"    : [],
                                "stok akhir"     : [],
                                "status"         : [],
                            },

                "juni"     : {  "kode"          : [],
                                "nama"           : [],
                                "kategori"       : [],
                                "harga beli"     : [],
                                "harga jual"     : [],
                                "stok awal"      : [],
                                "stok masuk"     : [],
                                "stok keluar"    : [],
                                "stok akhir"     : [],
                                "status"         : [],
                            },

                "juli"     : {  "kode"          : [],
                                "nama"           : [],
                                "kategori"       : [],
                                "harga beli"     : [],
                                "harga jual"     : [],
                                "stok awal"      : [],
                                "stok masuk"     : [],
                                "stok keluar"    : [],
                                "stok akhir"     : [],
                                "status"         : [],
                            },

                "agustus"  : {  "kode"          : [],
                                "nama"           : [],
                                "kategori"       : [],
                                "harga beli"     : [],
                                "harga jual"     : [],
                                "stok awal"      : [],
                                "stok masuk"     : [],
                                "stok keluar"    : [],
                                "stok akhir"     : [],
                                "status"         : [],
                            },

                "september" : { "kode"          : [],
                                "nama"           : [],
                                "kategori"       : [],
                                "harga beli"     : [],
                                "harga jual"     : [],
                                "stok awal"      : [],
                                "stok masuk"     : [],
                                "stok keluar"    : [],
                                "stok akhir"     : [],
                                "status"         : [],
                            },

                "oktober"  : {  "kode"          : [],
                                "nama"           : [],
                                "kategori"       : [],
                                "harga beli"     : [],
                                "harga jual"     : [],
                                "stok awal"      : [],
                                "stok masuk"     : [],
                                "stok keluar"    : [],
                                "stok akhir"     : [],
                                "status"         : [],
                            },

                "november" : {  "kode"          : [],
                                "nama"           : [],
                                "kategori"       : [],
                                "harga beli"     : [],
                                "harga jual"     : [],
                                "stok awal"      : [],
                                "stok masuk"     : [],
                                "stok keluar"    : [],
                                "stok akhir"     : [],
                                "status"         : [],
                            },
                
                "desember" : {  "kode"          : [],
                                "nama"           : [],
                                "kategori"       : [],
                                "harga beli"     : [],
                                "harga jual"     : [],
                                "stok awal"      : [],
                                "stok masuk"     : [],
                                "stok keluar"    : [],
                                "stok akhir"     : [],
                                "status"         : [],
                            }
                                                                    }

#Kamus histori/riwayat stok barang yang telah dihapus 
HISTORI_STOK_DELETED = { "kode"           : [],
                         "nama"           : [],
                         "kategori"       : [],
                         "harga beli"     : [],
                         "harga jual"     : [],
                         "stok awal"      : [],
                         "stok masuk"     : [],
                         "stok keluar"    : [],
                         "stok akhir"     : [],
                         "status"         : [] 
                                                                    }

#List nama-nama bulan 
list_nama_bulan = list(HISTORI_STOK.keys())

####DAFTAR FUNGSI####

#1 FUNGSI UNTUK MENAMPILKAN TABEL DATA STOK GUDANG
def tampilkan_tabel(bulan, data_stok):

    print("*"*130)
    print("\n")

    if bulan!=None:
        data_stok = data_stok[bulan.lower().strip()]
    
    jumlah_barang_unik = len(data_stok['kode'])
    print(' Kode  |     Nama\t|     Kategori    | Harga beli | Harga jual | Stok awal | Stok masuk | Stok keluar | Stok akhir |     Status   |')
    for i in range(jumlah_barang_unik) :
        print('{0:^7}|{1:^16}|{2:^17}|{3:^12}|{4:^12}|{5:^11}|{6:^12}|{7:^13}|{8:^12}| {9:^13}|'.format(data_stok['kode'][i], data_stok['nama'][i], data_stok['kategori'][i],
                                                                                               data_stok['harga beli'][i], data_stok['harga jual'][i], data_stok['stok awal'][i],
                                                                                               data_stok['stok masuk'][i], data_stok['stok keluar'][i], data_stok['stok akhir'][i], data_stok['status'][i]))
    
    print("\n")
    print("*"*130)

#2 Fungsi untuk update data stok otomatis ketika sudah memasuki awal bulan baru 
def update_histori_awal_bulan(bulan_hari_ini):
    if len(HISTORI_STOK[bulan_hari_ini]['kode'])==0:
        if bulan_hari_ini == "januari":
            bulan_sebelumnya = "desember"
        else:
            bulan_sebelumnya = list_nama_bulan[list_nama_bulan.index(bulan_hari_ini)-1]

        HISTORI_STOK[bulan_hari_ini]['kode'] = HISTORI_STOK[bulan_sebelumnya]['kode']
        HISTORI_STOK[bulan_hari_ini]['nama'] = HISTORI_STOK[bulan_sebelumnya]['nama']
        HISTORI_STOK[bulan_hari_ini]['kategori'] = HISTORI_STOK[bulan_sebelumnya]['kategori']
        HISTORI_STOK[bulan_hari_ini]['harga beli'] = HISTORI_STOK[bulan_sebelumnya]['harga beli']
        HISTORI_STOK[bulan_hari_ini]['harga jual'] = HISTORI_STOK[bulan_sebelumnya]['harga jual']
        HISTORI_STOK[bulan_hari_ini]['stok awal'] = HISTORI_STOK[bulan_sebelumnya]['stok akhir']
        HISTORI_STOK[bulan_hari_ini]['stok akhir'] = HISTORI_STOK[bulan_hari_ini]['stok awal']
        HISTORI_STOK[bulan_hari_ini]['stok masuk'] = [0]*len(HISTORI_STOK[bulan_sebelumnya]['stok masuk'])
        HISTORI_STOK[bulan_hari_ini]['stok keluar'] = [0]*len(HISTORI_STOK[bulan_sebelumnya]['stok keluar'])
        HISTORI_STOK[bulan_hari_ini]['status'] = HISTORI_STOK[bulan_sebelumnya]['status']

#3 Fungsi untuk exit/keluar dari mode input variabel
def exit_input(pilihan):
    exit_verification = False 
    if pilihan.replace(" ", "").lower() == "exit":
        exit_verification = True
    return exit_verification

#4 Fungsi untuk mengambil satu record berdasarkan masukkan user
def get_record_from_kode(kode, data_stok):
    #index baris dari kode barang yang yang akan dihapus
    index_kode_barang = data_stok['kode'].index(int(kode))

    #ambil record yang akan diupdate sesuai index baris kode barang
    record = {key : [value[i]] for key,value in data_stok.items() for i in range(len(data_stok['kode'])) if i==index_kode_barang}
    
    return index_kode_barang, record

#Sistem akan mengecek dulu apakah sudah memasuki bulan baru, jika sudah, maka tabel bulan ini akan di update
bulan_hari_ini = list_nama_bulan[int((datetime.now()).strftime("%m")[1])-1]
update_histori_awal_bulan(bulan_hari_ini)


#######################################  MASUK KE MENU UTAMA #################################################################
while True :
    pilihanMenu = input('''
            SELAMAT DATANG DI DATA STOK GUDANG BARANG DI HENDRA'S TOSERBA

            List Menu :
            1. Menampilkan tabel data stok barang
            2. Menambah barang baru
            3. Menghapus barang
            4. Update nama/harga barang atau menambah stok masuk/stok keluar
            5. Exit Program

            Masukkan angka Menu yang ingin dijalankan : ''')
    print("-"*60)

    #######################################  MASUK KE MENU 1) TAMPILKAN DATA ###################################
    if(pilihanMenu == '1') :
        while True :
            pilihan_sub_menu = input(''' 
                    ----------MENU TAMPILKAN DATA-------------
                    -----pilih salah satu jenis tampilan------

                    1. Tampilkan seluruh data (existing)
                    2. Tampilkan 1 baris data stok sesuai kode yang diinginkan
                    3. Tampilkan riwayat/histori seluruh data barang yang telah dihapus
                    4. Kembali ke Menu Utama
            
                    "Masukkan angka subMenu yang ingin dijalankan :   ''')
            print("-"*60)
 
            if pilihan_sub_menu == "1" :
                while True:
                    pilihanBulan = input(''' 
                        -----------------------SUB MENU TAMPILKAN SELURUH DATA-----------------------------
                        ------Tampilkan seluruh data stok berdasarkan bulan atau periode beberapa bulan----

                        1. Data Stok barang saat ini (hingga bulan sekarang)
                        2. Riwayat/Histori Data Stok barang per bulan
                        3. Riwayat/Histori Data Stok barang periode beberapa bulan
                        4. Kembali ke subMenu sebelumnya
                
                        "Masukkan angka subMenu yang ingin dijalankan :   ''')
                    print("-"*60)
                    print("\n")

                    if(pilihanBulan == "1"):

                        input_bulan = None #jika user ingin melihat sata stok gudang hingga sekarang (hari/bulan ini) masukkan bulan nya None
                        print('\t\tTabel stok barang di gudang dari bulan awal (januari) sampai saat ini ({})\t\t\n'.format(bulan_hari_ini))
                        tampilkan_tabel(input_bulan, STOK_BARANG)

                
                    elif(pilihanBulan == "2"):

                        while True:
                            print("---ketikkan exit untuk keluar---")
                            print("\n")
                            input_bulan = input("Masukkan nama bulan : ").strip().lower()

                            #cek dulu apakah user ingi exit/keluar
                            is_exit = exit_input(input_bulan)
                            if is_exit==True:
                                break
                            
                            if (input_bulan in list_nama_bulan) :
                                if (len(HISTORI_STOK[input_bulan]['kode']) == 0):
                                    print("Belum ada data histori bulan {}".format(input_bulan))
                                else:
                                    break
                            else:
                                print("Masukkan salah, silahkan input nama bulan")
                        
                        print("\n")
                        print('\t\tTabel histori stok barang di gudang bulan :  {}\t\t\n'.format(input_bulan))
                        tampilkan_tabel(input_bulan, HISTORI_STOK)

                    
                    elif(pilihanBulan == "3"):
                        while True: 
                            print("Masukkan periode bulan yang diinginkan dalam format bulan_awal-bulan_akhir.\n")
                            print("Contoh : Januari-Maret \n")
                            print("---ketikkan exit untuk keluar---")
                            print("\n")

                            while True:
                                input_bulan = input("Masukkan periode bulan : ")
                                input_bulan = input_bulan.strip().lower()

                                #cek dulu apakah user ingi exit/keluar
                                is_exit = exit_input(input_bulan)
                                if is_exit==True:
                                    break

                                periode = input_bulan.lower().strip().split("-")

                                if (len(periode)==2) and (periode[0] in list_nama_bulan) and (periode[1] in list_nama_bulan) :
                                    if (len(HISTORI_STOK[periode[0]]['kode'])==0):
                                        print("Belum ada data histori pada bulan awal : {}".format(periode[0]))
                                    elif (len(HISTORI_STOK[periode[1]]['kode'])==0):
                                        print("Belum ada data histori pada bulan akhir : {}".format(periode[1]))
                                    else :
                                        break
                                else :
                                    print("input salah, masukkan dalam format bulan_awal-bulan_akhir")

                            #keluar, jika user memasukkan exit
                            if is_exit==True:
                                break

                            #nomor bulan awal dan bulan akhir
                            nomor_bulan_awal = list_nama_bulan.index(periode[0])
                            nomor_bulan_akhir = list_nama_bulan.index(periode[1])

                            #membuat list of list dari stok masuk dan stok keluar dari periode bulan awal sampai bulan akhir
                            list_of_list_stok_masuk = [HISTORI_STOK[bulan]['stok masuk'] for bulan in [list_nama_bulan[i] for i in range(nomor_bulan_awal,nomor_bulan_akhir+1)]]
                            list_of_list_stok_keluar = [HISTORI_STOK[bulan]['stok keluar'] for bulan in [list_nama_bulan[i] for i in range(nomor_bulan_awal,nomor_bulan_akhir+1)]]
                                
                            #jumlahkan semua stok masuk dan stok keluar (akumulasi) setiap barang dari bulan awal sampai bulan akhir
                            akumulasi_stok_masuk = list(map(sum, zip(*list_of_list_stok_masuk)))
                            akumulasi_stok_keluar = list(map(sum, zip(*list_of_list_stok_keluar)))

                            #pembaruan status untuk periode bulan tertentu
                            new_status = [("ready" if stok_akhir > 0 else "out of stock") for stok_akhir in HISTORI_STOK[periode[1]]['stok akhir']]

                            #Buat tabel histori baru dengan akumulasi stok masuk dan keluar periode input_bulan (bulan awal-akhir)
                            HISTORI_STOK_PERIODE_BULAN = {input_bulan : {   "kode"          : HISTORI_STOK[periode[1]]['kode'],
                                                                            "nama"          : HISTORI_STOK[periode[1]]['nama'],
                                                                            "kategori"      : HISTORI_STOK[periode[1]]['kategori'],
                                                                            "harga beli"    : HISTORI_STOK[periode[1]]['harga beli'],
                                                                            "harga jual"    : HISTORI_STOK[periode[1]]['harga jual'],
                                                                            "stok awal"     : HISTORI_STOK[periode[0]]['stok awal'],
                                                                            "stok masuk"    : akumulasi_stok_masuk,
                                                                            "stok keluar"   : akumulasi_stok_keluar,
                                                                            "stok akhir"    : HISTORI_STOK[periode[1]]['stok akhir'],
                                                                            "status"        : new_status
                                                                                                                        }}
                            #tampilkan tabel
                            print("\n")
                            print('\t\tTabel histori stok barang di gudang bulan :  {}\t\t\n'.format(input_bulan))
                            tampilkan_tabel(input_bulan, HISTORI_STOK_PERIODE_BULAN)
                    

                    elif(pilihanBulan == "4"):
                        break
        
            elif pilihan_sub_menu == "2":
                while True :
                    print("---ketikkan exit untuk keluar---")
                    print("\n")
                    while True :   
                        pilihan_kode = input("Masukkan kode barang yang ingin ditampilkan : ")

                        #cek dulu apakah user ingi exit/keluar
                        is_exit = exit_input(pilihan_kode)
                        if is_exit==True:
                            break

                        if (pilihan_kode.replace(" ","").isdigit()) and (int(pilihan_kode) in STOK_BARANG['kode']):
                            #index baris dari kode barang yang diinput
                            index_kode_barang = STOK_BARANG['kode'].index(int(pilihan_kode))
                            record_to_show = {key : [value[i]] for key,value in STOK_BARANG.items() for i in range(len(STOK_BARANG['kode'])) if i==index_kode_barang}
                            break
                        elif (pilihan_kode.strip().isdigit()) and (int(pilihan_kode) not in STOK_BARANG['kode']):
                            print("kode barang tidak ditemukkan, coba lagi.")
                        else:
                            print("\tMasukkan salah, kode barang harus berupa bilangan asli bulat positif (n= 1,2,3,4,5,.. dst)")
                
                    if is_exit==True:
                        break

                    print("\n")
                    print("\t\tData barang dengan kode : {}".format(pilihan_kode))
                    tampilkan_tabel(None, record_to_show)
        
            elif pilihan_sub_menu == "3":
                print("\n")
                print("Berikut adalah tabel riwayat/histori dari data barang yang telah dihapus")
                tampilkan_tabel(None, HISTORI_STOK_DELETED)

            elif pilihan_sub_menu == "4" :
                break

    #######################################  MASUK KE MENU 2) TAMBAHKAN DATA ###################################
    elif(pilihanMenu == '2') :
        
        while True :
            addition = {key : [] for key in STOK_BARANG.keys()}
            while True:
                tampilkan_tabel(None, STOK_BARANG)
                print("\n")
                print("---SILAHKAN ISI DATA BARANG BARU--- ")
                print("---ketikkan exit jika ingin kembali ke Menu Utama--- ")
                print("\n")
                
                #1
                #Input nilai kode barang
                while True:
                    kode = input("--> Masukkan Kode Barang : ")

                    #cek dulu apakah user meminta exit/keluar dari mode input
                    is_exit = exit_input(kode)
                    if is_exit==True:
                        break

                    if kode.replace(" ","").isdigit():
                        if int(kode) in STOK_BARANG['kode'] :
                            print("\tkode barang sudah digunakan, pilih nomor kode yang berbeda")
                        elif int(kode) in addition['kode'] :
                            print("\tkode barang sudah ada di daftar barang yang akan ditambah")
                        elif int(kode) != 0:
                            break
                    else:
                        print("\tMasukkan salah, kode barang harus berupa bilangan asli (n= 1,2,3,4,5,.. dst)")

                if is_exit==True:
                    break

                #append kode
                addition['kode'].append(int(kode.replace(" ","")))

                #2
                #Input nama barang
                while True:
                    nama = input("--> Masukkan Nama Barang : ")

                    #cek dulu apakah user meminta exit/keluar dari mode input
                    is_exit = exit_input(nama)
                    if is_exit==True:
                        break

                    if nama.replace(" ","").isdigit():
                        print("\tMasukkan salah, tidak boleh angka semua")
                    elif nama.replace(" ", "").isalnum():
                        if nama.strip().lower() in STOK_BARANG['nama'] :
                            print("\tbarang ini sudah ada di tabel data stok gudang")
                        elif nama.strip().lower() in addition['nama'] :
                            print("\tbarang sudah ada di daftar barang yang akan ditambah")
                        else:
                            break
                    else:
                        print("\tMasukkan salah, masukkan harus berupa teks")

                if is_exit==True:
                        break

                #append nama
                addition['nama'].append(nama.strip().lower())

                #3
                #Inputkategori
                while True:
                    kategori = input("--> Masukkan Kategori Barang : ")

                    #cek dulu jika user ingin exit/keluar
                    is_exit = exit_input(kategori)
                    if is_exit==True:
                        break

                    if kategori.replace(" ","").isalpha():
                        break
                    else:
                        print("\tMasukkan salah, harus berupa teks")
                
                if is_exit==True:
                    break

                #Tambah kategori
                addition['kategori'].append(kategori.strip().lower())

                #4
                #Harga Beli
                while True:
                    harga_beli = input("--> Masukkan Harga Beli Barang : ")

                    #cek dulu jika user ingin exit/keluar
                    is_exit = exit_input(harga_beli)
                    if is_exit==True:
                        break

                    if harga_beli.replace(" ","").isdigit():
                        break
                    else:
                        print("\tMasukkan salah, harus berupa bilangan asli (n=1,2,3,4,5,...) ")

                if is_exit==True:
                    break

                #Tambah harga beli
                addition['harga beli'].append(int(harga_beli.replace(" ","")))

                
                #5
                #Harga Jual
                while True:
                    harga_jual = input("--> Masukkan Harga Jual Barang : ")

                    #cek dulu jika user ingin exit/keluar
                    is_exit = exit_input(harga_jual)
                    if is_exit==True:
                        break

                    if harga_jual.replace(" ","").isdigit():
                        break
                    else:
                        print("\tMasukkan salah, harus berupa bilangan asli (n=1,2,3,4,5,...) ")

                if is_exit==True:
                    break

                #Tambah harga jual
                addition['harga jual'].append(int(harga_jual.replace(" ","")))

                #6
                #stok awal
                while True:
                    stok_awal = input("--> Masukkan Stok Awal Barang : ")

                    #cek dulu jika user ingin exit/keluar
                    is_exit = exit_input(stok_awal)
                    if is_exit==True:
                        break

                    if stok_awal.replace(" ","").isdigit():
                        break
                    else:
                        print("\tMasukkan salah, harus berupa bilangan asli (n=1,2,3,4,5,...) ")

                if is_exit==True:
                    break

                #7
                # #Tambah stok awal
                addition['stok awal'].append(int(stok_awal.replace(" ","")))

                #8
                #Tambah stok akhir --> stok awal = stok akhir untuk barang yang baru dimasukkan
                addition['stok akhir'].append(int(stok_awal.replace(" ","")))

                #9
                #Stok masuk, keluar sama dengan 0, karena asumsinya barang yang baru ditambahkan belum ada barang masuk/keluar, hanya ada stok awal
                addition['stok masuk'].append(0)
                addition['stok keluar'].append(0)

                #10
                #Update status
                if int(stok_awal) > 0 :
                    addition['status'].append("ready")
                else:
                    addition['status'].append("out of stock")

                #Tampilkan 
                print("\n")
                print("\t\t\t Daftar barang yang akan ditambahkan ke tabel data stok gudang")
                print("\n")
                tampilkan_tabel(None, addition)

                #Verifikasi apa data yang dimasukkan sudah benar? jika belum maka pilih "No" -- > Masukkan ulang
                while True :
                    verifikasi = input("Apakah anda yakin untuk disimpan ke dalam tabel? (yes/no)")
                    if verifikasi.replace(" ", "").lower() in ['yes', 'no']:
                        break

                if verifikasi.strip().lower() == "yes":
                    print("mau")
                    for key, value in addition.items():
                        STOK_BARANG[key].extend(value)
                        HISTORI_STOK[bulan_hari_ini][key].extend(value)
                    print("\n")
                    tampilkan_tabel(None, STOK_BARANG)
                    break
                elif verifikasi.strip().lower() == "no":
                    #Clear isi dari record temporary "addition" jika user memilih no --> Input Ulang
                    addition = {key : [] for key in STOK_BARANG.keys()}
                    continue
            #kELUAR jika user memasukkan exit
            if is_exit==True:
                break

            #Verifikasi apakah akan menambah barang lagi atau tidak
            while True:
                verifikasi_2 = input("Apa anda ingin menambahkan barang lagi? (yes/no)")
                if verifikasi_2.replace(" ", "").lower() in ['yes', 'no'] :
                    break

            if verifikasi_2.replace(" ", "").lower() == "yes":
                continue
            elif verifikasi_2.replace(" ", "").lower() == "no" :
                break

    #######################################  MASUK KE MENU 3) HAPUS DATA ###################################
    elif(pilihanMenu == '3') :
        while True:
            print('\t\tTabel stok barang di gudang dari bulan awal (januari) sampai saat ini ({})\t\t\n'.format(bulan_hari_ini))
            tampilkan_tabel(None, STOK_BARANG)
            while True:
                print("\n")
                print("----------------MENU HAPUS DATA--------------------- ")
                print("---ketikkan exit jika ingin kembali ke Menu Utama--- ")
                print("\n")
                kode_to_delete = input("Masukkan kode barang yang ingin dihapus : ")

                #cek dulu apakah user meminta exit/keluar dari mode input
                is_exit = exit_input(kode_to_delete)
                if is_exit==True:
                        break

                if kode_to_delete.replace(" ","").isdigit() and int(kode_to_delete) in STOK_BARANG['kode']:
                    kode_to_delete = int(kode_to_delete)

                    #ambli satu record data berdasarkan kode yang dimasukkan
                    index_kode_barang, record_to_delete = get_record_from_kode(kode_to_delete, STOK_BARANG)
                    break
                else :
                    print("kode barang tidak ditemukkan, coba lagi.")
                    print("\n")

            if is_exit==True:
                break

            print("Berikut data yang akan dihapus")
            tampilkan_tabel(None, record_to_delete)

            while True:
                verifikasi_2 = input("Apakah anda yakin untuk menghapus data di atas?(yes/no)")
                verifikasi_2 = verifikasi_2.replace(" ","").lower()

                if verifikasi_2 == "yes":
                    for key,value in record_to_delete.items():
                        for val in value:
                            STOK_BARANG[key].remove(val)

                            #simpan record yang dihapus ke tabel HISTORI_STOK_DELETED
                            #note : record yang dihapus yang disimpan adalah stok total dari awal barang masuk, sampai dihapus atau tidak disimpan histori per bulan nya
                            HISTORI_STOK_DELETED[key].extend(value)

                            print("\n")
                            print("Data stok barang berhasil dihapus")
                            print("\n")
                            print("Berikut tabel yang baru per hari/bulan ini setelah dihapus")
                            tampilkan_tabel(None, STOK_BARANG)
                            #clear record_to_delete, user akan memasukkan kembali daftar barang yang akan dihapus
                    break
                elif verifikasi_2 == "no" :
                    print("\n")
                    break

    #######################################  MASUK KE MENU 4) UPDATE DATA ###################################
    elif(pilihanMenu == '4') :
        while True:
            print("\t\t Data stok di gudang sampai saat ini")
            tampilkan_tabel(None, STOK_BARANG)
            while True:
                print("----------------MENU UPDATE DATA--------------------- ")
                print("---ketikkan exit jika ingin kembali ke Menu Utama--- ")
                print("\n")

                #Masukkan kode yang diinginkan
                pilihan_kode = input('''--> Masukkan kode barang yang akan di update :  ''')

                #cek dulu apakah user meminta exit/keluar dari mode input
                is_exit = exit_input(pilihan_kode)
                if is_exit==True:
                    break

                if pilihan_kode.replace(" ","").isdigit() and int(pilihan_kode) in STOK_BARANG['kode']:
                    pilihan_kode = int(pilihan_kode)

                    #ambil satu record data berdasarkan kode yang dimasukkan
                    index_kode_barang, record_to_update = get_record_from_kode(pilihan_kode, STOK_BARANG)
                    break
                else :
                    print("kode barang tidak ditemukkan, coba lagi.")
                    print("\n")

            if is_exit==True:
                break
            
            print("\n")
            print("\t\tBaris data barang yang akan di update\n")
            tampilkan_tabel(None, record_to_update)

            while True :
                print("""
                Catatan : i) untuk stok masuk dan stok keluar tidak bisa diubah, tapi hanya bisa ditambah
                         ii) kolom stok awal TIDAK BISA DI UBAH NILAINYA 
                        iii) kolom stok akhir dan status akan terupdate otomatis ketika menambah stok masuk/keluar 
                        
                ----------------KETIKKAN exit jika ingin keluar atau mengubah index-------------------------------""")

                print("\n")

                while True:
                    pilihan_kolom = input("--> Masukkan nama kolom yang akan di ubah : ")

                    #cek dulu apakah user meminta exit/keluar dari mode input
                    is_exit = exit_input(pilihan_kolom)
                    if is_exit==True:
                        break

                    pilihan_kolom = pilihan_kolom.strip().lower()
                    
                    if (pilihan_kolom in STOK_BARANG.keys()):
                        if pilihan_kolom in ["index", "kode", "status", "stok awal", 'stok akhir']:
                            print("{} barang tidak bisa di ubah, masukkan kolom lain".format(pilihan_kolom))
                        elif pilihan_kolom in ['stok masuk', 'stok keluar']:
                            while True:
                                while True : 
                                    add_value = input("\t\tMasukkan angka tambahan {} : ".format(pilihan_kolom))
                                    add_value = add_value.replace(" ","")

                                    #cek dulu apakah user meminta exit/keluar dari mode input
                                    is_exit = exit_input(add_value)
                                    if is_exit==True:
                                        break

                                    #JIKA PILIHAN KOLOM STOK KELUAR --->  stok keluar tidak boleh lebih dari stok akhir + tambahan stok masuk
                                    if add_value.isdigit() and pilihan_kolom == "stok keluar" :
                                        stok_tersedia = STOK_BARANG['stok akhir'][index_kode_barang]
                                        if int(add_value) > stok_tersedia :
                                            print("Nilai tambahan stok akhir sebanyak {} melebihi kapasitas stok yang tersedia yaitu {}".format(add_value, stok_tersedia))
                                            continue
                                        elif int(add_value) <= stok_tersedia:
                                            break
                                    #Jika pilihan nya stok masuk langsung keluar dari while input
                                    elif add_value.isdigit() and pilihan_kolom == "stok masuk": 
                                        break
                                    else :
                                        print("Masukkan salah, harus berupa angka bulat asli (n=1,2,3,4,5,6...)")

                                #cek dulu apakah user meminta exit/keluar dari mode input
                                is_exit = exit_input(add_value)
                                if is_exit==True:
                                    break

                                while True :
                                    print("\n")
                                    verifikasi = input("{} akan ditambah sebanyak {}, apa akan disimpan? (yes/no)".format(pilihan_kolom, add_value))
                                    verifikasi = verifikasi.replace(" ","").lower()

                                    #cek dulu apakah user meminta exit/keluar dari mode input
                                    is_exit = exit_input(verifikasi)
                                    if is_exit==True:
                                        break

                                    if verifikasi == "yes":
                                        add_value = int(add_value)
                                        #tambahan nilai akan ditambah dulu dengan stok masuk/keluar di tabel awal
                                        record_to_update[pilihan_kolom][0] += add_value

                                        #MASUKKAN KE DATA STOK_BARANG DAN HISTORI_STOK
                                        STOK_BARANG[pilihan_kolom][index_kode_barang] = record_to_update[pilihan_kolom][0]
                                        HISTORI_STOK[bulan_hari_ini][pilihan_kolom][index_kode_barang] = record_to_update[pilihan_kolom][0]

                                        #UPDATE JUGA NILAI STOK AKHIRNYA
                                        STOK_BARANG['stok akhir'][index_kode_barang] = STOK_BARANG['stok awal'][index_kode_barang] + STOK_BARANG['stok masuk'][index_kode_barang] - STOK_BARANG['stok keluar'][index_kode_barang]
                                        HISTORI_STOK[bulan_hari_ini]['stok akhir'][index_kode_barang] = HISTORI_STOK[bulan_hari_ini]['stok awal'][index_kode_barang] + HISTORI_STOK[bulan_hari_ini]['stok masuk'][index_kode_barang] - HISTORI_STOK[bulan_hari_ini]['stok keluar'][index_kode_barang]

                                        #UPDATE JUGA STATUS NYA (READY ATAU OUT OF STOCK)
                                        if STOK_BARANG['stok akhir'][index_kode_barang] > 0:
                                            STOK_BARANG['status'][index_kode_barang] = "ready"
                                        else :
                                            STOK_BARANG['status'][index_kode_barang] = "out of stock"

                                        if HISTORI_STOK[bulan_hari_ini]['stok akhir'][index_kode_barang] > 0:
                                            HISTORI_STOK[bulan_hari_ini]['status'][index_kode_barang] = "ready"
                                        else :
                                            HISTORI_STOK[bulan_hari_ini]['status'][index_kode_barang] = "out of stock"

                                        #Notofikasi berhasil di update, lalu tampilkan tabel terbaru
                                        print("Yey! data {} berhasil diubah".format(pilihan_kolom))
                                        print("Berikut tampilan tabel terbaru per hari ini setelah di update :")
                                        tampilkan_tabel(None, STOK_BARANG)
                                        #is exit ini untuk keluar di while verifikasi
                                        is_exit = True
                                        break
                                    elif verifikasi == "no" :
                                        break
                                    else:
                                        print("masukkan salah, pilih yes/no")

                                if is_exit==True:
                                    break
                        else: #harga beli, harga jual, nama dan kategori
                            while True:
                                while True:
                                    new_value = input("Masukkan nilai baru kolom {} : ".format(pilihan_kolom))

                                    #cek dulu apakah user meminta exit/keluar dari mode input
                                    is_exit = exit_input(new_value)
                                    if is_exit==True:
                                        break
                            
                                    if (pilihan_kolom in ['harga beli', 'harga jual']) and (new_value.replace(" ", "").isdigit()) :
                                        new_value = int(new_value.replace(" ", ""))
                                        break
                                    elif (pilihan_kolom in ['nama', 'kategori']) and (new_value.replace(" ","").isalpha()):
                                        new_value = new_value.strip().lower()
                                        break
                                    else :
                                        print("masukkan salah, i) jika ingin update nama, kategori harus berupa teks)")
                                        print("              (ii) Jika mengubah harga jual, harga beli harus berupa angka")
                                
                                if is_exit==True:
                                        break

                                print("\n")
                                while True:
                                    verifikasi = input("{} akan diubah dari {} menjadi {}, apa akan disimpan? (yes/no)".format(pilihan_kolom,record_to_update[pilihan_kolom][0], new_value ))
                                    verifikasi = verifikasi.replace(" ","").lower()
                                    if verifikasi in ["yes", "no"]:
                                        break

                                #cek dulu apakah user meminta exit/keluar dari mode input
                                is_exit = exit_input(verifikasi)
                                if is_exit==True:
                                    break

                                if verifikasi == "yes":
                                    record_to_update[pilihan_kolom][0] = new_value

                                    STOK_BARANG[pilihan_kolom][index_kode_barang] = record_to_update[pilihan_kolom][0]
                                    HISTORI_STOK[bulan_hari_ini][pilihan_kolom][index_kode_barang] = record_to_update[pilihan_kolom][0]

                                    print("Yey! data {} berhasil diubah".format(pilihan_kolom))
                                    print("Berikut tampilan tabel terbaru per hari ini setelah di update :")
                                    tampilkan_tabel(None, STOK_BARANG)
                                    break
                                elif verifikasi == "no" :
                                    continue
       
                        if is_exit==True:
                            break 
                        
                        while True:
                            print("\n")
                            verifikasi_2 = input("Apakah akan update kolom lain? (yes/no)")
                            verifikasi_2 = verifikasi_2.strip().lower()
                            if verifikasi_2 in ['yes', 'no']:
                                break
                            print("\n")

                        
                        if verifikasi_2 == "yes":
                            #muat ulang record_to_update terbaru Lalu Tampilkan kembali (ini masih di kode barang yang sama karen pilihan nya "yes")
                            index_kode_barang, record_to_update = get_record_from_kode(pilihan_kode, STOK_BARANG)
                            tampilkan_tabel(None, record_to_update)
                            continue
                        elif verifikasi_2 == "no":
                            break
                    else :
                        print("Kolom tidak ditemukan")
                
                #keluar jika input exit
                if is_exit==True:
                        break
                
                #kembali ke menu update data, akrena verifikasi_2 ada dua while, jadi ketika user memasukkan no, harus keluar dari while pertama, lalu keluar while kedua, agar kembali ke menu masukkan kode barang
                if verifikasi_2=="no":
                    break

    elif(pilihanMenu == '5') :
        break