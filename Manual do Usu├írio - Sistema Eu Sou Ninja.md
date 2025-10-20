# Manual do Usuário - Sistema Eu Sou Ninja

**Sistema de Gestão de Alunos para Projeto Social de Capoeira**

**Versão:** 1.0.0  
**Data:** Outubro de 2025  
**Desenvolvido para:** Projeto Social Eu Sou Ninja - Abadá Capoeira

---

## Sumário

1. [Introdução](#introdução)
2. [Visão Geral do Sistema](#visão-geral-do-sistema)
3. [Requisitos do Sistema](#requisitos-do-sistema)
4. [Primeiros Passos](#primeiros-passos)
5. [Funcionalidades Principais](#funcionalidades-principais)
6. [Guia de Uso Detalhado](#guia-de-uso-detalhado)
7. [Hospedagem e Deploy](#hospedagem-e-deploy)
8. [Solução de Problemas](#solução-de-problemas)
9. [Perguntas Frequentes](#perguntas-frequentes)

---

## Introdução

O **Sistema Eu Sou Ninja** é uma aplicação web desenvolvida especificamente para o projeto social de capoeira "Eu Sou Ninja", filiado ao grupo internacional Abadá Capoeira. Este sistema foi criado para facilitar o gerenciamento de alunos e o controle de presença nas aulas de capoeira, proporcionando uma ferramenta moderna, segura e fácil de usar para os administradores do projeto.

### Objetivo do Sistema

O sistema tem como objetivo principal automatizar e simplificar as tarefas administrativas do projeto social, permitindo que os instrutores e coordenadores dediquem mais tempo ao ensino da capoeira e ao desenvolvimento dos alunos. As funcionalidades foram cuidadosamente planejadas para atender às necessidades específicas de um projeto social que trabalha com uma turma única de alunos de diversas idades.

### Características Principais

O sistema oferece uma solução completa para gestão de alunos com as seguintes características:

**Segurança e Privacidade:** Todos os dados dos alunos são protegidos por autenticação segura com criptografia de senhas. Apenas usuários autorizados podem acessar o sistema e visualizar informações sensíveis.

**Responsividade:** A interface foi desenvolvida para funcionar perfeitamente em dispositivos móveis (smartphones e tablets) e computadores desktop, permitindo que o controle de presença seja feito diretamente no local da aula usando um celular.

**Facilidade de Uso:** A interface intuitiva e em português brasileiro facilita o uso por pessoas com diferentes níveis de familiaridade com tecnologia.

**Controle Completo:** Todas as informações podem ser editadas, corrigidas ou excluídas quando necessário, garantindo que os dados estejam sempre atualizados e corretos.

---

## Visão Geral do Sistema

### Módulos do Sistema

O sistema é organizado em cinco módulos principais, cada um com funcionalidades específicas:

#### 1. Módulo de Alunos

Este módulo permite o cadastro completo dos alunos do projeto. As informações obrigatórias são o **nome completo** e a **data de nascimento**, essenciais para identificação e cálculo da idade. Informações adicionais como telefone, email, endereço, nome da mãe e do pai são opcionais, mas recomendadas para facilitar o contato com as famílias.

Para alunos menores de idade (menores de 18 anos), o sistema automaticamente solicita o cadastro de um **responsável legal**, incluindo nome completo, CPF, telefone e email do responsável. Esta funcionalidade garante que haja sempre um contato adulto responsável pelo aluno menor.

O módulo também permite marcar alunos como **ativos** ou **inativos**, facilitando a gestão de alunos que se afastaram temporariamente ou definitivamente do projeto.

#### 2. Módulo de Presença

O módulo de controle de presença é o coração do sistema. Ele permite que o instrutor registre a presença ou falta de cada aluno em cada aula realizada. O processo é simples e rápido:

1. Selecione a data da aula
2. Marque a presença de cada aluno individualmente usando checkboxes
3. Salve o registro de presença

O sistema oferece botões para marcar todos os alunos como presentes ou ausentes de uma vez, agilizando o processo quando necessário. Apenas alunos ativos aparecem na lista de presença, evitando confusão com alunos que já saíram do projeto.

#### 3. Módulo de Relatórios

Este módulo gera demonstrativos detalhados da frequência individual de cada aluno. Você pode selecionar um aluno específico e um período de datas para visualizar:

- **Total de aulas** realizadas no período
- **Número de presenças** do aluno
- **Número de faltas** do aluno
- **Taxa de frequência** em percentual
- **Histórico completo** de presença/falta por data

Estes relatórios são essenciais para acompanhar o engajamento dos alunos e identificar aqueles que precisam de atenção especial ou incentivo para melhorar a frequência.

#### 4. Módulo Sobre o Projeto

Uma aba informativa que apresenta a história, missão e objetivos do projeto Eu Sou Ninja. Este módulo serve como referência para novos usuários do sistema e para apresentar o projeto a visitantes ou parceiros. As informações foram baseadas no documento oficial do projeto e não fazem referências religiosas, mantendo o foco no aspecto social, cultural e educacional da capoeira.

#### 5. Módulo de Configurações

Neste módulo, os usuários podem:

- Visualizar suas informações de conta
- **Alterar a senha** de acesso ao sistema
- Ver informações sobre a versão do sistema

A funcionalidade de alteração de senha é importante para manter a segurança da conta, permitindo que cada usuário defina uma senha pessoal e a modifique quando necessário.

### Fluxo de Trabalho Típico

Um dia típico de uso do sistema seguiria este fluxo:

**Antes da Aula:** O instrutor acessa o sistema pelo celular ou computador e verifica a lista de alunos ativos para saber quantos alunos estão matriculados.

**Durante ou Após a Aula:** O instrutor abre o módulo de Presença, seleciona a data de hoje, e marca a presença de cada aluno que compareceu. Alunos ausentes ficam desmarcados. Ao final, clica em "Salvar Presença" para registrar os dados.

**Periodicamente:** O coordenador do projeto acessa o módulo de Relatórios para verificar a frequência dos alunos. Identifica alunos com baixa frequência e toma ações para entender os motivos e incentivar a participação.

**Quando Necessário:** Novos alunos são cadastrados no módulo de Alunos. Informações de alunos existentes são atualizadas conforme necessário. Alunos que saem do projeto são marcados como inativos.

---

## Requisitos do Sistema

### Para Uso do Sistema

**Navegador Web Moderno:** O sistema funciona em qualquer navegador atualizado, incluindo:
- Google Chrome (versão 90 ou superior)
- Mozilla Firefox (versão 88 ou superior)
- Safari (versão 14 ou superior)
- Microsoft Edge (versão 90 ou superior)

**Conexão com a Internet:** É necessária conexão com a internet para acessar o sistema, pois ele é hospedado online.

**Dispositivos Compatíveis:**
- Computadores desktop (Windows, macOS, Linux)
- Notebooks
- Tablets (iPad, Android)
- Smartphones (iPhone, Android)

**Resolução de Tela:** O sistema se adapta a qualquer tamanho de tela, mas recomenda-se uma resolução mínima de 320x568 pixels (tamanho de um iPhone SE).

### Para Instalação e Hospedagem

Se você deseja hospedar o sistema em seu próprio servidor, os requisitos técnicos são:

**Software Necessário:**
- Node.js versão 22.13.0 ou superior
- Banco de dados MySQL ou compatível (TiDB, MariaDB)
- Git para controle de versão

**Conhecimentos Técnicos:**
- Conhecimento básico de linha de comando
- Familiaridade com conceitos de hospedagem web
- Capacidade de seguir instruções técnicas

**Recursos do Servidor:**
- Mínimo de 512 MB de RAM
- 1 GB de espaço em disco
- Processador com pelo menos 1 núcleo

---

## Primeiros Passos

### Acessando o Sistema pela Primeira Vez

Quando o sistema estiver hospedado e online, você receberá uma URL (endereço web) para acessá-lo. Ao abrir esta URL em seu navegador, você verá a tela de login.

### Criando sua Conta

Na primeira vez que usar o sistema, você precisará criar uma conta:

1. Na tela de login, clique no botão **"Não tem conta? Registre-se"**
2. Preencha o formulário de registro com:
   - **Nome Completo:** Seu nome completo
   - **Email:** Um endereço de email válido (será seu nome de usuário)
   - **Senha:** Uma senha com no mínimo 6 caracteres
3. Clique em **"Criar Conta"**
4. Você será redirecionado para a tela de login

### Fazendo Login

Após criar sua conta ou em acessos posteriores:

1. Digite seu **email** no campo correspondente
2. Digite sua **senha** no campo de senha
3. Clique em **"Entrar"**
4. Você será direcionado para a página principal do sistema (Módulo de Alunos)

### Navegação no Sistema

Após fazer login, você verá uma barra lateral (sidebar) à esquerda da tela com os seguintes itens de menu:

- **Alunos:** Gerenciar cadastro de alunos
- **Presença:** Controlar presença nas aulas
- **Relatórios:** Visualizar estatísticas de frequência
- **Sobre o Projeto:** Informações sobre o Eu Sou Ninja
- **Configurações:** Alterar senha e ver informações da conta

No canto inferior da barra lateral, você verá seu nome e email, com um botão de **Sair** para fazer logout do sistema.

Em dispositivos móveis, a barra lateral pode aparecer como um menu hambúrguer (três linhas horizontais) no canto superior esquerdo. Clique neste ícone para abrir e fechar o menu.

---

## Funcionalidades Principais

### Cadastro de Alunos

O cadastro de alunos é a base do sistema. Cada aluno cadastrado possui um perfil completo com todas as informações necessárias para o projeto.

#### Campos do Cadastro

**Campos Obrigatórios:**
- **Nome Completo:** Nome completo do aluno (mínimo 3 caracteres)
- **Data de Nascimento:** Data no formato DD/MM/AAAA

**Campos Opcionais:**
- **Telefone:** Número de telefone para contato
- **Email:** Endereço de email do aluno
- **Endereço:** Endereço residencial completo
- **Nome da Mãe:** Nome completo da mãe
- **Nome do Pai:** Nome completo do pai
- **Status:** Ativo ou Inativo (padrão: Ativo)

**Campos de Responsável Legal (obrigatórios para menores de 18 anos):**
- **Nome do Responsável:** Nome completo do responsável legal
- **CPF do Responsável:** CPF no formato 000.000.000-00
- **Telefone do Responsável:** Telefone para contato
- **Email do Responsável:** Email para contato

#### Como Cadastrar um Novo Aluno

1. Acesse o módulo **"Alunos"** no menu lateral
2. Clique no botão **"+ Novo Aluno"** no canto superior direito
3. Preencha o formulário com as informações do aluno
4. Se o aluno for menor de idade, o sistema mostrará automaticamente os campos de responsável legal
5. Clique em **"Cadastrar Aluno"**
6. Uma mensagem de sucesso aparecerá e o aluno será adicionado à lista

#### Como Editar Informações de um Aluno

1. Na lista de alunos, localize o aluno que deseja editar
2. Clique no botão **"Editar"** (ícone de lápis) ao lado do nome do aluno
3. Modifique as informações necessárias no formulário
4. Clique em **"Salvar Alterações"**
5. As informações serão atualizadas imediatamente

#### Como Excluir um Aluno

**Atenção:** A exclusão de um aluno é permanente e também remove todos os registros de presença associados a ele. Use esta função apenas quando tiver certeza.

1. Na lista de alunos, localize o aluno que deseja excluir
2. Clique no botão **"Excluir"** (ícone de lixeira) ao lado do nome do aluno
3. Uma mensagem de confirmação aparecerá
4. Confirme a exclusão clicando em **"Sim, excluir"**
5. O aluno e seus registros serão removidos do sistema

**Alternativa:** Em vez de excluir, considere marcar o aluno como **"Inativo"** editando seu cadastro. Isso preserva o histórico do aluno no sistema.

### Controle de Presença

O controle de presença permite registrar quem compareceu a cada aula realizada.

#### Como Registrar Presença de uma Aula

1. Acesse o módulo **"Presença"** no menu lateral
2. Selecione a **data da aula** no campo "Data da Aula"
   - Por padrão, o sistema mostra a data de hoje
   - Você pode selecionar datas passadas para registrar aulas anteriores
3. A lista de todos os alunos ativos aparecerá
4. Marque a checkbox ao lado do nome de cada aluno que **esteve presente**
5. Deixe desmarcado os alunos que **faltaram**
6. Clique em **"Salvar Presença"** no final da lista
7. Uma mensagem de sucesso confirmará o registro

#### Funcionalidades Auxiliares

**Marcar Todos:** Clique no botão **"Marcar Todos"** para marcar todos os alunos como presentes de uma vez. Útil quando a maioria dos alunos compareceu.

**Desmarcar Todos:** Clique no botão **"Desmarcar Todos"** para desmarcar todos os alunos. Útil para começar do zero ou quando poucos alunos compareceram.

**Editar Presença Anterior:** Você pode selecionar uma data passada para visualizar e editar o registro de presença daquela aula. Isso é útil para corrigir erros ou atualizar informações.

**Indicador Visual:** O sistema mostra quantos alunos estão marcados como presentes em tempo real (ex: "5 de 20 aluno(s) presente(s)").

### Relatórios de Frequência

Os relatórios fornecem uma visão analítica da frequência de cada aluno ao longo do tempo.

#### Como Gerar um Relatório

1. Acesse o módulo **"Relatórios"** no menu lateral
2. Selecione um **aluno** no campo "Aluno"
3. (Opcional) Selecione uma **data inicial** para filtrar o período
4. (Opcional) Selecione uma **data final** para filtrar o período
5. O relatório será gerado automaticamente

Se você não selecionar datas, o relatório mostrará todas as aulas registradas desde o início.

#### Informações do Relatório

O relatório exibe quatro cartões principais com estatísticas:

**Total de Aulas:** Número total de aulas realizadas no período selecionado.

**Presenças:** Número de aulas em que o aluno esteve presente.

**Faltas:** Número de aulas em que o aluno faltou.

**Taxa de Frequência:** Percentual de presença calculado como (Presenças / Total de Aulas) × 100. Uma barra visual mostra este percentual graficamente.

Abaixo das estatísticas, você verá:

**Informações do Aluno:** Nome, data de nascimento, telefone e email do aluno selecionado.

**Histórico de Presença:** Lista completa de todas as aulas do período, mostrando a data de cada aula e se o aluno esteve presente ou ausente. As datas são mostradas por extenso (ex: "segunda-feira, 15 de outubro de 2025").

#### Interpretando a Taxa de Frequência

A taxa de frequência é um indicador importante do engajamento do aluno:

- **80% ou mais:** Excelente frequência, aluno muito engajado
- **60% a 79%:** Boa frequência, mas pode melhorar
- **40% a 59%:** Frequência regular, requer atenção
- **Abaixo de 40%:** Baixa frequência, requer intervenção

Use estes relatórios para identificar alunos que precisam de incentivo ou para entender padrões de frequência ao longo do ano.

### Alteração de Senha

Por questões de segurança, é recomendável alterar sua senha periodicamente.

#### Como Alterar sua Senha

1. Acesse o módulo **"Configurações"** no menu lateral
2. Role até a seção **"Alterar Senha"**
3. Digite sua **senha atual** no primeiro campo
4. Digite sua **nova senha** no segundo campo (mínimo 6 caracteres)
5. Digite novamente a **nova senha** no terceiro campo para confirmar
6. Clique em **"Alterar Senha"**
7. Uma mensagem de sucesso confirmará a alteração

**Dicas de Segurança:**
- Use uma senha com pelo menos 8 caracteres
- Combine letras maiúsculas, minúsculas e números
- Não use senhas óbvias como "123456" ou "senha"
- Não compartilhe sua senha com outras pessoas
- Altere sua senha a cada 3-6 meses

---

## Guia de Uso Detalhado

### Cenários Práticos de Uso

#### Cenário 1: Início do Ano Letivo

No início do ano ou semestre, você precisa cadastrar novos alunos que se inscreveram no projeto.

**Passo a Passo:**

1. Faça login no sistema
2. Acesse **"Alunos"** no menu
3. Para cada novo aluno:
   - Clique em **"+ Novo Aluno"**
   - Preencha nome completo e data de nascimento
   - Adicione telefone e email se disponível
   - Se menor de idade, preencha dados do responsável
   - Clique em **"Cadastrar Aluno"**
4. Verifique se todos os alunos foram cadastrados corretamente na lista

**Dica:** Prepare uma planilha ou lista com os dados dos alunos antes de começar o cadastro para agilizar o processo.

#### Cenário 2: Registro de Presença Após a Aula

Após cada aula, você precisa registrar quem compareceu.

**Passo a Passo:**

1. Acesse o sistema pelo celular ou computador
2. Vá para **"Presença"** no menu
3. Confirme que a data está correta (data de hoje)
4. Percorra a lista de alunos e marque os presentes
   - Você pode fazer isso durante a chamada oral
   - Ou pode anotar em papel e transferir depois
5. Clique em **"Salvar Presença"**
6. Aguarde a mensagem de confirmação

**Dica:** Se a maioria dos alunos compareceu, clique em "Marcar Todos" e depois desmarque apenas os ausentes. Isso é mais rápido.

#### Cenário 3: Verificação Mensal de Frequência

No final de cada mês, você quer verificar a frequência dos alunos.

**Passo a Passo:**

1. Acesse **"Relatórios"** no menu
2. Selecione o primeiro aluno da lista
3. Defina a data inicial como o primeiro dia do mês
4. Defina a data final como o último dia do mês
5. Analise a taxa de frequência
6. Anote alunos com frequência abaixo de 60%
7. Repita para os próximos alunos

**Dica:** Crie uma planilha externa para acompanhar a evolução da frequência mês a mês de cada aluno.

#### Cenário 4: Correção de Erro no Registro

Você percebeu que marcou um aluno como presente quando ele estava ausente em uma aula da semana passada.

**Passo a Passo:**

1. Acesse **"Presença"** no menu
2. Selecione a data da aula que precisa ser corrigida
3. O sistema mostrará o registro existente
4. Desmarque o aluno que estava ausente
5. Clique em **"Salvar Presença"**
6. O registro será atualizado

**Dica:** Sempre revise o registro de presença logo após salvá-lo para evitar erros.

#### Cenário 5: Aluno que Saiu do Projeto

Um aluno informou que não poderá mais participar das aulas.

**Passo a Passo:**

1. Acesse **"Alunos"** no menu
2. Localize o aluno na lista
3. Clique em **"Editar"**
4. Altere o status de "Ativo" para "Inativo"
5. Clique em **"Salvar Alterações"**

O aluno não aparecerá mais nas listas de presença, mas seu histórico será preservado.

**Não recomendado:** Excluir o aluno, pois isso apaga todo o histórico.

### Dicas de Uso Eficiente

**Acesse pelo Celular:** Instale um atalho do sistema na tela inicial do seu smartphone para acesso rápido. No Chrome, use a opção "Adicionar à tela inicial".

**Registre Presença Imediatamente:** Faça o registro logo após a aula para não esquecer quem compareceu.

**Revise Periodicamente:** Dedique alguns minutos por semana para revisar os cadastros e garantir que as informações estão atualizadas.

**Backup de Dados:** Embora o sistema armazene os dados de forma segura, é bom exportar relatórios importantes periodicamente (você pode fazer isso tirando screenshots ou anotando em um caderno).

**Comunique-se com as Famílias:** Use os relatórios de frequência como base para conversas com pais e responsáveis sobre o engajamento dos alunos.

---

## Hospedagem e Deploy

Esta seção é destinada a pessoas com conhecimentos técnicos que desejam hospedar o sistema em um servidor próprio ou em plataformas de hospedagem gratuitas.

### Opções de Hospedagem Gratuita

O sistema **não pode** ser hospedado no GitHub Pages, pois é uma aplicação full-stack com backend e banco de dados. As melhores opções gratuitas são:

#### 1. Vercel (Recomendado)

**Características:**
- Deploy automático a partir do GitHub
- Suporte nativo para Node.js
- SSL gratuito (HTTPS)
- Domínio gratuito (.vercel.app)

**Limitações do Plano Gratuito:**
- Limite de 100 GB de largura de banda por mês
- Funções serverless com timeout de 10 segundos

**Banco de Dados:** Você precisará usar um banco de dados externo como:
- **PlanetScale** (MySQL gratuito até 5 GB)
- **Railway** (PostgreSQL gratuito com limite de 500 MB)
- **Supabase** (PostgreSQL gratuito até 500 MB)

#### 2. Railway

**Características:**
- Deploy de aplicações Node.js completas
- Banco de dados PostgreSQL incluído
- SSL gratuito
- Domínio gratuito (.up.railway.app)

**Limitações do Plano Gratuito:**
- $5 de crédito mensal gratuito
- Após esgotar, o serviço é pausado até o próximo mês

#### 3. Render

**Características:**
- Deploy de aplicações web completas
- Banco de dados PostgreSQL gratuito
- SSL gratuito
- Domínio gratuito (.onrender.com)

**Limitações do Plano Gratuito:**
- Serviço hiberna após 15 minutos de inatividade
- Primeiro acesso após hibernação pode demorar 30-60 segundos

#### 4. Fly.io

**Características:**
- Deploy de aplicações Docker
- Suporte para Node.js
- SSL gratuito

**Limitações do Plano Gratuito:**
- Recursos limitados (256 MB RAM)
- 3 GB de armazenamento

### Guia de Deploy no Vercel

**Pré-requisitos:**
- Conta no GitHub
- Conta no Vercel (pode criar com sua conta GitHub)
- Conta no PlanetScale para banco de dados

**Passo a Passo:**

1. **Preparar o Repositório GitHub**
   - Faça upload do código do sistema para um repositório GitHub
   - Certifique-se de que o arquivo `.gitignore` não inclui a pasta `node_modules`

2. **Configurar Banco de Dados no PlanetScale**
   - Acesse [planetscale.com](https://planetscale.com) e crie uma conta
   - Crie um novo banco de dados
   - Copie a string de conexão (DATABASE_URL)

3. **Deploy no Vercel**
   - Acesse [vercel.com](https://vercel.com) e faça login
   - Clique em "New Project"
   - Importe seu repositório GitHub
   - Configure as variáveis de ambiente:
     - `DATABASE_URL`: String de conexão do PlanetScale
     - `JWT_SECRET`: Uma string aleatória longa (ex: use um gerador de senha)
   - Clique em "Deploy"

4. **Executar Migrações do Banco de Dados**
   - Após o deploy, acesse o terminal do Vercel
   - Execute: `pnpm db:push`
   - Isso criará as tabelas no banco de dados

5. **Acessar o Sistema**
   - Vercel fornecerá uma URL (ex: `seu-projeto.vercel.app`)
   - Acesse esta URL e crie sua primeira conta

### Guia de Deploy no Railway

**Passo a Passo:**

1. **Criar Conta no Railway**
   - Acesse [railway.app](https://railway.app)
   - Faça login com GitHub

2. **Criar Novo Projeto**
   - Clique em "New Project"
   - Selecione "Deploy from GitHub repo"
   - Escolha seu repositório

3. **Adicionar Banco de Dados**
   - No projeto, clique em "New"
   - Selecione "Database" → "Add PostgreSQL"
   - Railway criará automaticamente o banco

4. **Configurar Variáveis de Ambiente**
   - Clique no serviço da aplicação
   - Vá para "Variables"
   - Adicione:
     - `DATABASE_URL`: Railway preenche automaticamente se você conectar o banco
     - `JWT_SECRET`: String aleatória longa

5. **Deploy**
   - Railway faz deploy automaticamente
   - Acesse a URL fornecida

6. **Executar Migrações**
   - No painel do Railway, abra o terminal
   - Execute: `pnpm db:push`

### Guia de Deploy no Render

**Passo a Passo:**

1. **Criar Conta no Render**
   - Acesse [render.com](https://render.com)
   - Faça login com GitHub

2. **Criar Banco de Dados**
   - No dashboard, clique em "New +"
   - Selecione "PostgreSQL"
   - Escolha o plano gratuito
   - Copie a "Internal Database URL"

3. **Criar Web Service**
   - Clique em "New +" → "Web Service"
   - Conecte seu repositório GitHub
   - Configure:
     - **Build Command:** `pnpm install && pnpm build`
     - **Start Command:** `pnpm start`

4. **Configurar Variáveis de Ambiente**
   - Na seção "Environment", adicione:
     - `DATABASE_URL`: URL do banco criado anteriormente
     - `JWT_SECRET`: String aleatória longa

5. **Deploy**
   - Clique em "Create Web Service"
   - Render fará o deploy automaticamente

6. **Executar Migrações**
   - Após o deploy, acesse o Shell do Render
   - Execute: `pnpm db:push`

### Configuração de Domínio Personalizado

Se você possui um domínio próprio (ex: `eusouninja.com.br`), pode configurá-lo em qualquer uma das plataformas:

**Vercel:**
1. Vá para "Settings" → "Domains"
2. Adicione seu domínio
3. Configure os registros DNS conforme instruções

**Railway:**
1. Vá para "Settings" → "Networking"
2. Adicione "Custom Domain"
3. Configure os registros DNS

**Render:**
1. Vá para "Settings" → "Custom Domain"
2. Adicione seu domínio
3. Configure os registros DNS

### Manutenção e Atualizações

**Backups do Banco de Dados:**
- PlanetScale: Backups automáticos diários
- Railway: Backups manuais via painel
- Render: Backups automáticos no plano pago

**Atualizações do Sistema:**
- Faça um commit no GitHub com as alterações
- As plataformas farão deploy automático

**Monitoramento:**
- Todas as plataformas oferecem logs e métricas
- Configure alertas para erros críticos

---

## Solução de Problemas

### Problemas Comuns e Soluções

#### Não Consigo Fazer Login

**Problema:** Ao tentar fazer login, recebo mensagem de erro "Email ou senha incorretos".

**Soluções:**
1. Verifique se digitou o email corretamente (sem espaços extras)
2. Verifique se a senha está correta (atenção para maiúsculas e minúsculas)
3. Se esqueceu a senha, entre em contato com o administrador do sistema
4. Tente criar uma nova conta se ainda não tem uma

#### O Sistema Está Lento

**Problema:** As páginas demoram muito para carregar.

**Soluções:**
1. Verifique sua conexão com a internet
2. Tente recarregar a página (F5 ou Ctrl+R)
3. Limpe o cache do navegador
4. Tente usar outro navegador
5. Se hospedado no Render (plano gratuito), o primeiro acesso após inatividade demora mais

#### Não Vejo os Alunos na Lista de Presença

**Problema:** A lista de presença está vazia mesmo tendo alunos cadastrados.

**Soluções:**
1. Verifique se os alunos estão marcados como "Ativos" no cadastro
2. Apenas alunos ativos aparecem na lista de presença
3. Edite os alunos e altere o status para "Ativo" se necessário

#### Os Dados Não Estão Salvando

**Problema:** Ao clicar em "Salvar", os dados não são gravados.

**Soluções:**
1. Verifique se todos os campos obrigatórios estão preenchidos
2. Verifique se há mensagens de erro na tela
3. Tente recarregar a página e fazer login novamente
4. Verifique sua conexão com a internet
5. Entre em contato com o suporte técnico se o problema persistir

#### Erro ao Alterar Senha

**Problema:** Recebo erro ao tentar alterar a senha.

**Soluções:**
1. Certifique-se de que digitou a senha atual corretamente
2. Verifique se a nova senha tem no mínimo 6 caracteres
3. Certifique-se de que digitou a mesma senha nos campos "Nova Senha" e "Confirmar Nova Senha"
4. Tente fazer logout e login novamente

#### O Sistema Não Funciona no Celular

**Problema:** O sistema não carrega ou fica desconfigurado no smartphone.

**Soluções:**
1. Certifique-se de estar usando um navegador moderno (Chrome, Safari, Firefox)
2. Atualize seu navegador para a versão mais recente
3. Tente rotacionar a tela (modo retrato/paisagem)
4. Limpe o cache do navegador móvel
5. Tente acessar em modo anônimo/privado

#### Relatório Não Mostra Dados

**Problema:** Ao gerar relatório, não aparecem estatísticas.

**Soluções:**
1. Certifique-se de que selecionou um aluno
2. Verifique se há registros de presença para este aluno
3. Verifique se o período selecionado inclui aulas registradas
4. Tente remover os filtros de data para ver todos os registros

### Erros Técnicos

#### Erro 500 - Internal Server Error

**Causa:** Erro no servidor.

**Solução:**
1. Aguarde alguns minutos e tente novamente
2. Recarregue a página
3. Se persistir, entre em contato com o administrador

#### Erro 404 - Not Found

**Causa:** Página não encontrada.

**Solução:**
1. Verifique se a URL está correta
2. Volte para a página inicial e navegue novamente
3. Limpe o cache do navegador

#### Erro de Conexão com Banco de Dados

**Causa:** Problema na conexão com o banco de dados.

**Solução:**
1. Verifique se o serviço de banco de dados está ativo
2. Verifique as configurações de `DATABASE_URL`
3. Entre em contato com o suporte da plataforma de hospedagem

### Contato para Suporte

Se você não conseguir resolver um problema usando este manual, entre em contato:

**Email do Projeto:** projetoeusouninja@gmail.com  
**Telefone:** (027) 98151-3137  
**Responsável:** Alexandre Xavier de Lima

Ao entrar em contato, forneça:
- Descrição detalhada do problema
- Mensagens de erro (se houver)
- Navegador e dispositivo que está usando
- Passos que levaram ao erro

---

## Perguntas Frequentes

### Sobre o Sistema

**P: O sistema funciona offline?**  
R: Não. O sistema precisa de conexão com a internet para funcionar, pois os dados são armazenados em um servidor online.

**P: Quantos usuários podem acessar o sistema ao mesmo tempo?**  
R: Não há limite técnico. Múltiplos usuários podem acessar simultaneamente.

**P: Os dados são seguros?**  
R: Sim. As senhas são criptografadas e o sistema usa conexão HTTPS segura. Apenas usuários autenticados podem acessar os dados.

**P: Posso acessar de qualquer lugar?**  
R: Sim. Basta ter um dispositivo com navegador e internet.

**P: O sistema tem custo?**  
R: O sistema em si é gratuito. Pode haver custos de hospedagem dependendo da plataforma escolhida, mas existem opções gratuitas.

### Sobre Alunos

**P: Posso cadastrar alunos adultos?**  
R: Sim. O campo de responsável legal só é obrigatório para menores de 18 anos.

**P: Posso ter dois alunos com o mesmo nome?**  
R: Sim. O sistema diferencia alunos por um ID único interno.

**P: Como faço para reativar um aluno inativo?**  
R: Edite o cadastro do aluno e altere o status de "Inativo" para "Ativo".

**P: Posso cadastrar alunos sem telefone ou email?**  
R: Sim. Apenas nome e data de nascimento são obrigatórios.

### Sobre Presença

**P: Posso registrar presença de aulas passadas?**  
R: Sim. Selecione a data desejada no campo de data.

**P: Posso corrigir um registro de presença?**  
R: Sim. Acesse a data da aula e modifique os registros.

**P: O que acontece se eu salvar presença duas vezes na mesma data?**  
R: O sistema sobrescreve o registro anterior com o novo.

**P: Posso adicionar observações sobre a presença?**  
R: Atualmente não. Esta funcionalidade pode ser adicionada em versões futuras.

### Sobre Relatórios

**P: Posso exportar os relatórios para PDF ou Excel?**  
R: Atualmente não há função de exportação automática. Você pode tirar screenshots ou copiar os dados manualmente.

**P: Os relatórios incluem alunos inativos?**  
R: Sim, se você selecionar um aluno inativo no filtro, o relatório mostrará seu histórico.

**P: Posso ver um relatório geral de todos os alunos?**  
R: Atualmente não. Os relatórios são individuais por aluno.

### Sobre Segurança

**P: Outras pessoas podem ver meus dados?**  
R: Não. Cada usuário vê apenas os dados associados à sua conta.

**P: Posso ter múltiplas contas?**  
R: Tecnicamente sim, mas não é recomendado. Use uma conta por pessoa.

**P: O que fazer se esquecer minha senha?**  
R: Entre em contato com o administrador do sistema para resetar sua senha.

**P: Posso compartilhar minha senha?**  
R: Não é recomendado por questões de segurança. Cada pessoa deve ter sua própria conta.

---

## Conclusão

O Sistema Eu Sou Ninja foi desenvolvido para facilitar a gestão administrativa do projeto social de capoeira, permitindo que os instrutores e coordenadores foquem no que realmente importa: o desenvolvimento e a educação dos alunos através da capoeira.

Este manual cobriu todas as funcionalidades principais do sistema, desde o cadastro de alunos até a geração de relatórios de frequência. Com o uso regular e seguindo as boas práticas descritas, você terá um controle completo e organizado de todos os aspectos administrativos do projeto.

### Próximos Passos

Após ler este manual, recomendamos:

1. **Praticar:** Faça alguns cadastros de teste para se familiarizar com o sistema
2. **Explorar:** Navegue por todos os módulos para conhecer todas as funcionalidades
3. **Planejar:** Defina um fluxo de trabalho para uso regular do sistema
4. **Treinar:** Se houver outros usuários, treine-os usando este manual

### Sugestões e Melhorias

O sistema está em constante evolução. Se você tiver sugestões de melhorias ou novas funcionalidades, entre em contato através dos canais de suporte. Seu feedback é importante para tornar o sistema cada vez melhor.

### Agradecimentos

Agradecemos por usar o Sistema Eu Sou Ninja. Esperamos que esta ferramenta contribua para o sucesso e crescimento do projeto social, ajudando a transformar vidas através da capoeira.

**Axé!** 🥋

---

**Desenvolvido com dedicação para o Projeto Social Eu Sou Ninja**  
**Abadá Capoeira - Preservando a Cultura Brasileira**

---

## Informações Técnicas

**Versão do Sistema:** 1.0.0  
**Data de Lançamento:** Outubro 2025  
**Tecnologias Utilizadas:** React, Node.js, TypeScript, MySQL  
**Licença:** Uso exclusivo do Projeto Eu Sou Ninja  
**Desenvolvido por:** Manus AI

---

## Anexos

### Glossário de Termos

**Aluno Ativo:** Aluno que está frequentando as aulas atualmente.

**Aluno Inativo:** Aluno que não está mais participando do projeto, mas cujo histórico é mantido no sistema.

**Autenticação:** Processo de verificar a identidade do usuário através de email e senha.

**Banco de Dados:** Sistema que armazena todos os dados do sistema de forma organizada e segura.

**Checkbox:** Caixa de seleção que pode ser marcada ou desmarcada.

**Deploy:** Processo de publicar o sistema em um servidor para que fique acessível online.

**Frontend:** Parte visual do sistema que o usuário vê e interage.

**Backend:** Parte do sistema que processa dados e lógica de negócio no servidor.

**HTTPS:** Protocolo seguro de comunicação na internet.

**Responsável Legal:** Pessoa adulta responsável por um aluno menor de idade.

**Taxa de Frequência:** Percentual que indica quantas aulas o aluno compareceu em relação ao total de aulas realizadas.

**URL:** Endereço web para acessar o sistema (ex: https://eusouninja.vercel.app).

### Atalhos de Teclado

Embora o sistema seja otimizado para uso com mouse/touch, alguns atalhos úteis:

- **Ctrl + R** ou **F5:** Recarregar página
- **Ctrl + Shift + Delete:** Limpar cache do navegador
- **Ctrl + F:** Buscar na página (útil para encontrar alunos em listas longas)
- **Tab:** Navegar entre campos de formulário
- **Enter:** Submeter formulário (quando em um campo de input)

### Códigos de Status HTTP

Para referência técnica:

- **200 OK:** Requisição bem-sucedida
- **400 Bad Request:** Dados inválidos enviados
- **401 Unauthorized:** Não autenticado
- **403 Forbidden:** Sem permissão
- **404 Not Found:** Página não encontrada
- **500 Internal Server Error:** Erro no servidor

---

**Fim do Manual do Usuário**

