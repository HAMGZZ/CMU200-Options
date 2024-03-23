from Crypto.Cipher import ARC2
import struct
KEY = "Revision\0"  # decryption key for the data
STRUCT_TWO_UNSIGNED_INTS = "<II"
for line in open("SWOPT.DAT"):
    if len(line) == 17:
        cipher = ARC2.new(KEY)  # a new ARC2 cipher with the right key (ARC2 is a symmetric block cipher, we need a new cipher for each ciphertext)
        ciphertext = line.strip().decode("hex")  # Decode our ciphertext from hex, removing whitespace from the start and end
        plaintext = cipher.decrypt(ciphertext)  # Decrypt the cyphertext using the key
        a, b = struct.unpack(STRUCT_TWO_UNSIGNED_INTS, plaintext)  # unpack two unsigned ints from the plaintext
        print("SN: %d - %08x" % (a, b))

