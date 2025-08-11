class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        result = ''
        for letter in text.lower():
            position = self.alphabet.find(letter)
            if position >= 0:
                if is_encrypt:
                    result += self.alphabet[(position + shift) % 33]
                else:
                    result += self.alphabet[(position - shift) % 33]
            else:
                result += letter
        return result


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
)) 
