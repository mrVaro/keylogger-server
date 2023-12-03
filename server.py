from flask import Flask, request

app = Flask(__name__)

folder_path = 'C:/Users/PROBOOK/Desktop/'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file sent', 400

    fichier = request.files['file']
    fichier.save(folder_path + fichier.filename)
    return 'File successfull received', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
