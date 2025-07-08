import tkinter as tk
from tkinter import ttk, messagebox
from country_service import CountryService  

class CountryUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Listado de Países - World")
        self.root.geometry("800x500")
        self.root.configure(bg="#e0f7fa")
        self.service = CountryService()
        self._build_ui()
        self._load_countries()

    def _build_ui(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", background="#ffffff", foreground="#222", rowheight=30, fieldbackground="#e0f7fa")
        style.map('Treeview', background=[('selected', '#80deea')])
        style.configure("Treeview.Heading", background="#00838f", foreground="white", font=('Arial', 11, 'bold'))

        cols = ('Código', 'Nombre', 'Población', 'Capital', 'Población Capital')
        self.tree = ttk.Treeview(self.root, columns=cols, show='headings', height=12)
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor='center')
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        frm = tk.Frame(self.root, bg="#e0f7fa"); frm.pack(pady=10)
        tk.Button(frm, text="Refrescar", bg="#00838f", fg="white", font=('Arial', 10, 'bold'),
                  command=self._load_countries, width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(frm, text="Añadir", bg="#43a047", fg="white", font=('Arial', 10, 'bold'),
                  command=self._on_add, width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(frm, text="Editar", bg="#fbc02d", fg="black", font=('Arial', 10, 'bold'),
                  command=self._on_edit, width=12).pack(side=tk.LEFT, padx=5)

    def _load_countries(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for country in self.service.list_countries():
            self.tree.insert('', tk.END, values=country)

    def _on_add(self):
        def guardar_callback(data):
            self.service.add_country(data)
            self._load_countries()
        CountryDialog(self.root, title="Añadir País", on_save=guardar_callback)

    def _on_edit(self):
        sel = self.tree.focus()
        if not sel:
            messagebox.showwarning("Editar", "Seleccione un país")
            return
        data = self.tree.item(sel, 'values')
        def guardar_callback(new_data):
            self.service.update_country(new_data)
            self._load_countries()
        CountryDialog(self.root, title="Editar País", country=data, on_save=guardar_callback)

class CountryDialog(tk.Toplevel):
    def __init__(self, parent, title="Añadir/Editar País", country=None, on_save=None):
        super().__init__(parent)
        self.title(title)
        self.geometry("400x350")
        self.configure(bg="#f1f8e9")
        self.result = None
        self.on_save = on_save

        labels = ["Código", "Nombre", "Población", "Capital", "Población Capital"]
        self.entries = {}

        for i, label in enumerate(labels):
            tk.Label(self, text=label, bg="#f1f8e9", fg="#33691e", font=('Arial', 10, 'bold')).grid(row=i, column=0, padx=15, pady=10, sticky="e")
            entry = tk.Entry(self, font=('Arial', 10), bg="#ffffff", fg="#222")
            entry.grid(row=i, column=1, padx=15, pady=10)
            self.entries[label] = entry

        if country:
            for i, key in enumerate(labels):
                self.entries[key].insert(0, country[i])

        btn_frame = tk.Frame(self, bg="#f1f8e9")
        btn_frame.grid(row=len(labels), column=0, columnspan=2, pady=20)
        tk.Button(btn_frame, text="Guardar", bg="#43a047", fg="white", font=('Arial', 10, 'bold'),
                  command=self._on_save, width=10).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Cancelar", bg="#b71c1c", fg="white", font=('Arial', 10, 'bold'),
                  command=self.destroy, width=10).pack(side=tk.LEFT, padx=10)

        self.grab_set()
        self.transient(parent)
        self.wait_window(self)

    def _on_save(self):
        self.result = tuple(entry.get() for entry in self.entries.values())
        if self.on_save:
            self.on_save(self.result)
        self.destroy()