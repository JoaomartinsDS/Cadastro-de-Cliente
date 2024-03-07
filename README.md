# Integração com SQLite utilizando SQLAlchemy.
Projeto que visa a integração de um programa python com um banco de dados utilizando o framework SQLAlchemy.
 Foi utilizado os conceitos de ORM (Object Relational Mapper) para mapeamento das entidades. A fim de conectar o mundo de orientação a objeto com o mundo relacional dos bancos de dados SQL.

Toda a criação das tabelas e colunas foram feitas através do python utilizando o SqlAlchemy.orm. Foram criadas duas classes, uma de cliente e outra de endereços. Com uma relação entre cliente e endereços de 1 para muitos, onde foi utilizado a função relationship junto com uma chave estrangeira no atributo 'user_id' para conexão entre as tabelas