"""

DROP TABLE goal_reached;
DROP TABLE goal;
DROP TABLE game;
Tämä taulukko tallentaa tiedot keskeneräisistä peleistä.

CREATE TABLE GAME (
player_id INTEGER not NULL PRIMARY KEY AUTO_INCREMENT,
time_sec INTEGER DEFAULT 0,
screen_Name VARCHAR(20),
score INTEGER DEFAULT 0,
last_location VARCHAR(40),
AF_ BOOLEAN DEFAULT FALSE, AN_ BOOLEAN DEFAULT FALSE, AS_ BOOLEAN DEFAULT FALSE,
EU_ BOOLEAN DEFAULT FALSE, NA_ BOOLEAN DEFAULT FALSE, OC_ BOOLEAN DEFAULT FALSE,
SA_ BOOLEAN DEFAULT FALSE,
FOREIGN KEY (last_location) REFERENCES airport(ident) ON UPDATE CASCADE ON DELETE NO ACTION);

Tämä taulukko tallentaa tiedot pelatuista peleistä eli pelaajien tuloksista.

CREATE TABLE RESULTS (
player_id INTEGER NOT NULL,
screen_name VARCHAR(20),
score INTEGER,
time_sec INTEGER);

CREATE TABLE plane_info(
id INT NOT NULL,
emission INT(3) null,
risk INT(3) null,
questions INT(3) null,
velocity INT(3)null,
type VARCHAR(40));
INSERT INTO plane_info(id, emission, risk, questions, velocity, type)
VALUES (1, 2, 2, 16, 8,'vähänpästoinen');
INSERT INTO plane_info(id, emission, risk, questions, velocity, type)
VALUES (2, 4, 2, 12, 8,'matkustajankone');
INSERT INTO plane_info(id, emission, risk, questions, velocity, type)
VALUES (3, 8, 4, 8, 4,'yksityiskone');
INSERT INTO plane_info(id, emission, risk, questions, velocity, type)
VALUES (4, 16, 8, 4, 2,'hävittäjä');



DROP TABLE IF EXISTS



CREATE TABLE start_airports(
  id int(11) NOT null,
  ident varchar(40) NOT NULL,
  type varchar(40) DEFAULT NULL,
  name varchar(40) DEFAULT NULL,
  continent varchar(40) DEFAULT NULL,
  iso_country varchar(40) DEFAULT NULL,
  municipality varchar(40) DEFAULT NULL,
  keywords varchar(40) DEFAULT NULL,
  PRIMARY KEY (ident),
  FOREIGN KEY (iso_country) REFERENCES country(iso_country)
  )start_airports

INSERT INTO plane_info(id, emission, risk, questions, velocity)
VALUES ('1', '2', '20', '4', '8'), ('2', '2', '20', '4', '8'), ('3', '8', '40', '2', '4'), ('4', '16', '60', '1', '2');


SELECT * from airport where ident = 'DNMM' OR ident = 'ZBAA' OR ident = 'EDDF' OR ident = 'KLAS' OR ident = 'YSSY' OR ident = 'SBJH'


DELETE FROM airport WHERE type = 'closed' OR type = 'seaplane_base' OR TYPE = 'heliport'

DELETE FROM country WHERE iso_country NOT IN (SELECT iso_country FROM airport WHERE airport.iso_country = country.iso_country)

UPDATE airport
SET municipality = 'Not in any municipality'
WHERE municipality = ''
"""
