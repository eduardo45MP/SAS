# Secure Authentication System (SAS)

The Secure Authentication System (SAS) is a sample application that demonstrates the implementation of a secure authentication system using the Flask framework in Python. SAS allows users to register, log in, and access restricted areas of the application.

## Features

- User Registration: Users can register in the application by providing a username and password.
- User Authentication: Users can log in using their registered credentials.
- Password Protection: User passwords are securely stored using hash and salt.
- Password Verification: User passwords are securely verified during login.
- Password Validation: Passwords must adhere to specific security criteria.
- Web Interface: The application features web pages for registration, login, and access to restricted areas.

## Technologies Used

- Python
- Flask
- MariaDB
- Bcrypt (for password hashing)
- HTML (for web pages)

## Installation

1. Clone this repository to your local environment.
2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the MariaDB database as needed in the app/auth.py file.

5. Start the application:

   ```bash
   python run.py
   ```

6. Access the application in your web browser at http://localhost:5000.

## Contributing

Contributions are welcome! Feel free to submit pull requests or report issues.

## License

This project is licensed under the MIT License.

pt-br
# Sistema de Autenticação Segura (SAS)

O Sistema de Autenticação Segura (SAS) é uma aplicação de exemplo que demonstra a implementação de um sistema de autenticação seguro usando a estrutura Flask em Python. O SAS permite que os usuários se cadastrem, façam login e acessem áreas restritas do aplicativo.

## Recursos

- Registro de usuário: Os usuários podem se cadastrar no aplicativo, fornecendo um nome de usuário e senha.
- Autenticação de usuário: Os usuários podem fazer login usando suas credenciais cadastradas.
- Proteção de senha: Senhas dos usuários são armazenadas com segurança usando hash e salt.
- Verificação de senha: As senhas dos usuários são verificadas com segurança durante o login.
- Validação de senha: As senhas devem atender a critérios específicos de segurança.
- Interface Web: O aplicativo possui páginas web para registro, login e acesso a áreas restritas.

## Tecnologias Utilizadas

- Python
- Flask
- MariaDB
- Bcrypt (para hashing de senhas)
- HTML (para as páginas web)

## Instalação

1. Clone este repositório para o seu ambiente local.
2. Crie um ambiente virtual e ative-o:

   bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate

Instale as dependências:

bash

pip install -r requirements.txt

Configure o banco de dados MariaDB conforme necessário no arquivo app/auth.py.

Inicie o aplicativo:

bash

    python run.py

    Acesse o aplicativo em seu navegador em http://localhost:5000.

Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou relatar problemas.
Licença

Este projeto está licenciado sob a Licença MIT.
