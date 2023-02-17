# soudex
This is the project of the Basics of research information and Web of my university. 


Soundex is a phonetic algorithm for indexing names by sound, as pronounced in English. The goal is for homophones to be encoded to the same representation so that they can be matched despite minor differences in spelling. The algorithm mainly encodes consonants; a vowel will not be encoded unless it is the first letter. Soundex is the most widely known of all phonetic algorithms (in part because it is a standard feature of popular database software such as IBM Db2, PostgreSQL, MySQL, SQLite, Ingres, MS SQL Server, Oracle. Snowflake and SAP ASE.) Improvements to Soundex are the basis for many modern phonetic algorithms

The Soundex code for a name consists of a letter followed by three numerical digits: the letter is the first letter of the name, and the digits encode the remaining consonants. Consonants at a similar place of articulation share the same digit so, for example, the labial consonants B, F, P, and V are each encoded as the number 1.

The correct value can be found as follows:

   1. Retain the first letter of the name and drop all other occurrences of a, e, i, o, u, y, h, w.
   2. Replace consonants with digits as follows (after the first letter):
        b, f, p, v → 1
        c, g, j, k, q, s, x, z → 2
        d, t → 3
        l → 4
        m, n → 5
        r → 6
   3. If two or more letters with the same number are adjacent in the original name (before step 1), only retain the first letter; also two letters with the same number separated by 'h' , 'w' or 'y' are coded as a single number, whereas such letters separated by a vowel are coded twice. This rule also applies to the first letter.
   4. If there are too few letters in the word to assign three numbers, append zeros until there are three numbers. If there are four or more numbers, retain only the first three. 
   
Using this algorithm, both "Robert" and "Rupert" return the same string "R163" while "Rubin" yields "R150". "Ashcraft" and "Ashcroft" both yield "A261". "Tymczak" yields "T522" not "T520" (the chars 'z' and 'k' in the name are coded as 2 twice since a vowel lies in between them). "Pfister" yields "P236" not "P123" (the first two letters have the same number and are coded once as 'P'), and "Honeyman" yields "H555". 

The following algorithm is followed by most SQL languages (excluding PostgreSQL[example needed]):

   1. Save the first letter. Map all occurrences of a, e, i, o, u, y, h, w. to zero(0)
   2. Replace all consonants (include the first letter) with digits as in [2.] above.
   3. Replace all adjacent same digits with one digit, and then remove all the zero (0) digits
   4. If the saved letter's digit is the same as the resulting first digit, remove the digit (keep the letter).
   5. Append 3 zeros if result contains less than 3 digits. Remove all except first letter and 3 digits after it (This step same as [4.] in explanation above).
   

This code is an algorithm that calculates the soundex of every vocabulary at Apple.com.
