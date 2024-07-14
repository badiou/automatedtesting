# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
# Start the browser and navigate to http://automationpractice.com/index.php.
driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
# Find the element using the new syntax and send keys
driver.find_element(By.CSS_SELECTOR, "input[id='user-name']").send_keys("ourobadiou")

driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("ourobadiou")


# Trouver le bouton de connexion et cliquer dessus
#login_button = driver.find_element(By.ID, "input[id='login-button']")
#login_button.click()
# Attendre une interaction de l'utilisateur pour fermer le navigateur
input("Appuyez sur Entrée pour fermer le navigateur...")

# Fermer le navigateur
driver.quit()


