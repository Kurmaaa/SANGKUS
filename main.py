import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage
import random

# Inisialisasi tema dan default warna customtkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class Aplikasi(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SANGKUS SYSTEM")
        self.geometry("500x700")
        self.configure(fg_color="#4c5a45")

        # Buat container frame untuk menampung dua halaman UI
        self.container = ctk.CTkFrame(self, fg_color="#4c5a45")
        self.container.pack(fill="both", expand=True)

        # Inisialisasi frame halaman
        self.frames = {}

        # Buat frame dan simpan dalam dictionary frames
        for F in (HalamanSangkus, HalamanRolling, HalamanSpin):
            frame = F(parent=self.container, controller=self)
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)

        # Tampilkan halaman Sangkus (default)
        self.show_frame(HalamanSangkus)

    def show_frame(self, halaman_class):
        frame = self.frames[halaman_class]
        frame.tkraise()  # Membawa frame ke depan


class HalamanSangkus(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#707a70")
        self.controller = controller

        # Logo kiri dan kanan
        logo_left = ctk.CTkLabel(self, text="", width=50, height=60, corner_radius=10, fg_color="white")
        logo_left.place(relx=0.05, rely=0.05, anchor="nw")

        logo_right = ctk.CTkLabel(self, text="", width=50, height=60, corner_radius=10, fg_color="white")
        logo_right.place(relx=0.95, rely=0.05, anchor="ne")

        # Load gambar untuk logo kiri
        logo_left_image = Image.open("Gambar/logo smansa.jpg")
        logo_left_ctk = CTkImage(logo_left_image, size=(45, 55))
        logo_left.configure(image=logo_left_ctk)

        # Load gambar untuk logo kanan
        logo_right_image = Image.open("Gambar/logo jatim.jpeg")
        logo_right_ctk = CTkImage(logo_right_image, size=(45, 55))
        logo_right.configure(image=logo_right_ctk)

        # Judul SANGKUS
        label_title = ctk.CTkLabel(self, text="SANGKUS", font=ctk.CTkFont(family="Arial", size=50, weight="bold"))
        label_title.place(relx=0.5, rely=0.15, anchor="center")

        # Hexagon putih sebagai placeholder
        hex_frame = ctk.CTkFrame(self, width=200, height=190, corner_radius=15, fg_color="white")
        hex_frame.place(relx=0.5, rely=0.35, anchor="center")

        # Load gambar logo SANGKUS
        logo_image = Image.open("Gambar/logo SANGKUS.png")
        logo_ctk = CTkImage(logo_image, size=(190, 180))  # Sesuaikan ukuran gambar

        hex_icon_label = ctk.CTkLabel(hex_frame, image=logo_ctk, text="")
        hex_icon_label.place(relx=0.5, rely=0.5, anchor="center")

        # Tombol 1 (akan pindah ke UI HalamanRolling)
        btn1 = ctk.CTkButton(self, text="ROLLING", width=200, height=40, corner_radius=15,
                             fg_color="#8ba978", hover_color="#9dcf8e",
                             command=lambda: self.controller.show_frame(HalamanRolling),
                             font=ctk.CTkFont(size=15, weight="bold"))
        btn1.place(relx=0.50, rely=0.65, anchor="center")

        # Tombol 2 (akan pindah ke UI HalamanSpin)
        btn2 = ctk.CTkButton(self, text="SPIN", width=200, height=40, corner_radius=15,
                             fg_color="#8ba978", hover_color="#9dcf8e",
                             command=lambda: self.controller.show_frame(HalamanSpin),
                             font=ctk.CTkFont(size=15, weight="bold"))
        btn2.place(relx=0.50, rely=0.75, anchor="center")

        # Icon tanda tanya dan seru
        question_btn = ctk.CTkButton(self, text="?", width=40, height=40,
                                     fg_color="#a3a3a3", hover_color="#c3c3c3", corner_radius=20, font=ctk.CTkFont(size=20))
        question_btn.place(relx=0.1, rely=0.9, anchor="center")

        exclaim_btn = ctk.CTkButton(self, text="!", width=40, height=40,
                                    fg_color="#8c1a1a", hover_color="#b33b3b", corner_radius=20, font=ctk.CTkFont(size=20))
        exclaim_btn.place(relx=0.9, rely=0.9, anchor="center")


class HalamanRolling(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#7d8a7b")  # Warna abu kehijauan

        self.controller = controller

        # Inisialisasi list untuk menyimpan label kotak
        self.box_labels = []

        # Background dekorasi kiri dan kanan (bisa diganti gambar nantinya)
        # Karena sulit dengan customtkinter, kita pakai label teks sebagai placeholder dekorasi
        decor_left = ctk.CTkLabel(self, text="🌿🐞🦋", font=ctk.CTkFont(size=30))
        decor_left.place(relx=0.05, rely=0.35, anchor="w")

        decor_right = ctk.CTkLabel(self, text="🌼🦋🐞", font=ctk.CTkFont(size=30))
        decor_right.place(relx=0.95, rely=0.6, anchor="e")

        # Judul ROLLING
        label_title = ctk.CTkLabel(self, text="ROLLING", font=ctk.CTkFont(family="Arial", size=50, weight="bold"))
        label_title.place(relx=0.5, rely=0.1, anchor="center")

        # Kerangka kotak-kotak sebagai box panjang 100x50 dengan pembatas di tengah
        start_x = 0.23
        start_y = 0.18
        box_width = 100
        box_height = 50
        box_rel_width = box_width / 1000 # 0.2
        gap_between_pairs = 0.05
        gap_y = 0.1

        # boxes with row 4 and range 4 (to display 8 columns)
        for row in range(4):
            for pair in range(4):
                x = start_x + pair * (box_rel_width + gap_between_pairs)
                y = start_y + row * gap_y
                box = ctk.CTkFrame(self, width=box_width, height=box_height, fg_color="#7d8a7b",
                                   border_width=2, border_color="black")
                box.place(relx=x, rely=y, anchor="nw")
                # Pembatas di tengah
                divider = ctk.CTkFrame(box, width=2, height=box_height, fg_color="black")
                divider.place(relx=0.5, rely=0, anchor="n")
                # Tambahkan 2 label untuk nilai dadu
                label1 = ctk.CTkLabel(box, text="", font=ctk.CTkFont(size=20, weight="bold"), fg_color="transparent", text_color="black")
                label1.place(relx=0.25, rely=0.5, anchor="center")
                label2 = ctk.CTkLabel(box, text="", font=ctk.CTkFont(size=20, weight="bold"), fg_color="transparent", text_color="black")
                label2.place(relx=0.75, rely=0.5, anchor="center")
                self.box_labels.append(label1)
                self.box_labels.append(label2)

        # boxes with 1 row and range 2, positioned in the center
        for row in range(1):
            for pair in range(2):
                # Center the 2 boxes: total width 2*0.2 + 0.05 = 0.45, start_x = (1.0 - 0.45)/2 = 0.275
                x = 0.38 + pair * (box_rel_width + gap_between_pairs)
                y = start_y + (4 + row) * gap_y  # next row after 4
                box = ctk.CTkFrame(self, width=box_width, height=box_height, fg_color="#7d8a7b",
                                   border_width=2, border_color="black")
                box.place(relx=x, rely=y, anchor="nw")
                # Pembatas di tengah
                divider = ctk.CTkFrame(box, width=2, height=box_height, fg_color="black")
                divider.place(relx=0.5, rely=0, anchor="n")
                # Tambahkan 2 label untuk nilai dadu
                label1 = ctk.CTkLabel(box, text="", font=ctk.CTkFont(size=20, weight="bold"), fg_color="transparent", text_color="black")
                label1.place(relx=0.25, rely=0.5, anchor="center")
                label2 = ctk.CTkLabel(box, text="", font=ctk.CTkFont(size=20, weight="bold"), fg_color="transparent", text_color="black")
                label2.place(relx=0.75, rely=0.5, anchor="center")
                self.box_labels.append(label1)
                self.box_labels.append(label2)

        # Tombol dengan icon gambar placeholder paling kiri dari tombol
        tombol = ctk.CTkButton(self, text="ROLL ", width=200, height=45, corner_radius=20,
                               fg_color="#869d79", hover_color="#9bae82",
                               font=ctk.CTkFont(size=20, weight="bold"),
                               command=self.roll_dice)
        tombol.place(relx=0.5, rely=0.85, anchor="center")

        # Tombol logout (ikon panah merah kiri atas untuk kembali ke halaman Sangkus)
        logout_btn = ctk.CTkButton(self, text="←", width=40, height=40,
                                   fg_color="#8c1a1a", hover_color="#b33b3b",
                                   corner_radius=10, font=ctk.CTkFont(size=25, weight="bold"),
                                   command=lambda: controller.show_frame(HalamanSangkus))
        logout_btn.place(relx=0.04, rely=0.05, anchor="nw")

        # Tombol menu (3 garis) kanan atas sebagai placeholder
        menu_btn = ctk.CTkButton(self, text="≡", width=40, height=40,
                                 fg_color="#6b6b6b", corner_radius=10,
                                 font=ctk.CTkFont(size=25, weight="bold"))
        menu_btn.place(relx=0.96, rely=0.05, anchor="ne")

        # Icon tanda seru merah kanan bawah
        exclaim_btn = ctk.CTkButton(self, text="!", width=50, height=50,
                                    fg_color="#8c1a1a", hover_color="#b33b3b", corner_radius=25,
                                    font=ctk.CTkFont(size=30, weight="bold"))
        exclaim_btn.place(relx=0.9, rely=0.9, anchor="center")

    def roll_dice(self):
        dice_values = random.sample(range(1, 37), 36)
        # Update kotak dengan nilai dadu
        for i, value in enumerate(dice_values):
            if i < len(self.box_labels):
                self.box_labels[i].configure(text=str(value))
        return dice_values

class HalamanSpin(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#7d8a7b")  # Warna abu kehijauan

        self.controller = controller

         # Warna background buat frame utama sesuai gambar (soft green)
        self.configure(fg_color="#697761")

        # Label Judul SPIN tengah atas
        self.title_label = ctk.CTkLabel(self, text="SPIN",
                                        font=ctk.CTkFont(family="Arial", size=50, weight="bold"),
                                        text_color="#d5d8d1")
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        # Bagian 3. RESULT (kiri)
        self.result_frame = ctk.CTkFrame(self, width=280, height=350,
                                         fg_color="#7c8b72",
                                         corner_radius=10, border_width=1, border_color="#a2ac9a")
        self.result_frame.place(relx=0.15, rely=0.55, anchor="center")

        result_label = ctk.CTkLabel(self.result_frame, text="LIST",
                                    font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
                                    text_color="#1a1a1a")
        result_label.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        kelompok_names = ["KELOMPOK 1", "KELOMPOK 2", "KELOMPOK 3", "KELOMPOK 4", "KELOMPOK 5", "KELOMPOK 6"]
        self.team_frames = {}
        self.group_members = {name: [] for name in kelompok_names}
        self.selected_groups = []

        # Grid untuk team frames
        for i, name in enumerate(kelompok_names):
            row = (i // 2) + 1  # Start from row 1
            col = i % 2
            team_frame = ctk.CTkFrame(self.result_frame, width=120, height=120,
                                      fg_color="#7c8b72", corner_radius=5, border_width=2, border_color="#a2ac9a")
            team_frame.grid(row=row, column=col, padx=5, pady=5)

            team_label = ctk.CTkLabel(team_frame, text=name,
                                      font=ctk.CTkFont(family="Arial", size=10, weight="bold"),
                                      text_color="#1a1a1a")
            team_label.pack(pady=(5, 0))

            team_text = ctk.CTkTextbox(team_frame, width=100, height=80,
                                       fg_color="white", text_color="black", wrap="word")
            team_text.pack(padx=5, pady=5)
            team_text.configure(state="disabled")

            self.team_frames[name] = team_text

        # Bagian 2. CONTROLLER (tengah)
        self.controller_frame = ctk.CTkFrame(self, width=200, height=350,
                                             fg_color="#7c8b72",
                                             corner_radius=10, border_width=1, border_color="#a2ac9a")
        self.controller_frame.place(relx=0.5, rely=0.55, anchor="center")

        controller_label = ctk.CTkLabel(self.controller_frame, text="RESULT",
                                        font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
                                        text_color="#1a1a1a")
        controller_label.pack(pady=(5, 10))

        self.selected_label = ctk.CTkLabel(self.controller_frame, text="Pemateri",
                                           font=ctk.CTkFont(family="Arial", size=14, weight="bold"),
                                           text_color="#1a1a1a")
        self.selected_label.pack(pady=(10, 20))

        tombol = ctk.CTkButton(self.controller_frame, text="SPIN", width=150, height=40, corner_radius=20,
                               fg_color="#869d79", hover_color="#9bae82",
                               font=ctk.CTkFont(size=18, weight="bold"),
                               command=self.spin_wheel)
        tombol.pack(pady=(20, 10))

        # Bagian 1. INPUTS (kanan)
        self.inputs_frame = ctk.CTkFrame(self, width=250, height=350,
                                         fg_color="#7c8b72",
                                         corner_radius=10, border_width=1, border_color="#a2ac9a")
        self.inputs_frame.place(relx=0.85, rely=0.55, anchor="center")

        inputs_label = ctk.CTkLabel(self.inputs_frame, text="INPUTS",
                                    font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
                                    text_color="#1a1a1a")
        inputs_label.pack(pady=(5, 10))

        # Input field
        entry_frame = ctk.CTkFrame(self.inputs_frame, fg_color="transparent")
        entry_frame.pack(fill="x", padx=10, pady=10)

        self.entry_input = ctk.CTkEntry(entry_frame, width=150, height=30,
                                        fg_color="white", text_color="black",
                                        placeholder_text="Input here...")
        self.entry_input.pack(side="left")

        add_btn = ctk.CTkButton(entry_frame, text="+", width=30, height=30,
                                fg_color="#8ba978", hover_color="#9dcf8e",
                                command=self.add_name_global)
        add_btn.pack(side="right", padx=(5, 0))

        # Icon Logout (panah merah kiri atas)
        logout_btn = ctk.CTkButton(self, text="←", width=40, height=40,
                                   fg_color="#8c1a1a", hover_color="#b33b3b",
                                   corner_radius=10, font=ctk.CTkFont(size=25, weight="bold"),
                                   command=lambda: controller.show_frame(HalamanSangkus))
        logout_btn.place(relx=0.04, rely=0.05, anchor="nw")

        # Icon menu tiga garis kanan atas
        self.menu_btn = ctk.CTkButton(self, text="≡",
                                      width=40, height=40,
                                      fg_color="#5c675c", corner_radius=10,
                                      font=ctk.CTkFont(size=30, weight="bold"))
        self.menu_btn.place(relx=0.95, rely=0.05, anchor="ne")

        # Icon tanda seru merah kanan bawah
        self.exclaim_btn = ctk.CTkButton(self, text="!",
                                         width=50, height=50,
                                         fg_color="#8c1a1a", hover_color="#b33b3b",
                                         corner_radius=25,
                                         font=ctk.CTkFont(size=30, weight="bold"))
        self.exclaim_btn.place(relx=0.92, rely=0.9, anchor="center")
        # Hiasan Daun kiri bawah (placeholder label emoji)
        daun_label = ctk.CTkLabel(self, text="🌿", font=ctk.CTkFont(size=40))
        daun_label.place(relx=0.15, rely=0.95, anchor="s")

        # Hiasan kanan bawah kupu-kupu (placeholder emoji)
        kupu_label = ctk.CTkLabel(self, text="🦋", font=ctk.CTkFont(size=30))
        kupu_label.place(relx=0.85, rely=0.85, anchor="center")

    def add_name(self, group_name, entry):
        name = entry.get().strip()
        if name:
            self.group_members[group_name].append(name)
            entry.delete(0, 'end')
            print(f"Added {name} to {group_name}")
            # Update left frame to show names
            self.update_left_frame()

    def update_left_frame(self):
        # Clear existing labels
        for widget in self.left_frame.winfo_children():
            widget.destroy()
        kelompok_names = ["KELOMPOK 1", "KELOMPOK 2", "KELOMPOK 3", "KELOMPOK 4", "KELOMPOK 5", "KELOMPOK 6"]
        y_pos = 0.05
        for name in kelompok_names:
            lbl = ctk.CTkLabel(self.left_frame, text=name,
                               font=ctk.CTkFont(family="Arial", size=14, weight="bold"),
                               text_color="#1a1a1a")
            lbl.place(relx=0.5, rely=y_pos, anchor="center")
            y_pos += 0.1
            for member in self.group_members[name]:
                member_lbl = ctk.CTkLabel(self.left_frame, text=f"- {member}",
                                          font=ctk.CTkFont(family="Arial", size=12),
                                          text_color="#1a1a1a")
                member_lbl.place(relx=0.5, rely=y_pos, anchor="center")
                y_pos += 0.08

    def add_name_global(self):
        name = self.entry_input.get().strip()
        if name:
            # Find the group with the least members
            min_len = min(len(members) for members in self.group_members.values())
            candidates = [group for group, members in self.group_members.items() if len(members) == min_len]
            selected_group = random.choice(candidates)
            self.group_members[selected_group].append(name)
            self.entry_input.delete(0, 'end')
            print(f"Added {name} to {selected_group}")
            # Update the textbox
            self.update_result_textboxes()

    def update_result_textboxes(self):
        for group, members in self.group_members.items():
            text = "\n".join(members)
            self.team_frames[group].configure(state="normal")
            self.team_frames[group].delete("0.0", "end")
            self.team_frames[group].insert("0.0", text)
            self.team_frames[group].configure(state="disabled")

    def spin_wheel(self):
        all_groups = ["KELOMPOK 1", "KELOMPOK 2", "KELOMPOK 3", "KELOMPOK 4", "KELOMPOK 5", "KELOMPOK 6"]
        available_groups = [g for g in all_groups if g not in self.selected_groups]
        if not available_groups:
            print("All groups have been selected. No more spins available.")
            return None
        selected_group = random.choice(available_groups)
        self.selected_groups.append(selected_group)
        self.selected_label.configure(text=selected_group)
        print(f"Kelompok terpilih: {selected_group}")
        return selected_group

if __name__ == "__main__":
    app = Aplikasi()
    app.mainloop()