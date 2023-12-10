import numpy as np

k_listesi = [1, 3, 5, 7, 9, 11]

def siniflandir(egitim_seti, test_seti):
    # Doğru ve yanlış tahmin edilen sınıflar ayrı değişkenlerde tutulur.
    # Bu değişkenler kullanılarak bir başarı sonucu elde edilir.
    
    # Doğru sınıf bulduğunda sayısı artar
    dogru_sinif = 0
    # Yanlış sınıf bulduğunda sayısı artar
    yanlis_sinif = 0

    # Test setindeki verileri gezmek için kullanılan for döngüsü
    for i in range(len(test_seti)):
        
        # Her farklı test verisinde yeni bir k değeri atanır
        k = np.random.choice(k_listesi)
        
        # Her farklı test verisi k değeri kadar komşu tutar
        # Ayrıca komşu listesindeki komşular, genellik farklı olur
        # Bu listedeki veriler kullanılarak karşılaştırma yapılacak komşular belirlenir.
        yakin_komsu = []
        
        # Komşularının uzaklıklarıda bir listede tutulur
        # Bu listedeki veriler kullanılarak karşılaştırma yapılacak uzaklıklar belirlenir.
        uzaklik_listesi = []
        
        # Eğitim setindeki verileri gezmek için bir for döngüsü oluşturulur
        for j in range(len(egitim_seti)):
            
            # Test setindeki gezilen veri ile eğitim setinde gezilen verinin öklid uzaklığı hesaplanır.
            uzaklik = oklid_uzaklik(egitim_seti.iloc[j], test_seti.iloc[i])

            # Eğer yakin_komşu listesinin uzunluğu k değerinden küçük ise uzaklık uzaklik değişkeni uzaklik_listesine eklenir.
            # Eğitim setindeki gezilen veri de 'yakin_komsu' değişkenine aktarılır
            if len(yakin_komsu) < k:
                yakin_komsu.append(egitim_seti.iloc[j])
                uzaklik_listesi.append(uzaklik)
            # Eğer k değerinden küçük değil ise aşağıdaki bir takım işlemler çalışır.
            else:
                # uzaklik_lsitesi ve 'yakin_komsu' listesini gezebileceğimiz bir for döngüsü oluşturulur.
                for z in range(len(uzaklik_listesi)):
                    
                    # Eğer uzaklık listesindeki gezilen değer, uzaklik değişkeninden büyük ise uzaklik listedenki gezilen değere uzaklık değişkeni aktarılır
                    if uzaklik_listesi[z] > uzaklik:
                        uzaklik_listesi[z] = uzaklik
                        # yakin_komsuda ki gezilen değere ise egitim setindeki değer eklenir
                        yakin_komsu[z] = egitim_seti.iloc[j]
                        # Ardından bir daha atamama olmaması için döngü kırılır
                        break

        # yakin_komşu listesindeki verilerin sınıf değerlerini sayan değişkenler oluşturur.
        # Veri setindeki Exited sınıfında 2 adet değer bulunur 1 ve 0.
        # Bu değişkenler her test verisi için farklı değer tutar.
        
        # Bu değişken 1 değerini tutar
        sinif_1 = 0
        #Bu değişken 0 değerini tutar.
        sinif_2= 0
        
        # yakin_komsu listesini gezmek için bir for döngüsü oluşturuldu
        for x in range(len(yakin_komsu)):
            
            # Eğer yakın sınıfın değeri 1 ise sinif_1 değişkenin değeri 1 artar
            # Eğer 0 ise sinif_2 değişkenin değeri 1 artar.
            if yakin_komsu[x]['Exited'] == 1:
                sinif_1 += 1
            else:
                sinif_2 += 1
                
        # Eğer sinif_1 değeri, sinif_2 değerinden büyük yada küçük ise test verisinin değeri kontrol edilir
        if sinif_1 > sinif_2:
            
            # sinif_1 > sinif_2 ise test verisinin sınıfı 1 ise doğru tahmin edilmiş, 0 ise yanlış tahmin edilmiş.
            # dogru_sinif ve yanlis_sinif değişkenleri de buna göre artar.
            if  test_seti.iloc[i]['Exited'] == 1:
                dogru_sinif +=1
            else:
                yanlis_sinif +=1
        else:
            
            # sinif_1 < sinif_2 ise test verisinin sınıfı 0 ise doğru tahmin edilmiş, 1 ise yanlış tahmin edilmiş.
            # dogru_sinif ve yanlis_sinif değişkenleri de buna göre artar.
            if  test_seti.iloc[i]['Exited'] == 0:
                dogru_sinif +=1
            else:
                yanlis_sinif +=1
        
        
    # Sınıfının başarısını 0 ile 1 arasında belirtilen ondalık sayılarla gösterir.
    # 100 ile çarpılıp başına print('%', basari_orani) şeklinde yazdırılabilir.
    basari_orani = dogru_sinif / (dogru_sinif + yanlis_sinif)
    return basari_orani

def oklid_uzaklik(veri1, veri2):
    # Numpy kütüphaneleri ile öklid uzaklığı fonksiyonun uygulanması
    return np.sqrt(np.sum(np.square(veri1 - veri2)))


def siniflandir_ortalama_vektor(es, ts):
    # Doğru ve yanlış tahmin edilen sınıflar ayrı değişkenlerde tutulur.
    # Bu değişkenler kullanılarak bir başarı sonucu elde edilir.
    
    # Doğru sınıf bulduğunda sayısı artar
    dogru_sinif = 0
    # Yanlış sınıf bulduğunda sayısı artar
    yanlis_sinif = 0
    
   
    # Test setindeki verileri gezmek için kullanılan for döngüsü
    for i in range(len(ts)):
        
        
        # k = 3 olarak ayarlanır
        k = 3
        
        # Her farklı test verisi k değeri kadar negatif ve pozitif komşu tutar
      
        # Bu listedeki veriler kullanılarak karşılaştırma yapılacak komşular belirlenir.
        yakin_komsu_pozitif = []
        yakin_komsu_negatif = []
        
        # Komşularının uzaklıklarıda bir listede tutulur
        # Bu listedeki veriler kullanılarak karşılaştırma yapılacak uzaklıklar belirlenir.
        uzaklik_listesi_pozitif = []
        uzaklik_listesi_negatif = []
        
        
        for j in range(len(es)):
            
            # Test setindeki gezilen veri ile eğitim setinde gezilen verinin öklid uzaklığı hesaplanır.
            uzaklik = oklid_uzaklik(es.iloc[j], ts.iloc[i])

            # Eğer yakin_komşu listesinin uzunluğu k değerinden küçük ise uzaklık uzaklik değişkeni uzaklik_listesine eklenir.
            # Eğitim setindeki gezilen veri de 'yakin_komsu' değişkenine aktarılır
            if es.iloc[j]['Exited'] == 1:
                if len(yakin_komsu_pozitif) < k:
                    yakin_komsu_pozitif.append(es.iloc[j])
                    uzaklik_listesi_pozitif.append(uzaklik)
                # Eğer k değerinden küçük değil ise aşağıdaki bir takım işlemler çalışır.
                else:
                    # uzaklik_lsitesi ve 'yakin_komsu' listesini gezebileceğimiz bir for döngüsü oluşturulur.
                    for z in range(len(uzaklik_listesi_pozitif)):
                        
                        # Eğer uzaklık listesindeki gezilen değer, uzaklik değişkeninden büyük ise uzaklik listedenki gezilen değere uzaklık değişkeni aktarılır
                        if uzaklik_listesi_pozitif[z] > uzaklik:
                            uzaklik_listesi_pozitif[z] = uzaklik
                            # yakin_komsuda ki gezilen değere ise egitim setindeki değer eklenir
                            yakin_komsu_pozitif[z] = es.iloc[j]
                            # Ardından bir daha atamama olmaması için döngü kırılır
                            break
            else:
                if len(yakin_komsu_negatif) < k:
                    yakin_komsu_negatif.append(es.iloc[j])
                    uzaklik_listesi_negatif.append(uzaklik)
                # Eğer k değerinden küçük değil ise aşağıdaki bir takım işlemler çalışır.
                else:
                    # uzaklik_listesi ve 'yakin_komsu' listesini gezebileceğimiz bir for döngüsü oluşturulur.
                    for z in range(len(uzaklik_listesi_negatif)):
                        
                        # Eğer uzaklık listesindeki gezilen değer, uzaklik değişkeninden büyük ise uzaklik listedenki gezilen değere uzaklık değişkeni aktarılır
                        if uzaklik_listesi_negatif[z] > uzaklik:
                            uzaklik_listesi_negatif[z] = uzaklik
                            # yakin_komsuda ki gezilen değere ise egitim setindeki değer eklenir
                            yakin_komsu_negatif[z] = es.iloc[j]
                            # Ardından bir daha atamama olmaması için döngü kırılır
                            break
            
        
        # Sütunların ortalamalarını almak için oluşturulan değişkenler
        ortalama_pozitif_sonuc = 0
        ortalama_negatif_sonuc = 0
        
        # Ortalaması alınacak komşuların, sütun değerlerinin depolanacağı örnekler
        ortalama_pozitif_egitim_ornek = es.iloc[0]
        ortalama_negatif_egitim_ornek = es.iloc[0]
        
        for colum in es.columns:
            
            for x in range(k):
                
               # sütun değerleri toplanır
               ortalama_pozitif_sonuc += yakin_komsu_pozitif[x][colum]
               ortalama_negatif_sonuc += yakin_komsu_negatif[x][colum]
         
            # Yakın komşu sayısı kadar ortalaması alınır
            ortalama_pozitif_sonuc = ortalama_pozitif_sonuc / k
            ortalama_negatif_sonuc = ortalama_negatif_sonuc / k
            
            
            # Örnekelerin sütunlarına, eş değer sütun konumundaki değerleri yerleşir
            ortalama_pozitif_egitim_ornek[colum] = ortalama_pozitif_sonuc
            ortalama_negatif_egitim_ornek[colum] = ortalama_pozitif_sonuc
            
            # Ortalama değerler sınıflanır
            ortalama_pozitif_sonuc = 0
            ortalama_negatif_sonuc = 0
        
        
        # Negatif ve pozitif örneklerin, test verisi ile ilgili uzaklıkları hesaplanır
        negatif_uzaklik= oklid_uzaklik(ts.iloc[i],ortalama_negatif_egitim_ornek)
        pozitif_uzaklik= oklid_uzaklik(ts.iloc[i],ortalama_pozitif_egitim_ornek)
        
        # Bu durumda test setinin sınıfı 1 olarak tahmin edilir
        if pozitif_uzaklik < negatif_uzaklik:
            
            # 1 ise doğru tahmin edilmiştir
            if ts.iloc[i]['Exited'] == 1:
                
                dogru_sinif +=1
                
                
            else:
                # 0 ise yanlış tahmin edilmiştir
                yanlis_sinif +=1
        # Bu durumda test setinin sınıfı 0 olarak tahmin edilir
        else:
            #0 ise doğru tahmin edilmiştir
            if ts.iloc[i]['Exited'] == 0:
                
                dogru_sinif +=1
                
                
            else:
                # 1 ise yanlış tahmin edilmiştir
                yanlis_sinif +=1
                
        
        
        
        
    
        
        
    # Sınıfının başarısını 0 ile 1 arasında belirtilen ondalık sayılarla gösterir.
    # 100 ile çarpılıp başına print('%', basari_orani) şeklinde yazdırılabilir.
    
    basari_orani = dogru_sinif / (dogru_sinif + yanlis_sinif)
    return basari_orani

def siniflandir_tahmin(egitim_seti, test_seti, k):
    
    
    
   
   
    # Fonksiyon sonunda sınıf değerlerinin tutulup döndürüleceği dizi
    dizi = []

    # Test setindeki verileri gezmek için kullanılan for döngüsü
    for i in range(len(test_seti)):
        
        
        
        
        # Her farklı test verisi k değeri kadar komşu tutar
        # Ayrıca komşu listesindeki komşular, genellik farklı olur
        # Bu listedeki veriler kullanılarak karşılaştırma yapılacak komşular belirlenir.
        yakin_komsu = []
        
        # Komşularının uzaklıklarıda bir listede tutulur
        # Bu listedeki veriler kullanılarak karşılaştırma yapılacak uzaklıklar belirlenir.
        uzaklik_listesi = []
        
        # Eğitim setindeki verileri gezmek için bir for döngüsü oluşturulur
        for j in range(len(egitim_seti)):
            
            # Test setindeki gezilen veri ile eğitim setinde gezilen verinin öklid uzaklığı hesaplanır.
            uzaklik = oklid_uzaklik(egitim_seti.iloc[j], test_seti.iloc[i])

            # Eğer yakin_komşu listesinin uzunluğu k değerinden küçük ise uzaklık uzaklik değişkeni uzaklik_listesine eklenir.
            # Eğitim setindeki gezilen veri de 'yakin_komsu' değişkenine aktarılır
            if len(yakin_komsu) < k:
                yakin_komsu.append(egitim_seti.iloc[j])
                uzaklik_listesi.append(uzaklik)
            # Eğer k değerinden küçük değil ise aşağıdaki bir takım işlemler çalışır.
            else:
                # uzaklik_lsitesi ve 'yakin_komsu' listesini gezebileceğimiz bir for döngüsü oluşturulur.
                for z in range(len(uzaklik_listesi)):
                    
                    # Eğer uzaklık listesindeki gezilen değer, uzaklik değişkeninden büyük ise uzaklik listedenki gezilen değere uzaklık değişkeni aktarılır
                    if uzaklik_listesi[z] > uzaklik:
                        uzaklik_listesi[z] = uzaklik
                        # yakin_komsuda ki gezilen değere ise egitim setindeki değer eklenir
                        yakin_komsu[z] = egitim_seti.iloc[j]
                        # Ardından bir daha atamama olmaması için döngü kırılır
                        break

        # yakin_komşu listesindeki verilerin sınıf değerlerini sayan değişkenler oluşturur.
        # Veri setindeki Exited sınıfında 2 adet değer bulunur 1 ve 0.
        # Bu değişkenler her test verisi için farklı değer tutar.
        
        # Bu değişken 1 değerini tutar
        sinif_1 = 0
        #Bu değişken 0 değerini tutar.
        sinif_2= 0
        
        # yakin_komsu listesini gezmek için bir for döngüsü oluşturuldu
        for x in range(len(yakin_komsu)):
            
            # Eğer yakın sınıfın değeri 1 ise sinif_1 değişkenin değeri 1 artar
            # Eğer 0 ise sinif_2 değişkenin değeri 1 artar.
            if yakin_komsu[x]['Exited'] == 1:
                sinif_1 += 1
            else:
                sinif_2 += 1
        # Komşu sayısına göre sınıf çoğunluğu hangisiden ise test verisinin değeri o sınıf değer kabul edilir ve dizi adlı dizi ile birleştirilir
        if sinif_1 > sinif_2:
            dizi.append(1)
        else:
            dizi.append(0)
       
            
        
    
    
    return dizi

def final_siniflandirma(ts, tum_tahminler):
    
    # 1 olan sınıf sayısını tutan değişken
    sinif_1 = 0
    # 2 olan sınıf sayısını tutan değişken
    sinif_2 = 0
    # Tahmin edilen sınıf doğru ise değer artan değişken
    dogru_sinif = 0
    # Tahmin edilen sınıf yanlış ise değer artan değişken
    yanlis_sinif = 0
    
    
    # Test sınıfını ve tahminlerin sutununu gezmek için bir for döngüsü  
    for i in range(len(ts)):
        
        # Tahminler matriksini gezmek için bir for düngüsü
        for j in range(len(tum_tahminler)):
            
            
            sinif_1 = 0
            sinif_2 = 0
           
            # Tahminlerin gezdiği satır ve sütundaki değer 1 ise sinif_1 sayısını artırıyor
            if tum_tahminler[j][i] == 1:
                sinif_1 +=1
             
            # Tahminlerin gezdiği satır ve sütundaki değer 0 ise sinif_2 sayısını artırıyor
            else:
                
                sinif_2 +1
                
        
       
        # Eğer sınıf_1 sayısı çok ise bu test versiinin sınıfının 1 olacağı düşünülüyor
        if sinif_1 > sinif_2:
            # Eğer test verisinin sınıfı 1 ise dogru tahmin ediliyor
            if ts.iloc[i]['Exited'] == 1:
                dogru_sinif += 1
                
            # Eğer test verisinin sınıfı 0 ise yanlış tahmin ediliyor
            else:
                yanlis_sinif += 1
         
            # Eğer sınıf_1 sayısı çok ise bu test versiinin sınıfının 0 olacağı düşünülüyor
        else:
            # Eğer test verisinin sınıfı 0 ise dogru tahmin ediliyor
            if ts.iloc[i]['Exited'] == 0:
                dogru_sinif += 1
                
            # Eğer test verisinin sınıfı 1 ise yanlış tahmin ediliyor   
            else:
                yanlis_sinif += 1
                
    # Doğru ve yanlış tahmin edilen değerler, başarı sonucu döndürüyor
    return (dogru_sinif)/(dogru_sinif + yanlis_sinif)