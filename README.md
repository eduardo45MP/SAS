# Secure Authentication System (SAS)

The **Secure Authentication System (SAS)** is a sample application that demonstrates the implementation of a secure authentication system using the Flask framework in Python. SAS allows users to register, log in, and access restricted areas of the application, all with a focus on data security.

## Features

- **User Registration**: Users can create an account in the application by providing a username and a secure password.

- **User Authentication**: Users can log in using their registered credentials, with their passwords protected by hash and salt.

- **Password Validation**: Passwords must meet specific security criteria, ensuring robustness against threats.

- **Web Interface**: The application presents web pages for registration, login, and access to restricted areas, providing a user-friendly experience.

## Technologies Used

The project utilizes the following technologies:

- **Python**: The primary programming language.

- **Flask**: The web framework powering the application.

- **MariaDB**: The relational database for storing user information.

- **Bcrypt**: For password security through hashing.

- **HTML**: For creating web pages.

## Installation

To run SAS in your local environment, follow these steps:

1. **Clone the Repository**: Clone this repository to your local environment.

   ```bash
   git clone https://github.com/your-username/sas.git
   cd sas
   ```

2. **Create a Virtual Environment**: Create a virtual environment to isolate the project's dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**: Install the project's dependencies.

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**: Configure the MariaDB database as needed in the `app/auth.py` file.

5. **Start the Application**: Start the application.

   ```bash
   python run.py
   ```

6. **Access the Application**: Access the application in your web browser at [http://localhost:5000](http://localhost:5000).

## Usage Examples

- **User Registration**: Access the registration page, provide a username, and a password that meets the security criteria, then click "Register."

- **User Login**: Use the registered username and password to log in on the login page.

## Contributing

Contributions are welcome! Feel free to submit pull requests or report issues.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or need assistance, please feel free to contact us via our support email: eduardopeixoto45@outlook.com.

#pt-br
# Secure Authentication System (SAS)

O **Sistema de Autenticação Segura (SAS)** é um aplicativo de exemplo que demonstra a implementação de um sistema de autenticação seguro usando a estrutura Flask em Python. O SAS permite que os usuários se registrem, façam login e acessem áreas restritas do aplicativo, tudo isso com foco na segurança de dados.

## Recursos

- **Registro de Usuário**: Os usuários podem criar uma conta no aplicativo fornecendo um nome de usuário e senha segura.

- **Autenticação de Usuário**: Os usuários podem fazer login usando suas credenciais cadastradas, com suas senhas protegidas por hash e salt.

- **Validação de Senha**: Senhas devem atender a critérios específicos de segurança, garantindo robustez contra ameaças.

- **Interface Web**: O aplicativo apresenta páginas web para registro, login e acesso a áreas restritas, oferecendo uma experiência amigável.

## Tecnologias Utilizadas

O projeto utiliza as seguintes tecnologias:

- **Python**: A linguagem de programação principal.
- **Flask**: O framework web que impulsiona o aplicativo.
- **MariaDB**: O banco de dados relacional para armazenar informações de usuários.
- **Bcrypt**: Para a segurança das senhas através do hash.
- **HTML**: Para a criação das páginas web.

## Instalação

Para executar o SAS em seu ambiente local, siga estas etapas:

1. **Clone o Repositório**: Clone este repositório para o seu ambiente local.

   ```bash
   git clone https://github.com/seu-usuario/sas.git
   cd sas
   ```

2. **Crie um Ambiente Virtual**: Crie um ambiente virtual para isolar as dependências do projeto.

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as Dependências**: Instale as dependências do projeto.

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o Banco de Dados**: Configure o banco de dados MariaDB conforme necessário no arquivo `app/auth.py`.

5. **Inicie o Aplicativo**: Inicie o aplicativo.

   ```bash
   python run.py
   ```

6. **Acesse o Aplicativo**: Acesse o aplicativo em seu navegador em [http://localhost:5000](http://localhost:5000).

## Exemplos de Uso

- **Registro de Usuário**: Acesse a página de registro, forneça um nome de usuário e uma senha que atenda aos critérios de segurança e clique em "Registrar".

- **Login de Usuário**: Use o nome de usuário e a senha cadastrados para fazer login na página de login.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou relatar problemas.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## Contato

Se você tiver alguma dúvida ou precisar de assistência, sinta-se à vontade para entrar em contato conosco através do nosso e-mail de suporte: eduardopeixoto45@outlook.com.
