# FTP İstemci Programı Örnek Kullanımları

Bu klasör, FTP İstemci Programının çeşitli kullanım senaryolarını içerir.

## Örnek Senaryolar

1. **Temel Bağlantı ve Listeleme**
```python
from src.ftp_client import FTPClient

# FTP istemcisi oluştur
client = FTPClient()

# Sunucuya bağlan
client.connect("ftp.example.com")

# Giriş yap
client.login("username", "password")

# Dizin içeriğini listele
client.list_directory()

# Bağlantıyı kapat
client.disconnect()
```

2. **Dosya Transferi**
```python
from src.ftp_client import FTPClient

client = FTPClient()
client.connect("ftp.example.com")
client.login("username", "password")

# Dosya yükleme
client.upload_file("local_file.txt", "remote_file.txt")

# Dosya indirme
client.download_file("remote_file.txt", "downloaded_file.txt")

client.disconnect()
```

3. **Dizin İşlemleri**
```python
from src.ftp_client import FTPClient

client = FTPClient()
client.connect("ftp.example.com")
client.login("username", "password")

# Dizin oluştur
client.create_directory("new_folder")

# Dizin sil
client.delete_directory("old_folder")

client.disconnect()
```

## Test Sunucuları

Programı test etmek için kullanabileceğiniz ücretsiz FTP test sunucuları:

1. **ftp.gnu.org**
   - Host: ftp.gnu.org
   - Port: 21
   - Anonymous login

2. **ftp.debian.org**
   - Host: ftp.debian.org
   - Port: 21
   - Anonymous login

3. **ftp.ubuntu.com**
   - Host: ftp.ubuntu.com
   - Port: 21
   - Anonymous login
