from selenium import webdriver

from selenium.webdriver.common.keys import Keys

#
#driver = webdriver.Chrome(CAMINHO ONDE ESTA A PASTA)
driver = webdriver.Chrome(executable_path=r'./chromedriver')

#comando pra abrir o link de algum site // é preciso ter https ou http
#.get abre uma página especifica

driver.get('http://localhost:8765/users/login')

driver.find_element("name", "username").send_keys("administrador")
driver.find_element("name", "password").send_keys("123")
driver.find_element("xpath",'/html/body/main/div/form/button').click()


driver.find_element("name", "nome_da_fruta").send_keys("Maçã")
driver.find_element("name", "classificacao_id").send_keys("de primeira")
driver.find_element("xpath",'//*[@id="fresca"]').click()
driver.find_element("name", "qtde_disponivel").send_keys("1")
driver.find_element("name", "valor").send_keys("2.60")
#botao de cadastrar
driver.find_element("xpath",'/html/body/main/div/div/div/div/form/button').click()
#sair
#driver.find_element("xpath",'/html/body/nav/div[2]/div/a[3]').click()

#driver.get('https://www.google.com.br/')

#driver.find_element("name", "q").send_keys("Olá") # send_keys('') digitar algum valor

#driver.find_element("name", "q").send_keys(Keys.RETURN) # Keys.RETURN = ENTER

