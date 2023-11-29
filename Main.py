'''
Ad Soyad: Recep Baykan
OkulNo: 2019141037

Bu py dosyası, diğer Py dosyalarının kullanımına olanak sağlayan ana Py dosyasıdır.
Diğer sınıflardaki fonksiyonlar yani ödevin aşamaları, bu dosya üzerinden çalıştırılacaktır


'''

import pandas as pd
import kategorik_verileri_sayilastirma as kvs
import kayip_degerleri_doldurma as kdd
import gereksiz_kolon_silme as gks
import min_max_normalizasyonu as mmn
import setleri_olusturma as so

dosyaYolu = 'Churn_Modelling.csv'
veriSeti = pd.read_csv(dosyaYolu)

# Ortak Görev 1: Kategorik verileri sayısallaştırma
veriSeti = kvs.sayisallastirma(veriSeti);

# Ortak Görev 2 - 1: Kayıp veri oluşturma
veriSeti = kdd.kayipVeriOlustur(veriSeti)

# Ortak Görev 2 - 1: Kayıp veri giderme
veriSeti = kdd.kayipVeriGider(veriSeti)

# Ortak Görev 3: Gereksiz kolonları silme
veriSeti = gks.kolonSil(veriSeti)

# Ortak Görev 4: Min-Max Normalizasyonu uygulama 
# Not: Bu işlem 30 sn. kadar sürebilir.
#veriSeti = mmn.min_max(veriSeti)

# Ortak Görev 5: Eğitim seti ve Test Seti oluşturma

so.setOlustur(veriSeti)
egitim_seti = so.egitim_seti
test_seti = so.test_seti

