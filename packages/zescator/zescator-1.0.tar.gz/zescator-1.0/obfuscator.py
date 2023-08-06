import string
import random
import base64
import codecs

class Obfuscator:
    def __init__(self, code):
        self.code = code
        self.__obfuscate()

    def __xorED(self, text, key = None):
        newstring = ""
        if key is None:
            key = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(32, 64)))
        if not key[0] == " ":
            key = " " + key
        for i in range(len(text)):
            newstring += chr((ord(text[i]) ^ ord(key[(len(key) - 2) + 1])) % 256)
        return (newstring, key)

    def __encodestring(self, string):
        newstring = ''
        for i in string:
            if random.random() < 0.5:
                newstring += '\\x' + codecs.encode(i.encode(), 'hex').decode()
            else:
                newstring += '\\' + oct(ord(i))[2:].zfill(3)
        return newstring

    def __obfuscate(self):
        for _ in range(10):
            xorcod = self.__xorED(self.code)
            self.code = xorcod[0]
            encoded_code = base64.b64encode(codecs.encode(codecs.encode(self.code.encode(), 'bz2'), 'uu')).decode()
            encoded_code = [encoded_code[i:i + int(len(encoded_code) / 4)] for i in range(0, len(encoded_code), int(len(encoded_code) / 4))]
            new_encoded_code = []
            new_encoded_code.append(codecs.encode(encoded_code[0].encode(), 'uhex').decode() + 'u')
            new_encoded_code.append(codecs.encode(encoded_code[1], 'rot13') + 'r')
            new_encoded_code.append(codecs.encode(encoded_code[2].encode(), 'base64').decode() + 'h')
            new_encoded_code.append(base64.b85encode(codecs.encode(encoded_code[3].encode(), 'zlib')).decode() + 'x')
            self.code = ''.join(new_encoded_code)
        self.code = self.__encodestring(self.__xorED(self.code)[0])

class Deobfuscator:
    def init(self, code):
        self.code = code
        self.__deobfuscate()

    def __unXOR(self, text, key):
        newstring = ""
        for i in range(len(text)):
            newstring += chr((ord(text[i]) ^ ord(key[(len(key) - 2) + 1])) % 256)
        return newstring

    def __decodestring(self, string):
        index = 0
        newstring = ''
        while index < len(string):
            if string[index] == '\\' and string[index + 1] == 'x':
                newstring += codecs.decode(string[index + 2:index + 4], 'hex').decode()
                index += 4
            elif string[index] == '\\':
                newstring += chr(int(string[index + 1:index + 4], 8))
                index += 4
            else:
                newstring += string[index]
                index += 1
        return newstring

    def __deobfuscate(self):
        self.code = self.__decodestring(self.code)
        for _ in range(10):
            encoded_code = [self.code[i:i + 4] for i in range(0, len(self.code), 4)]
            new_encoded_code = []
            new_encoded_code.append(codecs.decode(encoded_code[0][:-1], 'uhex'))
            new_encoded_code.append(codecs.decode(encoded_code[1][:-1], 'rot13'))
            new_encoded_code.append(codecs.encode(encoded_code[2][:-1].encode(), 'base64').decode())
            new_encoded_code.append(codecs.decode(base64.b85decode(encoded_code[3][:-1].encode()), 'zlib').decode())
            self.code = base64.b64decode(codecs.decode(new_encoded_code[0].encode(), 'bz2')).decode()
            key = self.__unXOR(self.code, self.__decodestring(new_encoded_code[3]))
            self.code = self.__unXOR(self.code, key)

