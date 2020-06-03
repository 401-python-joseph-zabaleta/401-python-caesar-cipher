# Lab: Class 18 - Caesar Cipher

## Open Git Pull Requests  


## Overview  
Crytographic classic - the Caesar Cipher. Devise a method to encrypt a message that can then be decrypted when supplied with the corresponding key.  

## Feature Tasks and Requirements  
- [x] Create an `encrypt` function that takes in a plain text phrase and a numeric shift.  
    - the phrase will then be `shifted` that many letters.  
        - E.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. ecrypt(‘acb’, 10) would return ‘klm’  
    - [x] shifts that exceed 26 should wrap around:  
        - E.g. encrypt('abc':27) would return 'bcd'

- [x] Create a `decrypt` function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form as long as correct key is supplied.  
- [x] BREAK the ciphter so that an encrypted message can be transformed into its original state WITHOUT access to the key.  
- [x] Devise a method for the computer to determine if code was broken with minimal human guidance.  


## Implementation Notes:  
- In order to accomplish this task you'll need access to a `corpus` of English words.  
- A search on something like `python list of english words` should get you going.  


## User Acceptance Tests  
- [x] encrypt a string with a given `shift`.  
- [x] decrypt a previously encrypted string with the same `shift`.  
- [x] encryption should handle upper and lower case letters.  
- [x] encryption should allow non-alpha characters but ignore them, including white space.  
- [x] decrypt encrypted version of `It was the best of times, it was the worst of times.` WITHOUT knowing the shift used.  

## Dependencies  
- poetry  
- python  
- pyenv  

## Authors  
- Software Developer: Joseph Zabaleta
  - [Official Github](https://github.com/joseph-zabaleta)  

## Collaborations  
- none  

## License  
This project is under the MIT License.

## Acknowledgements / Resources  
- none

## Version History  
- 1.0.0 20200603  
    - Initial files created.  
- 1.0.1 20200603 
    - Lab Completed