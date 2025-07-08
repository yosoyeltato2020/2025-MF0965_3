import tkinter as tk
from tkinter import ttk, messagebox
from country_service import CountryService  

class CountryUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Listado de Países - World")
        self.service = CountryService()
        self._build_ui()
        self._load_countries()

    def _build_ui(self):
        cols = ('Código', 'Nombre', 'Población', 'Capital', 'Población Capital')
        self.tree = ttk.Treeview(self.root, columns=cols, show='headings')
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(fill=tk.BOTH, expand=True)

        frm = tk.Frame(self.root); frm.pack(pady=10)
        tk.Button(frm, text="Refrescar", command=self._load_countries).pack(side=tk.LEFT, padx=5)

    def _load_countries(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for country in self.service.list_countries():
            self.tree.insert('', tk.END, values=country)