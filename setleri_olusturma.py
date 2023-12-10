'''
Ad Soyad: Recep Baykan
OkulNo: 2019141037

Bu py dosyası, verilen verisetinden eğitim seti ve test seti oluşturmayı sağlar


'''


import numpy as np
import pandas as pd

def setOlustur(veriSeti):
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
    test_seti = veriSeti.iloc[test_indexleri]
    
   
    
    
   

    
    
    
    
    
    
    