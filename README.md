# academia-dev-python

### 📄 Sobre o Projeto

O projeto **academia-dev-python** é um **Sistema de Gerenciamento** desenvolvido utilizando o framework **Django** para a parte web (templates e views) e o **Django Rest Framework (DRF)** para a exposição de uma API RESTful completa.

O sistema é modularizado em aplicativos Django (`students`, `courses`, `enrollments`, `finance`) e permite a gestão das seguintes entidades:

* **Alunos:** Cadastro de informações como nome, email e CPF.
* **Cursos:** Gerenciamento de cursos com carga horária, taxa de matrícula e status.
* **Matrículas:** Relação entre alunos e cursos, com controle de data de matrícula e status financeiro.
* **Financeiro:** Visualização do resumo financeiro por aluno e listagem de matrículas filtradas por status.

A página inicial (`/`) oferece um painel de controle com o total de alunos, cursos ativos, matrículas pagas e matrículas pendentes.

***

### 🛠 Tecnologias Utilizadas

As principais tecnologias e dependências utilizadas no projeto são:

* **Linguagem:** Python.
* **Framework Web:** Django.
* **API:** Django Rest Framework.
* **Containerização:** Docker e Docker Compose.
* **Estilização:** Bootstrap.
* **Banco de Dados:** SQLite.

***

### 🌐 Rotas da Aplicação (Endpoints)

As rotas da aplicação são divididas entre **Web Views** e **API Endpoints**.

#### 1. Rotas Web (Views)

| URL Pattern | Nome | Descrição |
| :--- | :--- | :--- |
| `/` | `home` | Tela inicial da aplicação com um resumo dos indicadores. |
| `/admin/` | `admin` | Acesso ao painel administrativo do Django. |
| `/students/list/` | `student-list` | Exibe a lista completa de alunos. |
| `/students/<int:pk>/detail/` | `student-detail` | Detalhes de um aluno, com a listagem de seus cursos matriculados e totalização de pagamentos. |
| `/courses/list/` | `course-list` | Lista todos os cursos disponíveis. |
| `/enrollments/list/` | `enrollment-list` | Lista todas as matrículas realizadas. |
| `/finance/enrollments/` | `finance-enrollments` | Lista financeira das matrículas, com opção de filtro por status. |
| `/finance/<int:pk>/` | `finance-student` | Resumo financeiro de um aluno específico. |

#### 2. API Endpoints (v1)

| URL Pattern | Método(s) | Descrição |
| :--- | :--- | :--- |
| `/api/v1/students/` | `GET`, `POST` | Lista todos os alunos ou cria um novo aluno. |
| `/api/v1/students/<int:pk>/` | `GET`, `PUT`, `PATCH`, `DELETE` | Recupera, atualiza ou deleta um aluno específico. |
| `/api/v1/students/<int:pk>/enrollments/` | `GET` | Lista as matrículas de um aluno. |
| `/api/v1/students/reports/<int:pk>/` | `GET` | Gera um relatório simples com o nome do aluno e o total de pagamentos pendentes. |
| `/api/v1/courses/` | `GET`, `POST` | Lista todos os cursos ou cria um novo curso. |
| `/api/v1/courses/<int:pk>/` | `GET`, `PUT`, `PATCH`, `DELETE` | Recupera, atualiza ou deleta um curso específico. |
| `/api/v1/enrollments/` | `GET`, `POST` | Lista todas as matrículas ou cria uma nova matrícula. |
| `/api/v1/enrollments/<int:pk>/` | `GET`, `PUT`, `PATCH` | Recupera ou atualiza uma matrícula (usado apenas para alterar o `status`). |

***

### ⚙️ Instalação e Execução

O projeto é configurado para ser executado facilmente utilizando **Docker Compose**.

#### Pré-requisitos

Certifique-se de ter o **Docker** e o **Docker Compose** instalados em sua máquina.

#### Passos para Instalação e Inicialização

1.  **Clone o Repositório**
    ```bash
    git clone [URL_DO_SEU_REPOSITÓRIO]
    cd academia-dev-python
    ```

2.  **Inicie a Aplicação com Docker Compose**
    O comando abaixo irá construir a imagem Docker (`web`), instalar as dependências, rodar as migrações do Django e iniciar o servidor na porta `8000`.

    ```bash
    docker compose up --build
    ```

3.  **Acesse a Aplicação**
    Após o servidor ser inicializado, acesse o projeto no seu navegador:
    [http://localhost:8000](http://localhost:8000)

4.  **Acesso ao Admin (Opcional)**
    Para acessar o painel administrativo do Django (`/admin/`), você precisará criar um superusuário. Com o container rodando, abra um novo terminal na pasta do projeto e execute:
    ```bash
    docker exec -it academia_web python manage.py createsuperuser
    ```