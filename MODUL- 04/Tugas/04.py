class MhsTIF(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku


class buatArray(object):
    internalData = 11 * [None]

    def __getitem__(self, item):
        return self.internalData[item]

    def __setitem__(self, key, value):
        self.internalData[key] = value

    def kurang250rb(self):
        d = []
        for i in self:
            if i.uangSaku < 250000:
                d.append((i.nama, i.nim, i.kotaTinggal, i.uangSaku))
        return d


c = buatArray()
c[0] = MhsTIF('Novera', 10, 'Batang', 250000)
c[1] = MhsTIF('Budi', 51, 'Solo', 200000)
c[2] = MhsTIF('Andi', 2, 'Wonogiri', 245000)
c[3] = MhsTIF('Susanto', 18, 'Bandung', 240000)
c[4] = MhsTIF('Rio', 4, 'Surakarta', 235000)
c[5] = MhsTIF('Bowo', 31, 'Sragen', 260000)
c[6] = MhsTIF('Billy', 10, 'Klaten', 250000)
c[7] = MhsTIF('Putri', 5, 'Semarang', 220000)
c[8] = MhsTIF('Denis', 64, 'Klaten', 225000)
c[9] = MhsTIF('Novi', 23, 'Kendal', 215000)
c[10] = MhsTIF('Dina', 29, 'Purwodadi', 245000)


