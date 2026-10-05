# ♻️ EcoMap

> **Sistema web colaborativo para localização, mapeamento e gestão comunitária de pontos de reciclagem.**

[![Node.js](https://img.shields.io/badge/Node.js-v18+-green.svg?style=flat-square&logo=node.js)](https://nodejs.org/)
[![Express](https://img.shields.io/badge/Express-4.x-lightgrey.svg?style=flat-square&logo=express)](https://expressjs.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-blue.svg?style=flat-square&logo=sqlite)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-Não_definida-yellow.svg?style=flat-square)](#-licença)
[![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-orange.svg?style=flat-square)](#-status-do-projeto)

O **EcoMap** é uma plataforma desenvolvida para a disciplina **Open Source Contribution & Collaboration** ([UniFecaf](https://www.unifecaf.com.br/)). O projeto une sustentabilidade urbana e práticas modernas de engenharia de software colaborativa (Git, GitHub Flow, Code Reviews e CI/CD preliminar).

---

## 📌 Sumário

- [🌱 Sobre o Projeto](#-sobre-o-projeto)
- [🎯 Objetivos](#-objetivos)
- [✨ Funcionalidades](#-funcionalidades)
- [🛠️ Tecnologias e Dependências](#️-tecnologias-e-dependências)
- [🏗️ Arquitetura e Modelagem de Dados](#️-arquitetura-e-modelagem-de-dados)
- [🚀 Como Executar](#-como-executar)
- [🔌 Documentação Detalhada da API](#-documentação-detalhada-da-api)
- [📁 Estrutura de Diretórios](#-estrutura-de-diretórios)
- [🔀 Fluxo de Trabalho e Contribuição](#-fluxo-de-trabalho-e-contribuição)
- [🧪 Testes e Qualidade](#-testes-e-qualidade)
- [👥 Equipe e Agradecimentos](#-equipe-e-agradecimentos)
- [📄 Licença](#-licença)

---

## 🌱 Sobre o Projeto

O descarte incorreto de resíduos sólidos é um dos principais desafios ambientais urbanos. Muitas vezes, o cidadão deseja reciclar, mas não sabe **onde** descartar materiais específicos (como óleo de cozinha, pilhas, eletrônicos ou vidro).

O **EcoMap** resolve esse problema agregando e mapeando pontos de coleta seletiva e ecopontos. A plataforma permite:
1. **Busca Inteligente:** Localização rápida de pontos por proximidade, cidade e tipos de materiais aceitos.
2. **Engajamento Comunitário:** Futuro cadastro e validação de novos pontos por parte dos próprios usuários.
3. **Privacidade por Design:** A geolocalização do usuário é processada exclusivamente no navegador cliente, garantindo privacidade total.

---

## 🎯 Objetivos

- **Acessibilidade Informacional:** Mapear ecopontos e locais de coleta de forma gratuita e intuitiva.
- **Filtros Precisos:** Permitir buscas que combinem múltiplos critérios (ex.: Cidade + Tipo de Resíduo + Termo de busca).
- **Práticas Open Source:** Servir como ambiente prático de aprendizado para padrões de colaboração com Git, revisão de código por Pull Requests e escrita de código limpo.
- **Extensibilidade:** Manter uma API REST desacoplada que permita no futuro a criação de aplicações mobile (React Native/Flutter) ou integrações com órgãos públicos.

---

## ✨ Funcionalidades

### ✅ Implementadas (Backend & Client Core)

- **API RESTful e Servidor HTTP:**
  - Arquitetura Express modularizada.
  - Endpoint dedicado de monitoramento e integridade (`GET /health`).
  - Tratamento centralizado de erros e sanitização de requisições.
- **Gestão de Dados e Filtros Avançados:**
  - Consulta de pontos com suporte a busca textual insensível a acentos/caixa alta (*case and accent insensitive*).
  - Normalização de tipos de materiais via **slugs** (ex.: `oleo-de-cozinha`, `baterias-e-pilhas`).
  - Agregação do total de pontos disponíveis por tipo de material (`GET /api/materiais`).
- **Recursos Client-Side (Frontend Leve):**
  - Integração com a API de Geolocalização do navegador (`navigator.geolocation`).
  - Cálculo de distância geodésica em linha reta (Fórmula de Haversine / aproximação Euclidiana local).
  - Ordenação automática dos pontos cadastrados do mais próximo ao mais distante.
  - Estados Visuais na Interface: Indicadores de carregamento (*loading*), feedbacks de lista vazia e tratamento de erros de rede.

### 🚧 Em Desenvolvimento (Roadmap)

- [ ] **Interface de Usuário (UI):** Dashboard responsivo em HTML5/CSS3/JS Moderno.
- [ ] **Mapa Interativo:** Integração com [Leaflet.js](https://leafletjs.com/) / OpenStreetMap.
- [ ] **CRUD Completo via Interface:** Formulário interativo para cadastro, edição e remoção de pontos com modais de confirmação.
- [ ] **Suíte de Testes Automatizados:** Testes unitários e de integração com Jest e Supertest.
- [ ] **Acessibilidade & Responsividade:** Conformidade com as diretrizes WCAG 2.1 (AA).

---

## 🛠️ Tecnologias e Dependências

| Categoria | Tecnologia | Uso / Descrição |
| :--- | :--- | :--- |
| **Runtime** | [Node.js](https://nodejs.org/) (v18+) | Ambiente de execução JavaScript |
| **Framework Web** | [Express](https://expressjs.com/) | Construção do servidor HTTP e rotas da API |
| **Banco de Dados** | [SQLite3](https://www.sqlite.org/) | Banco de dados relacional em arquivo local |
| **Driver BD** | [better-sqlite3](https://github.com/WiseLibs/better-sqlite3) | Cliente SQLite síncrono e de altíssimo desempenho para Node.js |
| **Segurança** | [Helmet](https://helmetjs.github.io/) | Configuração de headers HTTP de segurança |
| **Segurança** | [CORS](https://github.com/expressjs/cors) | Gerenciamento de políticas de Origem Cruzada |
| **Desenvolvimento**| [Nodemon](https://nodemon.io/) | Auto-reload do servidor durante o desenvolvimento |
| **Versionamento** | [Git](https://git-scm.com/) & [GitHub](https://github.com/) | Controle de versão e hospedagem do código fonte |

---

## 🏗️ Arquitetura e Modelagem de Dados

O projeto adota uma arquitetura em camadas bem definida (MVC / Layered Architecture):

```text
HTTP Request ➔ Routes ➔ Middlewares / Validators ➔ Controllers ➔ Services / Models ➔ SQLite DB

```

### Relacionamento no Banco de Dados

```text
+-------------------+       +---------------------------+       +-------------------+
|      pontos       |       |      ponto_materiais      |       |     materiais     |
+-------------------+       +---------------------------+       +-------------------+
| id (PK)           |1     *| ponto_id (FK)             |*     1| id (PK)           |
| nome              |<----->| material_id (FK)          |<----->| nome              |
| endereco          |       +---------------------------+       | slug              |
| cidade            |                                           +-------------------+
| latitude          |
| longitude         |
| horario_func      |
+-------------------+

```

---

## 🚀 Como Executar

### 📋 Pré-requisitos

Certifique-se de ter os seguintes utilitários instalados:

* **Node.js**: `v18.0.0` ou superior
* **npm**: `v9.0.0` ou superior
* **Git**: `v2.x` ou superior

Verifique no seu terminal:

```bash
node -v
npm -v
git --version

```

### 1. Clonar e Instalar

```bash
# Clone este repositório
git clone [https://github.com/GustavoTalgatti/EcoMap.git](https://github.com/GustavoTalgatti/EcoMap.git)

# Entre na pasta do projeto
cd EcoMap

# Instale as dependências
npm install

```

### 2. Configurar Variáveis de Ambiente

Crie o arquivo `.env` baseado no exemplo fornecido (`.env.example`):

* **Linux / macOS:**
```bash
cp .env.example .env

```


* **Windows (CMD):**
```cmd
copy .env.example .env

```


* **Windows (PowerShell):**
```powershell
Copy-Item .env.example .env

```



Exemplo do conteúdo padrão do `.env`:

```env
PORT=3000
NODE_ENV=development
DB_PATH=./src/database/ecomap.sqlite

```

> ⚠️ **Atenção:** O arquivo `.env` é ignorado pelo `.gitignore` e **jamais** deve ser commitado no repositório.

### 3. Inicializar e Popular o Banco de Dados

Para criar as tabelas e inserir a carga inicial de dados de exemplo (*seed*):

```bash
npm run db:seed

```

### 4. Executar a Aplicação

#### Modo de Desenvolvimento (com auto-reload):

```bash
npm run dev

```

#### Modo de Produção:

```bash
npm start

```

Acesse no seu navegador: `http://localhost:3000`

---

## 🔌 Documentação Detalhada da API

Todas as rotas de dados estão sob o prefixo `/api`.

### 1. Check de Saúde (`/health`)

* **`GET /health`**
* **Descrição:** Retorna o status operacional da API.
* **Resposta de Sucesso (`200 OK`):**
```json
{
  "status": "OK",
  "uptime": 120.45,
  "timestamp": "2026-10-05T23:00:00.000Z"
}

```





---

### 2. Pontos de Reciclagem (`/api/pontos`)

| Método | Endpoint | Descrição |
| --- | --- | --- |
| `GET` | `/api/pontos` | Retorna lista de pontos com suporte a query params de filtro |
| `GET` | `/api/pontos/:id` | Retorna os detalhes de um ponto específico por ID |
| `POST` | `/api/pontos` | Cadastra um novo ponto de reciclagem |
| `PUT` | `/api/pontos/:id` | Atualiza completamente as informações de um ponto |
| `DELETE` | `/api/pontos/:id` | Remove um ponto de reciclagem |

#### Parâmetros de Busca (`GET /api/pontos`):

| Parâmetro | Tipo | Exemplo | Descrição |
| --- | --- | --- | --- |
| `cidade` | `string` | `?cidade=Campinas` | Filtra pontos localizados na cidade informada |
| `material` | `string` | `?material=plastico` | Filtra pontos que aceitam o material informado (**slug**) |
| `busca` | `string` | `?busca=recicla` | Busca textual no nome do ponto ou no nome dos materiais aceitos |

#### Exemplo de Resposta (`GET /api/pontos?cidade=Campinas&material=vidro`):

```json
[
  {
    "id": 1,
    "nome": "Ecoponto Central Campinas",
    "endereco": "Av. Francisco Glicério, 1000 - Centro",
    "cidade": "Campinas",
    "latitude": -22.9056,
    "longitude": -47.0608,
    "horario_funcionamento": "Seg a Sex das 08h às 17h",
    "materiais": [
      { "id": 1, "nome": "Vidro", "slug": "vidro" },
      { "id": 2, "nome": "Plástico", "slug": "plastico" }
    ]
  }
]

```

#### Exemplo de Payload para Cadastro (`POST /api/pontos`):

```json
{
  "nome": "Ponto de Coleta Bairro das Flores",
  "endereco": "Rua das Rosas, 123",
  "cidade": "São Paulo",
  "latitude": -23.5505,
  "longitude": -46.6333,
  "horario_funcionamento": "Sábados das 09h às 13h",
  "materiais_ids": [1, 3, 5]
}

```

---

### 3. Materiais (`/api/materiais`)

* **`GET /api/materiais`**
* **Descrição:** Lista todos os materiais suportados pelo sistema e a quantidade total de pontos associados.
* **Resposta (`200 OK`):**
```json
[
  {
    "id": 1,
    "nome": "Óleo de Cozinha",
    "slug": "oleo-de-cozinha",
    "total_pontos": 12
  },
  {
    "id": 2,
    "nome": "Plástico",
    "slug": "plastico",
    "total_pontos": 45
  }
]

```





---

## 📁 Estrutura de Diretórios

```text
EcoMap/
├── public/                 # Arquivos estáticos servidos diretamente (CSS, JS, imagens)
├── src/
│   ├── config/             # Configurações globais (env vars, constantes)
│   ├── controllers/        # Camada de controle (processa requests e envia responses)
│   ├── database/           # Conexão com SQLite, schema SQL e script de seed
│   │   ├── schema.sql      # DDL de criação das tabelas
│   │   └── seed/           # Dados inciais para preenchimento do BD
│   ├── middlewares/        # Middlewares Express (validação, segurança, erros)
│   ├── models/             # Camada de dados (consultas SQL via better-sqlite3)
│   ├── routes/             # Definição das rotas e endpoints REST
│   ├── services/           # Regras de negócio e processamentos auxiliares
│   ├── utils/              # Funções utilitárias (formatadores, sanitizadores)
│   ├── validators/         # Schemas de validação de dados de entrada
│   ├── app.js              # Instância e configuração de middlewares da aplicação
│   └── server.js           # Ponto de entrada (boot) do servidor HTTP
├── tests/                  # Casos de testes automatizados
├── views/                  # Templates/Páginas HTML renderizadas
├── .env.example            # Template oficial de variáveis de ambiente
├── .gitignore              # Lista de arquivos/pastas ignorados pelo Git
├── CONTRIBUTING.md         # Guia detalhado de boas práticas e regras de contribuição
├── package.json            # Manifest do projeto (dependências e scripts)
├── package-lock.json       # Trava de versões exatas das dependências
└── README.md               # Documentação principal

```

---

## 🔀 Fluxo de Trabalho e Contribuição

Para garantir a estabilidade do código, adotamos um fluxo rigoroso baseado no **GitHub Flow**:

1. **Abra ou escolha uma Issue:** Nenhuma alteração deve ser feita sem estar associada a uma Issue.
2. **Crie uma Branch:** A partir da `main`, crie uma branch com nome descritivo:
* `feature/nome-da-funcionalidade` (para novos recursos)
* `fix/descricao-da-correcao` (para correção de bugs)
* `docs/melhoria-documentacao` (para documentação)


3. **Desenvolva e Faça Commits:** Mantenha commits pequenos e com mensagens claras.
4. **Submeta um Pull Request (PR):** Abra um PR apontando para a branch `main`.
5. **Code Review:** Aguarde a revisão de pelo menos um integrante do grupo antes de realizar o merge.

```text
  [Issue #12]
       │
       ▼
┌──────────────┐      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│  Criar       │ ───► │  Commit &    │ ───► │  Pull        │ ───► │  Code Review │ ───► Merge na
│  Branch      │      │  Push        │      │  Request     │      │  & Aprovação │      branch main
└──────────────┘      └──────────────┘      └──────────────┘      └──────────────┘

```

> 📖 Para diretrizes detalhadas sobre padrões de commits e guia passo a passo, leia o [CONTRIBUTING.md](https://www.google.com/search?q=./CONTRIBUTING.md).

---

## 🧪 Testes e Qualidade

Os testes automatizados garantem que novas implementações não quebrem funcionalidades existentes.

Para rodar a suíte de testes:

```bash
npm test

```

Para rodar os testes em modo watch (reexecuta ao alterar arquivos):

```bash
npm run test:watch

```

---

## 👥 Equipe e Agradecimentos

Projeto desenvolvido para a disciplina **Open Source Contribution & Collaboration** da instituição **UniFecaf**.

* **Docente Responsável:** Prof. Robson Cardoso

### Integrantes / Desenvolvedores

| Integrante | GitHub |
| --- | --- |
| **Cláudio José Rodrigues de Oliveira Junior** | [@Claudio-Jr](https://www.google.com/search?q=https://github.com/Claudio-Jr) |
| **Felipe Pardinho Belarmino** | [@FelipePardinho](https://www.google.com/search?q=https://github.com/FelipePardinho) |
| **Gabriela Camarço** | [@GabrielaCamarco](https://www.google.com/search?q=https://github.com/GabrielaCamarco) |
| **Igor Ferreira Alves** | [@IgorAlves](https://www.google.com/search?q=https://github.com/IgorAlves) |
| **Luis Gustavo dos Santos Talgatti** | [@GustavoTalgatti](https://www.google.com/search?q=https://github.com/GustavoTalgatti) |
| **Matheus Silva Dantas** | [@MatheusDantas](https://www.google.com/search?q=https://github.com/MatheusDantas) |
| **Rickelmy Augusto Souza Pacheco** | [@RickelmyPacheco](https://www.google.com/search?q=https://github.com/RickelmyPacheco) |

---

## 📄 Licença

Este projeto está sob a licença **MIT** (ou licença a definir conforme orientação da instituição). Consulte o arquivo `LICENSE` para mais informações.

```

```
