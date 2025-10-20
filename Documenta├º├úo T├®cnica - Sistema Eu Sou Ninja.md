# Documentação Técnica - Sistema Eu Sou Ninja

**Sistema de Gestão de Alunos para Projeto Social de Capoeira**

**Versão:** 1.0.0  
**Data:** Outubro de 2025  
**Autor:** Manus AI

---

## Sumário

1. [Visão Geral Técnica](#visão-geral-técnica)
2. [Arquitetura do Sistema](#arquitetura-do-sistema)
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)
4. [Estrutura do Projeto](#estrutura-do-projeto)
5. [Banco de Dados](#banco-de-dados)
6. [Backend - API e Lógica de Negócio](#backend---api-e-lógica-de-negócio)
7. [Frontend - Interface do Usuário](#frontend---interface-do-usuário)
8. [Autenticação e Segurança](#autenticação-e-segurança)
9. [Guia de Instalação Local](#guia-de-instalação-local)
10. [Guia de Deploy em Produção](#guia-de-deploy-em-produção)
11. [Manutenção e Extensões](#manutenção-e-extensões)

---

## Visão Geral Técnica

O Sistema Eu Sou Ninja é uma aplicação web full-stack desenvolvida com tecnologias modernas para gerenciamento de alunos e controle de presença. A arquitetura segue o padrão cliente-servidor com separação clara entre frontend e backend, comunicação via tRPC para type-safety end-to-end, e banco de dados relacional MySQL.

### Características Técnicas Principais

**Type-Safe End-to-End:** Utilização de TypeScript em todo o stack com tRPC garantindo tipagem compartilhada entre cliente e servidor, eliminando erros de contrato de API.

**Autenticação Local:** Sistema de autenticação próprio com criptografia bcrypt para senhas e JWT para sessões, sem dependência de provedores externos.

**Responsividade:** Interface desenvolvida com Tailwind CSS e shadcn/ui, garantindo adaptação perfeita a qualquer tamanho de tela.

**Validação de Dados:** Validação em múltiplas camadas (frontend, backend, banco de dados) usando Zod para schemas consistentes.

**Arquitetura Modular:** Código organizado em módulos independentes facilitando manutenção e extensão.

---

## Arquitetura do Sistema

### Diagrama de Arquitetura

```
┌─────────────────────────────────────────────────────────────┐
│                        CLIENTE (Browser)                     │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  React 19 + TypeScript + Tailwind CSS + shadcn/ui   │  │
│  │  - Componentes de UI                                  │  │
│  │  - Gerenciamento de Estado (React Query)             │  │
│  │  - Roteamento (Wouter)                               │  │
│  └──────────────────────────────────────────────────────┘  │
└───────────────────────┬─────────────────────────────────────┘
                        │ tRPC (Type-Safe RPC)
                        │ HTTPS
┌───────────────────────┴─────────────────────────────────────┐
│                     SERVIDOR (Node.js)                       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Express 4 + tRPC 11 + TypeScript                    │  │
│  │  - Routers (API Endpoints)                           │  │
│  │  - Middleware de Autenticação                        │  │
│  │  - Lógica de Negócio                                 │  │
│  └──────────────────────────────────────────────────────┘  │
└───────────────────────┬─────────────────────────────────────┘
                        │ Drizzle ORM
                        │ MySQL Protocol
┌───────────────────────┴─────────────────────────────────────┐
│                    BANCO DE DADOS (MySQL)                    │
│  - Tabela: users (usuários do sistema)                      │
│  - Tabela: students (alunos cadastrados)                    │
│  - Tabela: guardians (responsáveis legais)                  │
│  - Tabela: attendance (registros de presença)               │
└──────────────────────────────────────────────────────────────┘
```

### Fluxo de Dados

1. **Requisição do Cliente:** Usuário interage com a interface React
2. **Chamada tRPC:** Cliente invoca procedimento tRPC tipado
3. **Validação:** Servidor valida dados com Zod
4. **Autenticação:** Middleware verifica JWT e sessão
5. **Lógica de Negócio:** Router executa lógica específica
6. **Acesso ao Banco:** Drizzle ORM executa queries SQL
7. **Resposta:** Dados retornam pelo mesmo caminho, tipados

---

## Tecnologias Utilizadas

### Frontend

| Tecnologia | Versão | Propósito |
|------------|--------|-----------|
| React | 19.x | Framework UI para construção de interfaces |
| TypeScript | 5.x | Superset de JavaScript com tipagem estática |
| Vite | 6.x | Build tool e dev server rápido |
| Tailwind CSS | 4.x | Framework CSS utility-first |
| shadcn/ui | Latest | Biblioteca de componentes UI acessíveis |
| tRPC Client | 11.x | Cliente RPC type-safe |
| React Query | 5.x | Gerenciamento de estado servidor |
| Wouter | 3.x | Roteamento leve para React |
| Sonner | Latest | Sistema de notificações toast |

### Backend

| Tecnologia | Versão | Propósito |
|------------|--------|-----------|
| Node.js | 22.13.0 | Runtime JavaScript servidor |
| Express | 4.x | Framework web para Node.js |
| TypeScript | 5.x | Tipagem estática |
| tRPC Server | 11.x | Framework RPC type-safe |
| Drizzle ORM | Latest | ORM TypeScript-first |
| bcrypt | 5.x | Criptografia de senhas |
| jsonwebtoken | 9.x | Geração e validação de JWT |
| Zod | 3.x | Validação de schemas |

### Banco de Dados

| Tecnologia | Versão | Propósito |
|------------|--------|-----------|
| MySQL | 8.x | Banco de dados relacional |
| mysql2 | Latest | Driver MySQL para Node.js |

### Ferramentas de Desenvolvimento

| Ferramenta | Propósito |
|------------|-----------|
| pnpm | Gerenciador de pacotes rápido |
| ESLint | Linter para JavaScript/TypeScript |
| Prettier | Formatador de código |
| Git | Controle de versão |

---

## Estrutura do Projeto

```
eusouninja/
├── client/                      # Frontend React
│   ├── public/                  # Arquivos estáticos
│   │   └── logo.jpg            # Logo do projeto
│   ├── src/
│   │   ├── _core/              # Funcionalidades core
│   │   │   └── hooks/
│   │   │       └── useAuth.tsx # Hook de autenticação
│   │   ├── components/         # Componentes React
│   │   │   ├── ui/             # Componentes shadcn/ui
│   │   │   ├── DashboardLayout.tsx
│   │   │   └── ErrorBoundary.tsx
│   │   ├── contexts/           # Contextos React
│   │   │   └── ThemeContext.tsx
│   │   ├── lib/                # Bibliotecas e utilitários
│   │   │   └── trpc.ts         # Cliente tRPC
│   │   ├── pages/              # Páginas da aplicação
│   │   │   ├── About.tsx       # Página sobre o projeto
│   │   │   ├── Attendance.tsx  # Controle de presença
│   │   │   ├── Login.tsx       # Login e registro
│   │   │   ├── NotFound.tsx    # Página 404
│   │   │   ├── Reports.tsx     # Relatórios de frequência
│   │   │   ├── Settings.tsx    # Configurações
│   │   │   └── Students.tsx    # Gerenciamento de alunos
│   │   ├── App.tsx             # Componente raiz com rotas
│   │   ├── const.ts            # Constantes da aplicação
│   │   ├── index.css           # Estilos globais
│   │   └── main.tsx            # Entry point do React
│   ├── index.html              # HTML principal
│   ├── package.json            # Dependências frontend
│   ├── tailwind.config.ts      # Configuração Tailwind
│   ├── tsconfig.json           # Configuração TypeScript
│   └── vite.config.ts          # Configuração Vite
│
├── server/                      # Backend Node.js
│   ├── _core/                  # Funcionalidades core
│   │   ├── context.ts          # Contexto tRPC
│   │   ├── cookies.ts          # Gerenciamento de cookies
│   │   ├── env.ts              # Variáveis de ambiente
│   │   ├── systemRouter.ts     # Router do sistema
│   │   └── trpc.ts             # Configuração tRPC
│   ├── db.ts                   # Funções de acesso ao banco
│   ├── routers.ts              # Routers da API
│   └── index.ts                # Entry point do servidor
│
├── drizzle/                     # Schema e migrações
│   └── schema.ts               # Definição das tabelas
│
├── shared/                      # Código compartilhado
│   └── const.ts                # Constantes compartilhadas
│
├── .env                        # Variáveis de ambiente (não versionado)
├── .gitignore                  # Arquivos ignorados pelo Git
├── package.json                # Dependências do projeto
├── pnpm-lock.yaml              # Lock file do pnpm
└── tsconfig.json               # Configuração TypeScript raiz
```

---

## Banco de Dados

### Schema do Banco de Dados

O banco de dados utiliza quatro tabelas principais com relacionamentos bem definidos.

#### Tabela: users

Armazena os usuários do sistema (administradores e instrutores).

```typescript
export const users = mysqlTable("users", {
  id: varchar("id", { length: 64 }).primaryKey(),
  name: text("name"),
  email: varchar("email", { length: 320 }).unique(),
  password: text("password"),
  role: mysqlEnum("role", ["user", "admin"]).default("user").notNull(),
  createdAt: timestamp("createdAt").defaultNow(),
  lastSignedIn: timestamp("lastSignedIn").defaultNow(),
});
```

**Campos:**
- `id`: Identificador único (UUID)
- `name`: Nome completo do usuário
- `email`: Email único para login
- `password`: Hash bcrypt da senha
- `role`: Papel do usuário (user ou admin)
- `createdAt`: Data de criação da conta
- `lastSignedIn`: Último login

#### Tabela: students

Armazena os alunos cadastrados no projeto.

```typescript
export const students = mysqlTable("students", {
  id: varchar("id", { length: 64 }).primaryKey(),
  name: text("name").notNull(),
  birthDate: date("birthDate").notNull(),
  phone: varchar("phone", { length: 20 }),
  email: varchar("email", { length: 320 }),
  address: text("address"),
  motherName: text("motherName"),
  fatherName: text("fatherName"),
  isActive: boolean("isActive").default(true).notNull(),
  createdAt: timestamp("createdAt").defaultNow(),
  updatedAt: timestamp("updatedAt").defaultNow().onUpdateNow(),
});
```

**Campos:**
- `id`: Identificador único (UUID)
- `name`: Nome completo do aluno (obrigatório)
- `birthDate`: Data de nascimento (obrigatório)
- `phone`: Telefone de contato (opcional)
- `email`: Email do aluno (opcional)
- `address`: Endereço residencial (opcional)
- `motherName`: Nome da mãe (opcional)
- `fatherName`: Nome do pai (opcional)
- `isActive`: Status ativo/inativo (padrão: true)
- `createdAt`: Data de cadastro
- `updatedAt`: Data da última atualização

#### Tabela: guardians

Armazena responsáveis legais de alunos menores de idade.

```typescript
export const guardians = mysqlTable("guardians", {
  id: varchar("id", { length: 64 }).primaryKey(),
  studentId: varchar("studentId", { length: 64 })
    .notNull()
    .references(() => students.id, { onDelete: "cascade" }),
  name: text("name").notNull(),
  cpf: varchar("cpf", { length: 14 }).notNull(),
  phone: varchar("phone", { length: 20 }).notNull(),
  email: varchar("email", { length: 320 }),
  createdAt: timestamp("createdAt").defaultNow(),
});
```

**Campos:**
- `id`: Identificador único (UUID)
- `studentId`: Referência ao aluno (FK com cascade delete)
- `name`: Nome completo do responsável (obrigatório)
- `cpf`: CPF do responsável (obrigatório)
- `phone`: Telefone do responsável (obrigatório)
- `email`: Email do responsável (opcional)
- `createdAt`: Data de cadastro

**Relacionamento:** Um aluno pode ter zero ou um responsável. Quando um aluno é excluído, seu responsável também é excluído automaticamente (cascade delete).

#### Tabela: attendance

Armazena registros de presença por aluno e data.

```typescript
export const attendance = mysqlTable("attendance", {
  id: varchar("id", { length: 64 }).primaryKey(),
  studentId: varchar("studentId", { length: 64 })
    .notNull()
    .references(() => students.id, { onDelete: "cascade" }),
  classDate: date("classDate").notNull(),
  present: boolean("present").notNull(),
  notes: text("notes"),
  createdAt: timestamp("createdAt").defaultNow(),
  updatedAt: timestamp("updatedAt").defaultNow().onUpdateNow(),
});
```

**Campos:**
- `id`: Identificador único (UUID)
- `studentId`: Referência ao aluno (FK com cascade delete)
- `classDate`: Data da aula
- `present`: Presente (true) ou ausente (false)
- `notes`: Observações (opcional, não usado atualmente)
- `createdAt`: Data de criação do registro
- `updatedAt`: Data da última atualização

**Relacionamento:** Um aluno pode ter múltiplos registros de presença. Quando um aluno é excluído, todos seus registros de presença também são excluídos automaticamente (cascade delete).

### Diagrama de Relacionamentos

```
┌──────────────┐
│    users     │
│              │
│ id (PK)      │
│ name         │
│ email (UQ)   │
│ password     │
│ role         │
└──────────────┘

┌──────────────┐         ┌──────────────┐
│   students   │         │  guardians   │
│              │         │              │
│ id (PK)      │◄────────│ studentId(FK)│
│ name         │  1:0..1 │ name         │
│ birthDate    │         │ cpf          │
│ phone        │         │ phone        │
│ email        │         │ email        │
│ address      │         └──────────────┘
│ motherName   │
│ fatherName   │
│ isActive     │
└──────┬───────┘
       │
       │ 1:N
       │
┌──────┴───────┐
│  attendance  │
│              │
│ studentId(FK)│
│ classDate    │
│ present      │
│ notes        │
└──────────────┘
```

### Índices e Performance

**Índices Automáticos:**
- Primary Keys em todas as tabelas (id)
- Unique index em users.email
- Foreign Keys em guardians.studentId e attendance.studentId

**Índices Recomendados para Produção:**

```sql
-- Melhorar performance de queries de presença por data
CREATE INDEX idx_attendance_date ON attendance(classDate);

-- Melhorar performance de queries de alunos ativos
CREATE INDEX idx_students_active ON students(isActive);

-- Melhorar performance de queries de presença por aluno e data
CREATE INDEX idx_attendance_student_date ON attendance(studentId, classDate);
```

### Migrações

O sistema usa Drizzle Kit para gerenciar migrações. Para aplicar o schema ao banco de dados:

```bash
pnpm db:push
```

Este comando:
1. Compara o schema em `drizzle/schema.ts` com o banco de dados
2. Gera SQL para sincronizar
3. Aplica as alterações automaticamente

---

## Backend - API e Lógica de Negócio

### Estrutura dos Routers tRPC

O backend é organizado em routers tRPC que definem os endpoints da API de forma type-safe.

#### Router de Autenticação

```typescript
auth: router({
  // Retorna usuário autenticado atual
  me: publicProcedure.query(opts => opts.ctx.user),
  
  // Logout (limpa cookie de sessão)
  logout: publicProcedure.mutation(({ ctx }) => {
    ctx.res.clearCookie(COOKIE_NAME, cookieOptions);
    return { success: true };
  }),
  
  // Login com email e senha
  login: publicProcedure
    .input(z.object({
      email: z.string().email(),
      password: z.string().min(6),
    }))
    .mutation(async ({ input, ctx }) => {
      // Busca usuário por email
      const user = await getUserByEmail(input.email);
      if (!user || !user.password) {
        throw new TRPCError({
          code: "UNAUTHORIZED",
          message: "Email ou senha incorretos",
        });
      }
      
      // Verifica senha com bcrypt
      const valid = await bcrypt.compare(input.password, user.password);
      if (!valid) {
        throw new TRPCError({
          code: "UNAUTHORIZED",
          message: "Email ou senha incorretos",
        });
      }
      
      // Gera JWT
      const token = jwt.sign(
        { userId: user.id, email: user.email },
        JWT_SECRET,
        { expiresIn: "7d" }
      );
      
      // Define cookie de sessão
      ctx.res.cookie(COOKIE_NAME, token, cookieOptions);
      
      return { user, token };
    }),
  
  // Registro de novo usuário
  register: publicProcedure
    .input(z.object({
      name: z.string().min(3),
      email: z.string().email(),
      password: z.string().min(6),
    }))
    .mutation(async ({ input, ctx }) => {
      // Verifica se email já existe
      const existing = await getUserByEmail(input.email);
      if (existing) {
        throw new TRPCError({
          code: "CONFLICT",
          message: "Email já cadastrado",
        });
      }
      
      // Criptografa senha com bcrypt
      const hashedPassword = await bcrypt.hash(input.password, 10);
      
      // Cria usuário
      const userId = crypto.randomUUID();
      await createUser({
        id: userId,
        name: input.name,
        email: input.email,
        password: hashedPassword,
      });
      
      // Gera JWT e define cookie
      const token = jwt.sign(
        { userId, email: input.email },
        JWT_SECRET,
        { expiresIn: "7d" }
      );
      
      ctx.res.cookie(COOKIE_NAME, token, cookieOptions);
      
      return { success: true };
    }),
  
  // Alteração de senha
  changePassword: protectedProcedure
    .input(z.object({
      currentPassword: z.string(),
      newPassword: z.string().min(6),
    }))
    .mutation(async ({ input, ctx }) => {
      // Busca usuário atual
      const user = await getUser(ctx.user.id);
      if (!user || !user.password) {
        throw new TRPCError({ code: "NOT_FOUND" });
      }
      
      // Verifica senha atual
      const valid = await bcrypt.compare(input.currentPassword, user.password);
      if (!valid) {
        throw new TRPCError({
          code: "UNAUTHORIZED",
          message: "Senha atual incorreta",
        });
      }
      
      // Atualiza senha
      const hashedPassword = await bcrypt.hash(input.newPassword, 10);
      await updateUserPassword(ctx.user.id, hashedPassword);
      
      return { success: true };
    }),
})
```

#### Router de Alunos

```typescript
students: router({
  // Listar todos os alunos
  list: protectedProcedure.query(async () => {
    return await getAllStudents();
  }),
  
  // Listar apenas alunos ativos
  listActive: protectedProcedure.query(async () => {
    return await getActiveStudents();
  }),
  
  // Buscar aluno por ID
  getById: protectedProcedure
    .input(z.object({ id: z.string() }))
    .query(async ({ input }) => {
      return await getStudentById(input.id);
    }),
  
  // Criar novo aluno
  create: protectedProcedure
    .input(z.object({
      name: z.string().min(3),
      birthDate: z.string(), // YYYY-MM-DD
      phone: z.string().optional(),
      email: z.string().email().optional(),
      address: z.string().optional(),
      motherName: z.string().optional(),
      fatherName: z.string().optional(),
      guardian: z.object({
        name: z.string(),
        cpf: z.string(),
        phone: z.string(),
        email: z.string().email().optional(),
      }).optional(),
    }))
    .mutation(async ({ input }) => {
      const studentId = crypto.randomUUID();
      
      // Cria aluno
      await createStudent({
        id: studentId,
        ...input,
        birthDate: new Date(input.birthDate),
      });
      
      // Cria responsável se fornecido
      if (input.guardian) {
        await createGuardian({
          id: crypto.randomUUID(),
          studentId,
          ...input.guardian,
        });
      }
      
      return { success: true, id: studentId };
    }),
  
  // Atualizar aluno
  update: protectedProcedure
    .input(z.object({
      id: z.string(),
      name: z.string().min(3).optional(),
      birthDate: z.string().optional(),
      phone: z.string().optional(),
      email: z.string().email().optional(),
      address: z.string().optional(),
      motherName: z.string().optional(),
      fatherName: z.string().optional(),
      isActive: z.boolean().optional(),
      guardian: z.object({
        name: z.string(),
        cpf: z.string(),
        phone: z.string(),
        email: z.string().email().optional(),
      }).optional(),
    }))
    .mutation(async ({ input }) => {
      const { id, guardian, ...studentData } = input;
      
      // Atualiza aluno
      await updateStudent(id, {
        ...studentData,
        birthDate: studentData.birthDate ? new Date(studentData.birthDate) : undefined,
      });
      
      // Atualiza ou cria responsável
      if (guardian) {
        const existing = await getGuardianByStudentId(id);
        if (existing) {
          await updateGuardian(existing.id, guardian);
        } else {
          await createGuardian({
            id: crypto.randomUUID(),
            studentId: id,
            ...guardian,
          });
        }
      }
      
      return { success: true };
    }),
  
  // Excluir aluno
  delete: protectedProcedure
    .input(z.object({ id: z.string() }))
    .mutation(async ({ input }) => {
      await deleteStudent(input.id);
      return { success: true };
    }),
})
```

#### Router de Presença

```typescript
attendance: router({
  // Registrar presença
  record: protectedProcedure
    .input(z.object({
      studentId: z.string(),
      classDate: z.string(), // YYYY-MM-DD
      present: z.boolean(),
    }))
    .mutation(async ({ input }) => {
      // Verifica se já existe registro para esta data
      const existing = await getAttendanceByStudentAndDate(
        input.studentId,
        input.classDate
      );
      
      if (existing) {
        // Atualiza registro existente
        await updateAttendance(existing.id, {
          present: input.present,
        });
      } else {
        // Cria novo registro
        await createAttendance({
          id: crypto.randomUUID(),
          studentId: input.studentId,
          classDate: new Date(input.classDate),
          present: input.present,
        });
      }
      
      return { success: true };
    }),
  
  // Buscar presença por data
  getByDate: protectedProcedure
    .input(z.object({ classDate: z.string() }))
    .query(async ({ input }) => {
      return await getAttendanceByDate(input.classDate);
    }),
  
  // Buscar presença por aluno
  getByStudent: protectedProcedure
    .input(z.object({
      studentId: z.string(),
      startDate: z.string().optional(),
      endDate: z.string().optional(),
    }))
    .query(async ({ input }) => {
      return await getAttendanceByStudent(
        input.studentId,
        input.startDate,
        input.endDate
      );
    }),
  
  // Estatísticas de frequência
  getStats: protectedProcedure
    .input(z.object({
      studentId: z.string(),
      startDate: z.string().optional(),
      endDate: z.string().optional(),
    }))
    .query(async ({ input }) => {
      const records = await getAttendanceByStudent(
        input.studentId,
        input.startDate,
        input.endDate
      );
      
      const total = records.length;
      const present = records.filter(r => r.present).length;
      const absent = total - present;
      const rate = total > 0 ? (present / total) * 100 : 0;
      
      return {
        total,
        present,
        absent,
        rate: Math.round(rate * 10) / 10,
      };
    }),
})
```

### Middleware de Autenticação

O sistema usa dois tipos de procedures:

**publicProcedure:** Acessível sem autenticação (login, registro)

**protectedProcedure:** Requer autenticação via JWT

```typescript
export const protectedProcedure = publicProcedure.use(({ ctx, next }) => {
  if (!ctx.user) {
    throw new TRPCError({
      code: "UNAUTHORIZED",
      message: "Você precisa estar autenticado",
    });
  }
  
  return next({
    ctx: {
      ...ctx,
      user: ctx.user, // Garante que user não é null
    },
  });
});
```

### Funções de Acesso ao Banco (db.ts)

Todas as queries ao banco são encapsuladas em funções reutilizáveis:

```typescript
// Exemplo: Buscar aluno por ID
export async function getStudentById(id: string) {
  const db = await getDb();
  if (!db) return undefined;
  
  const result = await db
    .select()
    .from(students)
    .where(eq(students.id, id))
    .limit(1);
  
  return result[0];
}

// Exemplo: Criar aluno
export async function createStudent(data: InsertStudent) {
  const db = await getDb();
  if (!db) throw new Error("Database not available");
  
  await db.insert(students).values(data);
}

// Exemplo: Atualizar aluno
export async function updateStudent(
  id: string,
  data: Partial<InsertStudent>
) {
  const db = await getDb();
  if (!db) throw new Error("Database not available");
  
  await db
    .update(students)
    .set(data)
    .where(eq(students.id, id));
}
```

---

## Frontend - Interface do Usuário

### Estrutura de Componentes

O frontend segue uma arquitetura baseada em componentes React com separação clara entre páginas, componentes reutilizáveis e lógica de negócio.

#### Componente de Login

```typescript
export default function Login() {
  const [isLogin, setIsLogin] = useState(true);
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
  });

  const loginMutation = trpc.auth.login.useMutation({
    onSuccess: () => {
      window.location.href = "/";
    },
    onError: (error) => {
      toast.error(error.message);
    },
  });

  const registerMutation = trpc.auth.register.useMutation({
    onSuccess: () => {
      window.location.href = "/";
    },
    onError: (error) => {
      toast.error(error.message);
    },
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    if (isLogin) {
      loginMutation.mutate({
        email: formData.email,
        password: formData.password,
      });
    } else {
      registerMutation.mutate(formData);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center">
      <Card className="w-full max-w-md">
        <CardHeader>
          <img src="/logo.jpg" alt="Eu Sou Ninja" className="h-32 mx-auto" />
          <CardTitle>{isLogin ? "Login" : "Criar Conta"}</CardTitle>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-4">
            {!isLogin && (
              <div>
                <Label htmlFor="name">Nome Completo</Label>
                <Input
                  id="name"
                  value={formData.name}
                  onChange={(e) => setFormData({...formData, name: e.target.value})}
                  required={!isLogin}
                />
              </div>
            )}
            
            <div>
              <Label htmlFor="email">Email</Label>
              <Input
                id="email"
                type="email"
                value={formData.email}
                onChange={(e) => setFormData({...formData, email: e.target.value})}
                required
              />
            </div>
            
            <div>
              <Label htmlFor="password">Senha</Label>
              <Input
                id="password"
                type="password"
                value={formData.password}
                onChange={(e) => setFormData({...formData, password: e.target.value})}
                required
              />
            </div>
            
            <Button type="submit" className="w-full">
              {isLogin ? "Entrar" : "Criar Conta"}
            </Button>
            
            <Button
              type="button"
              variant="outline"
              onClick={() => setIsLogin(!isLogin)}
              className="w-full"
            >
              {isLogin ? "Não tem conta? Registre-se" : "Já tem uma conta? Faça login"}
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}
```

#### Hook de Autenticação

```typescript
export function useAuth() {
  const { data: user, isLoading, error } = trpc.auth.me.useQuery();
  
  return {
    user,
    loading: isLoading,
    error,
    isAuthenticated: !!user,
  };
}
```

#### Componente de Cadastro de Aluno

```typescript
export default function Students() {
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [editingStudent, setEditingStudent] = useState<Student | null>(null);
  const [formData, setFormData] = useState({
    name: "",
    birthDate: "",
    phone: "",
    email: "",
    address: "",
    motherName: "",
    fatherName: "",
    isActive: true,
    guardian: {
      name: "",
      cpf: "",
      phone: "",
      email: "",
    },
  });

  const utils = trpc.useUtils();
  const { data: students } = trpc.students.list.useQuery();

  const createMutation = trpc.students.create.useMutation({
    onSuccess: () => {
      toast.success("Aluno cadastrado com sucesso!");
      utils.students.list.invalidate();
      setIsDialogOpen(false);
      resetForm();
    },
    onError: (error) => {
      toast.error(error.message);
    },
  });

  const updateMutation = trpc.students.update.useMutation({
    onSuccess: () => {
      toast.success("Aluno atualizado com sucesso!");
      utils.students.list.invalidate();
      setIsDialogOpen(false);
      resetForm();
    },
    onError: (error) => {
      toast.error(error.message);
    },
  });

  const deleteMutation = trpc.students.delete.useMutation({
    onSuccess: () => {
      toast.success("Aluno excluído com sucesso!");
      utils.students.list.invalidate();
    },
    onError: (error) => {
      toast.error(error.message);
    },
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    // Calcula idade
    const age = calculateAge(formData.birthDate);
    const needsGuardian = age < 18;
    
    if (needsGuardian && !formData.guardian.name) {
      toast.error("Aluno menor de idade precisa de responsável legal");
      return;
    }
    
    if (editingStudent) {
      updateMutation.mutate({
        id: editingStudent.id,
        ...formData,
        guardian: needsGuardian ? formData.guardian : undefined,
      });
    } else {
      createMutation.mutate({
        ...formData,
        guardian: needsGuardian ? formData.guardian : undefined,
      });
    }
  };

  // ... resto do componente
}
```

### Gerenciamento de Estado

O sistema usa **React Query** (via tRPC) para gerenciamento de estado servidor:

**Queries:** Buscar dados do servidor
```typescript
const { data, isLoading, error } = trpc.students.list.useQuery();
```

**Mutations:** Modificar dados no servidor
```typescript
const mutation = trpc.students.create.useMutation({
  onSuccess: () => {
    // Invalidar cache para refetch
    utils.students.list.invalidate();
  },
});
```

**Invalidação de Cache:** Após mutations, o cache é invalidado para refetch automático:
```typescript
const utils = trpc.useUtils();
utils.students.list.invalidate(); // Refetch lista de alunos
```

### Roteamento

O sistema usa **Wouter** para roteamento client-side:

```typescript
function Router() {
  return (
    <Switch>
      <Route path="/login" component={Login} />
      <Route path="/">
        <ProtectedRoute component={Students} />
      </Route>
      <Route path="/attendance">
        <ProtectedRoute component={Attendance} />
      </Route>
      <Route path="/reports">
        <ProtectedRoute component={Reports} />
      </Route>
      <Route path="/about">
        <ProtectedRoute component={About} />
      </Route>
      <Route path="/settings">
        <ProtectedRoute component={Settings} />
      </Route>
      <Route component={NotFound} />
    </Switch>
  );
}

function ProtectedRoute({ component: Component }) {
  const { user, loading } = useAuth();

  if (loading) return <LoadingSpinner />;
  if (!user) return <Redirect to="/login" />;

  return (
    <DashboardLayout>
      <Component />
    </DashboardLayout>
  );
}
```

### Estilização com Tailwind CSS

O sistema usa Tailwind CSS com tema personalizado:

```css
/* index.css */
@layer base {
  :root {
    --background: oklch(0.985 0 0);
    --foreground: oklch(0.145 0 0);
    --primary: oklch(0.35 0.15 30); /* Tom marrom/terra */
    --primary-foreground: oklch(0.985 0 0);
    /* ... outras variáveis */
  }
}
```

Componentes usam classes utility:

```tsx
<Card className="w-full max-w-4xl">
  <CardHeader>
    <CardTitle className="text-2xl font-bold">Alunos</CardTitle>
  </CardHeader>
  <CardContent className="space-y-4">
    {/* conteúdo */}
  </CardContent>
</Card>
```

---

## Autenticação e Segurança

### Fluxo de Autenticação

1. **Registro:**
   - Usuário preenche formulário com nome, email e senha
   - Frontend envia dados para `auth.register`
   - Backend valida dados com Zod
   - Backend criptografa senha com bcrypt (10 rounds)
   - Backend cria usuário no banco de dados
   - Backend gera JWT com payload `{userId, email}`
   - Backend define cookie httpOnly com JWT
   - Frontend redireciona para dashboard

2. **Login:**
   - Usuário preenche email e senha
   - Frontend envia para `auth.login`
   - Backend busca usuário por email
   - Backend compara senha com hash usando bcrypt
   - Se válido, gera JWT e define cookie
   - Frontend redireciona para dashboard

3. **Verificação de Sessão:**
   - A cada requisição, middleware extrai JWT do cookie
   - Verifica assinatura do JWT com `JWT_SECRET`
   - Decodifica payload e busca usuário no banco
   - Injeta usuário no contexto tRPC
   - Procedures protegidas verificam presença de usuário

4. **Logout:**
   - Frontend chama `auth.logout`
   - Backend limpa cookie de sessão
   - Frontend redireciona para login

### Segurança de Senhas

**Criptografia com bcrypt:**

```typescript
// Registro: hash da senha
const hashedPassword = await bcrypt.hash(password, 10);
// 10 = número de rounds (2^10 = 1024 iterações)

// Login: comparação segura
const valid = await bcrypt.compare(password, hashedPassword);
```

**Características do bcrypt:**
- Algoritmo adaptativo (pode aumentar rounds com hardware mais rápido)
- Inclui salt automático (protege contra rainbow tables)
- Resistente a ataques de timing
- Computacionalmente custoso (dificulta brute force)

### JWT (JSON Web Tokens)

**Estrutura do Token:**

```
Header.Payload.Signature
```

**Payload:**
```json
{
  "userId": "uuid-do-usuario",
  "email": "usuario@email.com",
  "iat": 1234567890,
  "exp": 1235172690
}
```

**Geração:**
```typescript
const token = jwt.sign(
  { userId, email },
  JWT_SECRET,
  { expiresIn: "7d" }
);
```

**Verificação:**
```typescript
const decoded = jwt.verify(token, JWT_SECRET);
```

### Cookies Seguros

**Configuração do Cookie:**

```typescript
const cookieOptions = {
  httpOnly: true,      // Não acessível via JavaScript
  secure: true,        // Apenas HTTPS em produção
  sameSite: "lax",     // Proteção CSRF
  maxAge: 7 * 24 * 60 * 60 * 1000, // 7 dias
  path: "/",
};
```

**Proteções:**
- `httpOnly`: Previne XSS (Cross-Site Scripting)
- `secure`: Garante transmissão apenas via HTTPS
- `sameSite`: Previne CSRF (Cross-Site Request Forgery)

### Validação de Dados

**Zod Schemas:**

Todos os inputs são validados com Zod antes de processamento:

```typescript
const loginSchema = z.object({
  email: z.string().email("Email inválido"),
  password: z.string().min(6, "Senha deve ter no mínimo 6 caracteres"),
});

// Uso no tRPC
.input(loginSchema)
.mutation(async ({ input }) => {
  // input é tipado e validado
});
```

### Proteção contra Ataques Comuns

**SQL Injection:** Drizzle ORM usa prepared statements automaticamente

**XSS:** React escapa automaticamente strings renderizadas

**CSRF:** Cookie com `sameSite: "lax"` + verificação de origem

**Brute Force:** bcrypt torna tentativas lentas (pode adicionar rate limiting)

---

## Guia de Instalação Local

### Pré-requisitos

Instale as seguintes ferramentas:

1. **Node.js 22.13.0 ou superior**
   - Download: https://nodejs.org/
   - Verifique: `node --version`

2. **pnpm (gerenciador de pacotes)**
   ```bash
   npm install -g pnpm
   ```
   - Verifique: `pnpm --version`

3. **MySQL 8.x**
   - Opções:
     - MySQL Community Server: https://dev.mysql.com/downloads/
     - Docker: `docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql:8`
   - Verifique: `mysql --version`

4. **Git**
   - Download: https://git-scm.com/
   - Verifique: `git --version`

### Passo a Passo

#### 1. Clonar o Repositório

```bash
git clone <url-do-repositorio>
cd eusouninja
```

#### 2. Instalar Dependências

```bash
pnpm install
```

Este comando instala todas as dependências listadas em `package.json`.

#### 3. Configurar Banco de Dados

Crie um banco de dados MySQL:

```sql
CREATE DATABASE eusouninja CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

#### 4. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
# Banco de Dados
DATABASE_URL="mysql://usuario:senha@localhost:3306/eusouninja"

# Segurança
JWT_SECRET="sua-chave-secreta-muito-longa-e-aleatoria"

# Aplicação
VITE_APP_TITLE="Eu Sou Ninja - Sistema de Gestão de Alunos"
VITE_APP_LOGO="/logo.jpg"
```

**Importante:**
- Substitua `usuario` e `senha` pelas credenciais do seu MySQL
- Gere um `JWT_SECRET` forte (ex: use `openssl rand -base64 32`)

#### 5. Aplicar Migrações

```bash
pnpm db:push
```

Este comando cria todas as tabelas no banco de dados.

#### 6. Iniciar Servidor de Desenvolvimento

```bash
pnpm dev
```

Isso inicia:
- Frontend (Vite): http://localhost:5173
- Backend (Express): http://localhost:3000

#### 7. Acessar o Sistema

Abra o navegador em: http://localhost:5173

### Scripts Disponíveis

```json
{
  "dev": "Inicia servidor de desenvolvimento",
  "build": "Compila para produção",
  "start": "Inicia servidor de produção",
  "db:push": "Aplica schema ao banco de dados",
  "db:studio": "Abre interface visual do banco",
  "lint": "Executa linter",
  "type-check": "Verifica tipos TypeScript"
}
```

### Solução de Problemas na Instalação

**Erro: Cannot find module 'bcrypt'**
```bash
pnpm add bcrypt
pnpm approve-builds bcrypt
```

**Erro: Cannot connect to database**
- Verifique se MySQL está rodando
- Verifique credenciais em `DATABASE_URL`
- Teste conexão: `mysql -u usuario -p`

**Erro: Port 3000 already in use**
- Mude a porta em `server/index.ts`
- Ou mate o processo: `lsof -ti:3000 | xargs kill`

**Erro: EACCES permission denied**
```bash
sudo chown -R $(whoami) ~/.pnpm-store
```

---

## Guia de Deploy em Produção

### Preparação para Deploy

#### 1. Build de Produção

```bash
pnpm build
```

Isso gera:
- `client/dist/`: Frontend compilado
- `server/dist/`: Backend compilado

#### 2. Variáveis de Ambiente

Configure as seguintes variáveis na plataforma de hospedagem:

```
DATABASE_URL=mysql://user:pass@host:3306/dbname
JWT_SECRET=chave-secreta-forte
NODE_ENV=production
VITE_APP_TITLE=Eu Sou Ninja - Sistema de Gestão de Alunos
VITE_APP_LOGO=/logo.jpg
```

### Deploy no Vercel

#### Pré-requisitos
- Conta no Vercel
- Conta no PlanetScale (banco de dados)
- Repositório no GitHub

#### Configuração do PlanetScale

1. Acesse https://planetscale.com
2. Crie novo banco de dados
3. Copie a connection string
4. Adicione à `DATABASE_URL`

#### Deploy no Vercel

1. **Conectar Repositório:**
   - Acesse https://vercel.com
   - New Project → Import Git Repository
   - Selecione seu repositório

2. **Configurar Build:**
   - Build Command: `pnpm build`
   - Output Directory: `client/dist`
   - Install Command: `pnpm install`

3. **Variáveis de Ambiente:**
   - Adicione todas as variáveis listadas acima

4. **Deploy:**
   - Clique em "Deploy"
   - Aguarde conclusão

5. **Migrações:**
   - Após deploy, acesse o terminal do Vercel
   - Execute: `pnpm db:push`

#### Configuração de Domínio

1. Vá em Settings → Domains
2. Adicione seu domínio
3. Configure DNS conforme instruções

### Deploy no Railway

#### Configuração

1. **Criar Projeto:**
   - Acesse https://railway.app
   - New Project → Deploy from GitHub

2. **Adicionar Banco de Dados:**
   - New → Database → PostgreSQL
   - Railway conecta automaticamente

3. **Variáveis de Ambiente:**
   - Railway preenche `DATABASE_URL` automaticamente
   - Adicione `JWT_SECRET` manualmente

4. **Deploy:**
   - Railway faz deploy automático
   - Execute migrações no terminal

### Deploy no Render

#### Configuração

1. **Criar Banco de Dados:**
   - New → PostgreSQL
   - Copie Internal Database URL

2. **Criar Web Service:**
   - New → Web Service
   - Conecte repositório GitHub

3. **Configurar Build:**
   - Build Command: `pnpm install && pnpm build`
   - Start Command: `pnpm start`

4. **Variáveis de Ambiente:**
   - Adicione todas as variáveis

5. **Deploy:**
   - Render faz deploy automático
   - Execute migrações no Shell

### Otimizações de Produção

#### Compressão

Adicione compressão gzip no Express:

```typescript
import compression from "compression";
app.use(compression());
```

#### Cache de Assets

Configure headers de cache para assets estáticos:

```typescript
app.use(express.static("client/dist", {
  maxAge: "1y",
  etag: true,
}));
```

#### Logging

Use Winston ou Pino para logs estruturados:

```typescript
import winston from "winston";

const logger = winston.createLogger({
  level: "info",
  format: winston.format.json(),
  transports: [
    new winston.transports.File({ filename: "error.log", level: "error" }),
    new winston.transports.File({ filename: "combined.log" }),
  ],
});
```

#### Monitoramento

Configure monitoramento de erros com Sentry:

```typescript
import * as Sentry from "@sentry/node";

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.NODE_ENV,
});
```

### Backup e Recuperação

#### Backup Automático

Configure backups automáticos do banco de dados:

**PlanetScale:** Backups automáticos diários incluídos

**Railway:** Configure backups manuais via CLI

**Render:** Backups automáticos no plano pago

#### Backup Manual

```bash
# Exportar banco de dados
mysqldump -u user -p eusouninja > backup.sql

# Importar backup
mysql -u user -p eusouninja < backup.sql
```

### Monitoramento de Performance

Use ferramentas para monitorar:

- **Uptime:** UptimeRobot, Pingdom
- **Performance:** New Relic, Datadog
- **Logs:** Papertrail, Loggly
- **Erros:** Sentry, Rollbar

---

## Manutenção e Extensões

### Adicionando Novas Funcionalidades

#### Exemplo: Adicionar Campo "Graduação" aos Alunos

**1. Atualizar Schema do Banco:**

```typescript
// drizzle/schema.ts
export const students = mysqlTable("students", {
  // ... campos existentes
  graduation: varchar("graduation", { length: 50 }), // Nova coluna
});
```

**2. Aplicar Migração:**

```bash
pnpm db:push
```

**3. Atualizar Funções do Banco:**

```typescript
// server/db.ts
export async function updateStudent(id: string, data: Partial<InsertStudent>) {
  // Já funciona automaticamente com novo campo
}
```

**4. Atualizar Router:**

```typescript
// server/routers.ts
students: router({
  create: protectedProcedure
    .input(z.object({
      // ... campos existentes
      graduation: z.string().optional(), // Validação
    }))
    .mutation(async ({ input }) => {
      // Já funciona automaticamente
    }),
})
```

**5. Atualizar Frontend:**

```typescript
// client/src/pages/Students.tsx
const [formData, setFormData] = useState({
  // ... campos existentes
  graduation: "",
});

// Adicionar campo no formulário
<div>
  <Label htmlFor="graduation">Graduação</Label>
  <Input
    id="graduation"
    value={formData.graduation}
    onChange={(e) => setFormData({...formData, graduation: e.target.value})}
  />
</div>
```

### Adicionando Novos Módulos

#### Exemplo: Módulo de Eventos

**1. Criar Tabela:**

```typescript
// drizzle/schema.ts
export const events = mysqlTable("events", {
  id: varchar("id", { length: 64 }).primaryKey(),
  title: text("title").notNull(),
  description: text("description"),
  eventDate: date("eventDate").notNull(),
  location: text("location"),
  createdAt: timestamp("createdAt").defaultNow(),
});
```

**2. Criar Funções de Acesso:**

```typescript
// server/db.ts
export async function getAllEvents() {
  const db = await getDb();
  if (!db) return [];
  return await db.select().from(events).orderBy(desc(events.eventDate));
}

export async function createEvent(data: InsertEvent) {
  const db = await getDb();
  if (!db) throw new Error("Database not available");
  await db.insert(events).values(data);
}
```

**3. Criar Router:**

```typescript
// server/routers.ts
events: router({
  list: protectedProcedure.query(async () => {
    return await getAllEvents();
  }),
  
  create: protectedProcedure
    .input(z.object({
      title: z.string().min(3),
      description: z.string().optional(),
      eventDate: z.string(),
      location: z.string().optional(),
    }))
    .mutation(async ({ input }) => {
      await createEvent({
        id: crypto.randomUUID(),
        ...input,
        eventDate: new Date(input.eventDate),
      });
      return { success: true };
    }),
})
```

**4. Criar Página Frontend:**

```typescript
// client/src/pages/Events.tsx
export default function Events() {
  const { data: events } = trpc.events.list.useQuery();
  
  return (
    <div>
      <h1>Eventos</h1>
      {events?.map(event => (
        <Card key={event.id}>
          <CardHeader>
            <CardTitle>{event.title}</CardTitle>
          </CardHeader>
          <CardContent>
            <p>{event.description}</p>
            <p>{new Date(event.eventDate).toLocaleDateString()}</p>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}
```

**5. Adicionar Rota:**

```typescript
// client/src/App.tsx
<Route path="/events">
  <ProtectedRoute component={Events} />
</Route>
```

### Atualizações de Dependências

#### Verificar Atualizações

```bash
pnpm outdated
```

#### Atualizar Dependências

```bash
# Atualizar todas (cuidado!)
pnpm update

# Atualizar específica
pnpm update react

# Atualizar para última versão
pnpm add react@latest
```

#### Testar Após Atualização

```bash
pnpm type-check
pnpm lint
pnpm build
pnpm dev # Testar manualmente
```

### Debugging

#### Logs no Backend

```typescript
console.log("Debug:", variavel);
console.error("Erro:", error);
```

#### Logs no Frontend

```typescript
console.log("Estado:", formData);
console.table(students); // Visualizar arrays
```

#### DevTools

- **React DevTools:** Inspecionar componentes
- **Network Tab:** Ver requisições tRPC
- **Console:** Ver erros e logs

#### Debugging com VSCode

Crie `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Debug Server",
      "program": "${workspaceFolder}/server/index.ts",
      "preLaunchTask": "tsc: build - tsconfig.json",
      "outFiles": ["${workspaceFolder}/server/dist/**/*.js"]
    }
  ]
}
```

### Testes

#### Testes Unitários com Vitest

```bash
pnpm add -D vitest
```

```typescript
// server/db.test.ts
import { describe, it, expect } from "vitest";
import { calculateAge } from "./utils";

describe("calculateAge", () => {
  it("calcula idade corretamente", () => {
    const birthDate = "2000-01-01";
    const age = calculateAge(birthDate);
    expect(age).toBeGreaterThan(20);
  });
});
```

#### Testes de Integração

```typescript
// server/routers.test.ts
import { describe, it, expect } from "vitest";
import { appRouter } from "./routers";

describe("Students Router", () => {
  it("cria aluno com sucesso", async () => {
    const caller = appRouter.createCaller({
      user: { id: "test", email: "test@test.com" },
    });
    
    const result = await caller.students.create({
      name: "Teste",
      birthDate: "2000-01-01",
    });
    
    expect(result.success).toBe(true);
  });
});
```

### Performance

#### Otimizar Queries

```typescript
// Evitar N+1 queries
const studentsWithGuardians = await db
  .select()
  .from(students)
  .leftJoin(guardians, eq(students.id, guardians.studentId));

// Usar índices
CREATE INDEX idx_students_active ON students(isActive);
```

#### Lazy Loading de Componentes

```typescript
import { lazy, Suspense } from "react";

const Reports = lazy(() => import("./pages/Reports"));

<Suspense fallback={<Loading />}>
  <Reports />
</Suspense>
```

#### Memoização

```typescript
import { useMemo } from "react";

const sortedStudents = useMemo(() => {
  return students?.sort((a, b) => a.name.localeCompare(b.name));
}, [students]);
```

---

## Conclusão

Esta documentação técnica cobre todos os aspectos do Sistema Eu Sou Ninja, desde a arquitetura até o deploy em produção. O sistema foi desenvolvido com tecnologias modernas e boas práticas de desenvolvimento, garantindo segurança, performance e facilidade de manutenção.

### Recursos Adicionais

**Documentação das Tecnologias:**
- React: https://react.dev
- TypeScript: https://www.typescriptlang.org
- tRPC: https://trpc.io
- Drizzle ORM: https://orm.drizzle.team
- Tailwind CSS: https://tailwindcss.com
- shadcn/ui: https://ui.shadcn.com

**Comunidades:**
- Discord do tRPC
- Stack Overflow
- GitHub Discussions

### Suporte

Para questões técnicas ou dúvidas sobre o código:

**Email:** projetoeusouninja@gmail.com  
**Desenvolvedor:** Manus AI  
**Repositório:** [URL do repositório]

---

**Desenvolvido com dedicação para o Projeto Social Eu Sou Ninja**  
**Versão 1.0.0 - Outubro 2025**

