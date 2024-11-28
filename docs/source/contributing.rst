Contributing Guidelines / Directives de Contribution
===============================================

How to Contribute / Comment Contribuer
--------------------------------

We welcome contributions to CIPHER! Here's how you can help: /
Nous accueillons les contributions à CIPHER! Voici comment vous pouvez aider:

Protocol Documentation / Documentation des Protocoles
----------------------------------------------

1. Fork the repository / Créez une copie du dépôt
2. Create a new branch / Créez une nouvelle branche
3. Add your protocol documentation / Ajoutez votre documentation de protocole
4. Submit a pull request / Soumettez une demande de fusion

Documentation Standards / Normes de Documentation
------------------------------------------

* Provide both English and French content / Fournir le contenu en anglais et en français
* Follow the existing bilingual format / Suivre le format bilingue existant
* Include all required sections / Inclure toutes les sections requises:
   - Overview/Aperçu
   - Standard Operating Procedure/Procédure Opérationnelle Standard
   - Implementation Details/Détails d'Implémentation
   - Regulatory Compliance/Conformité Réglementaire

Testing / Tests
-----------

Before submitting / Avant de soumettre:

1. Build documentation locally / Construire la documentation localement:
   ```bash
   poetry install
   cd docs
   poetry run make html
   ```
2. Check both languages / Vérifier les deux langues
3. Verify PDF generation / Vérifier la génération du PDF:
   ```bash
   poetry run make latexpdf
   ```

Questions? / Questions?
-------------------

Open an issue in the repository or contact the maintainers. /
Ouvrez un ticket dans le dépôt ou contactez les mainteneurs. 
