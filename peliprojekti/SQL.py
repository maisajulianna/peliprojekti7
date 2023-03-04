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
 """