from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'data'
app.config['EXCEL_FILE'] = 'data/uploaded_data.xlsx'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'xlsx', 'xls'}

# Ensure data directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'message': 'No file part'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'success': False, 'message': 'No file selected'}), 400
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Also save as the standard data file
            df = pd.read_excel(filepath)
            df.to_excel(app.config['EXCEL_FILE'], index=False)
            
            return jsonify({'success': True, 'message': 'File uploaded successfully'})
        else:
            return jsonify({'success': False, 'message': 'Invalid file type. Please upload .xlsx or .xls file'}), 400
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400

@app.route('/api/data')
def get_data():
    try:
        if os.path.exists(app.config['EXCEL_FILE']):
            df = pd.read_excel(app.config['EXCEL_FILE'])
            # Convert to dictionary format, handling NaN values
            data = df.fillna('').to_dict('records')
            return jsonify({'success': True, 'data': data})
        else:
            return jsonify({'success': True, 'data': []})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
