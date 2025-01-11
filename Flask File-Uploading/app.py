from flask import Flask,render_template,request,jsonify
import os
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER '] = UPLOAD_FOLDER 
os.makedirs(UPLOAD_FOLDER,exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'txt', 'pdf'}

def Allow_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload',methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error':'no file part in the request'}),400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error':'No file choosen for uploading'}),400
    
    if file and Allow_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER '],filename))
        return jsonify({"message": f"File '{filename}' uploaded successfully!"})
    
    else:
        return jsonify({'error':'Error !!'}),400

app.run(debug=True)
