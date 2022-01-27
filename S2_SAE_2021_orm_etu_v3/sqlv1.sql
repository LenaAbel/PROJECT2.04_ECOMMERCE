#mysql --user=stoillon --password=3006 --host=serveurmysql --database=BDD_stoillon

DROP TABLE IF EXISTS panier;
DROP TABLE IF EXISTS ligne_commande;
DROP TABLE IF EXISTS commande;
DROP TABLE IF EXISTS mesure;
DROP TABLE IF EXISTS est_de_couleur;
DROP TABLE IF EXISTS chaussure;
DROP TABLE IF EXISTS utilisateur;
DROP TABLE IF EXISTS etat;
DROP TABLE IF EXISTS type_chaussure;
DROP TABLE IF EXISTS couleur;
DROP TABLE IF EXISTS pointure;

CREATE TABLE utilisateur(
   id_utilisateur INT NOT NULL AUTO_INCREMENT,
   username VARCHAR(50),
   password VARCHAR(50),
   role VARCHAR(50),
   est_actif INT,
   pseudo VARCHAR(50),
   email VARCHAR(50),
   PRIMARY KEY(id_utilisateur)
);

INSERT INTO utilisateur
VALUES (1, 'Garou', 'qmskufg', 'client', NULL, 'Garou42', 'garoudu42@gmail.com'),
       (2, 'Jean-Charles', 'zeqj%FL', 'client', NULL, 'JC56', 'jean.charles@gmail.com');

CREATE TABLE etat(
   id_etat INT NOT NULL AUTO_INCREMENT,
   libelle_etat VARCHAR(50),
   PRIMARY KEY(id_etat)
);

INSERT INTO etat
VALUES (1,'en ligne'),
       (2,'déconnecter');

CREATE TABLE type_chaussure(
   id_type_chaussure INT NOT NULL AUTO_INCREMENT,
   nom_type_chaussure VARCHAR(50),
   PRIMARY KEY(id_type_chaussure)
);

INSERT INTO type_chaussure
VALUES (1, 'airmax'),
       (2, 'sandales');

CREATE TABLE couleur(
   id_couleur INT NOT NULL AUTO_INCREMENT,
   nom_couleur VARCHAR(50),
   PRIMARY KEY(id_couleur)
);

INSERT INTO couleur
VALUES (1, 'beige'),
       (2, 'noir');
CREATE TABLE pointure(
   id_pointure INT NOT NULL AUTO_INCREMENT,
   taille INT,
   PRIMARY KEY(id_pointure)
);

CREATE TABLE commande(
   id_commande INT NOT NULL AUTO_INCREMENT,
   date_achat DATE,
   id_utilisateur INT,
   id_etat INT,
   PRIMARY KEY(id_commande),
   FOREIGN KEY(id_utilisateur) REFERENCES utilisateur(id_utilisateur),
   FOREIGN KEY(id_etat) REFERENCES etat(id_etat)
);

CREATE TABLE chaussure(
   id_chaussure INT NOT NULL AUTO_INCREMENT,
   nom_chaussure VARCHAR(50),
   marque_chaussure VARCHAR(50),
   fournisseur_chaussure VARCHAR(50),
   id_type_chaussure INT,
   PRIMARY KEY(id_chaussure),
   FOREIGN KEY(id_type_chaussure) REFERENCES type_chaussure(id_type_chaussure)
);

CREATE TABLE panier(
   id_panier INT NOT NULL AUTO_INCREMENT,
   date_ajout DATE,
   prix_unit INT,
   quantite INT,
   id_chaussure INT,
   id_utilisateur INT,
   PRIMARY KEY(id_panier),
   FOREIGN KEY(id_chaussure) REFERENCES chaussure(id_chaussure),
   FOREIGN KEY(id_utilisateur) REFERENCES utilisateur(id_utilisateur)
);

CREATE TABLE ligne_commande(
   id_commande INT,
   id_chaussure INT,
   prix_unit INT,
   quantite INT,
   PRIMARY KEY(id_commande, id_chaussure),
   FOREIGN KEY(id_commande) REFERENCES commande(id_commande),
   FOREIGN KEY(id_chaussure) REFERENCES chaussure(id_chaussure)
);

CREATE TABLE mesure(
   id_chaussure INT,
   id_pointure INT,
   PRIMARY KEY(id_chaussure, id_pointure),
   FOREIGN KEY(id_chaussure) REFERENCES chaussure(id_chaussure),
   FOREIGN KEY(id_pointure) REFERENCES pointure(id_pointure)
);

CREATE TABLE est_de_couleur(
   id_chaussure INT,
   id_couleur INT,
   PRIMARY KEY(id_chaussure, id_couleur),
   FOREIGN KEY(id_chaussure) REFERENCES chaussure(id_chaussure),
   FOREIGN KEY(id_couleur) REFERENCES couleur(id_couleur)
);
