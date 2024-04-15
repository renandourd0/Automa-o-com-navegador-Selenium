from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("http://www.bancocn.com/admin/login.php")


navegador.find_element('xpath', 
                       '//*[@id="block-login"]/div/form/div[1]/div[2]/input').send_keys("admin")
navegador.find_element('xpath', 
                       '//*[@id="block-login"]/div/form/div[2]/div[2]/input').send_keys("senhafoda")

navegador.find_element('xpath', '//*[@id="block-login"]/div/form/div[3]/div/button').click()

navegador.find_element('xpath', '/html/body/a').click()