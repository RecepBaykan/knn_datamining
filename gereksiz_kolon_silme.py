'''
Ad Soyad: Recep Baykan
OkulNo: 2019141037

Bu py dosyası, veri setindeki gereksiz olduğu düşünülen kolonları silmek için yazılmıştır.

Veri Setinde gereksiz olduğunu düşündüğüm kolonlor
    
    rowNumber: Satir sayisini belirtiyor. 
    CustormerID: Eşsiz bir kimliği belirtiyor.
    Surname: Soyad belirtiyor. Bir nevi eşsiz kimlik sayılabilir

Öncelikle bu sütünların içindeki verileri kategorileştirmek çok güçtür. Çünkü en az iki tanesi (surname, customerID) eşsiz kimlik 
derecesinde sayılabilir. Yani her bir satır için bir kategori bilgisi olur. 

Satır sayısını da belirtmek için bir sütün eklemek de yine anlamsız. Bu veriyi tanımlayıcı bir özellik değildir. 
Tabi yine de belirli satırlar arasında bir birbirine yakın özellik gösteren kişiler olabilir. Belki bir istisnasdır 
ama eğitim seti, test seti belki de doğrulama seti oluşturmak için satırlar karıştırılacak zaten o yüzden bu istisna
olan durumun da bir anlamı yoktur.

Diğer bir neden veri karmakşılığına yol açar, aşırı öğrenmeye yol açar.

Pandas kütüphanesinin DataFrame sınıfı (yani veri setimiz diyebiliriz) içinde bulunan drop fonksiyonu sütun silmemize olanak
sağlar

    
'''


def kolonSil(veriSeti):
    
    
    veriSeti = veriSeti.drop("RowNumber", axis = 1)
    veriSeti = veriSeti.drop("CustomerId", axis = 1)
    veriSeti = veriSeti.drop("Surname", axis = 1)
    
    
    
    return veriSeti


