# 🎙️ Cara Menggunakan Audio Transcriber

## 🚀 Cara Menjalankan Aplikasi (Tanpa Terminal)

### 🐧 **Linux (Ubuntu/Debian)**
1. **Klik kanan** pada file `AudioTranscriber.desktop`
2. Pilih **"Allow Launching"** atau **"Properties"** → centang **"Allow executing file as program"**
3. **Double-click** file `AudioTranscriber.desktop` untuk menjalankan aplikasi
4. Atau **drag** file ke desktop/dock untuk membuat shortcut permanen

### 🪟 **Windows**
1. **Double-click** file `AudioTranscriber.bat`
2. Aplikasi akan otomatis terbuka
3. Untuk membuat shortcut di Desktop:
   - Klik kanan `AudioTranscriber.bat` → **"Send to"** → **"Desktop (create shortcut)"**

### 🍎 **macOS/Linux (Alternative)**
1. **Double-click** file `AudioTranscriber.sh`
2. Jika diminta permission, klik **"Open"** atau **"Allow"**

## 📱 Cara Menggunakan Aplikasi

1. **Klik tombol "Pilih File Audio"**
2. **Pilih file audio** yang ingin ditranskripsi (format: MP3, WAV, M4A, FLAC)
3. **Tunggu proses** transkripsi (akan muncul status progress)
4. **File Word** akan otomatis tersimpan dengan nama `[nama_file]_transkrip.docx`

## 🔧 Troubleshooting

### Jika aplikasi tidak bisa dibuka:
- **Linux**: Jalankan di terminal: `chmod +x AudioTranscriber.sh`
- **Windows**: Klik kanan → "Run as Administrator"
- **Pastikan Python dan dependencies terinstall**

### Jika error "Model not found":
Jalankan sekali di terminal:
```bash
cd /home/kodzjek/Development/Python/Audio-to-text/
source audio2word_env/bin/activate
python -c "import whisper; whisper.load_model('medium')"
```

## ✨ Tips
- File hasil transkripsi akan berada di folder yang sama dengan aplikasi
- Untuk audio panjang, proses mungkin memakan waktu beberapa menit
- Pastikan koneksi internet aktif saat pertama kali menjalankan (untuk download model)