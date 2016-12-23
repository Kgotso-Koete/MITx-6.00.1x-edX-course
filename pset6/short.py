import string


def get_message_text():
    return "hello"

def build_shift_dict(shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        assert (shift in range(0,26)), 'Shift value is out of range'
    
        caesar_dict= {}
        alphabet = string.ascii_letters #set alphabet as upper and lower case ascii charachters
        
        # For each alphabet and each letter of the alphabet apply the shift.
        for letter in range(len(alphabet)):
            new_letter = letter + shift
            if (new_letter >= 51):
                # Reset letters of the alphabet.
                new_letter -= 51
            caesar_dict[alphabet[letter]] = alphabet[new_letter]
                
        return caesar_dict  
        
def apply_shift(shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # get word to be encrypted        
        word = get_message_text()
        # create the shifted dictionary      
        alphabet = build_shift_dict(shift)
        #create encrypted word variable
        encrypted_word = ''
        
        for letter in word:
             encrypted_word += alphabet[letter]
            
        return  encrypted_word           
            
            
        
print(apply_shift(2))