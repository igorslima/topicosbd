-- criando tabelacreate table tdrive(taxista_id float, datetime varchar(19), longitude float, latitude float) pontos
CREATE TABLE pontos (id_ponto integer, longitude float, latitude float, PRIMARY KEY(id));

-- criando tabela com os caminhos
CREATE TABLE caminhos (id_caminho integer, id_source integer REFERENCES pontos(id_ponto),  id_target integer REFERENCES pontos(id_ponto), custo float)

-- adicionando primary key na tabela caminho, pois tinha me esquecido XD
ALTER TABLE caminhos ADD PRIMARY KEY(id_caminho)

-- criando tabela tdrive, por algum motivo o postgres não aceitava o double, por isso coloquei o precision
CREATE TABLE tdrive (id serial primary key ,taxista_id integer, datetime character varying(19), longitude double precision, latitude double precision)

-- criando tabela para o hash map
CREATE TABLE hash_map(id serial PRIMARY KEY, ponto_id integer  REFERENCES pontos(id_ponto), vertice_id integer REFERENCES tdrive(id))