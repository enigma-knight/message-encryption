# message-encryption
 This script takes a message and encodes it with a positionally determined encryption algorithm. This affects letter distribution in a way that makes it difficult to find a pattern, and therefore difficult to decode.
 
 ***

*ex. input:*
> Hello world! Wassup y'all?

*ouput:*
> GHFBDNS XRLBOUS TTCKHNW OVWIPQJ TT

<h3>Basic use case:</h3>
 <p>To change the file that you want to be encrypted, go to `file_to_encrypt` and change it to the path you want. 
After running the script, it will write it to `encrypted.txt`. Open it to see the encrypted version.</p>

 ```python
 file_to_read = 'message.txt'  # change this is if you like, or change the contents of message.txt
 file_to_write_to = 'encrypted.txt'  # this is where it will write the encrypted version to.
 ```
 
 ***
 
<p>After executing this script, the size of the message increases, typically by ~<i>30%</i>*, and skews the letter distribution rather impressively.</p>

| Letter | Dist. Before | Dist. Post |
| ------ | ------------ | ---------- |
| A | 8.4297 | 3.7382 |
| B | 1.5086 | 2.9069 |
| C | 2.3108 | 5.0531 |
| D | 4.8311 | 3.3150 |
| E | 12.5417 | 2.4330 |
| F | 2.2724 | 5.0949 |
| G | 2.4052 | 3.0609 |
| H | 6.1685 | 5.7548 |
| I | 6.7891 | 1.4726 |
| J | 0.0703 | 3.3624 |
| K | 0.7601 | 3.9979 |
| L | 3.8322 | 4.6633 |
| M | 2.5771 | 2.2070 |
| N | 7.2314 | 4.4899 |
| O | 7.0088 | 3.4996 |
| P | 1.7493 | 2.6427 |
| Q | 0.0669 | 3.0446 |
| R | 5.8917 | 4.5104 |
| S | 6.0820 | 5.5623 |
| T | 9.6468 | 7.0867 |
| U | 2.6448 | 3.9320 |
| V | 0.8902 | 4.4797 |
| W | 2.3236 | 3.7293 |
| X | 0.1395 | 2.4573 |
| Y | 1.7884 | 5.4979 |
| Z | 0.0395 | 2.0077 |
