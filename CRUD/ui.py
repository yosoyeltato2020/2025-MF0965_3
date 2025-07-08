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
        tk.Button(frm, text="Añadir",    command=self._on_add).pack(side=tk.LEFT, padx=5)
        tk.Button(frm, text="Editar",    command=self._on_edit).pack(side=tk.LEFT, padx=5)
        

    def _load_countries(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for country in self.service.list_countries():
            self.tree.insert('', tk.END, values=country)

    def _on_add(self):
        dialog = CountryDialog(self.root, title="Añadir País")
        if dialog.result:
            
            messagebox.showinfo("Añadir", f"Datos a guardar: {dialog.result}")
            self._load_countries()

    def _on_edit(self):
        sel = self.tree.focus()
        if not sel:
            messagebox.showwarning("Editar", "Seleccione un país")
            return
        data = self.tree.item(sel, 'values')
        dialog = CountryDialog(self.root, title="Editar País", country=data)
        if dialog.result:
            
            messagebox.showinfo("Editar", f"Datos actualizados: {dialog.result}")
            self._load_countries()

class CountryDialog(tk.Toplevel):
    def __init__(self, parent, title="Añadir/Editar País", country=None):
        super().__init__(parent)
        self.title(title)
        self.result = None

        labels = ["Código", "Nombre", "Población", "Capital", "Población Capital"]
        self.entries = {}

        for i, label in enumerate(labels):
            tk.Label(self, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(self)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[label] = entry

        if country:
            for i, key in enumerate(labels):
                self.entries[key].insert(0, country[i])

        btn_frame = tk.Frame(self)
        btn_frame.grid(row=len(labels), column=0, columnspan=2, pady=10)
        tk.Button(btn_frame, text="Guardar", command=self._on_save).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Cancelar", command=self.destroy).pack(side=tk.LEFT, padx=5)

        self.grab_set()
        self.transient(parent)
        self.wait_window(self)

    def _on_save(self):
        self.result = tuple(entry.get() for entry in self.entries.values())
        self.destroy()