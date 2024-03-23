from Crypto.Cipher import ARC2 #ARC2 enxryption
import struct

serial = 837109 #Your Serial number
serial2 = 35     #Your Second Serial number / decipher gives in hex
option = 20     #The option you want / decipher gives in hex

record = struct.pack("<II", serial, serial2 + (option <<20))  #combine serial 1 and 2 intro a struct of unsigned ints in little-endian fation then adding the option with a bitwase shift of 20
encyphered = ARC2.new("Revision\0").encrypt(record) #encrypt ACR2 encryption
print("HEX:  " + encyphered.encode("hex"))  #print out the hex result of encyphered ...