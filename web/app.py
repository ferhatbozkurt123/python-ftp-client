import sys
import os

# src dizinini Python yoluna ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request, jsonify, flash, redirect, url_for, session
from werkzeug.utils import secure_filename
from src.ftp_client import FTPClient

app = Flask(__name__)
app.secret_key = os.urandom(24)

# FTP istemci örneğini oturum bazlı yönetmek için
def get_ftp_client():
    if 'ftp_client' not in session:
        session['ftp_client'] = FTPClient()
    return session['ftp_client']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connect', methods=['POST'])
def connect():
    host = request.form.get('host')
    port = int(request.form.get('port', 21))
    username = request.form.get('username')
    password = request.form.get('password')
    
    client = get_ftp_client()
    
    # Bağlantıyı dene
    client.connect(host, port)
    if client.connected:
        success = client.login(username, password)
        if success:
            flash('FTP sunucusuna başarıyla bağlanıldı!', 'success')
            return jsonify({'status': 'success'})
    
    flash('Bağlantı başarısız!', 'error')
    return jsonify({'status': 'error'})

@app.route('/list', methods=['GET'])
def list_directory():
    path = request.args.get('path', '.')
    client = get_ftp_client()
    
    if not client.connected:
        return jsonify({'status': 'error', 'message': 'FTP sunucusuna bağlı değilsiniz!'})
    
    try:
        files = []
        client.ftp.retrlines('LIST ' + path, lambda x: files.append(x))
        return jsonify({'status': 'success', 'files': files})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'Dosya seçilmedi!'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'Dosya seçilmedi!'})
    
    remote_path = request.form.get('remote_path', file.filename)
    client = get_ftp_client()
    
    if not client.connected:
        return jsonify({'status': 'error', 'message': 'FTP sunucusuna bağlı değilsiniz!'})
    
    try:
        # Geçici dosya oluştur
        temp_path = os.path.join('/tmp', secure_filename(file.filename))
        file.save(temp_path)
        
        # Dosyayı FTP sunucusuna yükle
        with open(temp_path, 'rb') as fp:
            client.ftp.storbinary(f'STOR {remote_path}', fp)
        
        # Geçici dosyayı sil
        os.remove(temp_path)
        
        return jsonify({'status': 'success', 'message': 'Dosya başarıyla yüklendi!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/download', methods=['GET'])
def download_file():
    remote_path = request.args.get('path')
    if not remote_path:
        return jsonify({'status': 'error', 'message': 'Dosya yolu belirtilmedi!'})
    
    client = get_ftp_client()
    if not client.connected:
        return jsonify({'status': 'error', 'message': 'FTP sunucusuna bağlı değilsiniz!'})
    
    try:
        # Geçici dosya oluştur
        local_path = os.path.join('/tmp', secure_filename(os.path.basename(remote_path)))
        
        with open(local_path, 'wb') as fp:
            client.ftp.retrbinary(f'RETR {remote_path}', fp.write)
        
        # Dosyayı kullanıcıya gönder ve geçici dosyayı sil
        from flask import send_file
        return send_file(
            local_path,
            as_attachment=True,
            download_name=os.path.basename(remote_path)
        )
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/mkdir', methods=['POST'])
def create_directory():
    dir_name = request.form.get('dir_name')
    if not dir_name:
        return jsonify({'status': 'error', 'message': 'Dizin adı belirtilmedi!'})
    
    client = get_ftp_client()
    if not client.connected:
        return jsonify({'status': 'error', 'message': 'FTP sunucusuna bağlı değilsiniz!'})
    
    try:
        client.create_directory(dir_name)
        return jsonify({'status': 'success', 'message': 'Dizin oluşturuldu!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/rmdir', methods=['POST'])
def delete_directory():
    dir_name = request.form.get('dir_name')
    if not dir_name:
        return jsonify({'status': 'error', 'message': 'Dizin adı belirtilmedi!'})
    
    client = get_ftp_client()
    if not client.connected:
        return jsonify({'status': 'error', 'message': 'FTP sunucusuna bağlı değilsiniz!'})
    
    try:
        client.delete_directory(dir_name)
        return jsonify({'status': 'success', 'message': 'Dizin silindi!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/rename', methods=['POST'])
def rename_file():
    old_name = request.form.get('old_name')
    new_name = request.form.get('new_name')
    
    if not old_name or not new_name:
        return jsonify({'status': 'error', 'message': 'Eski ve yeni isim belirtilmedi!'})
    
    client = get_ftp_client()
    if not client.connected:
        return jsonify({'status': 'error', 'message': 'FTP sunucusuna bağlı değilsiniz!'})
    
    try:
        client.rename_file(old_name, new_name)
        return jsonify({'status': 'success', 'message': 'Dosya adı değiştirildi!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/disconnect', methods=['POST'])
def disconnect():
    client = get_ftp_client()
    if client.connected:
        client.disconnect()
        session.pop('ftp_client', None)
        return jsonify({'status': 'success', 'message': 'Bağlantı kapatıldı!'})
    return jsonify({'status': 'error', 'message': 'Zaten bağlı değilsiniz!'})

if __name__ == '__main__':
    app.run(debug=True) 