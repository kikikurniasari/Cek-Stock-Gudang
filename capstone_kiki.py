
# Data 
Menu = ['1. Report Stock Gudang',
        '2. Menambahkan Data Stock Gudang',
        '3. Mengubah Data Stock Gudang',
        '4. Menghapus Data Stock Gudang',
        '5. Exit']

Data_Gudang = [{'Kode_barang' : 'CR01MCA', 'Nama' : 'Madagascar', 'Jenis' : 'Toner', 'Negara' : 'Korea Selatan'}, 
{'Kode_barang' : 'SB01BAW', 'Nama' : 'Biore', 'Jenis' : 'Sunblock', 'Negara' : 'Jepang'},
{'Kode_barang' : 'TN01AVS', 'Nama' : 'Avoskin', 'Jenis' : 'Toner', 'Negara' : 'Indonesia'},
{'Kode_barang' : 'SB01BAW', 'Nama' : 'Biore', 'Jenis' : 'Sunblock', 'Negara' : 'Jepang'}]


#Menu Read data

Format_Menu ='1. Report Seluruh Data\n' '2. Report Data tertentu\n' '3. Kembali Ke Menu Utama'

def Read_Data():
    read = True
    while read != '3':
        print ("\n.........Report Data Stock Gudang.......\n", Format_Menu)                                                             
        read = input("Silakan Pilih Sub Menu Read Data [1-3] : ")
        if read == '1':
            if len(Data_Gudang) != 0 :                                                                      
                print('Daftar Stok Gudang :')
                print('index \t Kode_barang \t Nama \t\t Jenis \t Negara')
                for i in range(len(Data_Gudang)):
                    print('{}\t {} \t {} \t {} \t {}'.format(i,Data_Gudang[i]['Kode_barang'],Data_Gudang[i]['Nama'],Data_Gudang[i]['Jenis'],Data_Gudang[i]['Negara']))
                                                                                                              
            else:                                                                                   
                print('\n****Tidak ada Data Stock yang dimaksud****')   
            continue                                            
        elif read == '2':
            if len(Data_Gudang) != 0 :                                                                      
                std = input("Masukkan Kode_barang : ").upper() 
                print(f"Data Produk dg Kode_barang : {std}")                                              
                for j, i in enumerate(Data_Gudang):                                                                       
                    if i['Kode_barang'] == std:
                        print(f"{j+1}. Kode_barang : {i['Kode_barang']}, Nama : {i['Nama']}, Jenis : {i['Jenis']}, Negara : {i['Negara']}")  
                        break
                else:
                    print("\n****Tidak ada Data Stock yang dimaksud****")                                                       
            else:                                                                                   
                print('\n****Tidak ada Data Stock yang dimaksud****')  
            continue
        elif read == '3':
            Main_Menu() 



# Menu Create 

Format_Create_Menu = '1. Tambah Stock produk \n2. Kembali Ke Menu Utama'

def Create_Data():
    create = True 
    while create != '2':
        print("\n.........Menambah Data Stock Gudang.......\n",Format_Create_Menu)
        create = input('Silakan Pilih Sub Menu Create Data [1-2] : ')
        if create == '1':
            kode_barang = input('Masukkan Kode_barang : ').upper()
            for i in Data_Gudang:
                if i['Kode_barang'] == kode_barang:
                    print("Data Sudah Ada")
                    break
            else:
                nama = input("Masukkan Nama : ").capitalize()
                Jenis = input("Masukkan Jenis : ").capitalize()
                Negara = input("Masukkan Asal_Negara : ").capitalize()
                save = True
                while save:
                    simpan = input("Apakah Data akan disimpan? (Y/N) : ").upper()
                    if simpan == 'Y':
                        data = {'Kode_barang' : kode_barang, 'Nama' : nama, 'Jenis' : Jenis, 'Negara' : Negara}
                        Data_Gudang.append(data)
                        print('Data Tersimpan')
                        save = False
                        break
                    elif simpan == 'N':
                        print("Data Tidak Tersimpan")
                        save = False
                        break

        elif create == '2':
            Main_Menu()


# Menu Update

Format_Update_Menu = "1. Ubah Data Stock Gudang \n2. Kembali Ke Menu Utama"

def Update_Data():
    Update = True 
    while Update != '2':
        print("\n.........Mengubah Data Stock Gudang.......\n",Format_Update_Menu)
        Update = input('Silakan Pilih Sub Menu Update Data [1-2] : ')
        if Update == '1':
            kode_barang = input('Masukkan Kode_barang : ').upper()
            for i in Data_Gudang:
                if i['Kode_barang'] == kode_barang:
                    print(f"Kode_barang : {i['Kode_barang']}, Nama : {i['Nama']}, Jenis : {i['Jenis']}, Negara : {i['Negara']}")
                    askU = True
                    while askU:
                        ask = input("Tekan Y jika ingin lanjut Update data atau N jika ingin cancel Update (Y/N) : ").lower()
                        if ask == 'y':
                            kolom = input("Masukkan Kolom/Keterangan yg ingin di edit : ").capitalize()
                            new_data = input(f"Masukkan {kolom} Baru : ")
                            askU = False
                            save = True
                            while save:
                                simpan = input("Apakah Data akan diUpdate? (Y/N) : ").upper()
                                if simpan == 'Y':
                                    i[kolom] = new_data
                                    print('Data Updated')
                                    save = False
                                    break
                                elif simpan == 'N':
                                    print("Data Tidak TerUpdate")
                                    save = False
                                    break
                            break
                        elif ask == 'n':
                            print("Data Tidak TerUpdate")
                            askU = False
                        else:
                            continue
                    break
                else:
                    continue
            else:
                print("Data Tidak Ada")

        elif Update == '2':
            Main_Menu()


# Menu Delete 

Menu_del = "1. Hapus Data Gudang \n2. Kembali Ke Menu Utama"

def Delete_Data():
    Delete = True 
    while Delete != '2':
        print('\n.........Menghapus Data Stock Gudang.......\n',Menu_del)
        Update = input('Silakan Pilih Sub Menu Hapus Data [1-2] : ')
        if Update == '1':
            Kode_barang = input('Masukkan Kode_barang : ').upper()
            for i in Data_Gudang:
                if i['Kode_barang'] == Kode_barang:
                    Hapus = True
                    while Hapus:
                        Hapus = input("Apakah Data akan diHapus? (Y/N) : ").upper()
                        if Hapus == 'Y':
                            ind = Data_Gudang.index(i)
                            Data_Gudang.pop(ind)
                            print('Data Deleted')
                            Hapus = False
                            break
                        elif Hapus == 'N':
                            print("Data Tidak TerHapus")
                            Hapus = False
                            break
                    break
                else:
                    continue
            else:
                print("Data Tidak Ada")
            continue
        elif Update == '2':
            Main_Menu()

# Main Menu 
def Main_Menu():
    Opsi = 5


    while (Opsi != '5'):
        print("\n==========Data Record Stock Gudang Purwadhika Shop=============\n")
        for i in Menu:
            print(i)
        Opsi = input("Silakan Pilih Main_Menu [1-5] : ")
        if Opsi == '1':
            Read_Data()
        elif Opsi == '2':
            Create_Data()
        elif Opsi == '3':
            Update_Data()
        elif Opsi == '4':
            Delete_Data()
        elif Opsi == '5':
            print('-----Thank You, Have a Nice Day-----')
            quit()
        else:
            print("-----------Pilihan yang anda Masukkan Salah--------")


# Run 
Main_Menu()