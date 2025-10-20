# Guia de Deploy e Configuração do Sistema de Capoeira "Eu Sou Ninja" no Render

Este guia detalha o processo de deploy do sistema "Eu Sou Ninja" em um serviço Web no Render, incluindo a configuração de um banco de dados PostgreSQL, e aborda a correção do erro `ModuleNotFoundError: No module named 'src'`.

## 1. Diagnóstico e Correção do Erro `ModuleNotFoundError: No module named 'src'`

O erro `ModuleNotFoundError: No module named 'src'` ocorre quando o servidor Gunicorn, configurado no `Procfile`, tenta importar o módulo `main` de um subdiretório `src` que não existe na estrutura de arquivos do projeto. O caminho `src.main:app` indica que `main.py` estaria dentro de uma pasta `src`.

**Causa Raiz:**

O `Procfile` original especificava `web: gunicorn --bind 0.0.0.0:$PORT src.main:app`. Isso instrui o Gunicorn a procurar por um arquivo `main.py` dentro de um diretório `src`. No entanto, a estrutura do projeto fornecida tem `main.py` diretamente na raiz do projeto, e os módulos (`models`, `routes`) são importados diretamente, sem um prefixo `src`.

**Solução:**

1.  **Ajuste do `Procfile`:** Modificamos o `Procfile` para apontar diretamente para `main:app`, indicando que o arquivo `main.py` está na raiz do projeto. O novo `Procfile` ficou assim:

    ```
    web: gunicorn --bind 0.0.0.0:$PORT main:app
    ```

2.  **Ajuste das Importações nos Arquivos Python:** Todas as importações que faziam referência a `src.models` ou `src.routes` foram atualizadas para `models` e `routes` respectivamente. Por exemplo, `from src.models.user import User, db` foi alterado para `from models.user import User, db`.

3.  **Estrutura de Diretórios:** Garantiu-se que os diretórios `models` e `routes` (e `static`) estivessem na raiz do projeto, ao lado de `main.py`.

## 2. Configuração do Banco de Dados PostgreSQL no Render

Para garantir persistência de dados para múltiplos usuários, o sistema foi configurado para usar PostgreSQL no Render. O Render oferece um serviço de banco de dados PostgreSQL gerenciado que pode ser facilmente integrado ao seu serviço web.

### 2.1. Alterações no `main.py` para Suporte a PostgreSQL

O arquivo `main.py` foi modificado para ler a URL do banco de dados a partir de uma variável de ambiente `DATABASE_URL`. Esta é a maneira padrão de conectar aplicações a bancos de dados em ambientes de nuvem como o Render.

```python
# Database configuration - PostgreSQL for Render
database_url = os.environ.get(\'DATABASE_URL\')
if database_url and database_url.startswith(\'postgres://\'):
    # Fix for SQLAlchemy 1.4+ which requires postgresql:// instead of postgres://
    database_url = database_url.replace(\'postgres://\', \'postgresql://\', 1)

app.config[\'SQLALCHEMY_DATABASE_URI\'] = database_url or \'sqlite:///app.db\'
app.config[\'SQLALCHEMY_TRACK_MODIFICATIONS\'] = False
```

**Explicação:**

*   `os.environ.get('DATABASE_URL')`: O Render injetará automaticamente a URL de conexão do seu banco de dados PostgreSQL nesta variável de ambiente.
*   `database_url.replace('postgres://', 'postgresql://', 1)`: Uma correção comum para compatibilidade com versões mais recentes do SQLAlchemy, que esperam o esquema `postgresql://` em vez de `postgres://`.
*   `'sqlite:///app.db'`: Para desenvolvimento local, o sistema ainda pode usar SQLite se a variável `DATABASE_URL` não estiver definida.

### 2.2. Adição de `psycopg2-binary` ao `requirements.txt`

Para que a aplicação Python se conecte a um banco de dados PostgreSQL, é necessário um driver. O `psycopg2-binary` é o driver mais comum para PostgreSQL em Python. Ele foi adicionado ao `requirements.txt`:

```
psycopg2-binary==2.9.9
```

### 2.3. Configuração do `render.yaml` (Infraestrutura como Código)

Para automatizar a criação do serviço web e do banco de dados no Render, um arquivo `render.yaml` foi criado. Este arquivo define a infraestrutura do seu aplicativo.

```yaml
services:
  - type: web
    name: eu-sou-ninja-system
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn --bind 0.0.0.0:$PORT main:app
    plan: free
    envVars:
      - key: SECRET_KEY
        generateValue: true
      - key: FLASK_ENV
        value: production
    disk:
      name: eu-sou-ninja-disk
      mountPath: /opt/render/project/src/data
      sizeGB: 1

databases:
  - name: eu-sou-ninja-db
    databaseName: eu_sou_ninja
    user: eu_sou_ninja_user
    plan: free
```

**Explicação dos Campos:**

*   **`services`**: Define os serviços que compõem sua aplicação.
    *   `type: web`: Indica que é um serviço web.
    *   `name: eu-sou-ninja-system`: Nome do seu serviço web.
    *   `env: python`: Ambiente de execução Python.
    *   `buildCommand: pip install -r requirements.txt`: Comando para instalar as dependências durante o deploy.
    *   `startCommand: gunicorn --bind 0.0.0.0:$PORT main:app`: Comando para iniciar a aplicação Gunicorn. Note que `main:app` agora está correto.
    *   `plan: free`: Utiliza o plano gratuito do Render.
    *   `envVars`: Variáveis de ambiente para o serviço web.
        *   `SECRET_KEY`: Chave secreta para o Flask. `generateValue: true` faz o Render gerar uma automaticamente.
        *   `FLASK_ENV: production`: Define o ambiente como produção.
    *   `disk`: Configura um disco persistente para armazenar arquivos, se necessário (não usado diretamente pelo DB aqui, mas útil para logs ou uploads).
*   **`databases`**: Define os serviços de banco de dados.
    *   `name: eu-sou-ninja-db`: Nome do serviço de banco de dados.
    *   `databaseName: eu_sou_ninja`: Nome do banco de dados.
    *   `user: eu_sou_ninja_user`: Usuário do banco de dados.
    *   `plan: free`: Utiliza o plano gratuito do Render para o banco de dados.

## 3. Ajuste da Estrutura de Arquivos para o Render

A estrutura de arquivos foi organizada para ser compatível com o deploy no Render. O projeto agora tem a seguinte estrutura na raiz:

```
eu_sou_ninja_render_fixed/
├── main.py                 # Ponto de entrada da aplicação Flask
├── requirements.txt        # Dependências Python
├── Procfile                # Comando de inicialização do Gunicorn
├── render.yaml             # Definição da infraestrutura no Render
├── models/                 # Módulos de modelos de dados
│   ├── __init__.py
│   ├── user.py
│   ├── student.py
│   ├── class_model.py
│   └── attendance.py
├── routes/                 # Módulos de rotas da API
│   ├── __init__.py
│   ├── auth.py
│   ├── user.py
│   ├── student.py
│   ├── class_routes.py
│   ├── attendance.py
│   └── reports.py
└── static/                 # Arquivos estáticos (HTML, CSS, JS)
    ├── index.html
    └── app.js
```

Esta estrutura garante que o Gunicorn e o Flask encontrem todos os arquivos e módulos corretamente.

## 4. Passos para Deploy no Render

Com o projeto corrigido e o `render.yaml` configurado, siga estes passos para fazer o deploy:

1.  **Crie um Repositório Git:** Se você ainda não tem, crie um repositório Git (por exemplo, no GitHub) com todos os arquivos do projeto (`eu_sou_ninja_render_fixed`).
2.  **Conecte seu Repositório ao Render:**
    *   Acesse o painel do Render (app.render.com).
    *   Clique em "New Blueprint Instance".
    *   Conecte seu repositório Git onde o arquivo `render.yaml` está localizado.
3.  **Deploy Automático:** O Render detectará automaticamente o arquivo `render.yaml` e criará dois serviços:
    *   Um **Serviço Web** (`eu-sou-ninja-system`)
    *   Um **Banco de Dados PostgreSQL** (`eu-sou-ninja-db`)
4.  **Variáveis de Ambiente:**
    *   O Render irá automaticamente configurar a variável de ambiente `DATABASE_URL` no seu serviço web para apontar para o banco de dados PostgreSQL criado.
    *   A `SECRET_KEY` também será gerada automaticamente, conforme especificado no `render.yaml`.
5.  **Primeiro Deploy:** O Render iniciará o processo de build e deploy. Ele instalará as dependências, executará `db.create_all()` e criará o usuário `admin` padrão (conforme configurado em `main.py`).
6.  **Acesso:** Uma vez que o deploy for bem-sucedido, você receberá uma URL pública para seu serviço web. Você poderá acessar a aplicação por essa URL.

## 5. Teste e Validação do Sistema

Após o deploy, siga estes passos para testar o sistema:

1.  **Acesse a URL do Render:** Abra a URL pública do seu serviço web no navegador.
2.  **Login:** Tente fazer login com as credenciais padrão:
    *   **Usuário:** `admin`
    *   **Senha:** `admin123`
3.  **Verifique as Funcionalidades:** Navegue pelas seções de Alunos, Turmas, Presença e Relatórios para garantir que todas as operações (criar, ler, atualizar, deletar) estejam funcionando corretamente e que os dados estejam sendo persistidos no banco de dados PostgreSQL.

Com estas correções e o guia de deploy, seu sistema "Eu Sou Ninja" deverá funcionar corretamente no Render, utilizando um banco de dados PostgreSQL para persistência de dados e sem o erro de importação de módulo.`, type = 
