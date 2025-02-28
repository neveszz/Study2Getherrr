# Study2Gether

Projeto criado para promover estudos em grupo através de salas de chat temáticas.

## Tecnologias Utilizadas

- Python
- Django
- Tailwind CSS
- SQLite

## Funcionalidades

- Criação e edição de salas de estudo
- Sistema de autenticação com login e registro de usuários
- Participação em salas de estudo
- Sistema de mensagens em tempo real
- Filtro de salas por tópicos
- Perfil de usuário com histórico de salas

## Instalação

1. Clone o repositório:

```bash
https://github.com/seu-usuario/study2gether.git
```

2. Crie o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate # Linux/MacOS
venv\Scripts\activate # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure o banco de dados:

```bash
python manage.py migrate
```

5. Crie um superusuário (opcional):

```bash
python manage.py createsuperuser
```

6. Execute o servidor:

```bash
python manage.py runserver
```

Acesse o sistema em: [http://localhost:8000](http://localhost:8000)

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar um pull request ou abrir uma issue.

