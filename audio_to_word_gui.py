import tkinter as tk
from tkinter import filedialog, messagebox
import whisper
from docx import Document
import threading
import os

# Fungsi untuk transkripsi
def transcribe_audio(audio_path):
    try:
        status_label.config(text="Memuat model Whisper...")
        window.update()

        model = whisper.load_model("medium")  # bisa diganti "small", "medium", "large"
        
        status_label.config(text="Memproses audio...")
        window.update()

        result = model.transcribe(audio_path, language="Indonesian")

        text = result["text"]

        save_to_word(text, audio_path)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Simpan ke Word
def save_to_word(text, audio_path):
    try:
        filename = os.path.splitext(os.path.basename(audio_path))[0] + "_transkrip.docx"
        doc = Document()
        doc.add_paragraph(text)
        doc.save(filename)

        status_label.config(text=f"Transkrip selesai → {filename}")
        messagebox.showinfo("Selesai", f"Hasil transkrip disimpan di {filename}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Pilih file audio
def pilih_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Audio Files", "*.mp3 *.wav *.m4a *.flac"), ("All Files", "*.*")]
    )
    if file_path:
        status_label.config(text=f"File dipilih: {os.path.basename(file_path)}")
        threading.Thread(target=transcribe_audio, args=(file_path,), daemon=True).start()

# GUI
window = tk.Tk()
window.title("Audio to Word Transcriber")
window.geometry("400x200")

label = tk.Label(window, text="Pilih file audio untuk transkripsi ke Word", font=("Arial", 12))
label.pack(pady=10)

pilih_btn = tk.Button(window, text="Pilih File Audio", command=pilih_file, font=("Arial", 11))
pilih_btn.pack(pady=10)

status_label = tk.Label(window, text="Belum ada file dipilih", fg="blue", font=("Arial", 10))
status_label.pack(pady=20)

window.mainloop()
