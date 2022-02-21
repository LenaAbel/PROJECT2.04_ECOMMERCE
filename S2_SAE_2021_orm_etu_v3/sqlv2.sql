#mysql --user=stoillon --password=3006 --host=serveurmysql --database=BDD_stoillon

DROP TABLE IF EXISTS PANIER;
DROP TABLE IF EXISTS NOTE;
DROP TABLE IF EXISTS COMMENTAIRE;
DROP TABLE IF EXISTS LIGNE_COMMANDE;
DROP TABLE IF EXISTS COMMANDE;
DROP TABLE IF EXISTS MESURE;
DROP TABLE IF EXISTS EST_DE_COULEUR;
DROP TABLE IF EXISTS CHAUSSURE;
DROP TABLE IF EXISTS UTILISATEUR;
DROP TABLE IF EXISTS ETAT;
DROP TABLE IF EXISTS TYPE_CHAUSSURE;
DROP TABLE IF EXISTS MATIERE;
DROP TABLE IF EXISTS COULEUR;
DROP TABLE IF EXISTS MARQUE;
DROP TABLE IF EXISTS FOURNISSEUR;
DROP TABLE IF EXISTS POINTURE;

CREATE TABLE IF NOT EXISTS TYPE_CHAUSSURE(
   id_type_chaussure INT NOT NULL AUTO_INCREMENT,
   nom_type_chaussure VARCHAR(50),
   PRIMARY KEY(id_type_chaussure)
)CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS POINTURE(
   id_pointure INT NOT NULL AUTO_INCREMENT,
   taille INT,
   PRIMARY KEY(id_pointure)
)CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS COULEUR(
   id_couleur INT NOT NULL AUTO_INCREMENT,
   libelle_couleur VARCHAR(50),
   PRIMARY KEY(id_couleur)
)CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS MATIERE(
   id_matiere INT NOT NULL AUTO_INCREMENT,
   libelle_matiere VARCHAR(50),
   PRIMARY KEY(id_matiere)
)CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS UTILISATEUR(
   id_utilisateur INT NOT NULL AUTO_INCREMENT,
   username VARCHAR(50),
   password VARCHAR(100),
   role VARCHAR(50),
   est_actif INT,
   pseudo VARCHAR(50),
   email VARCHAR(50),
   PRIMARY KEY(id_utilisateur)
)CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS ETAT(
   id_etat INT NOT NULL AUTO_INCREMENT,
   libelle_etat VARCHAR(50),
   PRIMARY KEY(id_etat)
)CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS FOURNISSEUR(
   id_fournisseur INT NOT NULL AUTO_INCREMENT,
   libelle_fournisseur VARCHAR(50),
   PRIMARY KEY(id_fournisseur)
)CHARACTER SET 'utf8';


CREATE TABLE IF NOT EXISTS MARQUE(
   id_marque INT NOT NULL AUTO_INCREMENT,
   libelle_marque VARCHAR(50),
   PRIMARY KEY(id_marque)
)CHARACTER SET 'utf8';


CREATE TABLE IF NOT EXISTS CHAUSSURE(
   id_chaussure INT NOT NULL AUTO_INCREMENT,
   nom_chaussure VARCHAR(50),
   image_chaussure VARCHAR(50),
   prix_chaussure VARCHAR(50),
   stock_chaussure VARCHAR(50),
   id_marque INT NOT NULL,
   id_fournisseur INT NOT NULL,
   id_matiere INT NOT NULL,
   id_type_chaussure INT NOT NULL,
   marque_chaussure VARCHAR(50),
   fournisseur_chaussure VARCHAR(50),
   PRIMARY KEY(id_chaussure),
   CONSTRAINT chaussure_ibfk_1 FOREIGN KEY(id_marque) REFERENCES MARQUE(id_marque),
   CONSTRAINT chaussure_ibfk_2 FOREIGN KEY(id_fournisseur) REFERENCES FOURNISSEUR(id_fournisseur),
   CONSTRAINT chaussure_ibfk_3 FOREIGN KEY(id_matiere) REFERENCES MATIERE(id_matiere),
   CONSTRAINT chaussure_ibfk_4 FOREIGN KEY(id_type_chaussure) REFERENCES TYPE_CHAUSSURE(id_type_chaussure)
)CHARACTER SET 'utf8';


CREATE TABLE IF NOT EXISTS COMMENTAIRE(
   id_commentaire INT NOT NULL AUTO_INCREMENT,
   libelle_commentaire VARCHAR(50),
   id_chaussure INT NOT NULL,
   id_utilisateur INT NOT NULL,
   PRIMARY KEY(id_commentaire),
   CONSTRAINT commentaire_ibfk_1 FOREIGN KEY(id_chaussure) REFERENCES CHAUSSURE(id_chaussure),
   CONSTRAINT commentaire_ibfk_2 FOREIGN KEY(id_utilisateur) REFERENCES UTILISATEUR(id_utilisateur)
)CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS PANIER(
   id_panier INT NOT NULL AUTO_INCREMENT,
   date_ajout DATE,
   prix_unit INT,
   quantite INT,
   id_chaussure INT NOT NULL,
   id_utilisateur INT NOT NULL,
   PRIMARY KEY(id_panier),
   CONSTRAINT panier_ibfk_1 FOREIGN KEY(id_chaussure) REFERENCES CHAUSSURE(id_chaussure),
   CONSTRAINT panier_ibfk_2 FOREIGN KEY(id_utilisateur) REFERENCES UTILISATEUR(id_utilisateur)
)CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS COMMANDE(
   id_commande INT NOT NULL AUTO_INCREMENT,
   date_achat DATE,
   id_utilisateur INT NOT NULL,
   id_etat INT NOT NULL,
   PRIMARY KEY(id_commande),
   CONSTRAINT commande_ibfk_1 FOREIGN KEY(id_utilisateur) REFERENCES UTILISATEUR(id_utilisateur),
   CONSTRAINT commande_ibfk_2 FOREIGN KEY(id_etat) REFERENCES ETAT(id_etat)
)CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS NOTE(
   id_note INT NOT NULL AUTO_INCREMENT,
   note NUMERIC(6,2) default 3,
   id_utilisateur INT NOT NULL,
   id_chaussure INT NOT NULL,
   PRIMARY KEY(id_note),
   CONSTRAINT note_ibfk_1 FOREIGN KEY(id_utilisateur) REFERENCES UTILISATEUR(id_utilisateur),
   CONSTRAINT note_ibfk_2 FOREIGN KEY(id_chaussure) REFERENCES CHAUSSURE(id_chaussure)
)CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS MESURE(
   id_chaussure INT,
   id_pointure INT,
   PRIMARY KEY(id_chaussure, id_pointure),
   CONSTRAINT mesure_ibfk_1 FOREIGN KEY(id_chaussure) REFERENCES CHAUSSURE(id_chaussure),
   CONSTRAINT mesure_ibfk_2 FOREIGN KEY(id_pointure) REFERENCES POINTURE(id_pointure)
)CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS EST_DE_COULEUR(
   id_chaussure INT,
   id_couleur INT,
   PRIMARY KEY(id_chaussure, id_couleur),
   CONSTRAINT estdecouleur_ibfk_1 FOREIGN KEY(id_chaussure) REFERENCES CHAUSSURE(id_chaussure),
   CONSTRAINT estdecouleur_ibfk_2 FOREIGN KEY(id_couleur) REFERENCES COULEUR(id_couleur)
)CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS LIGNE_COMMANDE(
   id_chaussure INT,
   id_commande INT,
   prix_unit INT,
   quantite INT,
   PRIMARY KEY(id_chaussure, id_commande),
   CONSTRAINT lignecommande_ibfk_1 FOREIGN KEY(id_chaussure) REFERENCES CHAUSSURE(id_chaussure),
   CONSTRAINT lignecommande_ibfk_2 FOREIGN KEY(id_commande) REFERENCES COMMANDE(id_commande)
)CHARACTER SET 'utf8';

INSERT INTO UTILISATEUR VALUES (NULL, 'admin', 'sha256$pBGlZy6UukyHBFDH$2f089c1d26f2741b68c9218a68bfe2e25dbb069c27868a027dad03bcb3d7f69a', 'ROLE_admin', 1, 'admin', 'admin@admin.fr'),
                               (NULL, 'client', 'sha256$Q1HFT4TKRqnMhlTj$cf3c84ea646430c98d4877769c7c5d2cce1edd10c7eccd2c1f9d6114b74b81c4', 'ROLE_client', 1, 'client', 'client@client.fr'),
                               (NULL, 'client2', 'sha256$ayiON3nJITfetaS8$0e039802d6fac2222e264f5a1e2b94b347501d040d71cfa4264cad6067cf5cf3', 'ROLE_client',1, 'client2', 'client2@client2.fr');

INSERT INTO ETAT VALUES (NULL,'Expediée'),
                        (NULL,'En Cours');

INSERT INTO COMMANDE VALUES (NULL, '2019-12-20', 2, 1),
                            (NULL, '2021-02-03', 1, 2),
                            (NULL, '2021-09-29', 3, 2),
                            (NULL, '2021-12-07', 1, 2),
                            (NULL, '2019-05-19', 1, 2),
                            (NULL, '2022-01-25', 2, 2),
                            (NULL, '2021-11-11', 2, 2),
                            (NULL, '2020-12-25', 1, 2),
                            (NULL, '2020-07-12', 3, 2),
                            (NULL, '2020-01-05', 3, 2),
                            (NULL, '2020-10-14', 3, 2),
                            (NULL, '2020-04-08', 3, 2);


INSERT INTO TYPE_CHAUSSURE VALUES (NULL, 'Baskets'),
                                  (NULL, 'Claquettes'),
                                  (NULL, 'Bottes'),
                                  (NULL, 'Talons'),
                                  (NULL, 'Chaussons'),
                                  (NULL, 'Ballerines');

INSERT INTO COULEUR VALUES (NULL, 'Beige'),
                           (NULL, 'Noir'),
                           (NULL, 'Rouge'),
                           (NULL, 'Bleu'),
                           (NULL, 'Vert'),
                           (NULL, 'Jaune'),
                           (NULL, 'Cyan'),
                           (NULL, 'Violet'),
                           (NULL, 'Blanc'),
                           (NULL, 'Gris'),
                           (NULL, 'Rose'),
                           (NULL, 'Orange');


INSERT INTO POINTURE VALUES (NULL, 36.0),
                            (NULL, 36.5),
                            (NULL, 37.0),
                            (NULL, 37.5),
                            (NULL, 38.0),
                            (NULL, 38.5),
                            (NULL, 39.0),
                            (NULL, 39.5),
                            (NULL, 40.0),
                            (NULL, 40.5),
                            (NULL, 41.0),
                            (NULL, 41.5),
                            (NULL, 42.0),
                            (NULL, 42.5),
                            (NULL, 43.0),
                            (NULL, 43.5),
                            (NULL, 44.0),
                            (NULL, 44.5),
                            (NULL, 45.0),
                            (NULL, 45.5),
                            (NULL, 46.0),
                            (NULL, 46.5),
                            (NULL, 47.0),
                            (NULL, 47.5),
                            (NULL, 48.0);


INSERT INTO MATIERE VALUES (NULL, 'Cuir'),
                           (NULL, 'Laine'),
                           (NULL, 'Fibre synthetique');

INSERT INTO FOURNISSEUR VALUES (NULL, 'Point C'),
                               (NULL, 'Botru-Chausse'),
                               (NULL, 'Drof'),
                               (NULL, 'Nozama'),
                               (NULL, 'Eaki'),
                               (NULL, 'Odentinne');

INSERT INTO MARQUE VALUES (NULL, 'NIKE'),
                          (NULL, 'Balenciago'),
                          (NULL, 'Cannonne'),
                          (NULL, 'Letin'),
                          (NULL, 'Nokin'),
                          (NULL, 'Ssegue');

INSERT INTO CHAUSSURE VALUES (NULL, 'Galaxy', 'galaxy_nike.png',49.99, 20, 1, 1, 3, 1,'NIKE', 'Point C'),
                             (NULL, 'Illusion','illusion_balenciago.png',79.99, 10, 2, 2, 3, 1, 'Balenciago', 'Botru-Chausse'),
                             (NULL, 'Corail', 'corail_cannonne.png', 69.99, 50, 3, 3, 1,4, 'Cannonne', 'Drof'),
                             (NULL, 'Alpha', 'alpha_letin.png', 49.99, 50, 4, 4, 1, 6, 'Letin', 'Nozama'),
                             (NULL, 'Zilla','zilla_nokin.png', 39.99, 3, 5, 5, 1,3, 'Nokin', 'Eaki'),
                             (NULL, 'Ethernal', 'ethernal_ssegue.png', 25.99, 30, 6, 6, 3, 5, 'Ssegue', 'Odentine'),
                             (NULL, 'Octo', 'octo_nike.png', 12.99,15, 1, 1, 3,2,'NIKE', 'Point C'),
                             (NULL, 'Virtuos','virtuos_balenciago.png',29.99,21, 2, 2, 1, 2, 'Balenciago', 'Botru-Chausse'),
                             (NULL, 'Elite', 'elite_cannonne.png', 59.99,7, 3, 3, 1,4, 'Cannonne','Drof'),
                             (NULL, 'Digi', 'digi_letin.png',  35.99,70, 4, 4, 3,6, 'Letin','Nozama'),
                             (NULL, 'Star','star_nokin.png', 99.99,5, 5, 5, 1,3, 'Nokin', 'Eaki'),
                             (NULL, 'Joker','joker_ssegue.png',10.99,90, 6, 6, 2, 5, 'Ssegue', 'Odentine');



INSERT INTO LIGNE_COMMANDE VALUES (1, 1, 49.99, 1),
                                  (2, 2, 79.99, 2),
                                  (3, 3, 69.99, 1),
                                  (4, 10, 35.99, 2),
                                  (5, 11, 99.99, 1),
                                  (6, 4, 49.99, 1),
                                  (7, 9, 59.99, 1),
                                  (8, 5, 39.99, 2),
                                  (9, 8, 29.99, 2),
                                  (10, 6, 25.99, 1),
                                  (11, 12, 10.99,1),
                                  (12, 7, 12.99,3);



INSERT INTO MESURE VALUES (1, 18),
                          (2, 12),
                          (3, 3),
                          (4, 24),
                          (5, 19),
                          (6, 11),
                          (7, 15),
                          (8, 17),
                          (9, 9),
                          (10, 24),
                          (11, 13),
                          (12, 4);


INSERT INTO EST_DE_COULEUR VALUES (1, 11),
                                  (2, 2),
                                  (3, 3),
                                  (4, 11),
                                  (5, 10),
                                  (6, 7),
                                  (7, 8),
                                  (8, 4),
                                  (9, 10),
                                  (10, 7),
                                  (11, 2),
                                  (12, 10);

INSERT INTO PANIER VALUES (NULL, '2019-12-19', 49.99, 1, 1, 1),
                          (NULL, '2020-01-05', 79.99, 2, 2, 1),
                          (NULL, '2020-01-05', 69.99, 1, 3, 2),
                          (NULL, '2020-01-05', 35.99, 2, 10, 2),
                          (NULL, '2020-01-05', 99.99, 1, 11, 1),
                          (NULL,' 2020-01-05', 49.99, 1, 4, 2),
                          (NULL, '2020-01-05', 59.99, 1, 9, 3),
                          (NULL, '2020-01-05', 39.99, 2, 5, 1),
                          (NULL, '2020-01-05', 29.99, 2, 8, 2),
                          (NULL, '2020-01-05', 24.99, 1, 6, 1);

SELECT * FROM PANIER;
SELECT * FROM NOTE;
SELECT * FROM COMMENTAIRE;
SELECT * FROM LIGNE_COMMANDE;
SELECT * FROM COMMANDE;
SELECT * FROM MESURE;
SELECT * FROM EST_DE_COULEUR;
SELECT * FROM CHAUSSURE;
SELECT * FROM UTILISATEUR;
SELECT * FROM ETAT;
SELECT * FROM TYPE_CHAUSSURE;
SELECT * FROM MATIERE;
SELECT * FROM COULEUR;
SELECT * FROM MARQUE;
SELECT * FROM FOURNISSEUR;
SELECT * FROM POINTURE;

SELECT id_type_chaussure, COUNT(id_type_chaussure) AS nmbChaussures FROM CHAUSSURE GROUP BY id_type_chaussure ORDER BY id_type_chaussure ASC;