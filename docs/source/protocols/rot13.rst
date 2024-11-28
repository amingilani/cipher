ROT-N Voice Channel Specification / Spécification ROT-N pour Canaux Vocaux
=======================================================================

Protocol ID: Y3IGU

English
-------
:ref:`Version française <francais>`

Overview
~~~~~~~~
ROT is a simple substitution cipher that replaces each letter with another letter N positions after it in the alphabet (`ROT13 Details <https://en.wikipedia.org/wiki/ROT13>`_). While ROT13 is traditional (N=13), this specification supports any agreed-upon value of N. For testing or implementation, operators may use `CyberChef's ROT13 tool <https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,13)>`_.

For amateur radio voice communications, this specification defines a standard operating procedure for its use. Operators may deviate from the specific procedures described here, provided they:

1. Maintain sufficient information for message decryption
2. Stay within the spirit of clear and transparent communication
3. Ensure both parties understand the encoding method being used

Standard Operating Procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~

Initialization
^^^^^^^^^^^^
1. Signal intention to begin ROT procedure and specify N value if not 13
   Example: "INITIATING ROT13 PROCEDURE" or "INITIATING ROT20 PROCEDURE"

Transmission Format
^^^^^^^^^^^^^^^
* Signal the start of an encoded message 
  Example: "CIPHER FOLLOWS"
* Speak each word clearly using ITU phonetic alphabet
* Signal the end of encoded transmission
  Example: "CIPHER ENDS"

Example Transmission
^^^^^^^^^^^^^^^

.. code-block:: text

   OPERATOR 1: "INITIATING ROT20 PROCEDURE"
   OPERATOR 2: "ROT20 ACKNOWLEDGED"
   OPERATOR 1: "CIPHER FOLLOWS"
   OPERATOR 1: "HOTEL ECHO LIMA LIMA OSCAR"
   OPERATOR 1: "CIPHER ENDS"

Implementation Details
~~~~~~~~~~~~~~~~~~~

Encryption and Decryption
^^^^^^^^^^^^^^^^^^^^^

To encrypt a message:

1. For each letter in the original message:

   * Count forward N positions in the alphabet
   * Wrap around to 'A' after 'Z'
   * Numbers and special characters remain unchanged

2. Example with N=13:

   * "HELLO" → "URYYB"
   * "ABC" with N=2 → "CDE"
   * "Z" with N=1 → "A"

To decrypt a message:

1. For each letter in the encoded message:

   * Count backward N positions in the alphabet
   * Wrap around to 'Z' after 'A'
   * Numbers and special characters remain unchanged
2. Example with N=13:

   * "URYYB" → "HELLO"
   * "CDE" with N=2 → "ABC"
   * "A" with N=1 → "Z"

Formula:

* Encryption: E(x) = (x + N) mod 26
* Decryption: D(x) = (x - N) mod 26
* Where x is the position in alphabet (A=0, B=1, etc.)

Selecting N Value
^^^^^^^^^^^^^

* Any value of N from 1 to 25 is valid
* N=13 is traditional and recommended for general use
* Both stations must agree on N value before transmission
* N value may be changed mid-session with mutual agreement

Alphabet Mapping Example (N=13)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Original", "Encoded", "Original", "Encoded"
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

Security Considerations
~~~~~~~~~~~~~~~~~~~~
* ROT-N, regardless of N value, is not secure encryption
* Different N values do not significantly increase security
* Use only for training, recreation, or basic privacy
* Consider N value public information, not a secret key


.. _francais:

Français
--------
:ref:`English version <English>`

Aperçu
~~~~~~
ROT est un chiffrement par substitution simple qui remplace chaque lettre par la lettre située N positions après elle dans l'alphabet (`Détails ROT13 <https://en.wikipedia.org/wiki/ROT13>`_). Bien que ROT13 soit traditionnel (N=13), cette spécification prend en charge toute valeur convenue de N. Pour les tests ou l'implémentation, les opérateurs peuvent utiliser `l'outil ROT13 de CyberChef <https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,13)>`_.

Pour les communications vocales en radio amateur, cette spécification définit une procédure opérationnelle standard. Les opérateurs peuvent s'écarter des procédures spécifiques décrites ici, à condition de :

1. Maintenir des informations suffisantes pour le déchiffrement des messages
2. Rester dans l'esprit d'une communication claire et transparente
3. S'assurer que les deux parties comprennent la méthode d'encodage utilisée

Procédure Opérationnelle Standard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Initialisation
^^^^^^^^^^^^
1. Signaler l'intention de commencer la procédure ROT et spécifier la valeur N si différente de 13
   Exemple : "INITIATION PROCÉDURE ROT13" ou "INITIATION PROCÉDURE ROT20"

Format de Transmission
^^^^^^^^^^^^^^^^^^
* Signaler le début d'un message encodé
  Exemple : "CHIFFREMENT SUIT"
* Épeler chaque mot clairement en utilisant l'alphabet phonétique ITU
* Signaler la fin de la transmission encodée
  Exemple : "FIN DU CHIFFREMENT"

Exemple de Transmission
^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   OPÉRATEUR 1 : "INITIATION PROCÉDURE ROT20"
   OPÉRATEUR 2 : "ROT20 CONFIRMÉ"
   OPÉRATEUR 1 : "CHIFFREMENT SUIT"
   OPÉRATEUR 1 : "HOTEL ECHO LIMA LIMA OSCAR"
   OPÉRATEUR 1 : "FIN DU CHIFFREMENT"

Détails d'Implémentation
~~~~~~~~~~~~~~~~~~~~~

Chiffrement et Déchiffrement
^^^^^^^^^^^^^^^^^^^^^^^^
Pour chiffrer un message :

1. Pour chaque lettre du message original :

   * Compter N positions en avant dans l'alphabet
   * Revenir à 'A' après 'Z'
   * Les chiffres et caractères spéciaux restent inchangés

2. Exemple avec N=13 :

   * "HELLO" → "URYYB"
   * "ABC" avec N=2 → "CDE"
   * "Z" avec N=1 → "A"

Pour déchiffrer un message :

1. Pour chaque lettre du message encodé :

   * Compter N positions en arrière dans l'alphabet
   * Revenir à 'Z' après 'A'
   * Les chiffres et caractères spéciaux restent inchangés

2. Exemple avec N=13 :

   * "URYYB" → "HELLO"
   * "CDE" avec N=2 → "ABC"
   * "A" avec N=1 → "Z"

Formule :

* Chiffrement : E(x) = (x + N) mod 26
* Déchiffrement : D(x) = (x - N) mod 26
* Où x est la position dans l'alphabet (A=0, B=1, etc.)

Sélection de la Valeur N
^^^^^^^^^^^^^^^^^^^^^^
* Toute valeur de N de 1 à 25 est valide
* N=13 est traditionnel et recommandé pour l'usage général

Table de Correspondance Alphabétique Exemple (N=13)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Original", "Encodé", "Original", "Encodé"
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

Considérations de Sécurité
~~~~~~~~~~~~~~~~~~~~~~~
* ROT-N, quelle que soit la valeur de N, n'est pas un chiffrement sécurisé
* Différentes valeurs de N n'augmentent pas significativement la sécurité
* Utiliser uniquement pour la formation, le loisir ou la confidentialité de base
* Considérer la valeur N comme une information publique, non comme une clé secrète
