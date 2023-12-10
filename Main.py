'''
Ad Soyad: Recep Baykan
OkulNo: 2019141037

Bu py dosyası, diğer Py dosyalarının kullanımına olanak sağlayan ana Py dosyasıdır.
Diğer sınıflardaki fonksiyonlar yani ödevin aşamaları, bu dosya üzerinden çalıştırılacaktır


'''

# İlgili sınıflar ve kütüphaneler import ediliyor.
import pandas as pd
import numpy as np

import kategorik_verileri_sayilastirma as kvs
import kayip_degerleri_doldurma as kdd
import gereksiz_kolon_silme as gks
import min_max_normalizasyonu as mmn
import setleri_olusturma as so
import knn_algoritmasi as knn

dosyaYolu = 'Churn_Modelling.csv'
veriSeti = pd.read_csv(dosyaYolu)

#-------- Ortak Görev 1: Kategorik verileri sayısallaştırma --------#


    # Veri setininin yolunu bir string ifade olduğunda, 'dosyaYolu' adlı değişkende tutmak daha sağlıklı olur.
    #dosyaYolu = 'Churn_Modelling.csv'

    # Pandas kütüphanesinin read_csv fonskiyonu ile 'veriSeti' adlı değişkene Veri Setimizi aktarıyoruz.

    #veriSeti = pd.read_csv(dosyaYolu);

    # Konsol ekranında yazdırmak için 'print' metodu kullanılabilir. Spyder IDE kullanıyorsak, 'Variable Explorer' sekmesinde, Ram'e (belleğe) kaydedilen veriler görülebilir.
    #print(veriSeti)


    # Kategorik verileri, sayısal verilere dönüştürme aşaması

    # Kategorik sütünları bir değişkene aktarma

    # İlk önce satır sayısını bir değişkende tutalım

    gender = veriSeti['Gender']
    geography = veriSeti['Geography']



    #İlk önce gender sütünunu yani cinsiyeti sayısallaştıralım

    gender.replace({'Male': 0, 'Female': 1}, inplace=True)
    
    
        


    # Şimdi geogpraphy sütununu yani bölgeyi sayısallaştıralım

    # İlk önce kaç farklı bölge var, onları sayalım

    #print(geography.value_counts())

    # Veri setinde 3 adet bölge, kişilere dağılmış durumda. Bu bölgeler France, Germany, Spain

    # Şimdi sayısallaştırma aşamasına geçelim

    geography.replace({'France': 0, 'Germany':1, 'Spain':2}, inplace=True)

    # Şimdi sayısallaştırılan sütünları, veri setindeki konumlarıyla değiştirileim

    veriSeti['Gender'] = gender
    veriSeti['Geography'] = geography
    
    # unique olan verileri de 1, 2, 3 ... şeklinde sıralayalım
    
    for i in range(len(veriSeti)):
        
        veriSeti.iloc[i]['CustomerId'] = i
        veriSeti.iloc[i]['Surname'] = i
        
    
    return veriSeti
veriSeti = kvs.sayisallastirma(veriSeti);

# Ortak Görev 2 - 1: Kayıp veri oluşturma --------#


    
    #veriSeti = pd.read_csv('Churn_Modelling.csv')   

    # Şimdi satır ve sütünları rastgele olasılıkla 'NaN' yapalım
    # Bu algoritma her satırda, sütunları tek tek gezer
    # Eğer gezintinden önce 0 ile 100 arasında rastgele sayıyı, rastgele_sayi adlı değişkene atar
    # Eğer rastgele sayi, 2'den (yada başka bir sayı) küçükse o anki durdurduğu satır ve sütunu Numpy kütüphanesinin yardımıyla 'nan' yani kayıp değer yapar.
    # Yalnız ilk 3 sütun için nan değerini eklemedim.
    # Çünkü anlamsız olur. 'rowNumber' satır sayısı demek, 'CustomerID' unique (eşsiz kimlik), 'surname' ise eşsiz kimlik sayılabilecek bir değerdir.
    # Ayrıca bu özellikler, bir veri setinde çıkarım yapmak için göz ardı edilebilecek türde özelliklerdir.

    rastgele_sayi = 0;

    for i in range(veriSeti.shape[0]):
        
        for j in range(3,veriSeti.shape[1]): 
            if j == 10:
                break
            rastgele_sayi =  np.random.randint(0, 101)
            if rastgele_sayi<2:
                veriSeti.iloc[i,j] = np.nan
    return veriSeti
veriSeti = kdd.kayipVeriOlustur(veriSeti)
# Ortak Görev 2 - 2: Kayıp veri giderme
veriSeti = kdd.kayipVeriGider(veriSeti)



    # Şimdi kayıp verileri düzenleyelim  
    # İlk önce Churn_Modelling adlı veri setindeki ilk 3 sütun hariç diğer sütunları değişkenlere aktaralım
    # Bunun için dışarıdan bir sutun sayacı ekledim
    sutun_sayacı = 0;
    
    # ilk önce sütun isimlerini alalım
    # Sütün isimleri, Pandas ile oluşturduğumuz veriSeti değişkenin sonuna .columns ekleyerek ulaşabileceğimiz bir koleksiyon/dizi/liste şeklinde.
    # Bu isimleri veriSeti[sütünİsmi] (aşağıdada belirtilen foreach yapısında veriSeti[colum]) şeklinde tek tek parçalayıp, işlemleri yapabiliriz.
    for colum in veriSeti.columns:
        
        if colum == 'Exited':
            break
        
        sutun_sayacı =  sutun_sayacı + 1;
        
            
        # ilk 3 sütun anlamsız olduğu için 4. sütündan başlayalım
        if  sutun_sayacı > 3:
            # VeriSetini sütünlara ayırıp işleme öyle devam ediliyor
            veri = veriSeti[colum]
           
            
            
            # Sütünların satırlarını gezmek için bir for döngüsü oluşturuldu
            for i in range(len(veri)):
            
              # Sütünları gezerken Pandas kütüphanesini isna fonksiyonunu kullanarak sütunun satılarını gezerken 'NaN' ifadeleri kontrol ediyor.
              if pd.isna(veri[i]):
                   # NaN veri var ise yani kayıp veri var ise sütunda en çok tekrar edilen veriyi, kayıp veriyle değiştiriyor.
                   veri[i] = veriSeti[colum].value_counts().max();
                   
                   
                    
            # Kayıp verileri giderilen sütun, veri setindeki karşılık gelen sütun ile değiştiriliyor
            veriSeti[colum] = veri
            
           
                    

    #veriSeti.to_csv('Churn_Modelling.csv', index = False)
    return veriSeti
#-------- Ortak Görev 3: Gereksiz kolonları silme --------#


veriSeti = gks.kolonSil(veriSeti)

#-------- Ortak Görev 4: Min-Max Normalizasyonu uygulama  --------#


veriSeti = mmn.min_max(veriSeti)

#-------- Ortak Görev 5: Eğitim seti ve Test Seti oluşturma --------#
    # Başka bir py dosyasından yada başka bir bloktan erişebilmek için global türde egitim_seti ve test_seti değişkenleri oluşturulur.
    global egitim_seti
    global test_seti
    
    # Veri setinin satır sayısın yüzde 70'ine denk gelen sayı, tam sayıya dönüştürülerek eğitim setine aktarılır.
    egitim_yuzde = int(len(veriSeti) * 0.7)
    # Veri setinin satır sayısın yüzde 30'una denk gelen sayı, tam sayıya dönüştürülerek eğitim setine aktarılır.
    test_yuzde = int(len(veriSeti) * 0.3)
    
    # Veri setinin satır numaraları karıştırılır ve sira adlı değişkene aktarılır.
    sira = np.random.permutation(len(veriSeti))
    
    # sira dizisi/listesi içinde bulunan rastgele karışmış ve sıralanmış sayılar, egitim_yuzde sayısına kadar egitim_indexleri dizisine/listesine atılır
    egitim_indexleri = sira[:egitim_yuzde]
    # sira dizisi/listesi içinde bulunan rastgele karışmış ve sıralanmış, egitim_yüzde sayısından sonraki karışmış sayılar, test_indexleri dizisine/listesine aktarılır
    test_indexleri = sira[egitim_yuzde: egitim_yuzde + test_yuzde]
    
    # egitim_indexleri değişkeninde karışık halde bulunan sayılar, veri setinden indisleri temsil eder ve verisetinden çekilerek karışmış halde egitim_seti değişkenine aktarılır.
    egitim_seti = veriSeti.iloc[egitim_indexleri]
    # test_indexleri değişkeninde karışık halde bulunan sayılar, veri setinden indisleri temsil eder ve verisetinden çekilerek karışmış halde test_seti değişkenine aktarılır.
    test_seti = veriSeti.iloc[test_indexleri
so.setOlustur(veriSeti)
egitimSeti = so.egitim_seti
testSeti = so.test_seti

#####################################################################################################
# 1. seviye görevİ (1-1): Her test verisi için farklı k değeri  ile KNN sınıflandırması yapılması ###
#####################################################################################################



# Not: Geçen sene ödevimiz için anında buluyordu. Çünkü 150 veri vardı. Bu sefer 10.000 veri olduğu için bayağı uzun sürebiliyor.
# Geçen dönemki ödevimiz, 5 sütün ve 150 satırdan oluşan bir verisetini işlemek idi, bu dönem verisetini temizlememize rağmen 11 sütün ve 10.000 satır.
# Bir de hazır metot, fonksiyon kullanmamız yasak olduğu için kendim geliştirdim bu algoritmayı ondan uzun sürüyor.
# Pandas ve Numpy dışında başka sınıf kullanmadım.
# Bu uzun süre sorunu çözmek için veri setini parçalara ayırıyorum. 200'erli şekilde parçalıyorum.
# Daha sonra her 200 parça kendi içinde eğitim ve test seti oluşturuyor.
# Bu parçalara ayrı ayrı KNN uyguluyorum.
# Başarı oranlarını toplayıp, ortalamasını alıyorum.


# veriSetiListesi adlı dizi/koleksiyon/liste, veri setinin parçalarını tutacaktır
veriSetiListesi = []
# Her parçanın boyutu
parca_boyutu = 200  

# Veri setini parçalara ayırıyoruz
for i in range(0, len(veriSeti), parca_boyutu):
    # Bir veri seti parçası oluşturuyor
    parca = veriSeti[i:i + parca_boyutu]
    # Listeye parçayı ekliyor
    veriSetiListesi.append(parca)
    
# Daha sonra parçaların eğitim ve test setlerini oluşturuyoruz ve KNN uyguluyoruz.
#Başarı sonuçlarını tutacak değişken 
basari_sonucu_1_1 = 0

# veriSetiListesini gezdiğimiz for  döngüsü
for i in range(len(veriSetiListesi)):
    # Her parçayı karıyoruz
    so.setOlustur(veriSetiListesi[i])
    # Her parçanın eğitim setini oluşturuyoruz.
    egitimSeti = so.egitim_seti
    # Her parçanın test setini oluşturuyoruz.
    testSeti= so.test_seti
    # Her parçanın başarı sonucunu ölçüyoruz.
    # Sonuç kesin geliyor. 1 dk. kadar bekletebilir.
    basari_sonucu_1_1 += knn.siniflandir(egitimSeti, testSeti)
    
    
    
    
basari_sonucu_1_1 = (100)*(basari_sonucu_1_1/len(veriSetiListesi))
print('1.1 görevi başarı sonucu %', basari_sonucu_1_1)
    

################################################################################################################################################
###### 2. Seviye görevi (2-1): Belirli K komşu sayısı ile pozitifi ve negatif sınıflara göre komşuları ayırarak KNN algoritması uygulamak ######
################################################################################################################################################

'''
Bu görevde, k = 3 için test verisini test verisini test ederken, test verisine en yakın üç pozitif sınıfı olan örneği ve üç negatif sınıfı olan örneğini alacağız.
Her bir test verisinin en yakın üç pozitif sınıfı olan komşusunun ortalama vektörü alınacak, aynısı üç yakın negatif sınıfı olan komşusu için de geçerli olacaktır.
Daha sonra test verisinin hangi ortalama vektörüne daha yakın ise test verisinin sınıfı ona göre belirlenecek. 
Örnek negatif sınıfa daha yakın, o zaman sınıfı negatif olarak tahmin edilecektir.

'''





# Veri setini tekrar parçalara ayırarak, kısa süre başarı sonucu elde etmeye çalışıyoruz.
# Her parçanın boyutu
parca_boyutu = 200
veriSetiListesi = []

# Veri setini parçalara ayırıyoruz
for i in range(0, len(veriSeti), parca_boyutu):
    # Bir veri seti parçası oluşturuyor
    parca = veriSeti[i:i + parca_boyutu]
    # Listeye parçayı ekliyor
    veriSetiListesi.append(parca)
    
# Daha sonra parçaların eğitim ve test setlerini oluşturuyoruz ve KNN uyguluyoruz.
#Başarı sonuçlarını tutacak değişken 
basari_sonucu_2_1 = 0



# veriSetiListesini gezdiğimiz for  döngüsü
for i in range(len(veriSetiListesi)):
    # Her parçayı karıyoruz
    setOlustur(veriSetiListesi[i])
    # Her parçanın eğitim setini oluşturuyoruz.
    egitimSeti = egitim_seti
    # Her parçanın test setini oluşturuyoruz.
    testSeti= test_seti
    # Her parçanın başarı sonucunu ölçüyoruz.
    # Sonuç kesin geliyor. 1 dk. kadar bekletebilir.
    basari_sonucu_2_1 += siniflandir_ortalama_vektor(egitimSeti, testSeti)
   
   


basari_sonucu_2_1 = 100*(basari_sonucu_2_1/len(veriSetiListesi))

print('2.1 görevi başarı sonucu %', basari_sonucu_2_1)





######################################################
############ 3. Seviye görevi (3-1): #################
######################################################

'''
Bu görevde sırayla 1, 3, 5, 7 ve 9, k değeri için başarı oranı hesaplanmadan sadece sınıf tahminleri
ayrı ayrı dizilerde tutulacak.

Daha sonra bu diziler birleştirilip bir matriks halinde tutulacak.

Daha sonra final sınıflandırıcı yapılacak. 

Bu sınıflandırıcı test setinin her bir verisi için sınıfın değeri, birleştirilen dizilerde en çok tekrar eden 
değere göre sınıf tahmini yapılır ve başarı sonucu hesaplanır.


'''


# K değerine göre test verilenin tahmin edilen sınıfları, sınıf değeri olarak aşağıdaki dizilerde tutulacaktır.
tahmin_1 = []
tahmin_3 = []
tahmin_5 = []
tahmin_7 = []
tahmin_9 = []







veriSetiListesi = []

# Veri setini parçalara ayırıyoruz
for i in range(0, len(veriSeti), parca_boyutu):
    # Bir veri seti parçası oluşturuyor
    parca = veriSeti[i:i + parca_boyutu]
    # Listeye parçayı ekliyor
    veriSetiListesi.append(parca)

egitimSetiListe = []
testSetiListe = []

# Eğitim ve test setini kaydet
for i in range(len(veriSetiListesi)):
    # Her parçayı karıyoruz
    setOlustur(veriSetiListesi[i])
    # Her parçanın eğitim setini oluşturuyoruz.
    egitimSetiListe.append(egitim_seti)
    # Her parçanın test setini oluşturuyoruz.
    testSetiListe.append(test_seti)
   
    



for i in range(len(veriSetiListesi)):
   
    # Tahmin dizilerini, tahmin edilen sınıflar ile doldurduluyor
    tahmin_1 +=(knn.siniflandir_tahmin(egitimSetiListe[i], testSetiListe[i], 1))
    tahmin_3 +=(knn.siniflandir_tahmin(egitimSetiListe[i], testSetiListe[i], 3)) 
    tahmin_5 +=(knn.siniflandir_tahmin(egitimSetiListe[i], testSetiListe[i], 5)) 
    tahmin_7 +=(knn.siniflandir_tahmin(egitimSetiListe[i], testSetiListe[i], 7)) 
    tahmin_9 +=(knn.siniflandir_tahmin(egitimSetiListe[i], testSetiListe[i], 9)) 
   

    
# Tahminler birleştiriliyor
tum_tahminler = []
tum_tahminler.append(tahmin_1)
tum_tahminler.append(tahmin_3)
tum_tahminler.append(tahmin_5)
tum_tahminler.append(tahmin_7)
tum_tahminler.append(tahmin_9)




# Parçalanmış test setinin tekrar birleştiriyoruz
# Çünkü işlemleri hızlandırmak için veri setlerini bölmüştüm ama  final_siniflandırma için yeniden birleşecek
for i in range(len(testSetiListe)):

    if i == 0:
        testSeti = testSetiListe[i]
    else:
        testSeti =  pd.concat([testSeti, testSetiListe[i]])
    
   

# Sonuçları bulmak için biraz bekliyor. Özellike 3.1 görevi için
# Kullanım ipuçları gibi konsol ekranında uyarular verdiği için tüm sonuçları temiz bir şekilde burada gösteriyoruz.
print('Tüm seviyelerin başarı sonucunun gösteri')
print('1.1 görevi başarı sonucu %', basari_sonucu_1_1)
print('2.1 görevi başarı sonucu %', basari_sonucu_2_1)
print('3.1 görevi başarı sonucu %', 100* knn.final_siniflandirma(testSeti, tum_tahminler))



















