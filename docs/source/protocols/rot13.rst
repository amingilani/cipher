ROT13 Voice Channel Specification / Spécification ROT13 pour Canaux Vocaux
=======================================================================

Overview / Aperçu
----------------
ROT13 is a simple substitution cipher that replaces each letter with the letter 13 positions after it in the alphabet. 
For amateur radio voice communications, this specification defines a standard operating procedure for its use.

ROT13 est un chiffrement par substitution simple qui remplace chaque lettre par la lettre située 13 positions après elle dans l'alphabet.
Pour les communications vocales en radio amateur, cette spécification définit une procédure opérationnelle standard.

Standard Operating Procedure / Procédure Opérationnelle Standard
-------------------------------------------------------------

Initialization / Initialisation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Announce intention / Annoncer l'intention:
   - EN: "INITIATING ROT13 PROCEDURE"
   - FR: "INITIATION PROCÉDURE ROT13"

2. Confirm reception / Confirmer la réception:
   - EN: Receiving station must acknowledge with "ROT13 READY"
   - FR: La station réceptrice doit confirmer avec "ROT13 PRÊT"

Transmission Format / Format de Transmission
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Prefix each encoded message / Préfixer chaque message encodé:
   - EN: "CIPHER FOLLOWS"
   - FR: "CHIFFREMENT SUIT"
* Speak each word clearly using ITU phonetic alphabet / Épeler chaque mot clairement en utilisant l'alphabet phonétique ITU
* End transmission / Terminer la transmission:
   - EN: "CIPHER ENDS"
   - FR: "FIN DU CHIFFREMENT"

Example Transmission / Exemple de Transmission
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   OPERATOR/OPÉRATEUR 1: "INITIATING ROT13 PROCEDURE / INITIATION PROCÉDURE ROT13"
   OPERATOR/OPÉRATEUR 2: "ROT13 READY / ROT13 PRÊT"
   OPERATOR/OPÉRATEUR 1: "CIPHER FOLLOWS / CHIFFREMENT SUIT"
   OPERATOR/OPÉRATEUR 1: "HOTEL ECHO LIMA LIMA OSCAR" (Original: "HELLO")
   OPERATOR/OPÉRATEUR 1: "CIPHER ENDS / FIN DU CHIFFREMENT"

Implementation Details / Détails d'Implémentation
--------------------------------------------

Alphabet Mapping / Table de Correspondance Alphabétique
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :header: "Original", "Encoded/Encodé", "Original", "Encoded/Encodé"
   :widths: 25, 25, 25, 25

   A, N, N, A
   B, O, O, B
   C, P, P, C
   D, Q, Q, D
   E, R, R, E
   F, S, S, F
   G, T, T, G
   H, U, U, H
   I, V, V, I
   J, W, W, J
   K, X, X, K
   L, Y, Y, L
   M, Z, Z, M

Regulatory Compliance / Conformité Réglementaire
-------------------------------------------
This implementation complies with Canadian Radiocommunication Regulations by: /
Cette implémentation est conforme aux règlements de radiocommunication canadiens car :

1. Being publicly documented / Elle est documentée publiquement
2. Using a well-known, reversible algorithm / Elle utilise un algorithme réversible bien connu
3. Maintaining transparency in communications / Elle maintient la transparence dans les communications

Notes / Notes
----------
* ROT13 is not secure encryption and should only be used for training or recreational purposes /
  ROT13 n'est pas un chiffrement sécurisé et ne doit être utilisé qu'à des fins de formation ou de loisir
* All transmissions must comply with Canadian amateur radio regulations /
  Toutes les transmissions doivent être conformes aux règlements canadiens de radio amateur
* Keep a copy of this specification available during operation /
  Gardez une copie de cette spécification disponible pendant l'opération 
