'''
Ad Soyad: Recep Baykan
OkulNo: 2019141037

Bu py dosyası, veri setindeki kayıp değerleri bulmak ve onları düzenlemek için vardır.
Benim ödevimin veri seti 'Churn_Modelling' olduğu  kayıp veri bulunmamaktadır. 
Bu yüzden kayıp verileri kendim oluşturacağım.

Daha sonra kayıp verileri, dolduracağız

'''

import pandas as pd
import numpy as np
# İlk önce Churn_Modelling veri setini, Pandas kütüphanesini yardımıyla bir değişkene aktaralım
    
def kayipVeriOlustur(veriSeti):
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
            rastgele_sayi =  np.random(0,100,1)
            if rastgele_sayi<2:
                veriSeti.iloc[i,j] = np.nan
    return veriSeti
    
    


def kayipVeriGider(veriSeti):
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

    
    
    
    
    



    
    




