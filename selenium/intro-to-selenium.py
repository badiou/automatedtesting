# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
# Start the browser and navigate to http://automationpractice.com/index.php.
driver = webdriver.Chrome()
url='https://www.saucedemo.com/'

print('Navigation vers url:'+url)
driver.get(url)
# Find the element using the new syntax and send keys
username='ourobadiou'
motdepasse='B44674ng12n42020'
driver.find_element(By.CSS_SELECTOR, "input[id='user-name']").send_keys(username)

driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("B44674ng12n42020")

print('Saisie des informations d\'authentification:'+username)

# Trouver le bouton de connexion et cliquer dessus
#login_button = driver.find_element(By.ID, "input[id='login-button']")
#login_button.click()
# Attendre une interaction de l'utilisateur pour fermer le navigateur
input("Appuyez sur Entrée pour fermer le navigateur...")

# Fermer le navigateur
driver.quit()


