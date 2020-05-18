daftar = [['Belajar Pyton Pemula', 40000], ['Belajar PHP Pemula', 40000], ["Belajar C++ Pemula", 39000],
["Belajar C# Pemula", 45000],["HTML 5", 38000],["CSS 3", 35000],["Networking", 40000],["Robotika", 41000],
["Android 2020", 80000],["DataBase Edisi 4", 75600],["Belajar Java Pemula", 40000],["Kecerdasan Buatan", 50000],
["TCP/IP", 34000],["Citra Digita", 30000],["Software Engineering", 40000],["Javascript Pemula", 38000],
["Python OOP", 45000],["Dasar-Dasar Pembuatan Website", 45000],["Aplikasi Android", 43000],
["Belajar Android Pemula", 45000],["Troubleshooting", 37500],["Kamus Saku Komputer", 15000],]

def daftar_buku(): 
    print("Daftar Buku dan Harga")
    print("----------------------")
    i = 1 
    for item in daftar: 
        print(str(i) + " . " + item[0] + " => " + str(item[1])) 
        i += 1 
    print("------------------------------------")
    return 

#pemangilan fungsi
print("Selamat Datang di Toko Buku Orbit")
pilih1=input("Masukan Pilihan Anda (1.Pembelian)(2.Admin) :")

####################### Bagian Pembelian ########################
if pilih1=="1":
    print("Selamat Datang di Aplikasi Pembelian Buku Orbit")
    print("-------------------------------------------")

    beli1=input("Apakah Anda Ingin Melakukan Pembelian :")
    
    if beli1 in["ya","Ya","YA"]:
        print("Buku Yang Tersedia :")
    
    ###################################
    daftar_buku() 
    beli = "" 
    pilih = [] 
    while beli != "0":
        beli = input("Pilih Buku yang di Beli : ") 
        print("Selesai [0]")
       
        if beli != "0": 
            pilih.append(int(beli)-1)    
                   
        no = 1 
        print("Pembelian : ") 
        total = 0 
        #bayar=0
        bayaran=""
        for pilihan in pilih: 
            print("Buku yang dibeli ke-" + str( no) + " = " + daftar[pilihan][0] + " Harga Rp. " + str(daftar[pilihan][1])) 
            no += 1 
            total = total + daftar[pilihan][1] 
        
        print("Total pembayaran = " + str(total))

        for bayar in beli:
            if bayar == "0":
                bayaran = input("Pembayaran = ")
                kembalian= int(bayaran)-total
                print("Kembalian :",kembalian )
        print("----------------------------------")
        print("----------------------------------")

###################### Bagian Admin ############################
elif pilih1=="2":
    print("Selamat Datang Admin Pada Aplikasi Toko Buku Orbit")
    print("---------------------------------------------------")
    print("Stok Buku Toko Orbit")
    daftar_buku()
    print("Tekan 1 untuk <Menambah>, Tekan 2 untuk <Mengubah>, Tekan 3 untuk <Menghapus>")
    pilih2=input("Masukan Pilihan Anda :")
    tambah=""
    ubah=""
    hapus=""
    a=""
    if pilih2== "1":
        while tambah !="selesai":
            tambah=input("Buku Yang  Ditambah :")
            daftar.extend([[tambah]])
            print("Telah ditambah",daftar)
           
    
    elif pilih2=="2":
        while ubah !="selesai":
            ubah =input("Nomor Buku yang Diubah :")
            jdl=input("Judul :")
            daftar[int(ubah)]=(jdl)
            print("Telah diubah :",daftar)
            

    elif pilih2=="3":
        while hapus !="selesai":
            daftar_buku()
            hapus=input("Buku yang Dihapus :")
            daftar.pop(int(hapus))
            print("Buku yang telah dihapus :",daftar)
               
else:
    print("Maaf,Format yang Anda Masukan Salah!")
    
#@http://rofilde.web.id/post/88
