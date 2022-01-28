#mysql --user=stoillon --password=3006 --host=serveurmysql --database=BDD_stoillon

DROP TABLE IF EXISTS PANIER;
DROP TABLE IF EXISTS LIGNE_COMMANDE;
DROP TABLE IF EXISTS COMMANDE;
DROP TABLE IF EXISTS MESURE;
DROP TABLE IF EXISTS EST_DE_COULEUR;
DROP TABLE IF EXISTS CHAUSSURE;
DROP TABLE IF EXISTS UTILISATEUR;
DROP TABLE IF EXISTS ETAT;
DROP TABLE IF EXISTS TYPE_CHAUSSURE;
DROP TABLE IF EXISTS COULEUR;
DROP TABLE IF EXISTS POINTURE;

CREATE TABLE IF NOT EXISTS UTILISATEUR(
   id_utilisateur INT NOT NULL AUTO_INCREMENT,
   username VARCHAR(50),
   mot_de_passe VARCHAR(100),
   role_utilisateur VARCHAR(50),
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

CREATE TABLE IF NOT EXISTS COMMANDE(
   id_commande INT NOT NULL AUTO_INCREMENT,
   date_achat DATE,
   id_utilisateur INT NOT NULL,
   id_etat INT NOT NULL,
   PRIMARY KEY(id_commande),
   FOREIGN KEY(id_utilisateur) REFERENCES UTILISATEUR(id_utilisateur),
   FOREIGN KEY(id_etat) REFERENCES ETAT(id_etat)
)CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS TYPE_CHAUSSURE(
   id_type_chaussure INT NOT NULL AUTO_INCREMENT,
   nom_type_chaussure VARCHAR(50),
   PRIMARY KEY(id_type_chaussure)
)CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS COULEUR(
   id_couleur INT NOT NULL AUTO_INCREMENT,
   nom_couleur VARCHAR(50),
   PRIMARY KEY(id_couleur)
);

CREATE TABLE IF NOT EXISTS POINTURE(
   id_pointure INT NOT NULL AUTO_INCREMENT,
   taille NUMERIC(3,1),
   PRIMARY KEY(id_pointure)
)CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS CHAUSSURE(
   id_chaussure INT NOT NULL AUTO_INCREMENT,
   nom_chaussure VARCHAR(50),
   marque_chaussure VARCHAR(50),
   fournisseur_chaussure VARCHAR(50),
   id_type_chaussure INT,
   PRIMARY KEY(id_chaussure),
   FOREIGN KEY(id_type_chaussure) REFERENCES TYPE_CHAUSSURE(id_type_chaussure)
)CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS PANIER(
   id_panier INT NOT NULL AUTO_INCREMENT,
   date_ajout DATE,
   prix_unit NUMERIC(6, 2),
   quantite INT,
   id_chaussure INT,
   id_utilisateur INT,
   PRIMARY KEY(id_panier),
   FOREIGN KEY(id_chaussure) REFERENCES CHAUSSURE(id_chaussure),
   FOREIGN KEY(id_utilisateur) REFERENCES UTILISATEUR(id_utilisateur)
)CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS MESURE(
   id_chaussure INT,
   id_pointure INT,
   PRIMARY KEY(id_chaussure, id_pointure),
   FOREIGN KEY(id_chaussure) REFERENCES CHAUSSURE(id_chaussure),
   FOREIGN KEY(id_pointure) REFERENCES POINTURE(id_pointure)
)CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS EST_DE_COULEUR(
   id_chaussure INT,
   id_couleur INT,
   PRIMARY KEY(id_chaussure, id_couleur),
   FOREIGN KEY(id_chaussure) REFERENCES CHAUSSURE(id_chaussure),
   FOREIGN KEY(id_couleur) REFERENCES COULEUR(id_couleur)
)CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS LIGNE_COMMANDE(
   id_commande INT NOT NULL,
   id_chaussure INT NOT NULL,
   prix_unit INT,
   quantite INT,
   PRIMARY KEY(id_commande, id_chaussure),
   FOREIGN KEY(id_commande) REFERENCES COMMANDE(id_commande),
   FOREIGN KEY(id_chaussure) REFERENCES CHAUSSURE(id_chaussure)
)CHARACTER SET 'utf8';

INSERT INTO UTILISATEUR VALUES (NULL, 'Garou', 'Loup', 'ROLE_client', 1, 'Garou42', 'garoudu42@gmail.com'),
                               (NULL, 'Jean-Charles', 'Eude', 'ROLE_client', 1, 'JC56', 'jean.charles@gmail.com'),
                               (NULL, 'admin', 'admin', 'ROLE_admin', 1, 'admin', 'admin@admin.fr'),  #sha256$pBGlZy6UukyHBFDH$2f089c1d26f2741b68c9218a68bfe2e25dbb069c27868a027dad03bcb3d7f69a
                               (NULL, 'client', 'client', 'ROLE_client', 1, 'client', 'client@client.fr'), #sha256$Q1HFT4TKRqnMhlTj$cf3c84ea646430c98d4877769c7c5d2cce1edd10c7eccd2c1f9d6114b74b81c4
                               (NULL, 'client2', 'client2', 'ROLE_client',1, 'client2', 'client2@client2.fr'), #sha256$ayiON3nJITfetaS8$0e039802d6fac2222e264f5a1e2b94b347501d040d71cfa4264cad6067cf5cf3
                               (NULL, 'Nicolas Picot', '2012', 'ROLE_admin', 1, 'Nicolas', 'nicolas.picot@gmail.com'),
                               (NULL, 'Lucas Dubol', '1705', 'ROLE_admin', 1, 'Lucas', 'lucas.dubol@gmail.com'),
                               (NULL, 'Lena Abel', '0310', 'ROLE_admin', 1, 'Lena', 'lena.abel@gmail.com'),
                               (NULL, 'Samuel Toillon', '3006', 'ROLE_admin', 1, 'Samuel', 'samuel.toillon@gmail.com');

INSERT INTO ETAT VALUES (NULL,'Expediée'),
                        (NULL,'En Cours'),
                        (NULL,'Recu');

INSERT INTO TYPE_CHAUSSURE VALUES (NULL, 'Baskets'),
                                  (NULL, 'Claquettes'),
                                  (NULL, 'Bottes'),
                                  (NULL, 'Talons'),
                                  (NULL, 'Chaussons')
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

INSERT INTO COMMANDE VALUES (NULL, "2019-12-20", 2, 3),
                            (NULL, "2021-02-03", 4, 3),
                            (NULL, "2021-09-29", 9, 2),
                            (NULL, "2021-12-07", 7, 1),
                            (NULL, "2019-05-19", 8, 3),
                            (NULL, "2022-01-25", 6, 1),
                            (NULL, "2021-11-11", 5, 2),
                            (NULL, "2020-12-25", 7, 3),
                            (NULL, "2020-07-12", 5, 2),
                            (NULL, "2020-01-05", 1, 3);

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

INSERT INTO CHAUSSURE VALUES (NULL, 'Oui', 'NIKE', 'Point C', 1),
                             (NULL, 'Non', 'Balenciago', 'Botru-Chausse', 2),
                             (NULL, 'Corail', 'Cannonne', 'Drof', 4),
                             (NULL, 'Alpha', 'Letin', 'Nozama', 6),
                             (NULL, 'Zilla', 'Nokin', 'Eaki', 3),
                             (NULL, 'Ethernal', 'Ssegue', 'Odentinne', 5)
                             (NULL, 'Octo', 'NIKE', 'Point C', 1),
                             (NULL, 'Virtuos', 'Balenciago', 'Botru-Chausse', 2),
                             (NULL, 'Elite', 'Cannonne', 'Drof', 4),
                             (NULL, 'Digi', 'Letin', 'Nozama', 6),
                             (NULL, 'Star', 'Nokin', 'Eaki', 3),
                             (NULL, 'Joker', 'Ssegue', 'Odentinne', 5);

INSERT INTO LIGNE_COMMANDE VALUES (1, 1, 49.99, 1),
                                  (2, 2, 79.99, 2),
                                  (3, 3, 69.99, 1),
                                  (4 10, 35.99, 2),
                                  (5, 11, 99.99, 1),
                                  (6, 4, 49.99, 1),
                                  (7, 9, 59.99, 1),
                                  (8, 5, 39.99, 2),
                                  (9, 8, 29.99, 2),
                                  (10, 6, 25.99, 1);


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
                                  (3, 3,
                                  (4, 11),
                                  (5, 10),
                                  (6, 7),
                                  (7, 8),
                                  (8, 4),
                                  (9, 10),
                                  (10, 7),
                                  (11, 2),
                                  (12, 10);

INSERT INTO PANIER VALUES (NULL, "2019-12-19", 49.99, 1, 1, 1), 
                          (NULL, "2020-01-05", 79.99, 2, 2, 2),
                          (NULL, "2020-01-05", 69.99, 1, 3, 4),
                          (NULL, "2020-01-05", 35.99, 2, 10, 6),
                          (NULL, "2020-01-05", 99.99, 1, 11, 7),
                          (NULL, "2020-01-05", 49.99, 1, 4, 3),
                          (NULL, "2020-01-05", 59.99, 1, 9, 9),
                          (NULL, "2020-01-05", 39.99, 2, 5, 5),
                          (NULL, "2020-01-05", 29.99, 2, 8, 7),
                          (NULL, "2020-01-05", 24.99, 1, 6, 8);

SELECT * FROM UTILISATEUR;
SELECT * FROM ETAT;
SELECT * FROM TYPE_CHAUSSURE;
SELECT * FROM COULEUR;
SELECT * FROM COMMANDE;
SELECT * FROM POINTURE;
SELECT * FROM CHAUSSURE;
SELECT * FROM LIGNE_COMMANDE;
SELECT * FROM MESURE;
SELECT * FROM EST_DE_COULEUR;
SELECT * FROM PANIER;
