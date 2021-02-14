#Nama : Augusta Clarissa Silvy Pascalin
#Universitas Kristen Duta Wacana
#Topik : Penggunaan Variabel, Ekspresi, dan Statement pada Python

#Pak Kenan akan mengoreksi jawaban test para mahasiswanya. Ketentuannya adalah tiap jawaban yang benar akan diberi poin 1. 
#sedangkan jawaban yang salah akan diberi poin -1 dan soal yang tidak dijawab tidak akan diberi poin, alias 0.
#Bantulah Pak Kenan agar dapat mengoreksi jawaban test dengan cepat yaitu membuat program yang dapat menghitung total nilai!

#input : nama mahasiswa, banyaknya soal, jawaban benar, jawaban salah, jumlah soal yang tidak dijawab
#proses : menghitung semua inputan kecuali nama mahasiswa, rumus : (jawaban benar*1+jawaban salah*-1+jumlah soal yang tidak dijawab*0)/total soal *100
#output : jadi dari (banyaknya soal), (nama mahasiswa) mendapat nilai, (total nilai)

namaMhs = str(input("Masukkan nama mahasiswa : "))
totalSoal = int(input("Banyaknya soal : "))
jawabanBenar = int(input("Banyaknya jawaban benar : "))
jawabanSalah = int(input("Banyaknya jawaban salah : "))
tidakDijawab = int(input("Banyaknya soal yang tidak dijawab : "))
totalNilai = (jawabanBenar*1+jawabanSalah*-1+tidakDijawab*0)/totalSoal*100
print("Jadi dari ", totalSoal, "soal", namaMhs, "mendapat nilai", totalNilai)