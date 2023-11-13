# carros-api

Olá nesse repositório temos uma api back-end para um site de veículos usados, na construção dessa api usei o framework Python chamado Flask com auxílio de algumas bibliotecas como flask-sqlalchemy, boto3, psycopg2 e outras. Para iniciar essa api na sua máquina é necessário a instalação de todas bibliotecas necessárias, uma forma de fazer isso é abrir o seu terminal e usar o seguinte comando: pip install -r requirements.txt, com isso feito basta iniciar o arquivo run.py digitando no seu terminal o seguinte comando: python3 run.py. Caso você não queira iniciar a api no seu computador, por tempo limitado eu hospedei ela em uma instância do AWS EC2 e o endereço para requisições é o: http://54.208.196.225:5000/<endpoint escolhido>.
Para persistência de dados estou usando um Postgres hospedado com AWS RDS, disponível também por tempo limitado, se você quiser dar uma olhada no banco e concecta-lo a um database manager, as credenciais estão dentro do arquivo __init__.py, mas eu vou deixa-las aqui também.
USER: postgres
PASSWORD: 34215547
URL: carros-usados-db.cgjfydnkuq23.us-east-1.rds.amazonaws.com
DATABASE: carrosusados
Para armazenar e carregar as fotos dos carros estou usando um bucket do AWS S3.
A autenticação é feita primeiramente com email e senha e depois é gerado um token JWT para consumo dos endpoints, o endpoint de login é o /login, o método usado é o POST e o payload é:
{
    "email": "<email cadastrado>",
    "senha": "<senha>"
}
Para cadastrar um usuário o endpoint é /users/registeruser, o método é POST e o payload é:
{
    "nome": "<Nome Completo>",
    "email": "<email>",
    "senha": "<senha>"
}

Repositório front-end: https://github.com/FRNS1/carros-front.git

# OBS: Por conta de um problema de CORS que não consegui identificar em tempo hábil tive que despadronizar as rotas de users, por isso ela é a única com prefixo /users
