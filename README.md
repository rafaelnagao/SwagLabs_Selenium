# 🧪 SwagLabs Selenium Pytest

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge" />
  <img src="https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium Badge" />
  <img src="https://img.shields.io/badge/Pytest-Test%20Framework-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest Badge" />
  <img src="https://img.shields.io/badge/GitHub%20Actions-CI-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions Badge" />
  <img src="https://img.shields.io/badge/Chrome-Headless-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Chrome Badge" />
</p>

Projeto de automação de testes end-to-end para o site **SauceDemo / Swag Labs**, desenvolvido com Python, Selenium WebDriver e pytest. A suíte segue Page Object Model (POM), usa fixtures para setup/teardown e possui integração contínua com GitHub Actions.

***

## 📌 Visão geral

Este projeto foi criado para validar fluxos principais da aplicação, como login, navegação, carrinho e checkout, com foco em organização, reutilização de código e estabilidade da execução. O uso de page objects e fixtures ajuda a manter os testes mais legíveis e menos frágeis.

## 🛠️ Stack

- 🐍 Python 3
- 🌐 Selenium WebDriver
- ✅ pytest
- 📊 pytest-cov
- ⚙️ GitHub Actions
- 🧭 Google Chrome Headless

O pytest oferece suporte nativo a fixtures e markers, o que facilita a separação de setup, teardown e grupos funcionais de testes.

## 📂 Estrutura do projeto

```text
SwagLabs_Selenium/
├── .github/
│   └── workflows/
│       └── selenium-ci.yml
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   └── cart_page.py
├── tests/
│   ├── 01_Login/
│   ├── 02_Homepage/
│   └── 04_Cart/
├── conftest.py
├── pytest.ini
└── requirements.txt
```

A separação entre `pages`, `tests` e arquivos de configuração segue a organização típica de frameworks Selenium com POM.

## ✅ Funcionalidades cobertas

- 🔐 Login com sucesso.
- 🚫 Login com falhas de validação.
- 🏠 Homepage, filtros e menu lateral.
- 🛒 Carrinho de compras.
- 🧾 Checkout step one e step two.
- 🔁 Fluxos end-to-end com markers.

Os markers do pytest permitem executar grupos específicos da suíte sem precisar rodar todos os cenários.

## ⚙️ Pré-requisitos

Antes de executar localmente:

- Python 3.12 ou compatível.
- Google Chrome instalado.
- Ambiente virtual recomendado.
- Dependências instaladas com `requirements.txt`.

O pipeline em CI também usa Python 3.12 e Chrome headless para manter o comportamento consistente entre máquina local e GitHub Actions.

## 🚀 Instalação

Clone o repositório:

```bash
git clone https://github.com/rafaelnagao/SwagLabs_Selenium.git
cd SwagLabs_Selenium
```

Crie e ative o ambiente virtual:

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## ▶️ Como executar

### Rodar a suíte completa

```bash
python -m pytest -v
```

### Coletar os testes

```bash
python -m pytest --collect-only -q
```

### Rodar por marker

```bash
python -m pytest -v -m login
python -m pytest -v -m homepage
python -m pytest -v -m cart
python -m pytest -v -m e2e
```

A documentação do pytest recomenda declarar markers no `pytest.ini` para evitar avisos e permitir organização clara da suíte.

## 🧩 Configuração do browser

O WebDriver é configurado no `conftest.py` com suporte a execução local e em CI. Em ambiente GitHub Actions, o Chrome roda em modo headless com opções como `--no-sandbox` e `--disable-dev-shm-usage`, padrão comum para maior estabilidade em runners Linux.

As fixtures com `yield` fazem a criação e finalização do navegador de forma controlada, que é o padrão recomendado pelo pytest para gerenciamento de recursos.

## 🧠 Boas práticas aplicadas

- Page Object Model para encapsular ações da interface.
- Fixtures para setup e teardown reutilizáveis.
- Isolamento entre testes para evitar shared state.
- Markers para segmentação funcional.
- Pipeline automatizado com GitHub Actions.

A recomendação oficial do Selenium é evitar compartilhamento de estado entre testes, pois isso reduz flakiness e dependência da ordem de execução.

## 🔄 CI com GitHub Actions

O workflow automatiza:

- Instalação de dependências.
- Setup do Python.
- Setup do Google Chrome.
- Execução da suíte com pytest.
- Geração de relatório JUnit XML.
- Upload de artifacts.

Esse fluxo está alinhado com o uso do GitHub Actions para pipelines Python com pytest e publicação de resultados de execução.

## 📦 Artefatos

Durante o pipeline, podem ser gerados e publicados:

- `reports/junit.xml`
- `screenshots/`

O upload de artifacts é um recurso padrão do GitHub Actions e facilita depuração de falhas em CI.

## 📁 Arquivos principais

| Arquivo | Descrição |
|---|---|
| `conftest.py` | Fixtures, setup e teardown do WebDriver. |
| `pytest.ini` | Markers, testpaths e configuração do pytest. |
| `pages/` | Implementação dos page objects. |
| `tests/` | Casos de teste organizados por funcionalidade. |
| `.github/workflows/selenium-ci.yml` | Pipeline de integração contínua. |

## 📈 Melhorias futuras

- Adicionar job de lint.
- Separar smoke tests e e2e.
- Criar matriz de versões Python.
- Publicar relatórios mais ricos no CI.

Essas extensões são comuns em pipelines mais maduros para projetos Python com testes automatizados.
