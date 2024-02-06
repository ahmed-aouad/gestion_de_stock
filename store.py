import tkinter as tk
from tkinter import ttk, messagebox
from product import Product

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
        self.root.geometry("800x500")  # Définit la taille de l'interface

        # Initialise le gestionnaire de produits en utilisant la configuration de la base de données
        self.product_manager = Product(db_config)

        # Variable pour stocker l'ID du produit sélectionné
        self.selected_product_id = None

        # Crée les widgets de l'interface utilisateur
        self.create_widgets()

        # Charge les données depuis la base de données
        self.load_data()

    def create_widgets(self):
        # Crée des étiquettes et des champs de saisie pour différents attributs du produit
        tk.Label(self.root, text="Nom").grid(row=0, column=0, padx=10, pady=10)
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

        # Configuration des boutons d'ajout, de mise à jour et de suppression
        tk.Button(self.root, text="Ajouter", command=self.add_product).grid(row=5, column=0, pady=10)
        tk.Button(self.root, text="Mettre à jour", command=self.update_product).grid(row=5, column=1, pady=10)
        tk.Button(self.root, text="Supprimer", command=self.delete_product).grid(row=5, column=2, pady=10)

        # Configuration du tableau pour afficher les produits
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nom", "Description", "Prix", "Quantité", "ID Catégorie"), show="headings")
        self.tree.grid(row=6, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)

        self.tree.heading("ID", text="ID")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Prix", text="Prix")
        self.tree.heading("Quantité", text="Quantité")
        self.tree.heading("ID Catégorie", text="ID Catégorie")

        # Ajustement de la largeur des colonnes
        self.tree.column("ID", width=50)
        self.tree.column("Nom", width=100)
        self.tree.column("Description", width=300)
        self.tree.column("Prix", width=80)
        self.tree.column("Quantité", width=80)
        self.tree.column("ID Catégorie", width=100)

        
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

    def load_data(self):
        # Efface toutes les lignes du tableau
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Récupère tous les produits depuis la base de données
        products = self.product_manager.get_all_products()

        # Insère les produits dans le tableau
        for product in products:
            self.tree.insert("", tk.END, values=(product[0], product[1], product[2], product[3], product[4], product[5]))

    def clear_fields(self):
        
        self.name_var.set("")
        self.description_var.set("")
        self.price_var.set(0)
        self.quantity_var.set(0)
        self.id_category_var.set(0)
        self.selected_product_id = None

    def on_tree_select(self, event):
        # Fonction appelée lorsqu'un élément du tableau est sélectionné
        selected_item = self.tree.selection()[0]
        selected_product = self.tree.item(selected_item)['values']
        self.selected_product_id = selected_product[0]

        # Remplit les champs de saisie avec les informations du produit sélectionné
        self.name_var.set(selected_product[1])
        self.description_var.set(selected_product[2])
        self.price_var.set(selected_product[3])
        self.quantity_var.set(selected_product[4])
        self.id_category_var.set(selected_product[5])

    def add_product(self):
        # Appelle la méthode d'ajout de produit avec les valeurs des champs de saisie
        self.product_manager.add_product(
            self.name_var.get(),
            self.description_var.get(),
            self.price_var.get(),
            self.quantity_var.get(),
            self.id_category_var.get()
        )
        # réinitialise les champs de saisie et affiche un message de succès
        self.load_data()
        self.clear_fields()
        messagebox.showinfo("Succès", "Produit ajouté avec succès")

    def update_product(self):
        if self.selected_product_id:
            # Appelle la méthode de mise à jour de produit avec les valeurs des champs de saisie et l'ID du produit sélectionné
            self.product_manager.update_product(
                self.selected_product_id,
                self.name_var.get(),
                self.description_var.get(),
                self.price_var.get(),
                self.quantity_var.get()
            )
            # Recharge les données dans le tableau, réinitialise les champs de saisie et affiche un message de succès
            self.load_data()
            self.clear_fields()
            messagebox.showinfo("Succès", "Produit mis à jour avec succès")
        else:
            messagebox.showwarning("Sélectionnez un produit", "Veuillez sélectionner un produit dans le tableau")

    def delete_product(self):
        if self.selected_product_id:
            # Appelle la méthode de suppression de produit avec l'ID du produit sélectionné
            self.product_manager.delete_product(self.selected_product_id)
            
            self.load_data()
            self.clear_fields()
            messagebox.showinfo("Succès", "Produit supprimé avec succès")
        else:
            messagebox.showwarning("Sélectionnez un produit", "Veuillez sélectionner un produit dans le tableau")

if __name__ == "__main__":
    root = tk.Tk()
    app = StockManagementApp(root)
    root.mainloop()
















