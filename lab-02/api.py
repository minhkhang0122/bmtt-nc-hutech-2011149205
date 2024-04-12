from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.playfair.playfair_cipher import PlayFairCipher
from cipher.transposition.transposition_cipher import TranspositionCipher


app = Flask(__name__)
vigenere_Cipher = VigenereCipher()
caesar_cipher = CaesarCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()
transposition_cipher = TranspositionCipher()


#Transposition API Call
@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = transposition_cipher.encrypt(plain_text,key)
    return jsonify({'encrypted_text': encrypted_text})
@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypt_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypt_text})



#PlayFair API Call
@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})
@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypt_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypt_text})
@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data= request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted-text': decrypted_text})    
    
#RailFence API Call
@app.route('/api/railfence/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})


# Vigenere API Call
@app.route('/api/vigenere/encrypt', methods =['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_Cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route('/api/vigenere/decrypt', methods =['POST'])
def vigenere_decrypt():
    data  = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_Cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})
    
# CAESAR API Call
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
