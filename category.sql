mysql> CREATE TABLE category (  --création d'une table nommée: product 
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     name VARCHAR(255)
    -> );

-- insertion de catégiries de produits dans la table : category
mysql> INSERT INTO category (id, name) VALUES (1, 'multimédia'), (2, 'telephonie'), (3, 'informatique');
