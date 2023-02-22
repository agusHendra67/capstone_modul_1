# DATA STOK GUDANG
*CRUD project untuk membuat program sederhana tentang data stok gudang*

Program ini merupakan tugas capstone moodul 1 JC Data Science Purwadhika (Online)

Terdapat beberapa menu pada program pada Data Stok Gudang di Toko Hendra's Toserba

**MENU**

1. Tampilkan Data stok barang
2. Tambah Data baru
3. Hapus Data barang
4. Update nama/harga barang atau menambah stok masuk/stok keluar
5. Exit Program

## Contoh tabel data stok

| Kode |Nama|Kategori|Harga beli|Harga Jual|Stok awal|Stok masuk|Stok keluar|Stok akhir|Status|
|------|:--:|:------:|:--------:|:--------:|:-------:|:--------:|:---------:|:--------:|-----:|
| **1** | piring | peralatan dapur |   10000    |   12000    |    100    |     61     |      9      |    162     |     ready    |
| **2** | sendok | peralatan dapur |    3000    |    4000    |    180    |     12     |      0      |    192     |     ready    |
| **3** | garpu  | peralatan dapur |    3000    |    4000    |    180    |     12     |      0      |    192     |     ready    |
| **4** | sabun  | peralatan mandi |    3500    |    4500    |    300    |     60     |      0      |    360     |     ready    |
| **5** | sampo  | peralatan mandi |    5000    |    6000    |    250    |     60     |      0      |    310     |     ready    |
| **6** | kabel  |   kelistrikan   |    4000    |    5000    |    40     |     10     |     50      |     0      | out of stock |


### Deskripsi Data
Berikut merupakan penjelasan data dari setiap kolom pada tabel

|       Kolom       |                                                 Deskripsi                                                                                                              |
|-------------------|:---------------------------------------------------------------------------------------------------------------------:                                                 |
|      **Kode**     | **Kode barang yang menunjukkan ID unik barang yang ditulis dengan tipe integer elemen bilangan asli (n =  1,2,3,4,5)**                                                 |
|      **Nama**     | **Nama dari barang dengan tipe teks**                                                                                                                                  |
|    **Kategori**   | **Kategori barang sesuai dengan kegunaan nya. Contoh : sendok masuk ke kategori peralatan dapur**                                                                      |
|   **Harga beli**  | **Nilai harga beli per unit barang dalam Rupiah**                                                                                                                      |
|   **Harga jual**  | **Nilai harga jual per unit barang dalam Rupiah**                                                                                                                      |
|   **Stok awal**   | **Merupakan banyak nya barang/unit (stok) yang tersedia di gudang sebelum ada barang masuk/keluar di satu bulan/periode bulan tertentu**                               |
|   **Stok masuk**  | **Merupakan banyak nya barang/unit (stok) yang masuk ke gudang yang akan ditambah dengan stok awal di satu bulan/periode bulan tertentu**                              |
|   **Stok keluar** | **Merupakan banyak nya barang/unit (stok) yang keluar dari gudang  di satu bulan/periode bulan tertentu**                                                              |
|   **Stok akhir**  | **Merupakan banyak nya barang/unit (stok) yang tersisa :  stok akhir = stok awal + stok masuk - stok keluar**                                                          |
|     **Status**    | **Menunjukkan ketersediaan dari barang tersebut apakah *ready* atau *out of stock***                                                                                    |
