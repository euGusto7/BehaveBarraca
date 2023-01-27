from behave import given, when, then
from time import sleep
from selenium import webdriver

navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get("http://localhost/ProjetoCake/ProjetoC/users/login")

#---------------------LOGIN ADMINISTRADOR-----------------------#

@given(u'que o administrador está na página de login')
def step_aa(context):
    pass


@when(u'o administrador preencher os campos "username", "password"')
def step_administrador(context):
    context.element = navegador.find_element('xpath', '//*[@id="username"]')
    context.element.send_keys("administrador")
    context.element = navegador.find_element('xpath', '//*[@id="password"]')
    context.element.send_keys("123")
    sleep(1)


@when(u'se os campos estiverem corretos')
def step_acessar(context):
    context.element.submit()


#---------------CADASTRANDO UMA FRUTA--------------------#

@then(u'poderá cadastrar uma fruta')
def step_fim1(context):
    sleep(3)
    context.element = navegador.find_element('xpath', '//*[@id="nome-da-fruta"]')
    context.element.send_keys("Banana")
    sleep(1)
    context.element = navegador.find_element('xpath', '//*[@id="classificacao-id"]')
    context.element.send_keys("de primeira")
    sleep(1)
    context.element = navegador.find_element('xpath', '//*[@id="fresca"]')
    context.element.click()
    sleep(1)
    context.element = navegador.find_element('xpath', '//*[@id="quantidade-disponivel"]')
    context.element.send_keys("4")
    sleep(1)
    context.element = navegador.find_element('xpath', '//*[@id="valor"]')
    context.element.send_keys("5")
    sleep(1)
    context.element.submit()
    sleep(3)


#------------VISUALIZANDO A FRUTA-----------#

@given(u'que o administrador está nas frutas cadastradas')
def step_view(context):
    pass
sleep(4)
    
@when(u'clicar em visualizar')
def step_view(context):
    context.element = navegador.find_element('xpath', '/html/body/main/div/div/div[2]/table/tbody/tr/td[7]/a[1]')
    context.element.click()
    sleep(5)

@then(u'poderá ver as informações da fruta')
def step_enviar(context):
    context.element = navegador.find_element('xpath', '/html/body/nav/div[2]/div/a[1]')
    context.element.click()
    sleep(3)

#------------EDITANDO A FRUTA-----------#

@given(u'que o administrador estará nas frutas cadastradas')
def step_editar(context):
    pass
sleep(4)

@when(u'clicar em editar')
def step_edit(context):
    context.element = navegador.find_element('xpath', '/html/body/main/div/div/div[2]/table/tbody/tr[1]/td[7]/a[2]')
    context.element.click()
    sleep(3)
    context.element = navegador.find_element('xpath', '//*[@id="classificacao-id"]')
    context.element.send_keys("de segunda")
    sleep(2)
    context.element = navegador.find_element('xpath', '//*[@id="fresca"]')
    context.element.click()
    sleep(2)

@then(u'poderá editar a fruta')
def step_enviar(context):
    context.element.submit()
    sleep(3)
    context.element = navegador.find_element('xpath', '/html/body/nav/div[2]/div/a[3]')
    context.element.click()
    sleep(5)


#------------LOGIN VENDEDOR-------------#

@given(u'que o vendedor esteja na página de login')
def step_login_vendedor(context):
    pass

@when(u'o vendedor preencha os campos "username", "password"')
def step_preencher_vendedor(context):
    context.element = navegador.find_element('xpath', '//*[@id="username"]')
    context.element.send_keys("vendedor")
    sleep(2)
    context.element = navegador.find_element('xpath', '//*[@id="password"]')
    context.element.send_keys("123")
    sleep(2)
    context.element.submit()
    sleep(3)

#-----------------PESQUISAR---------------------#

@then(u'poderá pesquisar e vender uma fruta')
def step_psq(context):
    sleep(2)
    context.element = navegador.find_element('xpath', '//*[@id="pesquisar"]')
    context.element.send_keys("Banana")
    sleep(1)
    context.element.submit()
    sleep(3)

    context.element = navegador.find_element('xpath', '/html/body/nav/div[2]/a[3]')
    context.element.click()
    sleep(1)

#-------------VENDENDO A FRUTA----------------#

    context.element = navegador.find_element('xpath', '//*[@id="fruta-id"]')
    context.element.send_keys("Banana")
    sleep(1)
    context.element = navegador.find_element('xpath', '//*[@id="quantidade"]')
    context.element.send_keys("2")
    sleep(1)
    context.element = navegador.find_element('xpath', '//*[@id="desconto-id"]')
    context.element.send_keys("nenhum")
    sleep(1)
    context.element = navegador.find_element('xpath','//*[@id="valor-da-venda"]')
    context.element.send_keys("2")
    sleep(1)
    context.element.submit()
    sleep(4)

#---------VISUALIZANDO A VENDA---------#

@given(u'que o vendedor está no relatório de vendas')
def step_v(context):
    pass
sleep(4)
    
@when(u'clicar para visualizar a venda')
def step_vv(context):
    context.element = navegador.find_element('xpath', '/html/body/main/div/div/div[2]/table/tbody/tr/td[7]/a[1]')
    context.element.click()
    sleep(5)
    
@then(u'poderá visualizar as informações da venda')
def step_i(context):
    context.element = navegador.find_element('xpath', '/html/body/nav/div[2]/a[1]')
    context.element.click()
    sleep(3)

#----------------EDITANDO A VENDA--------------#

@given(u'que o vendedor esteja no relatório de vendas')
def step_editar(context):
    pass
sleep(4)

@when(u'clicar para editar uma venda')
def step_edit(context):
    context.element = navegador.find_element('xpath', '/html/body/main/div/div/div[2]/table/tbody/tr[1]/td[7]/a[2]')
    context.element.click()
    sleep(3)
    context.element = navegador.find_element('xpath', '//*[@id="quantidade"]')
    context.element.send_keys("1")
    sleep(2)
    context.element = navegador.find_element('xpath', '//*[@id="desconto-id"]')
    context.element.send_keys("10")
    sleep(2)
    context.element = navegador.find_element('xpath', '//*[@id="valor-da-venda"]')
    context.element.send_keys("1")
    sleep(2)

@then(u'a venda será editada')
def step_enviar(context):
    context.element.submit()
    sleep(3)
    context.element = navegador.find_element('xpath', '/html/body/nav/div[2]/a[4]')
    context.element.click()
    sleep(8)

      # This was autogenerated using cucumber syntax.
      # Please convert to use regular expressions, as Behave does not currently support Cucumber Expressions