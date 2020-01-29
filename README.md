# message-encryption
This script takes a message and encodes it with a positionally determined encryption algorithm. This affects letter distribution in a way that makes it difficult to find a pattern, and therefore difficult to decode.


*ex. input:*
> Hello world! Wassup y'all?

*ouput:*
> GHFBDNS XRLBOUS TTCKHNW OVWIPQJ TT

<h3>Basic use case:</h3>
>To change the file that you want to be encrypted, go to `file_to_encrypt` and change it to the path you want. 
>After running the script, it will write it to `encrypted.txt`. Open it to see the encrypted version.
> ```python
> file_to_read = 'message.txt'  # change this is if you like, or change the contents of message.txt
> file_to_write_to = 'encrypted.txt'  # this is where it will write the encrypted version to.
> ```
