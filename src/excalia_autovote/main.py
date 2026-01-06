from seleniumbase import Driver

driver = Driver(uc=True)
url = ("https://top-serveurs.net/minecraft/vote/excalia?pseudo=Wallans")
driver.uc_open_with_reconnect(url, 4)
driver.uc_gui_click_captcha()
driver.quit()