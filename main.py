import tkinter as tk
from tkinter import filedialog
from tkinter import Toplevel
import pandas as pd

def veri_sec():
    dosya_path = filedialog.askopenfilename(filetypes=[("Excel Dosyaları", "*.xlsx")])
    if dosya_path:
        # Excel dosyasını oku ve verileri sakla
        global veriler  # Verilere erişebilmek için global olarak tanımlıyoruz
        veriler = pd.read_excel(dosya_path)
        print("Seçilen Excel dosyası yolu:", dosya_path)
        print("Excel verileri:")
        print(veriler)
        hesaplamalara_basla_dugme.config(state=tk.NORMAL)  # "Hesaplamalara Başla" düğmesini etkinleştir

def hesaplamalara_basla():
    # Hesaplamaları burada yapabilirsiniz
    hesaplamalar_penceresi = Toplevel(root)
    hesaplamalar_penceresi.title("Hesaplamalar")
    hesaplamalar_penceresi.geometry("600x400")  # Yeni pencerenin boyutunu 600x400 olarak ayarladık
    # Hesaplamaları bu yeni pencerede gösterebilirsiniz

# Ana tkinter penceresini oluştur
root = tk.Tk()
root.title("Excel Veri Seçme Aracı")

# Başlangıç ekranını küçültme
root.geometry("400x300")  # Örneğin, 400x300 boyutunda bir pencere

# "Veri Seç" düğmesini oluştur
veri_sec_dugme = tk.Button(root, text="Veri Seç", command=veri_sec)
veri_sec_dugme.pack(pady=20)

# "Hesaplamalara Başla" düğmesini oluştur ve etkisizleştir
hesaplamalara_basla_dugme = tk.Button(root, text="Hesaplamalara Başla", command=hesaplamalara_basla, state=tk.DISABLED)
hesaplamalara_basla_dugme.pack(pady=20)

# Ana döngüyü başlat
root.mainloop()
