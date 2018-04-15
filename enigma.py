import random
from collections import deque


class EnigmaRotor:
    """Creates rotor for an enigma machine, and manipulates it.
           -Starting rotor position is used as seed for random number generator .
           -Rotates rotor.
           -Output position for next rotor
           -Output letter for next rotor
           """
    
    def __init__(self, start_pos):
        '''initializes start position of rotor (0-127)'''
        random.seed(a = start_pos) #seed based of set rotor position
        self.rotor = deque([x for x in random.sample(range(128), 128)])
        self.rotations_count = 0 #starts counter for rotation
    
    def rotate_rotor(self):
        '''rotates rotor and keeps count of how many times it has rotated'''
        self.rotor.rotate(1)
        self.rotations_count += 1
   
    def next(self, input, is_encrypt = True):
        '''takes in a input and gives number(position) or letter as output'''
        if is_encrypt:
            return self.rotor[input]
        else:
            return self.rotor.index(input)

        
class EnigmaMachine:
    """Creates Enigma Machine with three rotors, that can decrypt or encrypt.
    """
    
    def __init__(self, start_settings = [0,1,2]):
        r1, r2, r3 = start_settings
        self.rotor1 = EnigmaRotor(r1)
        self.rotor2 = EnigmaRotor(r2)
        self.rotor3 = EnigmaRotor(r3)
        self.mirror = EnigmaRotor(r1+r2+r3)
    
    def crypt(self, message, is_encrypt = True):
        """ outputs encrypted message or decrypted, based of boolean"""
        encrypted_message = ''
        for letter in message:
            encrypted_message += self.next_letter(letter, is_encrypt)
        return encrypted_message
        
    def next_letter(self, letter, is_encrypt = True):
        '''gives output of letter from letter input'''
        pos = ord(letter)
        #first pass

        pos = self.rotor1.next(pos, is_encrypt)
        pos = self.rotor2.next(pos, is_encrypt)
        pos = self.rotor3.next(pos, is_encrypt)
        #mirrir
        pos = self.mirror.next(pos, is_encrypt)
        #second pass
        pos = self.rotor3.next(pos, is_encrypt)
        pos = self.rotor2.next(pos, is_encrypt)
        pos = self.rotor1.next(pos, is_encrypt)
        
        #Handles rotation of rotors
        rotor1_count = self.rotor1.rotate_rotor()
        if rotor1_count == 128:
            rotor2_count = self.rotor2.rotate_rotor()
            rotor1.rotations_count = 0
            if rotor2_count == 128:
                rotor3_count = self.rotor3.rotate_rotor()
                rotor2.rotations_count = 0
                
        return chr(pos) # letter output

    
    
if __name__ == "__main__":
    enc = EnigmaMachine([2,3,4]).crypt('ffffff', True)
    print(enc)
    de = EnigmaMachine([2,3,4]).crypt(enc, False)
    print(de)
        
