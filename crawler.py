
def academico():
    urlLogin = 'https://academico.ifpi.edu.br/qacademico/index.asp?t=1001'

    body = {
        "SUBMIT":'63ba1eadfd0c5d3480d830eed2de80b0',
        "LOGIN":"29ab4c2dedf5c19367c3025928a72761",
        "SENHA":"86550c9cbee01fff6a2e5a2aad664be2",
        "TIPO_USU":"491d80bf6cb1faf9a265829d8e67fabf"

    }

    headers = {
        "Content-type": "application/x-www-form-urlencoded"
    }

    sucess = requests.post(urlLogin,data=body,headers=headers)
    print(sucess.text)

academico()

#"https://academico.ifpi.edu.br/qacademico/index.asp?t=2032&COD_MATRICULA=-1&cmbanos=2018&cmbperiodos=1&Exibir=Exibir+Boletim"


#url = "https://academico.ifpi.edu.br/qacademico/index.asp?t=2032&COD_MATRICULA=-1&cmbanos=2018&cmbperiodos=1&Exibir=Exibir+Boletim"
#pages = download(url)

#soup = BeautifulSoup(pages, "html.parser")
#print(soup)
#tabela = soup.findAll('table',{'class':'rotulo'})[1]

#tabela = soup.find_all(['tr','td'])
#classe = soup.select('td')
#linha = soup({'td':'media'})
#print(linha)

#classe = tabela.find_all('tr')

#linhas = tabela.findAll('tr')

#object = {}




#tabela = soup.findAll('tbody', {'class': 'rotulo'})

#linhas = tabela.findAll('tr')#


#print(tabela)
#print(classe)

