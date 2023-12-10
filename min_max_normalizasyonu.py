'''
Ad Soyad: Recep Baykan
OkulNo: 2019141037

Bu py dosyası, veri setindeki sütunlarda bulunan değerlere, min-max normalizasyonu 
uygulamak için yazılmıştır.

'''


def min_max(veriSeti):
    
    # Sütunların değerlerini gezmek için columns adlı koleksiyon/liste/diziden sütün isimlerini çekiyoruz. 
    # Pandas ile veriseti oluşturduğumuzda sütün isimleri, columns adlı değişkende toplanır
    for column in veriSeti.columns:
        
        max_value = veriSeti[column].max() # Seçili sütunun en büyük değerini temsil eder
        min_value = veriSeti[column].min() # Seçili sütunun en küçük değerini temsil eder
        
        # Notlarımda bulunan min - max normalizasyonu formülünü buraya yazıyorum
        # Min - Max optimizasyonu, sütunlardaki tüm değerleri 0 ile 1 arasında ondalıklı değerlere dönüştürür.
        veriSeti[column] = (veriSeti[column] - min_value) / (max_value - min_value)
    
    return veriSeti



