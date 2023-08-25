# Secure Authentication System (SAS)

Welcome to the Secure Authentication System (SAS), a secure authentication system developed in Python using the Flask framework. SAS allows users to sign up, log in, and maintain their accounts securely with strict password requirements.

## Prerequisites

Make sure you have the following requirements installed before you begin:

- Python 3.9
- MariaDB (or MySQL)
- The Python libraries listed in requirements.txt

## Database Configuration

Before starting the application, you should set up the MariaDB database and create a database named "SAS." You can do this using the following SQL:

```sql
CREATE DATABASE SAS;
```

Additionally, you need to configure the database user and password in the auth.py file:

```python
conn = mariadb.connect(
    user='YOUR_USER',
    password='YOUR_PASSWORD',
    host='localhost',
    database='SAS'
)
```

## Installation

1. Clone the SAS repository to your local machine:

```bash
git clone https://github.com/eduardo45MP/SAS.git
cd SAS
```

2. Install the Python dependencies listed in the requirements.txt file:

```bash
pip install -r requirements.txt
```

## Running the Application

After configuring the database and installing the dependencies, you can start the Flask application:

```bash
python run.py
```

The application will be available at [http://localhost:5000/](http://localhost:5000/) in your web browser.

## Features

SAS offers the following features:

- User registration with password validation:
  - Password must be at least 8 characters long.
  - Must contain at least one special character (!@#$%^&*(),.?-_":{}|<>).
  - Must contain at least one uppercase letter.
  - Must contain at least one numeric digit.
- Account locking after a defined number of failed login attempts.
- Recovery of locked accounts after a specified time period.

## Project Structure

The project is structured as follows:

- `app`: Contains the main Flask application code.
  - `templates`: Stores the HTML templates used by the application.
  - `auth.py`: Handles authentication and user management.
  - `__init__.py`: Initializes the Flask application.
  - `name_tk.py`: Checks the availability of usernames.
  - `routes.py`: Defines the application's routes and handles business logic.
  - `valid_pw.py`: Checks the validity of user passwords.
- `__pycache__`: Contains automatically generated Python files.
- `README.md`: This file you are reading.

## Contribution

Feel free to contribute improvements to SAS. You can open issues or submit pull requests with your contributions.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or need assistance, please feel free to contact us via our support email: eduardopeixoto45@outlook.com.

#pt-br
# Secure Authentication System (SAS)

Bem-vindo ao Secure Authentication System (SAS), um sistema de autenticação seguro desenvolvido em Python usando o framework Flask. O SAS permite que os usuários se cadastrem, façam login e mantenham suas contas seguras com requisitos rigorosos de senha.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados antes de começar:

- Python 3.9
- MariaDB (ou MySQL)
- As bibliotecas Python listadas em requirements.txt

## Configuração do Banco de Dados

Antes de iniciar o aplicativo, você deve configurar o banco de dados MariaDB e criar um banco de dados chamado "SAS". Para fazer isso, você pode usar o seguinte SQL:

```sql
CREATE DATABASE SAS;
```

Além disso, você precisa configurar o usuário e a senha do banco de dados no arquivo auth.py:

```python
conn = mariadb.connect(
    user='SEU_USUARIO',
    password='SUA_SENHA',
    host='localhost',
    database='SAS'
)
```

## Instalação

1. Clone o repositório do SAS em sua máquina local:

```bash
git clone https://github.com/eduardo45MP/SAS.git
cd SAS
```

2. Instale as dependências do Python listadas no arquivo requirements.txt:

```bash
pip install -r requirements.txt
```

## Executando o Aplicativo

Após configurar o banco de dados e instalar as dependências, você pode iniciar o aplicativo Flask:

```bash
python run.py
```

O aplicativo estará disponível em [http://localhost:5000/](http://localhost:5000/) em seu navegador.

## Funcionalidades

O SAS oferece as seguintes funcionalidades:

- Cadastro de usuário com validação de senha:
  - A senha deve ter pelo menos 8 caracteres.
  - Deve conter pelo menos um caractere especial (!@#$%^&*(),.?-_":{}|<>).
  - Deve conter pelo menos uma letra maiúscula.
  - Deve conter pelo menos um dígito numérico.
- Bloqueio de conta após um número definido de tentativas de login malsucedidas.
- Recuperação de conta bloqueada após um período de tempo.

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- `app`: Contém o código principal do aplicativo Flask.
  - `templates`: Armazena os modelos HTML usados pelo aplicativo.
  - `auth.py`: Lida com a autenticação e o gerenciamento de usuários.
  - `__init__.py`: Inicializa o aplicativo Flask.
  - `name_tk.py`: Verifica a disponibilidade de nomes de usuário.
  - `routes.py`: Define as rotas do aplicativo e lida com a lógica de negócios.
  - `valid_pw.py`: Verifica a validade das senhas dos usuários.
- `__pycache__`: Contém arquivos gerados automaticamente pelo Python.
- `README.md`: Este arquivo que você está lendo.

## Contribuição

Sinta-se à vontade para contribuir com melhorias para o SAS. Você pode abrir problemas (issues) ou enviar solicitações de pull (pull requests) com suas contribuições.

## Licença

Este projeto é distribuído sob a licença MIT.

## Contato

Se você tiver alguma dúvida ou precisar de assistência, sinta-se à vontade para entrar em contato conosco através do nosso e-mail de suporte: eduardopeixoto45@outlook.com.
