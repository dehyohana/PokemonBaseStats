**Table of Contents**

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#arquitetura-projeto">Arquitetura do projeto</a>
      <ul>
        <li><a href="#pre-requisitos">Pré requisitos</a></li>
      </ul>
    </li>
    <li>
      <a href="#instalar-programas">Como instalar os programas:</a>
    </li>
    <li><a href="#uso">Utilização</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


# Pokémon Stats
## Tabela de status dos pokemóns - Abr/22


Repositório de códigos criados para extrair o base stats dos pokemons através de uma página web, criar uma tabela com os valores e salvar em banco de dados PostgreSQL gerenciado por container docker através do Docker Compose.
- Página web utilizada: https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_base_stats_(Generation_VIII-present)

**Construído com:**
-   Python
-   PostgreSQL
-   Docker
-   Docker Compose

## Arquitetura do projeto
![app](https://svgshare.com/i/gMh.svg)


## Pré requisitos
- [Docker]
- [Docker Compose]

## Como instalar os programas
Atualize o pacote apt e instale os pacotes para permitir que o apt use um repositório sobre HTTPS:
```sh
 sudo apt-get update
 sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
``` 
Adicione a chave GPG oficial do Docker:
```sh
 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
``` 
Utilize o seguinte comando para configurar o repositório estável:
```sh
 echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
``` 
Instale a Docker Engine:
```sh
 sudo apt-get update
 sudo apt-get install docker-ce docker-ce-cli containerd.io
``` 

- [Docker Compose]

Utilize o seguinte comando para baixar a versão estável e mais atual do Docker Compose:
```sh
 sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
``` 
Aplique permissões executáveis ao binário:
```sh
 sudo chmod +x /usr/local/bin/docker-compose
``` 
Teste a instalação:
```sh
  docker-compose --version
``` 
**Adicionais**
 - [Virtualenv]
 Uma virtual env permite a execução do projeto em um ambiente virtual, isto é, ela empacota todas as dependências que um projeto precisa e armazena em um diretório, fazendo com que nenhum pacote seja instalado diretamente no sistema operacional. Sendo assim, cada projeto pode possuir seu próprio ambiente e, consequentemente, suas bibliotecas em versões específicas.

Primeiro, instale o pip:
```sh
sudo apt-get install python3-pip
```
Instale o virtual env utilizando o pip:
```sh
sudo pip3 install virtualenv
```

## Utilização
Clone o repositório:

```sh
git clone dehyohana/PokemonBaseStats
```
Após instalar os recursos e clonar o projeto, caso deseje criar um ambiente virtual de execução com as bibliotecas necessárias para a execução, utilize o seguinte comando no diretório do projeto:
```sh
make init
```
Para utilização das versões dos pacotes utilizados na construção do projeto semelhantemente é possível utilizar o comando:
```sh
make init-poetry
```

Crie variáveis ambientes com as credenciais para conexão do banco de dados. Por exemplo, posso criar um arquivo .env com as seguintes variáveis ambientes:

```sh
 POSTGRES_USER=root
 POSTGRES_PASSWORD=root
 POSTGRES_DATABASE=pokemon_stats
 POSTGRES_ADDRESS=localhost
```

Uma vez definidas, você pode criar o container indo no diretório Docker e executando o comando:
```
docker-compose up 
```
Você pode querer deixar o terminal livre, para isto adicione a tag -d no final do comando acima.
Agora basta executar o comando main.py para criarmos um banco de dados com a tabela do status dos nossos pokémons :) 

   [docker]: <https://docs.docker.com/engine/install/ubuntu/>
   [docker compose]: <https://docs.docker.com/compose/install/>
   [virtualenv]: <https://gist.github.com/frfahim/73c0fad6350332cef7a653bcd762f08d>
  
<!-- CONTACT -->
## Contato

Deborah Yohana Bertoldo da Silva - [Linkedin](https://www.linkedin.com/in/deborah-yohana-bertoldo/) - deh.yohana@gmail.com

Project Link: [Github](https://github.com/dehyohana)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Sqlalchemy](https://www.sqlalchemy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Docker](https://www.docker.com/)
* [Postgresql](https://www.postgresql.org/)