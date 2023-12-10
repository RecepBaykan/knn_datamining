'''
Ad Soyad: Recep Baykan
Okul No: 2019141037

Bu py dosyası, 'Churn_Modelling' adlı veri setinin içindeki kategorik olarak değeri belirtilen özelliklerini,
sayısal bir veriye dönüştürmek için yazılmıştır.

'Churn_Modelling' veri setinde;
    Geography
    Gender
adındaki stünlar kategorik olarak düşünülebilirken 'Surname' adlı sütün,
bu veri setiyle ilgili bir çıkarım yaparken etkili özellik (sütun) değil
gibi gözüküyor. Ayrıca, her ne kadar tablo içinde 'CustomerID' olsa bile
'Surname' bir nevi unique (eşsiz) bir kimlik sayılabilir çoğu zaman ve katergorik olarak
kabul etmek anlamsız olur. 


'''

import pandas as pd

def sayisallastirma(veriSeti):
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

    # Düzenlenen veri seti değişkenini csv olarak tekrar kaydedelim

    #veriSeti.to_csv('Churn_Modelling.csv', index = False)
    
    return veriSeti

    







    
    
    
        
        
    













