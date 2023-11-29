'''
Ad Soyad: Recep Baykan
OkulNo: 2019141037

Bu py dosyası, verilen verisetinden eğitim seti ve test seti oluşturmayı sağlar


'''

import pandas as pd
import random as rand

egitim_seti = pd.DataFrame()
test_seti = pd.DataFrame()

def setOlustur(veriSeti):
    
    global egitim_seti
    global test_seti
    
    
    egitim_yuzde =  int((len(veriSeti) * 70) / (100))
    test_yuzde =  int((len(veriSeti) * 30) / (100))
    
    print(egitim_yuzde)
    
   
    
    
    for i in range(egitim_yuzde):
        
        rand = (0, len(veriSeti))
        
        egitim_seti = egitim_seti(veriSeti[rand], ignore_index=True)
        
        veriSeti = veriSeti.drop(veriSeti[rand])
        
        
        
        
        
    
    
    for i in range(test_yuzde):
        
        
        rand = (0, len(veriSeti))
        
        test_seti = test_seti.append(veriSeti[rand], ignore_index=True)
        
        veriSeti = veriSeti.drop(veriSeti[rand])
    
        
        
        
    
    
   

    
    
    
    
    
    
    