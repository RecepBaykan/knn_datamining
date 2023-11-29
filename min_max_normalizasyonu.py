'''
Ad Soyad: Recep Baykan
OkulNo: 2019141037

Bu py dosyası, veri setindeki sütunlarda bulunan değerlere, min-max normalizasyonu 
uygulamak için yazılmıştır.

'''

def min_max(veriSeti):
    
    # Sütunların değerlerini gezmek için columns adlı koleksiyon/liste/diziden sütün isimlerini çekiyoruz.
    # Pandas ile veriseti oluşturduğumuzda sütün isimleri, columns adlı değişkende toplanır.
    
    max_value = 0 # Bir Sütunun en büyük değerini temsil eder
    min_value = 0 # Bir Sütunun en küçük değerini temsil eder
    for colum in veriSeti.columns:
        
        # sutun adlı değişkene, veriSeti[colum] adlı sutunu atıyorum
        sutun = veriSeti[colum]
        
        max_value = sutun.max()
        min_value = sutun.min()
        
        for i in range(len(sutun)):
            
            # Notlarımda bulunan min - max normalizasyonu formülünü buraya yazıyorum
            # Min - Max optimizasyonu, sütunlardaki tüm değerleri 0 ile 1 arasında ondalıklı değerlere dönüştürür.
            # Not: Bu işlem 30 sn. kadar sürebilir. Çünkü yüz bine yakın değeri tek tek değiştiriyor.
            
            sutun[i] =  (sutun[i] - min_value) / (max_value - min_value)
            
            
            
            
        veriSeti[colum] = sutun
        
        
        
        
    
           
           
    
    return veriSeti