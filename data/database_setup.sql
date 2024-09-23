BEGIN;
DROP SCHEMA IF EXISTS programacao_filmes;
CREATE SCHEMA programacao_filmes;

USE programacao_filmes;

CREATE TABLE canal(
    num_canal INT,
    nome VARCHAR(50),
    sigla VARCHAR(25),
    PRIMARY KEY (num_canal)
);


CREATE TABLE filme(
    num_filme INT,
    titulo_original VARCHAR(80) NOT NULL,
    titulo_brasil VARCHAR(80),
    ano_lancamento YEAR NOT NULL,
    pais_origem VARCHAR(30),
    categoria VARCHAR(25),
    duracao INT NOT NULL,
    PRIMARY KEY (num_filme)
);


CREATE TABLE exibicao(
    num_filme INT,
    num_canal INT,
    data DATETIME,
    PRIMARY KEY (num_filme, num_canal, data),
    FOREIGN KEY (num_filme) REFERENCES filme (num_filme) ON DELETE CASCADE,
    FOREIGN KEY (num_canal) REFERENCES canal (num_canal) ON DELETE CASCADE
);


DELIMITER $$

-- Trigger que verifica a duração do filme antes de uma inserção
CREATE TRIGGER verifica_duracao_filme
BEFORE INSERT ON filme
FOR EACH ROW
BEGIN
    IF NEW.duracao < 30 OR NEW.duracao > 210 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'A duração do filme deve ser maior que 30 minutos e menor que 3 horas e 30 minutos.';
    END IF;
END$$

-- Trigger que verifica a duração do filme antes de uma atualização
CREATE TRIGGER verifica_duracao_filme_update
BEFORE UPDATE ON filme
FOR EACH ROW
BEGIN
    IF NEW.duracao < 30 OR NEW.duracao > 210 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'A duração do filme deve ser maior que 30 minutos e menor que 3 horas e 30 minutos.';
    END IF;
END$$

DELIMITER ;


INSERT INTO canal VALUES
(1, 'Fox Broadcasting Company', 'FOX'),
(2, 'Home Box Office', 'HBO'),
(3, 'Nickelodeon', 'Nick'),
(4, 'Cartoon Network', 'CN'),
(5, 'Telecine', 'TC');


INSERT INTO filme VALUES
(1, 'Dune: part two', 'Duna: parte dois', 2024, 'Estados Unidos', 'Ficção científica', 166),
(2, 'Interstellar', 'Interestelar', 2014, 'Estados Unidos', 'Ficção científica', 169),
(3, 'A Quiet Place: Day One', 'Um Lugar Silencioso: Dia Um', 2024, 'Estados Unidos', 'Terror', 99),
(4, 'Moonlight', 'Moonlight: Sob a Luz do Luar', 2016, 'Estados Unidos', 'Drama', 110),
(5, 'Ratatouille', 'Ratatouille', 2007, 'Estados Unidos', 'Animação', 111),
(6, 'Marte Um', 'Marte Um', 2022, 'Brasil', 'Drama', 115),
(7, 'Forrest Gump', 'Forrest Gump - O Contador de Histórias', 1994, 'Estados Unidos', 'Comédia', 142),
(8, 'Coco', 'Viva: A vida é uma festa', 2017, 'Estados Unidos', 'Animação', 105),
(9, 'Knives Out', 'Entre Facas e Segredos', 2019, 'Estados Unidos', 'Comédia', 130),
(10, 'Que Horas Ela Volta?', 'Que Horas Ela Volta?', 2015, 'Brasil', 'Drama', 114);


INSERT INTO exibicao VALUES
(1, 2, '2024-08-30 15:25:00'),
(2, 2, '2024-08-25 19:10:00'),
(5, 3, '2024-08-10 13:50:00'),
(8, 4, '2024-08-11 09:25:00'),
(5, 4, '2024-08-30 10:30:00'),
(7, 2, '2024-08-30 08:30:00'), 
(10, 5, '2024-08-12 08:30:00'), 
(6, 5, '2024-08-14 10:30:00');

COMMIT;
