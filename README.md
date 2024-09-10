# PDI-Feevale
Este projeto é uma aplicação de Processamento Digital de Imagens (PDI) desenvolvida utilizando Vue.js e FastAPI, com suporte para execução tanto na web quanto no desktop.

## Pré-requisitos
Certifique-se de ter as seguintes ferramentas instaladas em sua máquina antes de continuar:

* Node.js (versão 14.x ou superior)
* npm (gerenciador de pacotes do Node.js)
* Python (para a API FastAPI)
## Instalação
### Windows
Execute o script instalar.bat para instalar todas as dependências do projeto. O script cuidará da instalação dos pacotes necessários tanto para o front-end quanto para a API.
## Outros sistemas operacionais
### Para usuários de Linux ou Mac, siga estas etapas:

```bash
# Instale as dependências do front-end
npm install

# Instale as dependências do back-end
pip install -r requirements.txt
```
## Executando o projeto
### Modo Web
Para rodar a aplicação no navegador, execute o seguinte comando:

```bash
npm run dev
```
A aplicação estará disponível em http://localhost:8080.

### Modo Desktop
Para rodar a versão desktop com Electron, utilize o seguinte comando:

```bash
npm run electron:serve
```
## Funcionalidades
A aplicação oferece as seguintes operações de processamento de imagens:

* Transladar: Move a imagem em uma direção especificada.
* Rotacionar: Gira a imagem em torno de seu eixo central.
* Espelhar: Gera uma cópia invertida da imagem horizontalmente ou verticalmente.
* Aumentar/Diminuir: Altera a escala da imagem, aumentando ou diminuindo seu tamanho.
## Contribuição
Sinta-se à vontade para fazer um fork deste repositório e propor melhorias através de pull requests.
