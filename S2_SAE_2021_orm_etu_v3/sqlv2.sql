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
                        (NULL, 'Recu');

INSERT INTO TYPE_CHAUSSURE VALUES (NULL, 'Baskets'),
                                  (NULL, 'Claquettes'),
                                  (NULL, 'Bottes');

INSERT INTO COULEUR VALUES (NULL, 'Beige'),
                           (NULL, 'Noir'),
                           (NULL, 'Rouge'),
                           (NULL, 'Bleu'),
                           (NULL, 'Vert'),
                           (NULL, 'Jaune'),
                           (NULL, 'Cyan'),
                           (NULL, 'Violet'),
                           (NULL, 'Blanc'),
                           (NULL, 'Rose');

INSERT INTO COMMANDE VALUES (NULL, "2019-12-20", 2, 2),
                            (NULL, "2020-01-05", 1, 2);

INSERT INTO POINTURE VALUES (NULL, 42.0),
                            (NULL, 42.5),
                            (NULL, 43.0),
                            (NULL, 43.5),
                            (NULL, 44.0),
                            (NULL, 44.5),
                            (NULL, 45.0),
                            (NULL, 45.5);

INSERT INTO CHAUSSURE VALUES (NULL, 'Oui', 'NIKE', 'Point C', 1),
                             (NULL, 'Non', 'Balenciago', 'Botru-Chausse', 2);

INSERT INTO LIGNE_COMMANDE VALUES (1, 2, 79.99, 8),
                                  (2, 1, 49.99, 50);

INSERT INTO MESURE VALUES (1, 2),
                          (2, 1);

INSERT INTO EST_DE_COULEUR VALUES (1, 2),
                                  (2, 1);

INSERT INTO PANIER VALUES (NULL, "2019-12-19", 49.99, 3, 1, 1), 
                          (NULL, "2020-01-05", 79.99, 1, 2, 2);

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
