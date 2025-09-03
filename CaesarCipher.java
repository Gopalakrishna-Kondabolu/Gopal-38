import java.util.*;

public class CaesarCipher {

    // Encryption function
    public static String encrypt(String plaintext, int key) {
        StringBuilder encryptedText = new StringBuilder();
        plaintext = plaintext.toUpperCase();

        for (int i = 0; i < plaintext.length(); i++) {
            char ch = plaintext.charAt(i);
            if (Character.isLetter(ch)) {
                char shifted = (char) ((ch - 'A' + key) % 26 + 'A');
                encryptedText.append(shifted);
            } else {
                encryptedText.append(ch); // Keep spaces & punctuation unchanged
            }
        }
        return encryptedText.toString();
    }

    // Decryption function
    public static String decrypt(String ciphertext, int key) {
        StringBuilder decryptedText = new StringBuilder();
        ciphertext = ciphertext.toUpperCase();

        for (int i = 0; i < ciphertext.length(); i++) {
            char ch = ciphertext.charAt(i);
            if (Character.isLetter(ch)) {
                char shifted = (char) ((ch - 'A' - key + 26) % 26 + 'A');
                decryptedText.append(shifted);
            } else {
                decryptedText.append(ch);
            }
        }
        return decryptedText.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Get input
        System.out.print("Enter plaintext: ");
        String plaintext = sc.nextLine();

        System.out.print("Enter key (shift value 0-25): ");
        int key = sc.nextInt();

        // Encrypt
        String encrypted = encrypt(plaintext, key);
        System.out.println("Encrypted text: " + encrypted);

        // Decrypt
        String decrypted = decrypt(encrypted, key);
        System.out.println("Decrypted text: " + decrypted);

        sc.close();
    }
}
