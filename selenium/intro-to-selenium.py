#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Démarrer le navigateur et naviguer vers le site web
driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

# Saisir le nom d'utilisateur
username_input = driver.find_element(By.CSS_SELECTOR, "input#user-name")
username_input.send_keys("standard_user")  # Utilisateur de test

# Saisir le mot de passe
password_input = driver.find_element(By.CSS_SELECTOR, "input#password")
password_input.send_keys("secret_sauce")  # Mot de passe de test

# Trouver le bouton de connexion et cliquer dessus
login_button = driver.find_element(By.CSS_SELECTOR, "input#login-button")
login_button.click()

# Attendre quelques secondes pour permettre le chargement de la page suivante
driver.implicitly_wait(5)  # Attente implicite de 5 secondes

# Vérifier la présence des produits sur la page suivante
try:
    products = driver.find_elements(By.CSS_SELECTOR, ".inventory_item")
    if products:
        print(f"Nombre de produits trouvés : {len(products)}")
        for product in products:
            print(product.text)
    else:
        print("Aucun produit trouvé sur la page.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")

# Attendre une interaction de l'utilisateur pour fermer le navigateur
input("Appuyez sur Entrée pour fermer le navigateur...")

# Fermer le navigateur
driver.quit()
