# Sistema Eu Sou Ninja

Este é um sistema de gestão de alunos para um projeto social de capoeira, desenvolvido com React, TypeScript, tRPC, Express e MySQL.

## Estrutura do Projeto

- `client/`: Contém o código do frontend (aplicação React).
- `server/`: Contém o código do backend (API Node.js com Express e tRPC).
- `drizzle/`: Contém o schema do banco de dados.
- `shared/`: Contém código e constantes compartilhadas entre frontend e backend.

## Configuração e Execução

### Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

- Node.js (versão 22.13.0 ou superior)
- pnpm (gerenciador de pacotes)
- MySQL (ou compatível como TiDB, MariaDB)
- Git

### 1. Configuração do Banco de Dados

1. Crie um banco de dados MySQL para o projeto.
2. Configure a string de conexão do banco de dados. Você precisará de um arquivo `.env` na raiz do diretório `server/` com a variável `DATABASE_URL`.

   Exemplo de `.env` em `server/.env`:
   ```
   DATABASE_URL="mysql://user:password@host:port/database_name"
   JWT_SECRET="seu_segredo_jwt_aqui"
   OWNER_ID="id_do_usuario_admin_inicial"
   ```

   **Importante:** Substitua `user`, `password`, `host`, `port`, `database_name`, `seu_segredo_jwt_aqui` e `id_do_usuario_admin_inicial` pelos seus dados.

3. As migrações do Drizzle ORM devem ser executadas para criar as tabelas no banco de dados. Isso geralmente é feito através de scripts no `package.json` do `server/` ou de uma ferramenta de linha de comando do Drizzle. (Não incluído neste README, mas é um passo crucial para a configuração do DB).

### 2. Instalação e Execução do Backend (Server)

1. Navegue até o diretório `server/`:
   ```bash
   cd eusouninja/server
   ```
2. Instale as dependências:
   ```bash
   pnpm install
   ```
3. Compile o código TypeScript:
   ```bash
   pnpm run build
   ```
4. Inicie o servidor (em modo de desenvolvimento, se desejar):
   ```bash
   pnpm run dev
   # ou pnpm start para produção
   ```
   O servidor estará rodando em `http://localhost:3000` (ou na porta configurada).

### 3. Instalação e Execução do Frontend (Client)

1. Navegue até o diretório `client/`:
   ```bash
   cd eusouninja/client
   ```
2. Instale as dependências:
   ```bash
   pnpm install
   ```
3. Inicie a aplicação em modo de desenvolvimento:
   ```bash
   pnpm run dev
   ```
   A aplicação estará disponível em `http://localhost:5173` (ou na porta indicada pelo Vite).

## Erros Corrigidos e Melhorias

- **Reorganização da Estrutura de Pastas:** Os arquivos foram reorganizados para seguir a estrutura `client/`, `server/`, `drizzle/` e `shared/` conforme a documentação técnica.
- **Criação de Arquivos Essenciais:** Foram criados `index.html` e `main.tsx` para o frontend, `package.json` e `tsconfig.json` para ambos frontend e backend, `vite.config.ts` para o frontend, e os arquivos de configuração do tRPC (`_core/context.ts`, `_core/cookies.ts`, `_core/env.ts`, `_core/systemRouter.ts`, `_core/trpc.ts`) e o ponto de entrada `index.ts` para o backend.
- **Ajuste de Caminhos de Importação:** Corrigidos os caminhos de importação em diversos arquivos (`App.tsx`, `Reports.tsx`, `Students.tsx`, `Attendance.tsx`, `Settings.tsx`, `db.ts`, `trpc.ts`) para refletir a nova estrutura de pastas e o uso de aliases (`@/`).
- **Movimentação de Ativos:** A imagem `Eusouninja.jpg` foi movida para `client/public/logo.jpg` para ser acessível pelo frontend.
- **Criação de `shared/const.ts`:** Para centralizar constantes compartilhadas como `COOKIE_NAME`.

## Próximos Passos (Recomendações)

- **Executar Migrações do Banco de Dados:** Implementar e executar as migrações do Drizzle ORM para garantir que o schema do banco de dados esteja atualizado.
- **Testes Completos:** Realizar testes abrangentes em todas as funcionalidades do sistema (login, registro, CRUD de alunos, presença, relatórios, etc.).
- **Configuração de Variáveis de Ambiente:** Garantir que todas as variáveis de ambiente necessárias (`DATABASE_URL`, `JWT_SECRET`, `OWNER_ID`) estejam corretamente configuradas para ambientes de desenvolvimento e produção.
- **Implementar Componentes `ui`:** Certificar-se de que todos os componentes `ui` referenciados (shadcn/ui) estão instalados e configurados corretamente no frontend.

Espero que essas correções e a nova estrutura ajudem no desenvolvimento e implantação do seu projeto!
