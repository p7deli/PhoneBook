import tkinter as tk
from customtkinter import CTkButton, CTkLabel, CTkFrame, CTkTabview, CTkEntry, END
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from khayyam import JalaliDatetime
from database_ import Database
import webbrowser


class PhoneBook(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Phone Book")
        self.geometry("950x600+200+20")
        self.resizable(False, False)
        self.config(bg="#6b6080")
        self.iconbitmap("icons/phonebook.ico")

        # label title
        CTkLabel(self, text="Phone Book", font=("Arial", 30, "bold"), text_color="white"
                 , corner_radius=20, fg_color="#302247", height=50).place(x=20, y=10)

        # Date & Clock Label
        self.date = str(JalaliDatetime.now()).split(" ")[0].replace("-", "/")
        CTkLabel(self, text=f"Date: {self.date}", font=("Arial", 20, "bold"), fg_color="#a59db3", corner_radius=20,
                 bg_color="#6b6080", text_color="#1c0647", height=40).place(x=730, y=15)

        self.lbl_clock = CTkLabel(self, text="", font=("Arial", 20, "bold"), fg_color="#a59db3",
                                  corner_radius=20, bg_color="#6b6080", text_color="#1c0647", width=200, height=40,
                                  anchor="w")
        self.lbl_clock.place(x=515, y=15)

        # TabViewBtn
        self.tab_view = CTkTabview(self, width=910, height=500, border_width=4, border_color="black",
                                   fg_color="#a59db3", bg_color="#6b6080", segmented_button_fg_color="black",
                                   segmented_button_selected_color="black", text_color="white",
                                   segmented_button_unselected_color="#3d3b40",
                                   segmented_button_selected_hover_color="#120f17",
                                   segmented_button_unselected_hover_color="#665580")
        self.tab_view.place(x=20, y=80)
        self.tab_view.add("Home")
        self.tab_view.add("Add User")
        self.tab_view.add("Edit User")
        self.tab_view.add("Delete User")
        self.tab_view.add("Search User")
        self.tab_view.add("About Me")

        # Tab Home _________________________________________
        CTkLabel(self.tab_view.tab("Home"), text="", fg_color="#837994", width=800, height=70).place(x=40, y=50)
        CTkLabel(self.tab_view.tab("Home"), text="Hello Welcome TO PhoneBook", fg_color="#302247", width=800, height=70,
                 text_color="white", font=("Arial", 30, "bold")).place(x=50, y=40)

        self.pic_title = Image.open("pictures/phone.png")
        self.pic_title = self.pic_title.resize((400, 350))
        self.ph_title = ImageTk.PhotoImage(self.pic_title)
        tk.Label(self.tab_view.tab("Home"), text="", image=self.ph_title, bg="#a59db3").place(x=250, y=120)
        # Tab Add User _________________________________________
        CTkLabel(self.tab_view.tab("Add User"), text="", fg_color="#837994", width=800, height=70).place(x=40, y=30)
        CTkLabel(self.tab_view.tab("Add User"), text="Add User Tab", fg_color="#302247", width=800, height=70,
                 text_color="white", font=("Arial", 30, "bold")).place(x=50, y=20)

        self.img_add_user = Image.open("pictures/adduser.png")
        self.img_add_user = self.img_add_user.resize((200, 200))
        self.ph_add_user = ImageTk.PhotoImage(self.img_add_user)
        tk.Label(self.tab_view.tab("Add User"), text="", image=self.ph_add_user, bg="#a59db3").place(x=50, y=160)

        self.frame_add_user_tab = CTkFrame(self.tab_view.tab("Add User"), width=550, height=300, fg_color="#514366",
                                           border_width=2, border_color="black")
        self.frame_add_user_tab.place(x=305, y=130)

        CTkLabel(self.frame_add_user_tab, text="Enter The Details", font=("Arial", 20), width=546, height=30,
                 text_color="white", fg_color="#302247").place(x=2, y=2)

        CTkLabel(self.frame_add_user_tab, text="First Name", font=("Arial", 20), corner_radius=10, fg_color="#302247",
                 text_color="white", height=40, width=150, anchor="w").place(x=30, y=45)
        self.txt_fname_tab_add = CTkEntry(self.frame_add_user_tab, width=300, border_width=3, border_color="#302247",
                                          corner_radius=10, font=("Arial", 20, "bold"), height=40)
        self.txt_fname_tab_add.place(x=190, y=45)

        CTkLabel(self.frame_add_user_tab, text="Last Name", font=("Arial", 20), corner_radius=10, fg_color="#302247",
                 text_color="white", height=40, width=150, anchor="w").place(x=30, y=90)
        self.txt_lname_tab_add = CTkEntry(self.frame_add_user_tab, width=300, border_width=3, border_color="#302247",
                                          corner_radius=10, font=("Arial", 20, "bold"), height=40)
        self.txt_lname_tab_add.place(x=190, y=90)

        CTkLabel(self.frame_add_user_tab, text="Phone Number", font=("Arial", 20), corner_radius=10, fg_color="#302247",
                 text_color="white", height=40, anchor="w").place(x=30, y=135)
        self.txt_number_tab_add = CTkEntry(self.frame_add_user_tab, width=300, border_width=3, border_color="#302247",
                                           corner_radius=10, font=("Arial", 20, "bold"), height=40)
        self.txt_number_tab_add.place(x=190, y=135)

        CTkLabel(self.frame_add_user_tab, text="Address", font=("Arial", 20), corner_radius=10, fg_color="#302247",
                 text_color="white", height=40, width=150, anchor="w").place(x=30, y=180)
        self.txt_address_tab_add = CTkEntry(self.frame_add_user_tab, width=300, border_width=3, border_color="#302247",
                                            corner_radius=10, font=("Arial", 20, "bold"), height=40)
        self.txt_address_tab_add.place(x=190, y=180)

        self.btn_add = CTkButton(self.frame_add_user_tab, text="Add User", font=("Arial", 20, "bold"),
                                 width=520, height=40, text_color="white", fg_color="#302247", hover_color="#631bcf",
                                 border_width=2, border_color="white", command=self.add_user_db)
        self.btn_add.place(x=15, y=250)

        # Tab Edit User _________________________________________
        CTkLabel(self.tab_view.tab("Edit User"), text="", fg_color="#837994", width=800, height=70).place(x=40, y=20)
        CTkLabel(self.tab_view.tab("Edit User"), text="Edit User Tab", fg_color="#302247", width=800, height=70,
                 text_color="white", font=("Arial", 30, "bold")).place(x=50, y=10)

        self.img_edit_user = Image.open("pictures/edit.png")
        self.img_edit_user = self.img_edit_user.resize((50, 50))
        self.ph_edit_user = ImageTk.PhotoImage(self.img_edit_user)
        tk.Label(self.tab_view.tab("Edit User"), text="", image=self.ph_edit_user, bg="#302247").place(x=100, y=16)
        tk.Label(self.tab_view.tab("Edit User"), text="", image=self.ph_edit_user, bg="#302247").place(x=750, y=16)

        self.frame_edit_user_tab1 = CTkFrame(self.tab_view.tab("Edit User"), width=450, height=320, fg_color="#514366",
                                             border_width=2, border_color="black")
        self.frame_edit_user_tab1.place(x=2, y=110)

        self.scrollbar_edit = tk.Scrollbar(self.frame_edit_user_tab1)
        self.scrollbar_edit.pack(side="right", fill="y")

        self.table_edit = ttk.Treeview(self.frame_edit_user_tab1, columns=("1", "2", "3", "4", "5"), show="headings",
                                       yscrollcommand=self.scrollbar_edit.set, height=15)
        self.table_edit.pack(side="left", fill="y")

        self.table_edit.column("1", width=180, anchor="center")
        self.table_edit.heading("1", text="Address", anchor="center")

        self.table_edit.column("2", width=104, anchor="center")
        self.table_edit.heading("2", text="NumberPhone", anchor="center")

        self.table_edit.column("3", width=60, anchor="center")
        self.table_edit.heading("3", text="Family", anchor="center")

        self.table_edit.column("4", width=60, anchor="center")
        self.table_edit.heading("4", text="Name", anchor="center")

        self.table_edit.column("5", width=35, anchor="center")
        self.table_edit.heading("5", text="Id", anchor="center")

        self.scrollbar_edit.config(command=self.table_edit.yview)
        self.table_edit.bind("<Button-1>", self.get_selection_edit)
        self.show_edit_table()

        self.frame_edit_user_tab2 = CTkFrame(self.tab_view.tab("Edit User"), width=430, height=320, fg_color="#514366",
                                             border_width=2, border_color="black")
        self.frame_edit_user_tab2.place(x=470, y=110)

        CTkLabel(self.frame_edit_user_tab2, text="Enter The Details", font=("Arial", 20), width=450, height=30,
                 text_color="white", fg_color="#302247").place(x=2, y=2)

        CTkLabel(self.frame_edit_user_tab2, text="First Name", font=("Arial", 20), corner_radius=10, fg_color="#302247",
                 text_color="white", height=40, width=150, anchor="w").place(x=15, y=45)
        self.txt_fname_tab_edit = CTkEntry(self.frame_edit_user_tab2, width=245, border_width=3, border_color="#302247",
                                           corner_radius=10, font=("Arial", 20, "bold"), height=40)
        self.txt_fname_tab_edit.place(x=170, y=45)

        CTkLabel(self.frame_edit_user_tab2, text="Last Name", font=("Arial", 20), corner_radius=10, fg_color="#302247",
                 text_color="white", height=40, width=150, anchor="w").place(x=15, y=90)
        self.txt_lname_tab_edit = CTkEntry(self.frame_edit_user_tab2, width=245, border_width=3, border_color="#302247",
                                           corner_radius=10, font=("Arial", 20, "bold"), height=40)
        self.txt_lname_tab_edit.place(x=170, y=90)

        CTkLabel(self.frame_edit_user_tab2, text="Phone Number", font=("Arial", 20), corner_radius=10,
                 fg_color="#302247",
                 text_color="white", height=40, anchor="w").place(x=15, y=135)
        self.txt_number_tab_edit = CTkEntry(self.frame_edit_user_tab2, width=245, border_width=3,
                                            border_color="#302247",
                                            corner_radius=10, font=("Arial", 20, "bold"), height=40)
        self.txt_number_tab_edit.place(x=170, y=135)

        CTkLabel(self.frame_edit_user_tab2, text="Address", font=("Arial", 20), corner_radius=10, fg_color="#302247",
                 text_color="white", height=40, width=150, anchor="w").place(x=15, y=180)
        self.txt_address_tab_edit = CTkEntry(self.frame_edit_user_tab2, width=245, border_width=3,
                                             border_color="#302247",
                                             corner_radius=10, font=("Arial", 20, "bold"), height=40)
        self.txt_address_tab_edit.place(x=170, y=180)

        self.btn_edit = CTkButton(self.frame_edit_user_tab2, text="Edit User", font=("Arial", 20, "bold"),
                                  width=400, height=40, text_color="white", fg_color="#302247", hover_color="#631bcf",
                                  border_width=2, border_color="white", command=self.edit_)
        self.btn_edit.place(x=15, y=270)

        # Tab Delete User _________________________________________
        CTkLabel(self.tab_view.tab("Delete User"), text="", fg_color="#837994", width=800, height=70).place(x=40, y=20)
        CTkLabel(self.tab_view.tab("Delete User"), text="Delete User Tab", fg_color="#302247", width=800, height=70,
                 text_color="white", font=("Arial", 30, "bold")).place(x=50, y=10)

        self.frame_delete_user_tab = CTkFrame(self.tab_view.tab("Delete User"), width=550, height=320,
                                              fg_color="#514366",
                                              border_width=2, border_color="black")
        self.frame_delete_user_tab.place(x=50, y=110)

        self.scrollbar_delete = tk.Scrollbar(self.frame_delete_user_tab)
        self.scrollbar_delete.pack(side="right", fill="y")

        self.table_delete = ttk.Treeview(self.frame_delete_user_tab, columns=("1", "2", "3", "4", "5"), show="headings",
                                         yscrollcommand=self.scrollbar_delete.set, height=15)
        self.table_delete.pack(side="left", fill="y")

        self.table_delete.column("1", width=220, anchor="center")
        self.table_delete.heading("1", text="Address", anchor="center")

        self.table_delete.column("2", width=120, anchor="center")
        self.table_delete.heading("2", text="NumberPhone", anchor="center")

        self.table_delete.column("3", width=100, anchor="center")
        self.table_delete.heading("3", text="Family", anchor="center")

        self.table_delete.column("4", width=100, anchor="center")
        self.table_delete.heading("4", text="Name", anchor="center")

        self.table_delete.column("5", width=35, anchor="center")
        self.table_delete.heading("5", text="Id", anchor="center")

        self.scrollbar_delete.config(command=self.table_delete.yview)
        self.show_delete_table()

        self.img_delete_user = Image.open("pictures/delete.png")
        self.img_delete_user = self.img_delete_user.resize((150, 150))
        self.ph_delete_user = ImageTk.PhotoImage(self.img_delete_user)
        tk.Label(self.tab_view.tab("Delete User"), text="", image=self.ph_delete_user, bg="#a59db3").place(x=700, y=150)

        self.btn_delete = CTkButton(self.tab_view.tab("Delete User"), text="Delete User", font=("Arial", 20, "bold"),
                                    width=200, height=40, text_color="white", fg_color="#f52a2a", hover_color="#f20000",
                                    border_width=2, border_color="white", command=self.delete_user)
        self.btn_delete.place(x=680, y=350)

        # Tab Search User _________________________________________
        CTkLabel(self.tab_view.tab("Search User"), text="", fg_color="#837994", width=800, height=70).place(x=40, y=20)
        CTkLabel(self.tab_view.tab("Search User"), text="Search User Tab", fg_color="#302247", width=800, height=70,
                 text_color="white", font=("Arial", 30, "bold")).place(x=50, y=10)

        self.img_search_user = Image.open("pictures/search.png")
        self.img_search_user = self.img_search_user.resize((50, 50))
        self.ph_search_user = ImageTk.PhotoImage(self.img_search_user)
        tk.Label(self.tab_view.tab("Search User"), text="", image=self.ph_search_user, bg="#302247").place(x=100, y=16)
        tk.Label(self.tab_view.tab("Search User"), text="", image=self.ph_search_user, bg="#302247").place(x=750, y=16)

        CTkLabel(self.tab_view.tab("Search User"), text="First Name", font=("Arial", 15), corner_radius=10,
                 fg_color="#302247", text_color="white", height=40, width=50, anchor="w").place(x=15, y=95)
        self.txt_fname_tab_search = CTkEntry(self.tab_view.tab("Search User"), width=100, border_width=3,
                                             border_color="#302247", corner_radius=10, font=("Arial", 20, "bold"),
                                             height=40)
        self.txt_fname_tab_search.place(x=115, y=95)

        CTkLabel(self.tab_view.tab("Search User"), text="Last Name", font=("Arial", 15), corner_radius=10,
                 fg_color="#302247", text_color="white", height=40, width=50, anchor="w").place(x=220, y=95)
        self.txt_lname_tab_search = CTkEntry(self.tab_view.tab("Search User"), width=100, border_width=3,
                                             border_color="#302247", corner_radius=10, font=("Arial", 20, "bold"),
                                             height=40)
        self.txt_lname_tab_search.place(x=315, y=95)

        CTkLabel(self.tab_view.tab("Search User"), text="PhoneNumber Name", font=("Arial", 15), corner_radius=10,
                 fg_color="#302247", text_color="white", height=40, width=50, anchor="w").place(x=420, y=95)
        self.txt_number_tab_search = CTkEntry(self.tab_view.tab("Search User"), width=200, border_width=3,
                                              border_color="#302247", corner_radius=10, font=("Arial", 20, "bold"),
                                              height=40)
        self.txt_number_tab_search.place(x=580, y=95)

        self.btn_search = CTkButton(self.tab_view.tab("Search User"), text="Search User", font=("Arial", 15, "bold"),
                                    width=100, height=40, text_color="white", fg_color="#2b84f0", hover_color="#0f4485",
                                    border_width=2, border_color="white", corner_radius=10, command=self.search_user)
        self.btn_search.place(x=785, y=95)

        self.frame_search_user_tab = CTkFrame(self.tab_view.tab("Search User"), fg_color="#514366",
                                              border_width=2, border_color="black")
        self.frame_search_user_tab.place(x=50, y=150)

        self.scrollbar_search = tk.Scrollbar(self.frame_search_user_tab)
        self.scrollbar_search.pack(side="right", fill="y")

        self.table_search = ttk.Treeview(self.frame_search_user_tab, columns=("1", "2", "3", "4", "5"), show="headings",
                                         yscrollcommand=self.scrollbar_search.set, height=13)
        self.table_search.pack(side="left", fill="y")

        self.table_search.column("1", width=270, anchor="center")
        self.table_search.heading("1", text="Address", anchor="center")

        self.table_search.column("2", width=150, anchor="center")
        self.table_search.heading("2", text="NumberPhone", anchor="center")

        self.table_search.column("3", width=150, anchor="center")
        self.table_search.heading("3", text="Family", anchor="center")

        self.table_search.column("4", width=150, anchor="center")
        self.table_search.heading("4", text="Name", anchor="center")

        self.table_search.column("5", width=60, anchor="center")
        self.table_search.heading("5", text="Id", anchor="center")

        self.scrollbar_search.config(command=self.table_search.yview)

        # Tab About User _________________________________________
        CTkLabel(self.tab_view.tab("About Me"), text="", fg_color="#837994", width=800, height=70).place(x=40, y=20)
        CTkLabel(self.tab_view.tab("About Me"), text="About Tab", fg_color="#302247", width=800, height=70,
                 text_color="white", font=("Arial", 30, "bold")).place(x=50, y=10)

        self.img_about_user = Image.open("pictures/about.png")
        self.img_about_user = self.img_about_user.resize((300, 300))
        self.ph_about_user = ImageTk.PhotoImage(self.img_about_user)
        tk.Label(self.tab_view.tab("About Me"), text="", image=self.ph_about_user, bg="#a59db3").place(x=550, y=100)

        self.img_programmer = Image.open("pictures/poria.jpg")
        self.img_programmer = self.img_programmer.resize((150, 150))
        self.ph_programmer = ImageTk.PhotoImage(self.img_programmer)
        tk.Label(self.tab_view.tab("About Me"), text="", image=self.ph_programmer, bg="#a59db3",
                 highlightthickness=5, highlightbackground="#4a198a").place(x=50, y=100)

        CTkLabel(self.tab_view.tab("About Me"), text="👨 My Name Is Poria Delavarian",
                 font=("Arial", 20, "bold"), text_color="#1c1b1f").place(x=250, y=130)
        CTkLabel(self.tab_view.tab("About Me"), text="💻 Python Programmer",
                 font=("Arial", 20, "bold"), text_color="#1c1b1f").place(x=250, y=160)
        CTkLabel(self.tab_view.tab("About Me"), text="🏠 Born in 1996 from Iran",
                 font=("Arial", 20, "bold"), text_color="#1c1b1f").place(x=250, y=190)

        CTkLabel(self.tab_view.tab("About Me"), text="My social networks", font=("Arial", 20, "bold"),
                 text_color="black").place(x=50, y=270)

        self.img_telegram = Image.open("pictures/telegram.png")
        self.img_telegram = self.img_telegram.resize((50, 50))
        self.ph_telegram = ImageTk.PhotoImage(self.img_telegram)
        tk.Label(self.tab_view.tab("About Me"), text="", image=self.ph_telegram, bg="#a59db3").place(x=50, y=300)
        self.lbl_tel = CTkLabel(self.tab_view.tab("About Me"), text="https://t.me/P7deli", font=("Arial", 20, "bold"),
                                text_color="#164cab")
        self.lbl_tel.place(x=120, y=315)
        self.lbl_tel.bind("<Button-1>", self.open_link_telg)

        self.img_instagram = Image.open("pictures/instagram.png")
        self.img_instagram = self.img_instagram.resize((50, 50))
        self.ph_instagram = ImageTk.PhotoImage(self.img_instagram)
        tk.Label(self.tab_view.tab("About Me"), text="", image=self.ph_instagram, bg="#a59db3").place(x=50, y=350)
        self.lbl_insta = CTkLabel(self.tab_view.tab("About Me"), text="P7deli", font=("Arial", 20, "bold"),
                                  text_color="#b8309c")
        self.lbl_insta.place(x=120, y=365)
        self.lbl_insta.bind("<Button-1>", self.open_link_instagram)

        self.img_git = Image.open("pictures/github.png")
        self.img_git = self.img_git.resize((50, 50))
        self.ph_git = ImageTk.PhotoImage(self.img_git)
        tk.Label(self.tab_view.tab("About Me"), text="", image=self.ph_git, bg="#a59db3").place(x=50, y=400)
        self.lbl_git = CTkLabel(self.tab_view.tab("About Me"), text="P7deli", font=("Arial", 20, "bold"),
                                text_color="#1a1619")
        self.lbl_git.place(x=120, y=415)
        self.lbl_git.bind("<Button-1>", self.open_link_github)

    # ------------------------------------------- Show clock
    def clock_show(self):
        clock_ = str(JalaliDatetime.now()).split(" ")[1]
        self.lbl_clock.configure(text=f"Clock: {clock_[:clock_.index('.')]}")
        self.after(1000, self.clock_show)

    # ------------------------------------------ open Links
    def open_link_telg(self, event):
        webbrowser.open("https://t.me/P7deli")

    def open_link_instagram(self, event):
        webbrowser.open("https://www.instagram.com/p7deli/")

    def open_link_github(self, event):
        webbrowser.open("https://github.com/p7deli")

    # -----------------------------------------------------------------------
    # ------------------------------------------ Methods
    # -----------------------------------------------------------------------
    def add_user_db(self):
        name, family, number, address = (self.txt_fname_tab_add.get(), self.txt_lname_tab_add.get(),
                                         self.txt_number_tab_add.get(), self.txt_address_tab_add.get())
        if name != "" and family != "" and number != "" and address != "":
            if number.isnumeric():
                ob = Database("phone_book.db")
                ob.connect_db()
                if ob.create_user(name, family, number, address):
                    messagebox.showinfo("Message", "Add User Successfully!!!!")
                    ob.close_db()
                    for txt in [self.txt_fname_tab_add, self.txt_lname_tab_add,
                                self.txt_number_tab_add, self.txt_address_tab_add]:
                        txt.delete("0", END)
                    self.show_edit_table()
                    self.show_delete_table()
                    self.txt_fname_tab_add.focus_set()
                else:
                    messagebox.showerror("Error", "First Or Last Name Available!!!!!")
                    ob.close_db()
            else:
                messagebox.showerror("Error", "The phone number must be a number only!!!!!")
        else:
            messagebox.showerror("Error", "Please fill in all the boxes!!!!!")

    def get_selection_edit(self, event):
        selection_row = self.table_edit.selection()
        if selection_row != ():
            firstname = self.table_edit.item(selection_row)["values"][3]
            lastname = self.table_edit.item(selection_row)["values"][2]
            number = self.table_edit.item(selection_row)["values"][1]
            address = self.table_edit.item(selection_row)["values"][0]

            for txt in [self.txt_fname_tab_edit, self.txt_lname_tab_edit,
                        self.txt_number_tab_edit, self.txt_address_tab_edit]:
                txt.delete("0", END)

            count = 1
            for txt in [self.txt_fname_tab_edit, self.txt_lname_tab_edit,
                        self.txt_number_tab_edit, self.txt_address_tab_edit]:
                if count == 1:
                    txt.insert("0", firstname)
                elif count == 2:
                    txt.insert("0", lastname)
                elif count == 3:
                    txt.insert("0", number)
                elif count == 4:
                    txt.insert("0", address)
                count += 1

    def edit_(self):
        selection_row = self.table_edit.selection()
        if selection_row != ():
            id_ = self.table_edit.item(selection_row)["values"][4]
            name, family, number, address = (self.txt_fname_tab_edit.get(), self.txt_lname_tab_edit.get(),
                                             self.txt_number_tab_edit.get(), self.txt_address_tab_edit.get())
            ob = Database("phone_book.db")
            ob.connect_db()
            if name != "" and family != "" and number != "" and address != "":
                if number.isnumeric():
                    ob.edit(id_, name, family, number, address)
                    ob.close_db()
                    self.show_edit_table()
                    self.show_delete_table()
                    messagebox.showinfo("Message", "Edit User Successfully!!!")
                    for txt in [self.txt_fname_tab_edit, self.txt_lname_tab_edit,
                                self.txt_number_tab_edit, self.txt_address_tab_edit]:
                        txt.delete("0", END)
                    self.txt_fname_tab_edit.focus_set()
                else:
                    messagebox.showerror("Error", "First Or Last Name Available!!!!!")
                    ob.close_db()
            else:
                messagebox.showerror("Error", "The phone number must be a number only!!!!!")

    def delete_user(self):
        selection_row = self.table_delete.selection()
        if selection_row != ():
            ques = messagebox.askyesno("Delete", "Are you sure to delete this user?")
            if ques:
                id_ = self.table_delete.item(selection_row)["values"][4]
                ob = Database("phone_book.db")
                ob.connect_db()
                ob.delete(id_)
                ob.close_db()
                self.show_edit_table()
                self.show_delete_table()

    def search_user(self):
        name, family, number = (self.txt_fname_tab_search.get(), self.txt_lname_tab_search.get(),
                                self.txt_number_tab_search.get())
        if name == "" and family == "" and number == "":
            messagebox.showerror("Error", "Enter at least one")
        else:
            ob = Database("phone_book.db")
            ob.connect_db()
            res = list(ob.search(name, family, number))
            if len(res) >= 1:
                for row in self.table_search.get_children():
                    self.table_search.delete(row)

                for item in res:
                    id_, first_name, lastname, number, address = item[0], item[1], item[2], item[3], item[4]
                    self.table_search.insert('', "end", text="1", value=[address, number, lastname, first_name, id_])
                ob.close_db()
            else:
                messagebox.showerror("Error", "There is no user with this profile")
                ob.close_db()

    def show_edit_table(self):
        for row in self.table_edit.get_children():
            self.table_edit.delete(row)
        ob = Database("phone_book.db")
        ob.connect_db()
        for item in ob.show_users():
            id_, first_name, lastname, number, address = item[0], item[1], item[2], item[3], item[4]
            self.table_edit.insert('', "end", text="1", value=[address, number, lastname, first_name, id_])
        ob.close_db()

    def show_delete_table(self):
        for row in self.table_delete.get_children():
            self.table_delete.delete(row)
        ob = Database("phone_book.db")
        ob.connect_db()
        for item in ob.show_users():
            id_, first_name, lastname, number, address = item[0], item[1], item[2], item[3], item[4]
            self.table_delete.insert('', "end", text="1", value=[address, number, lastname, first_name, id_])
        ob.close_db()


def main():
    app = PhoneBook()
    app.clock_show()
    app.mainloop()


if __name__ == "__main__":
    main()
