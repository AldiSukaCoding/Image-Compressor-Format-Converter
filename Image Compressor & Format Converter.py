import os
import threading
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
class ImageProcessorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🖼️ IMG Compressor & Format Converter Pro")
        self.geometry("650x580")
        self.resizable(False, False)
        self.berkas_dipilih = []
        self.folder_tujuan = os.path.expanduser("~/Pictures")
        self.format_target = ctk.StringVar(value="JPEG")
        self.kualitas_kompresi = ctk.IntVar(value=70)
        self.title_label = ctk.CTkLabel(self, text="IMG Compressor & Converter", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(padx=20, pady=(20, 5))
        self.sub_label = ctk.CTkLabel(self, text="Kompresi ukuran dan ubah format gambar secara massal", font=ctk.CTkFont(size=12, slant="italic"))
        self.sub_label.pack(padx=20, pady=(0, 15))
        self.btn_select_files = ctk.CTkButton(self, text="➕ Pilih File Gambar (Bisa Banyak)", font=ctk.CTkFont(weight="bold"), height=40, fg_color="#1f5375", hover_color="#153b54", command=self.pilih_gambar)
        self.btn_select_files.pack(padx=20, pady=10)
        self.setting_frame = ctk.CTkFrame(self)
        self.setting_frame.pack(padx=20, pady=10, fill="x")
        self.lbl_format = ctk.CTkLabel(self.setting_frame, text="Format Target:", font=ctk.CTkFont(weight="bold"))
        self.lbl_format.grid(row=0, column=0, padx=(20, 5), pady=15, sticky="w")
        self.menu_format = ctk.CTkOptionMenu(self.setting_frame, values=["JPEG", "PNG", "WEBP"], variable=self.format_target)
        self.menu_format.grid(row=0, column=1, padx=5, pady=15, sticky="w")
        self.lbl_kualitas = ctk.CTkLabel(self.setting_frame, text="Kualitas (Quality):", font=ctk.CTkFont(weight="bold"))
        self.lbl_kualitas.grid(row=0, column=2, padx=(30, 5), pady=15, sticky="w")
        self.slider_kualitas = ctk.CTkSlider(self.setting_frame, from_=10, to=100, number_of_steps=9, variable=self.kualitas_kompresi, command=self.perbarui_label_kualitas)
        self.slider_kualitas.grid(row=0, column=3, padx=5, pady=15, sticky="w")
        self.lbl_nilai_kualitas = ctk.CTkLabel(self.setting_frame, text="70%", font=ctk.CTkFont(weight="bold"))
        self.lbl_nilai_kualitas.grid(row=0, column=4, padx=(5, 20), pady=15, sticky="w")
        self.folder_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.folder_frame.pack(padx=20, pady=5, fill="x")
        self.btn_folder = ctk.CTkButton(self.folder_frame, text="Pilih Folder Tujuan", width=140, command=self.pilih_folder_tujuan)
        self.btn_folder.grid(row=0, column=0, padx=(10, 10))
        self.lbl_folder_path = ctk.CTkLabel(self.folder_frame, text=self.folder_tujuan, text_color="gray", font=ctk.CTkFont(size=11))
        self.lbl_folder_path.grid(row=0, column=1, sticky="w")
        self.log_text = ctk.CTkTextbox(self, width=600, height=180, font=ctk.CTkFont(family="Courier", size=11))
        self.log_text.pack(padx=20, pady=10)
        self.log_text.configure(state="disabled")
        self.cetak_log("[SISTEM]: Aplikasi siap. Silakan pilih gambar yang ingin diproses.")
        self.action_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.action_frame.pack(padx=20, pady=15)
        self.btn_start = ctk.CTkButton(self.action_frame, text="🚀 Mulai Proses", width=200, height=42, font=ctk.CTkFont(size=14, weight="bold"), command=self.mulai_proses_thread)
        self.btn_start.grid(row=0, column=0, padx=10)
        self.btn_clear = ctk.CTkButton(self.action_frame, text="🗑️ Bersihkan Antrean", width=150, height=42, fg_color="#a83232", hover_color="#822525", command=self.bersihkan_antrean)
        self.btn_clear.grid(row=0, column=1, padx=10)
    def cetak_log(self, teks):
        """Menampilkan riwayat proses ke textbox GUI."""
        self.log_text.configure(state="normal")
        self.log_text.insert("end", teks + "\n")
        self.log_text.see("end")
        self.log_text.configure(state="disabled")
    def perbarui_label_kualitas(self, nilai):
        self.lbl_nilai_kualitas.configure(text=f"{int(nilai)}%")
    def pilih_gambar(self):
        filetypes = [("Gambar", "*.jpg *.jpeg *.png *.webp *.bmp")]
        files = filedialog.askopenfilenames(title="Pilih File Gambar", filetypes=filetypes)
        if files:
            self.berkas_dipilih = list(files)
            self.cetak_log(f"\n📥 [INPUT]: Berhasil memuat {len(files)} file gambar.")
            for f in files:
                self.cetak_log(f" -> {os.path.basename(f)}")
    def pilih_folder_tujuan(self):
        folder = filedialog.askdirectory(initialdir=self.folder_tujuan, title="Pilih Folder Output")
        if folder:
            self.folder_tujuan = folder
            self.lbl_folder_path.configure(text=folder)
            self.cetak_log(f"📁 [FOLDER]: Output dialihkan ke {folder}")
    def bersihkan_antrean(self):
        self.berkas_dipilih = []
        self.cetak_log("\n🗑️ [SISTEM]: Antrean gambar dibersihkan.")
    def mulai_proses_thread(self):
        if not self.berkas_dipilih:
            self.cetak_log("⚠️ [PERINGATAN]: Tidak ada gambar di dalam antrean untuk diproses!")
            return
        self.btn_start.configure(state="disabled", text="Memproses...")
        self.btn_select_files.configure(state="disabled")
        self.btn_clear.configure(state="disabled")
        threading.Thread(target=self.proses_gambar_massal, daemon=True).start()
    def proses_gambar_massal(self):
        fmt = self.format_target.get()
        kualitas = self.kualitas_kompresi.get()
        total = len(self.berkas_dipilih)
        sukses = 0
        self.cetak_log(f"\n⚙️ [PROSES]: Memulai konversi massal ke format {fmt} (Kualitas: {kualitas}%)...")
        for idx, path in enumerate(self.berkas_dipilih, 1):
            nama_file_asli = os.path.basename(path)
            nama_tanpa_ekstensi = os.path.splitext(nama_file_asli)[0]
            ext_baru = f".{fmt.lower()}"
            if fmt == "JPEG":
                ext_baru = ".jpg"
            path_output = os.path.join(self.folder_tujuan, f"{nama_tanpa_ekstensi}_converted{ext_baru}")
            try:
                with Image.open(path) as img:
                    if fmt == "JPEG" and img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    if fmt in ("JPEG", "WEBP"):
                        img.save(path_output, format=fmt, quality=kualitas)
                    else:
                        img.save(path_output, format=fmt, optimize=True)
                uk_asli = os.path.getsize(path) / 1024
                uk_baru = os.path.getsize(path_output) / 1024
                self.cetak_log(f"✅ [{idx}/{total}] {nama_file_asli} -> ({uk_asli:.1f} KB menjadi {uk_baru:.1f} KB)")
                sukses += 1
            except Exception as e:
                self.cetak_log(f"❌ [{idx}/{total}] Gagal memproses {nama_file_asli}. Eror: {str(e)}")
        self.after(0, self.proses_selesai, sukses, total)
    def proses_selesai(self, sukses, total):
        self.btn_start.configure(state="normal", text="🚀 Mulai Proses")
        self.btn_select_files.configure(state="normal")
        self.btn_clear.configure(state="normal")
        self.cetak_log(f"\n✨ [SELESAI]: {sukses} dari {total} gambar berhasil diproses!")
        if sukses == total:
            self.berkas_dipilih = []
        popup = ctk.CTkToplevel(self)
        popup.title("Selesai")
        popup.geometry("300x150")
        popup.resizable(False, False)
        popup.attributes("-topmost", True)
        lbl = ctk.CTkLabel(popup, text=f"Tugas Selesai!\n\n{sukses} Gambar sukses diproses.", justify="center")
        lbl.pack(padx=20, pady=20, expand=True)
        btn = ctk.CTkButton(popup, text="OK", width=80, command=popup.destroy)
        btn.pack(padx=20, pady=(0, 20))
if __name__ == "__main__":
    app = ImageProcessorApp()
    app.mainloop()