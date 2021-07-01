class Dosya():


    def __init__(self):


        with open("metin.txt","r",encoding="utf-8") as file:


            dosya_icerigi = file.read()



            kelimeler = dosya_icerigi.split()
            self.sade_kelimeler = list() # sade kelimeler noktasız virgülsüz anlamında ve self de dosyanın elemanı olması için ve daha sonra kullanılması için yazıldı.

            for i in kelimeler:
                i = i.strip("\n")

                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")

                self.sade_kelimeler.append(i)
            for i in self.sade_kelimeler:
                print(i)
    def tum_kelimeler(self):

        kelimeler_kumesi = set() # küme kullanımın nedeni, kümenin aynı değeri sadece 1 tane olarak barındırması yani aaynı kelimeden 2 tane gelirse bi tane gözükecek.

        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i)


        print("Tüm kelimeler.............. ")


        for i in kelimeler_kumesi:
            print(i)




            print(">>>>>>>>>>>>>>>>>>")

    def kelime_frekansı(self):

        self.kelime_sozluk = dict()


        for i in self.sade_kelimeler:

            if (i in self.kelime_sozluk):
                self.kelime_sozluk[i] += 1

            else:
                self.kelime_sozluk[i] = 1

        for sayı,kelime in self.kelime_sozluk.items():
            print("{} kelimesi {} defa geçiyor....".format(sayı,kelime))


            print("-----------------------------------------")



    def kelime_bulma(self):

        kelime1 = input("Kelime giriniz:")

        for i,j in self.kelime_sozluk.items():

            if (i == kelime1 ):
                print("{} kelimesi {} defa geçiyor.".format(i,j))












dosya = Dosya()

dosya.tum_kelimeler()
dosya.kelime_frekansı()
dosya.kelime_bulma()