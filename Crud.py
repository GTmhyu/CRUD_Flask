from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

# Konfigurasi database atau datalogic di sini (jika diperlukan)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/api/book', methods=['POST'])
def create_book():
    # Mendapatkan data dari request JSON
    data = request.get_json()
    
    # Melakukan operasi pembuatan data baru dalam database atau datalogic di sini
    
    return jsonify({'message': 'Book created successfully!'})

@app.route('/api/book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    # Mendapatkan data buku berdasarkan ID dari database atau datalogic di sini
    book = {'id': book_id, 'title': 'Book Title', 'author': 'Book Author'}
    
    return jsonify(book)

@app.route('/api/book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    # Mendapatkan data dari request JSON
    data = request.get_json()
    
    # Melakukan operasi perbarui data buku berdasarkan ID dalam database atau datalogic di sini
    
    return jsonify({'message': 'Book updated successfully!'})

@app.route('/api/book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    # Menghapus data buku berdasarkan ID dari database atau datalogic di sini
    
    return jsonify({'message': 'Book deleted successfully!'})


