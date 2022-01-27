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


############################

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
   mot_de_passe VARCHAR(50),
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
   taille INT,
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
   prix_unit INT,
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
