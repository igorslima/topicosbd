-- criando tabela pontos
CREATE TABLE pontos (id_ponto integer, longitude float, latitude float, PRIMARY KEY(id));

-- criando tabela com os caminhos
CREATE TABLE caminhos (id_caminho integer, id_source integer REFERENCES pontos(id_ponto),  id_target integer REFERENCES pontos(id_ponto), custo float)
-- adicionando primary key na tabela caminho, pois tinha me esquecido XD
ALTER TABLE caminhos ADD PRIMARY KEY(id_caminho)