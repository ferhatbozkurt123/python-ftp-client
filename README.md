# FTP İstemci Programı

Bu proje, Python programlama dili kullanılarak geliştirilmiş kullanıcı dostu bir FTP istemci programıdır. Program, temel FTP işlemlerini renkli bir terminal arayüzü üzerinden kolayca gerçekleştirebilmenizi sağlar.

## Özellikler

- ✅ FTP sunucusuna bağlanma ve giriş yapma
- ✅ Yerel ve uzak dizin içeriğini listeleme
- ✅ Dosya yükleme ve indirme
- ✅ Dizin oluşturma ve silme
- ✅ Dosya adı değiştirme
- ✅ Renkli ve kullanıcı dostu terminal arayüzü
- ✅ Detaylı hata mesajları ve durum bildirimleri

## Gereksinimler

- Python 3.x (3.6 veya üzeri)
- colorama (renkli terminal çıktıları için)

## Kurulum

1. Python'un yüklü olduğundan emin olun:
```bash
python3 --version
```

2. Gerekli paketleri yükleyin:
```bash
python3 -m pip install colorama
```

## Programı Çalıştırma

1. Terminal veya komut istemcisini açın
2. Proje dizinine gidin:
```bash
cd /path/to/project
```
3. Programı çalıştırın:
```bash
python3 src/ftp_client.py
```

## Kullanım Kılavuzu

Program başlatıldığında, aşağıdaki menü seçenekleri sunulur:

1. **Sunucuya Bağlan**
   - FTP sunucusunun adresini girin
   - Port numarasını girin (varsayılan: 21)

2. **Giriş Yap**
   - Kullanıcı adınızı girin
   - Şifrenizi girin

3. **Dizin Listele**
   - Listelenecek dizin yolunu girin (varsayılan: mevcut dizin)

4. **Dosya Yükle**
   - Yüklenecek dosyanın yerel yolunu girin
   - Uzak sunucudaki hedef yolu girin

5. **Dosya İndir**
   - İndirilecek dosyanın uzak yolunu girin
   - Yerel kayıt yolunu girin

6. **Dizin Oluştur**
   - Oluşturulacak dizin adını girin

7. **Dizin Sil**
   - Silinecek dizin adını girin

8. **Dosya Adı Değiştir**
   - Eski dosya adını girin
   - Yeni dosya adını girin

9. **Bağlantıyı Kapat**
   - Mevcut FTP bağlantısını güvenli bir şekilde kapatır

0. **Çıkış**
   - Programdan çıkar

## Önemli Notlar

- Her işlem öncesi sunucuya bağlı olduğunuzdan emin olun
- Dosya yolları girerken tam yol kullanmanız önerilir
- Büyük dosyaların transferi sırasında bağlantının kopmamasına dikkat edin
- İşlemler sırasında hata durumları kontrol edilir ve renkli mesajlarla bildirilir

## Güvenlik Uyarıları

- Program standart FTP protokolü kullanmaktadır (şifrelenmemiş)
- Şifreler terminal üzerinde düz metin olarak görünür
- Hassas bilgilerin transferi için SFTP kullanmanız önerilir
- Güvenli olmayan ağlarda kullanırken dikkatli olun

## Hata Ayıklama

Eğer program çalıştırılırken hata alırsanız:

1. Python'un doğru şekilde yüklendiğinden emin olun
2. Gerekli paketlerin yüklendiğini kontrol edin
3. İnternet bağlantınızı kontrol edin
4. FTP sunucusunun erişilebilir olduğunu doğrulayın

