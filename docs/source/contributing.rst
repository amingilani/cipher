Contributing Guidelines / Directives de Contribution
================================================

.. _english:

English 
-------

`Version française <francais_>`_


How to Contribute
---------------

We welcome contributions to CIPHER! Here's how you can help:

1. Fork the repository
2. Create a new branch
3. Add your protocol documentation
4. Submit a pull request

Documentation Standards
--------------------

Protocol Structure
~~~~~~~~~~~~~~~~

* 5-character alphanumeric protocol ID (generate using: ``python3 -c "import random, string; print(''.join(random.choices(string.ascii_uppercase + string.digits, k=5)))"`` )
* Bilingual content (English and French)
* Cross-references between language versions
* Follow RST formatting standards:

  * `Sphinx RST Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
  * `RST Documentation <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`_

Required Sections
~~~~~~~~~~~~~~~

1. Overview:

   * Purpose and basic description
   * Links to relevant tools/references
   * Protocol flexibility statement

2. Standard Operating Procedure:

   * Initialization
   * Transmission Format
   * Example Transmission

3. Implementation Details:

   * Core procedure
   * Examples with test data
   * Look-up tables if needed

4. Security Considerations:

   * Security limitations
   * Intended use cases

Testing
-------

Before submitting:

1. Build documentation locally:
   
   Install dependencies: ``poetry install``
   
   Build docs: ``cd docs && poetry run make html``

2. Verify both language versions:

   * Check cross-references
   * Ensure content parity
   * Validate all examples

3. Optional: Test PDF generation: ``poetry run make latexpdf``

Questions?
---------

Open an issue in the repository or contact the maintainers.

.. _francais:

Français
--------

`English version <english_>`_

Comment Contribuer
----------------

Nous accueillons les contributions à CIPHER! Voici comment vous pouvez aider:

1. Créez une copie du dépôt
2. Créez une nouvelle branche
3. Ajoutez votre documentation de protocole
4. Soumettez une demande de fusion

Normes de Documentation
---------------------

Structure du Protocole
~~~~~~~~~~~~~~~~~~~~

* ID de protocole alphanumérique de 5 caractères (générer avec: ``python3 -c "import random, string; print(''.join(random.choices(string.ascii_uppercase + string.digits, k=5)))"`` )
* Contenu bilingue (anglais et français)
* Références croisées entre versions linguistiques
* Suivre les normes de formatage RST:

  * `Guide RST Sphinx <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
  * `Documentation RST <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`_

Sections Requises
~~~~~~~~~~~~~~~

1. Aperçu:

   * Objectif et description de base
   * Liens vers outils/références pertinents
   * Déclaration de flexibilité du protocole

2. Procédure Opérationnelle Standard:

   * Initialisation
   * Format de Transmission
   * Exemple de Transmission

3. Détails d'Implémentation:

   * Procédure principale
   * Exemples avec données de test
   * Tables de consultation si nécessaire

4. Considérations de Sécurité:

   * Limites de sécurité
   * Cas d'utilisation prévus

Tests
-----

Avant de soumettre:

1. Construire la documentation localement:
   
   Installer les dépendances: ``poetry install``
   
   Construire la documentation: ``cd docs && poetry run make html``

2. Vérifier les deux versions linguistiques:

   * Vérifier les références croisées
   * Assurer la parité du contenu
   * Valider tous les exemples

3. Optionnel: Tester la génération PDF: ``poetry run make latexpdf``

Questions?
---------

Ouvrez un ticket dans le dépôt ou contactez les mainteneurs.
