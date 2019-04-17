import csv

prasarana = [
    ('1', 'Laboratorium Multimedia', '135-Ruang Praktek Siswa', '12.0', '8.0', 'Milik', 'Baik'),
    ('2', 'Laboratorium Komputer', '301-Ruang Praktek Siswa', '14.0', '8.0', 'Milik', 'Baik'),
    ('3', 'Kamar Mandi/WC Guru Laki-laki', 'Ruang Penunjang', '2.0', '1.0', 'Milik', 'Baik'),
    ('4', 'Ruang Teori/Kelas', '132-Ruang Teori', '9.0', '8.0', 'Milik', 'Baik'),
    ('5', 'Ruang Teori/Kelas', '126-Ruang Teori', '9.0', '8.0', 'Milik', 'Baik'),
    ('6', 'Ruang TU', 'Ruang Penunjang', '8.0', '6.0', 'Milik', 'Baik'),
    ('7', 'Laboratorium Hotel', '125-RPS', '9.0', '8.0', 'Milik', 'Baik'),
    ('8', 'Gudang', '404-Ruang Penunjang', '7.0', '4.0', 'Milik', 'Baik'),
    ('9', 'Kamar Mandi/WC Guru Perempuan', 'Ruang Penunjang', '2.0', '1.0', 'Milik', 'Baik'),
    ('10', 'Laboratorium Komputer', '302-Ruang Praktek Siswa', '8.0', '7.0', 'Milik', 'Baik'),
]

f = open('prasarana.csv','w')
w = csv.writer(f)
w.writerow(('No','Jenis Prasarana', 'Nama', 'Panjang(m)','Lebar(m)','Kepemilikan','Kondisi Kerusakan'))

for p in prasarana:
    w.writerow(p)

f.close()










