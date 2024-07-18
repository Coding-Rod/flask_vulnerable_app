from cryptography.fernet import Fernet

from config.config import fernet_key

fernet = Fernet(fernet_key)

class Encryptor:
    """
    A class for encrypting and decrypting text
    """
    @staticmethod
    def encrypt_text(text: str) -> str:
        """ This function encrypts a text

        Args:
            text (str): Text to encrypt

        Returns:
            str: Encrypted text
        """
        text_bytes = text.encode('utf-8')
        encrypted_text = fernet.encrypt(text_bytes).decode('utf-8')
        return encrypted_text
    
    @staticmethod
    def compare_text(plain_text: str, encrypted_text: str) -> bool:
        """ This function compares a plain text with an encrypted text

        Args:
            plain_text (str): Plain text
            encrypted_text (str): Encrypted text

        Returns:
            bool: True if the plain text is the same as the decrypted text, False otherwise
        """
        
        def decrypt_text(text: str) -> str:
            """ This function decrypts a text

            Args:
                text (str): Text to decrypt

            Returns:
                str: Decrypted text
            """
            text_bytes = text.encode('utf-8')
            decrypted_text = fernet.decrypt(text_bytes).decode('utf-8')
            return decrypted_text
        
        decrypted_text = decrypt_text(encrypted_text)
        return plain_text == decrypted_text