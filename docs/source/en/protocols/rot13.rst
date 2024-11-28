ROT13 Voice Channel Specification
===============================

Overview
--------
ROT13 is a simple substitution cipher that replaces each letter with the letter 13 positions after it in the alphabet. 
For amateur radio voice communications, this specification defines a standard operating procedure for its use.

Standard Operating Procedure
--------------------------

Initialization
~~~~~~~~~~~~
1. Announce intention to use ROT13: "INITIATING ROT13 PROCEDURE"
2. Confirm reception: Receiving station must acknowledge with "ROT13 READY"

Transmission Format
~~~~~~~~~~~~~~~~
* Prefix each encoded message with "CIPHER FOLLOWS"
* Speak each word clearly using ITU phonetic alphabet
* End encoded transmission with "CIPHER ENDS"

Example Transmission
~~~~~~~~~~~~~~~~~~

.. code-block:: text

   OPERATOR 1: "INITIATING ROT13 PROCEDURE"
   OPERATOR 2: "ROT13 READY"
   OPERATOR 1: "CIPHER FOLLOWS"
   OPERATOR 1: "HOTEL ECHO LIMA LIMA OSCAR" (Original: "HELLO")
   OPERATOR 1: "CIPHER ENDS"

Implementation Details
-------------------

Alphabet Mapping
~~~~~~~~~~~~~~

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

Regulatory Compliance
------------------
This implementation complies with Canadian Radiocommunication Regulations by:

1. Being publicly documented
2. Using a well-known, reversible algorithm
3. Maintaining transparency in communications

Notes
-----
* ROT13 is not secure encryption and should only be used for training or recreational purposes
* All transmissions must comply with Canadian amateur radio regulations
* Keep a copy of this specification available during operation
