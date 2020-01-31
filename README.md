##  <a href="https://github.com/oakenduck/message-encryption">v1.8.0</a>

This script takes a message and encodes it with a positionally determined encryption algorithm. This affects letter distribution in a way that makes it difficult to find a pattern, and therefore difficult to decode.
 
 ***

*ex. input:*
> Hello world! Wassup y'all?

*ouput:*
> GHFBDNS XRLBOUS TTCKHNW OVWIPQJ TT

<br/><br/>
<h3>Basic use case:</h3>
 <p>To change the file that you want to be encrypted, go to <b>file_to_encrypt</b> and change it to the path you want. 
 After running the script, it will write it to <b>encrypted.txt</b>. Open it to see the encrypted version.</p>

 ```python
 file_to_read = 'message.txt'  # change this is if you like, or change the contents of message.txt
 file_to_write_to = 'encrypted.txt'  # this is where it will write the encrypted version to.
 ```

<br/><br/>
 ```diff
- WARNING!!
- The script will not encrypt numbers into letters. This will be included in a future patch.
```

<br/><br/>

 ***
 
<p>After executing this script, the size of the message increases, typically by ~<i>30%</i>, and skews the letter distribution rather impressively.<br>This is data taken from <i>War of the Worlds</i>:</p>

| Letter | Distr. Before | Distr. After |
| ------ | ------------ | ---------- |
| A | 8.4297% | 3.7382% |
| B | 1.5086% | 2.9069% |
| C | 2.3108% | 5.0531% |
| D | 4.8311% | 3.3150% |
| E | 12.5417% | 2.4330% |
| F | 2.2724% | 5.0949% |
| G | 2.4052% | 3.0609% |
| H | 6.1685% | 5.7548% |
| I | 6.7891% | 1.4726% |
| J | 0.0703% | 3.3624% |
| K | 0.7601% | 3.9979% |
| L | 3.8322% | 4.6633% |
| M | 2.5771% | 2.2070% |
| N | 7.2314% | 4.4899% |
| O | 7.0088% | 3.4996% |
| P | 1.7493% | 2.6427% |
| Q | 0.0669% | 3.0446% |
| R | 5.8917% | 4.5104% |
| S | 6.0820% | 5.5623% |
| T | 9.6468% | 7.0867% |
| U | 2.6448% | 3.9320% |
| V | 0.8902% | 4.4797% |
| W | 2.3236% | 3.7293% |
| X | 0.1395% | 2.4573% |
| Y | 1.7884% | 5.4979% |
| Z | 0.0395% | 2.0077% |

<p>As can be seen, several letter, most notably A and E, are misrepresented in distribution after encryption, with both reducing in distribution by up to <i>10</i>%. The letters that in English are not nearly as common, Z being the least common, go up by a few percent on average. Typically, any one letter, in either encrypted or unencrypted form, has an average of ~<i>3.8461</i>%.<br>If we compare all the letters in both versions to that average, we get a second distribution:</p>

| Letter | Comparison, unencrypted | Comparison, encrypted |
| ------ | ----------------------- | --------------------- |
| A | 2.1917% | 0.9719% |
| B | 0.3922% | 0.7558% |
| C | 0.6008% | 1.3138% |
| D | 1.2561% | 0.8619% |
| E | 3.2609% | 0.6326% |
| F | 0.5908% | 1.3247% |
| G | 0.6254% | 0.7958% |
| H | 1.6038% | 1.4962% |
| I | 1.7652% | 0.3829% |
| J | 0.0184% | 0.8742% |
| K | 0.1976% | 1.0395% |
| L | 0.9964% | 1.2125% |
| M | 0.6700% | 0.5738% |
| N | 1.8802% | 1.1674% |
| O | 1.8223% | 0.9099% |
| P | 0.4548% | 0.6871% |
| Q | 0.0174% | 0.7916% |
| R | 1.5318% | 1.1727% |
| S | 1.5813% | 1.4462% |
| T | 2.5082% | 1.8425% |
| U | 0.6877% | 1.0223% |
| V | 0.2315% | 1.1647% |
| W | 0.6041% | 0.9696% |
| X | 0.0363% | 0.6389% |
| Y | 0.4650% | 1.4295% |
| Z | 0.0103% | 0.5220% |
