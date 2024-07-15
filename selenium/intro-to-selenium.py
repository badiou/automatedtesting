from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_item"))
)

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

#######################################################################################
# Vérifier le clic sur le bouton add-to-cart-sauce-labs-backpack
#######################################################################################
try:
    addcarts = driver.find_elements(By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory")
    if addcarts:
        print(f"Nombre de boutons 'Add to cart' : {len(addcarts)}")
        for addcart in addcarts:
            print(f"Bouton trouvé avec le texte : {addcart.text}")
            addcart.click()
            print('Clic sur le bouton avec la classe Add cart réussi')

            # Attendre que le bouton se transforme en bouton "Remove"
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".btn_secondary.btn_small.btn_inventory"))
            )
            print('Le bouton s\'est transformé en bouton Remove')
    else:
        print("Aucun produit trouvé sur la page.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")

# Attendre une interaction de l'utilisateur pour fermer le navigateur
input("Appuyez sur Entrée pour fermer le navigateur...")

# Fermer le navigateur
driver.quit()
