# 📚 Module de Gestion des Livres et des Prix (pour Agent IA)

Ce projet, nommé `agent_ia`, contient un module Python simple (`book.py`) conçu pour gérer un catalogue de livres avec leurs prix. Bien que le nom du dépôt suggère une application plus large d'intelligence artificielle, ce module sert de composant fondamental pour la récupération et le calcul des prix, potentiellement utilisable par un agent IA pour des tâches comme la recommandation de produits, la gestion de stocks ou le traitement de commandes.

## ✨ Fonctionnalités

- **Catalogue de Livres :** Maintient une liste prédéfinie de livres avec leurs prix.
- **Récupération de Prix :** Permet de récupérer le prix d'un livre spécifique.
- **Calcul de Prix Totaux :** (Fonctionnalité supposée basée sur l'extrait `calcu...`) Capacité à calculer le coût total d'une sélection de livres.

## 🚀 Technologies Utilisées

- **Python** (version 3.x)

## 📂 Structure du Projet

Le projet est minimaliste et contient un seul fichier Python principal :


.
├── book.py             # Contient la logique de gestion des livres et des prix.
└── README.md           # Ce fichier.


## 🛠️ Installation et Configuration

Pour commencer avec ce projet, suivez les étapes ci-dessous :

1.  **Clonez le dépôt :**
    bash
    git clone https://github.com/xXmouhibXx/agent_ia.git
    cd agent_ia
    

2.  **Assurez-vous d'avoir Python installé :**
    Le script nécessite Python 3.x. Vous pouvez vérifier votre version avec :
    bash
    python3 --version
    
    Si Python n'est pas installé, veuillez le télécharger depuis le [site officiel de Python](https://www.python.org/downloads/).

Aucune dépendance externe spécifique n'est requise au-delà de Python standard.

## 💡 Utilisation

Le module `book.py` est conçu pour être importé et utilisé dans d'autres scripts Python.

Voici un exemple d'utilisation dans un interpréteur Python ou un script séparé :

python
# exemple_utilisation.py
from book import get_book_price, calculate_total_price, get_all_books

# Afficher le catalogue complet des livres
print("--- Catalogue de Livres ---")
for book_name, price in get_all_books().items():
    print(f"- {book_name.replace('_', ' ').title()}: {price:.2f}€")
print("---------------------------\n")

# Récupérer le prix d'un livre spécifique
python_price = get_book_price("python_guide")
print(f"Le prix du 'Python Guide' est : {python_price:.2f}€")

data_science_price = get_book_price("data_science")
print(f"Le prix du 'Data Science' est : {data_science_price:.2f}€\n")

# Essayer de récupérer le prix d'un livre inexistant
unknown_book_price = get_book_price("unknown_book")
print(f"Le prix de 'Unknown Book' est : {unknown_book_price:.2f}€ (0.00€ si non trouvé)\n")

# Calculer le prix total d'une sélection de livres
selected_books = ["python_guide", "data_science", "web_dev"]
total_cost = calculate_total_price(selected_books)
print(f"Le coût total pour '{', '.join(b.replace('_', ' ').title() for b in selected_books)}' est : {total_cost:.2f}€")

# Exemple avec un livre inexistant dans la sélection
selected_books_with_unknown = ["python_guide", "machine_learning", "non_existent_book"]
total_cost_with_unknown = calculate_total_price(selected_books_with_unknown)
print(f"Le coût total pour '{', '.join(b.replace('_', ' ').title() for b in selected_books_with_unknown)}' est : {total_cost_with_unknown:.2f}€")


Pour exécuter cet exemple (après avoir créé `exemple_utilisation.py` dans le même répertoire que `book.py`):

bash
python3 exemple_utilisation.py


### Note sur les fonctions imaginées

L'extrait de code fourni montrait `calcu...`. Pour les besoins de ce README, j'ai supposé l'existence de deux fonctions supplémentaires dans `book.py` qui pourraient être utiles :

-   `calculate_total_price(book_list)` : Prend une liste de noms de livres et retourne leur prix total.
-   `get_all_books()` : Retourne le dictionnaire complet des livres et de leurs prix.

Si ces fonctions ne sont pas encore implémentées, ce README peut servir de guide pour les futures extensions.

## 🧪 Tests

Bien qu'aucun fichier de test ne soit fourni dans l'extrait, il est recommandé d'écrire des tests unitaires pour assurer la robustesse du module. Vous pouvez utiliser des frameworks comme `unittest` (intégré à Python) ou `pytest`.

Exemple de test simple avec `unittest` (fichier `test_book.py`):

python
import unittest
from book import get_book_price, calculate_total_price, books # Assurez-vous d'importer le dictionnaire `books` si nécessaire pour les tests

class TestBookFunctions(unittest.TestCase):

    def test_get_book_price_existing(self):
        self.assertEqual(get_book_price("python_guide"), 25.99)
        self.assertEqual(get_book_price("machine_learning"), 55.25)

    def test_get_book_price_non_existing(self):
        self.assertEqual(get_book_price("unknown_book"), 0.00)

    def test_calculate_total_price_multiple_books(self):
        selected_books = ["python_guide", "data_science"]
        expected_total = books["python_guide"] + books["data_science"]
        self.assertAlmostEqual(calculate_total_price(selected_books), expected_total, places=2)

    def test_calculate_total_price_single_book(self):
        selected_books = ["web_dev"]
        expected_total = books["web_dev"]
        self.assertAlmostEqual(calculate_total_price(selected_books), expected_total, places=2)

    def test_calculate_total_price_with_non_existing_book(self):
        selected_books = ["python_guide", "non_existent_book"]
        expected_total = books["python_guide"]
        self.assertAlmostEqual(calculate_total_price(selected_books), expected_total, places=2)

    def test_calculate_total_price_empty_list(self):
        self.assertEqual(calculate_total_price([]), 0.00)

if __name__ == '__main__':
    unittest.main()


Pour exécuter les tests :

bash
python3 -m unittest test_book.py


## 🤝 Contribution

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce module, voici comment procéder :

1.  **Forkez** ce dépôt.
2.  **Créez une nouvelle branche** pour votre fonctionnalité ou correction de bug (`git checkout -b feature/ma-super-fonctionnalite`).
3.  **Implémentez** vos modifications et assurez-vous que tous les tests passent (et ajoutez de nouveaux tests si nécessaire).
4.  **Commitez** vos modifications (`git commit -am 'feat: Ajout d\'une fonctionnalité X'`).
5.  **Pushez** votre branche (`git push origin feature/ma-super-fonctionnalite`).
6.  **Ouvrez une Pull Request**.

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.