import ftplib
import os
from colorama import init, Fore, Style
import sys

# Colorama'yı başlat
init()

class FTPClient:
    def __init__(self):
        self.ftp = None
        self.connected = False

    def connect(self, host, port=21):
        """FTP sunucusuna bağlanma"""
        try:
            self.ftp = ftplib.FTP()
            self.ftp.connect(host, port)
            print(f"{Fore.GREEN}Sunucuya başarıyla bağlanıldı: {host}{Style.RESET_ALL}")
            self.connected = True
        except Exception as e:
            print(f"{Fore.RED}Bağlantı hatası: {str(e)}{Style.RESET_ALL}")
            self.connected = False

    def login(self, username, password):
        """FTP sunucusuna giriş yapma"""
        if not self.connected:
            print(f"{Fore.RED}Önce sunucuya bağlanmalısınız!{Style.RESET_ALL}")
            return False

        try:
            self.ftp.login(username, password)
            print(f"{Fore.GREEN}Giriş başarılı!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}Giriş hatası: {str(e)}{Style.RESET_ALL}")
            return False

    def list_directory(self, path='.'):
        """Dizin içeriğini listeleme"""
        if not self.connected:
            print(f"{Fore.RED}Önce sunucuya bağlanmalısınız!{Style.RESET_ALL}")
            return

        try:
            print(f"\n{Fore.CYAN}Dizin içeriği ({path}):{Style.RESET_ALL}")
            self.ftp.dir(path)
        except Exception as e:
            print(f"{Fore.RED}Listeleme hatası: {str(e)}{Style.RESET_ALL}")

    def upload_file(self, local_path, remote_path):
        """Dosya yükleme"""
        if not self.connected:
            print(f"{Fore.RED}Önce sunucuya bağlanmalısınız!{Style.RESET_ALL}")
            return

        try:
            with open(local_path, 'rb') as file:
                self.ftp.storbinary(f'STOR {remote_path}', file)
            print(f"{Fore.GREEN}Dosya başarıyla yüklendi: {remote_path}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Yükleme hatası: {str(e)}{Style.RESET_ALL}")

    def download_file(self, remote_path, local_path):
        """Dosya indirme"""
        if not self.connected:
            print(f"{Fore.RED}Önce sunucuya bağlanmalısınız!{Style.RESET_ALL}")
            return

        try:
            with open(local_path, 'wb') as file:
                self.ftp.retrbinary(f'RETR {remote_path}', file.write)
            print(f"{Fore.GREEN}Dosya başarıyla indirildi: {local_path}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}İndirme hatası: {str(e)}{Style.RESET_ALL}")

    def create_directory(self, dir_name):
        """Dizin oluşturma"""
        if not self.connected:
            print(f"{Fore.RED}Önce sunucuya bağlanmalısınız!{Style.RESET_ALL}")
            return

        try:
            self.ftp.mkd(dir_name)
            print(f"{Fore.GREEN}Dizin başarıyla oluşturuldu: {dir_name}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Dizin oluşturma hatası: {str(e)}{Style.RESET_ALL}")

    def delete_directory(self, dir_name):
        """Dizin silme"""
        if not self.connected:
            print(f"{Fore.RED}Önce sunucuya bağlanmalısınız!{Style.RESET_ALL}")
            return

        try:
            self.ftp.rmd(dir_name)
            print(f"{Fore.GREEN}Dizin başarıyla silindi: {dir_name}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Dizin silme hatası: {str(e)}{Style.RESET_ALL}")

    def rename_file(self, old_name, new_name):
        """Dosya adı değiştirme"""
        if not self.connected:
            print(f"{Fore.RED}Önce sunucuya bağlanmalısınız!{Style.RESET_ALL}")
            return

        try:
            self.ftp.rename(old_name, new_name)
            print(f"{Fore.GREEN}Dosya adı başarıyla değiştirildi: {old_name} -> {new_name}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Dosya adı değiştirme hatası: {str(e)}{Style.RESET_ALL}")

    def disconnect(self):
        """FTP bağlantısını kapatma"""
        if self.connected:
            self.ftp.quit()
            self.connected = False
            print(f"{Fore.YELLOW}Bağlantı kapatıldı.{Style.RESET_ALL}")

def main():
    client = FTPClient()
    
    while True:
        print("\n" + "="*50)
        print(f"{Fore.CYAN}FTP İstemci Programı{Style.RESET_ALL}")
        print("="*50)
        print("1. Sunucuya Bağlan")
        print("2. Giriş Yap")
        print("3. Dizin Listele")
        print("4. Dosya Yükle")
        print("5. Dosya İndir")
        print("6. Dizin Oluştur")
        print("7. Dizin Sil")
        print("8. Dosya Adı Değiştir")
        print("9. Bağlantıyı Kapat")
        print("0. Çıkış")
        
        choice = input("\nSeçiminiz (0-9): ")
        
        if choice == '1':
            host = input("Sunucu adresi: ")
            port = int(input("Port (varsayılan: 21): ") or "21")
            client.connect(host, port)
            
        elif choice == '2':
            username = input("Kullanıcı adı: ")
            password = input("Şifre: ")
            client.login(username, password)
            
        elif choice == '3':
            path = input("Dizin yolu (varsayılan: .): ") or '.'
            client.list_directory(path)
            
        elif choice == '4':
            local_path = input("Yüklenecek dosyanın yerel yolu: ")
            remote_path = input("Uzak sunucudaki hedef yol: ")
            client.upload_file(local_path, remote_path)
            
        elif choice == '5':
            remote_path = input("İndirilecek dosyanın uzak yolu: ")
            local_path = input("Yerel kayıt yolu: ")
            client.download_file(remote_path, local_path)
            
        elif choice == '6':
            dir_name = input("Oluşturulacak dizin adı: ")
            client.create_directory(dir_name)
            
        elif choice == '7':
            dir_name = input("Silinecek dizin adı: ")
            client.delete_directory(dir_name)
            
        elif choice == '8':
            old_name = input("Eski dosya adı: ")
            new_name = input("Yeni dosya adı: ")
            client.rename_file(old_name, new_name)
            
        elif choice == '9':
            client.disconnect()
            
        elif choice == '0':
            if client.connected:
                client.disconnect()
            print(f"{Fore.YELLOW}Program sonlandırılıyor...{Style.RESET_ALL}")
            sys.exit(0)
            
        else:
            print(f"{Fore.RED}Geçersiz seçim!{Style.RESET_ALL}")

if __name__ == "__main__":
    main() 