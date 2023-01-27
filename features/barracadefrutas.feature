# language: pt

Funcionalidade: Entrando no sistema da barraca de frutas

    Cenário: Cadastrar uma fruta no sistema
        Dado que o administrador está na página de login
        Quando o administrador preencher os campos "username", "password"
        E se os campos estiverem corretos
        Então poderá cadastrar uma fruta

    Cenário: Visualizando uma fruta
        Dado que o administrador está nas frutas cadastradas
        Quando clicar em visualizar
        Então poderá ver as informações da fruta

    Cenário: Editando uma fruta
        Dado que o administrador estará nas frutas cadastradas
        Quando clicar em editar
        Então poderá editar a fruta

    Cenário: Realizar uma venda no sistema
        Dado que o vendedor esteja na página de login
        Quando o vendedor preencha os campos "username", "password"
        Então poderá pesquisar e vender uma fruta

    Cenário: Visualizando uma venda
        Dado que o vendedor está no relatório de vendas
        Quando clicar para visualizar a venda
        Então poderá visualizar as informações da venda

    Cenário: Editando uma venda
        Dado que o vendedor esteja no relatório de vendas
        Quando clicar para editar uma venda
        Então a venda será editada