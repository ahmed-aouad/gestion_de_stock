import tkinter as tk
from tkinter import ttk, messagebox
from product import Product
from category import Category  

# Configuration de la base de données
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'ouarda2017',
    'database': 'store'
}

class StockManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des Stocks")
        self.root.geometry("800x500")  # Taille ajustée pour plus d'espace

        self.product_manager = Product(db_config)
        self.category_manager = Category(db_config)  # Initialise l'instance de Category

        self.selected_product_id = None

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        # Widgets pour la gestion des produits
        tk.Label(self.root, text="Nom du produit").grid(row=0, column=0, padx=10, pady=10)
        self.name_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.name_var).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Description").grid(row=1, column=0, padx=10, pady=10)
        self.description_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.description_var).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Prix").grid(row=2, column=0, padx=10, pady=10)
        self.price_var = tk.IntVar()
        tk.Entry(self.root, textvariable=self.price_var).grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Quantité").grid(row=3, column=0, padx=10, pady=10)
        self.quantity_var = tk.IntVar()
        tk.Entry(self.root, textvariable=self.quantity_var).grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.root, text="ID Catégorie").grid(row=4, column=0, padx=10, pady=10)
        self.id_category_var = tk.IntVar()
        tk.Entry(self.root, textvariable=self.id_category_var).grid(row=4, column=1, padx=10, pady=10)

        # Boutons pour les opérations sur les produits
        tk.Button(self.root, text="Ajouter Produit", command=self.add_product).grid(row=5, column=0, pady=10)
        tk.Button(self.root, text="Mettre à jour Produit", command=self.update_product).grid(row=5, column=1, pady=10)
        tk.Button(self.root, text="Supprimer Produit", command=self.delete_product).grid(row=5, column=2, pady=10)

        # Tableau pour afficher les produits
        self.product_tree = ttk.Treeview(self.root, columns=("ID", "Nom", "Description", "Prix", "Quantité", "ID Catégorie"), show="headings")
        self.product_tree.grid(row=6, column=0, columnspan=6, sticky='nsew', padx=10, pady=10)
        self.product_tree.heading("ID", text="ID")
        self.product_tree.heading("Nom", text="Nom")
        self.product_tree.heading("Description", text="Description")
        self.product_tree.heading("Prix", text="Prix")
        self.product_tree.heading("Quantité", text="Quantité")
        self.product_tree.heading("ID Catégorie", text="ID Catégorie")

        # Ajustement de la largeur des colonnes
        self.product_tree.column("ID", width=50)
        self.product_tree.column("Nom", width=100)
        self.product_tree.column("Description", width=300)  
        self.product_tree.column("Prix", width=80)
        self.product_tree.column("Quantité", width=80)
        self.product_tree.column("ID Catégorie", width=100)

        self.product_tree.bind("<<TreeviewSelect>>", self.on_tree_select)

    def load_data(self):
        for i in self.product_tree.get_children():
            self.product_tree.delete(i)
        products = self.product_manager.get_all_products()
        for product in products:
            self.product_tree.insert("", tk.END, values=(product[0], product[1], product[2], product[3], product[4], product[5]))

    def on_tree_select(self, event):
         # Fonction appelée lorsqu'un produit est sélectionné dans le tableau
        selected_item = self.product_tree.selection()[0]
        selected_product = self.product_tree.item(selected_item)['values']
        self.selected_product_id = selected_product[0]
        self.name_var.set(selected_product[1])
        self.description_var.set(selected_product[2])
        self.price_var.set(selected_product[3])
        self.quantity_var.set(selected_product[4])
        self.id_category_var.set(selected_product[5])

    def add_product(self):
        self.product_manager.add_product(
            self.name_var.get(),
            self.description_var.get(),
            self.price_var.get(),
            self.quantity_var.get(),
            self.id_category_var.get()
        )
        self.load_data()
        messagebox.showinfo("Succès", "Produit ajouté avec succès")

    def update_product(self):
        if self.selected_product_id:
            self.product_manager.update_product(
                self.selected_product_id,
                self.name_var.get(),
                self.description_var.get(),
                self.price_var.get(),
                self.quantity_var.get()
            )
            self.load_data()
            messagebox.showinfo("Succès", "Produit mis à jour avec succès")
        else:
            messagebox.showwarning("Erreur", "Veuillez sélectionner un produit")

    def delete_product(self):
        if self.selected_product_id:
            self.product_manager.delete_product(self.selected_product_id)
            self.load_data()
            messagebox.showinfo("Succès", "Produit supprimé avec succès")
        else:
            messagebox.showwarning("Erreur", "Veuillez sélectionner un produit")

if __name__ == "__main__":
    root = tk.Tk()
    app = StockManagementApp(root)
    root.mainloop()


















