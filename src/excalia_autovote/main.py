from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

def topServeurVote(pseudo):
    from seleniumbase import Driver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    driver = Driver(uc=True)
    pseudo = os.getenv("PSEUDO", "Wallans")
    url = f"https://top-serveurs.net/minecraft/vote/excalia?pseudo={pseudo}"
    driver.uc_open_with_reconnect(url, 4)

    # Attendre le pop-up et cliquer sur "Autoriser"
    wait = WebDriverWait(driver, 10)
    bouton_autoriser = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Autoriser')]"))
    )
    bouton_autoriser.click()

    # Validation du captcha (click sur le bouton de validation)
    driver.uc_gui_click_captcha()

    # Attendre la validation du captcha et valider le vote
    wait = WebDriverWait(driver, 10)
    bouton_valider = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Voter')]"))
    )
    bouton_valider.click()

    driver.quit()