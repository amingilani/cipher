Spécification ROT13 pour Canaux Vocaux
===================================

Aperçu
------
ROT13 est un chiffrement par substitution simple qui remplace chaque lettre par la lettre située 13 positions après elle dans l'alphabet.
Pour les communications vocales en radio amateur, cette spécification définit une procédure opérationnelle standard.

Procédure Opérationnelle Standard
-------------------------------

Initialisation
~~~~~~~~~~~~
1. Annoncer l'intention d'utiliser ROT13 : "INITIATION PROCÉDURE ROT13"
2. Confirmer la réception : La station réceptrice doit confirmer avec "ROT13 PRÊT"

Format de Transmission
~~~~~~~~~~~~~~~~~~~
* Préfixer chaque message encodé avec "CHIFFREMENT SUIT"
* Épeler chaque mot clairement en utilisant l'alphabet phonétique ITU
* Terminer la transmission encodée avec "FIN DU CHIFFREMENT"

Exemple de Transmission
~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   OPÉRATEUR 1 : "INITIATION PROCÉDURE ROT13"
   OPÉRATEUR 2 : "ROT13 PRÊT"
   OPÉRATEUR 1 : "CHIFFREMENT SUIT"
   OPÉRATEUR 1 : "HOTEL ECHO LIMA LIMA OSCAR" (Original: "HELLO")
   OPÉRATEUR 1 : "FIN DU CHIFFREMENT"

Détails d'Implémentation
---------------------

Correspondance Alphabétique
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Original
     - Encodé
   * - A
     - N
   * - B
     - O
   * - C
     - P
   * - (etc...)

Conformité Réglementaire
---------------------
Cette implémentation est conforme aux règlements de radiocommunication canadiens car :

1. Elle est documentée publiquement
2. Elle utilise un algorithme réversible bien connu
3. Elle maintient la transparence dans les communications

Notes
-----
* ROT13 n'est pas un chiffrement sécurisé et ne doit être utilisé qu'à des fins de formation ou de loisir
* Toutes les transmissions doivent être conformes aux règlements canadiens de radio amateur
* Gardez une copie de cette spécification disponible pendant l'opération 
