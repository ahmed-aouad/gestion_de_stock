CREATE DATABASE store;  --création d'une base de données appelée: store

mysql> CREATE TABLE product (  --création d'une table nommée: product 
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     name VARCHAR(255),
    ->     description TEXT,
    ->     price INT,
    ->     quantity INT,
    ->     id_category INT
    -> );

-- insertion de produits dans la table: product
mysql> INSERT INTO product (name, description, price, quantity, id_category) VALUES
    -> ('Tablette', 'la tablette dernière génération', 900, 20, 1),
    -> ('Smartphone', 'le Smartphone le moins cher du marché', 300, 30, 2),
    -> ('ordinateur', 'le meilleur rapport qualité prix', 400, 40, 3),
    -> ('camera', 'une caméra avec une qualité image exceptionnelle', 800, 60, 1),
    -> ('disque dure', 'une capacité de sockage excepionnelle', 150, 50, 3),
    -> ('Tablette', 'la tablette dernière génération', 900, 20, 1),
    -> ('telephone fixe', 'telephone fixe sans fil avec repondeur integré', 800, 60, 2);
