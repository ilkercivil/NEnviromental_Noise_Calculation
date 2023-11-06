import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea, QFormLayout

class VeriGirmeEkrani(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Veri Giriş Ekranı")
        self.setGeometry(100, 100, 800, 600)  # Pencere boyutunu ayarlayabilirsiniz

        self.layout = QVBoxLayout()
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_area.setWidget(self.scroll_widget)
        self.layout.addWidget(self.scroll_area)

        self.form_layout = QFormLayout()
        self.scroll_widget.setLayout(self.form_layout)

        self.veri_etiketleri = [
            "Ölçüm Nokta Adı",  # Ölçüm Nokta Adı eklendi
            "LApeak [dB]", "LAFmax [dB]", "LAeq [dB]", "LAeq Ln [dB] L10", "LAeq Ln [dB] L90",
            "LCpeak [dB]", "LCFmax [dB]", "LCeq [dB]", "LZpeak [dB]", "LZFmax [dB]",
            "1/3 Oct LAeq [dB] 20 Hz", "1/3 Oct LAeq [dB] 25 Hz", "1/3 Oct LAeq [dB] 31.5 Hz",
            "1/3 Oct LAeq [dB] 40 Hz", "1/3 Oct LAeq [dB] 50 Hz", "1/3 Oct LAeq [dB] 63 Hz",
            "1/3 Oct LAeq [dB] 80 Hz", "1/3 Oct LAeq [dB] 100 Hz", "1/3 Oct LAeq [dB] 125 Hz",
            "1/3 Oct LAeq [dB] 160 Hz", "1/3 Oct LAeq [dB] 200 Hz", "1/3 Oct LAeq [dB] 250 Hz",
            "1/3 Oct LAeq [dB] 315 Hz", "1/3 Oct LAeq [dB] 400 Hz", "1/3 Oct LAeq [dB] 500 Hz",
            "1/3 Oct LAeq [dB] 630 Hz", "1/3 Oct LAeq [dB] 800 Hz", "1/3 Oct LAeq [dB] 1000 Hz",
            "1/3 Oct LAeq [dB] 1250 Hz", "1/3 Oct LAeq [dB] 1600 Hz", "1/3 Oct LAeq [dB] 2000 Hz",
            "1/3 Oct LAeq [dB] 2500 Hz", "1/3 Oct LAeq [dB] 3150 Hz", "1/3 Oct LAeq [dB] 4000 Hz",
            "1/3 Oct LAeq [dB] 5000 Hz", "1/3 Oct LAeq [dB] 6300 Hz", "1/3 Oct LAeq [dB] 8000 Hz",
            "1/3 Oct LAeq [dB] 10000 Hz", "1/3 Oct LAeq [dB] 12500 Hz", "1/3 Oct LAeq [dB] 16000 Hz",
            "1/3 Oct LAeq [dB] 20000 Hz", "1/3 Oct LAeq [dB] Total A", "1/3 Oct LAeq [dB] Total C",
            "1/3 Oct LAeq [dB] Total Z"
        ]

        self.veri_girme_kutulari = {}

        for etiket in self.veri_etiketleri:
            label = QLabel(etiket)
            entry = QLineEdit()

            # Sadece belirli kutucukları küçültün
            if etiket != "Ölçüm Nokta Adı":
                entry.setFixedSize(80, 20)  # Genişlik ve yükseklik ayarlarını değiştirebilirsiniz

            self.form_layout.addRow(label, entry)
            self.veri_girme_kutulari[etiket] = entry

        self.kaydet_dugme = QPushButton("Verileri Kaydet")
        self.kaydet_dugme.clicked.connect(self.verileri_kaydet)

        self.layout.addWidget(self.kaydet_dugme)
        self.setLayout(self.layout)

    def verileri_kaydet(self):
        veriler = {etiket: entry.text() for etiket, entry in self.veri_girme_kutulari.items()}

        # Verileri işleme veya kaydetme işlemlerini burada gerçekleştirebilirsiniz

        # Örnek olarak, verileri yazdıralım:
        print("Girilen Veriler:")
        for etiket, deger in veriler.items():
            print(f"{etiket}: {deger}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VeriGirmeEkrani()
    window.show()
    sys.exit(app.exec_())
