#fmt:off
from flask import render_template, request, redirect, url_for
import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for non-GUI rendering
import matplotlib.pyplot as plt
import io
import base64
from werkzeug.utils import secure_filename
from flask_app_plots import app

ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Process the CSV file
            data = pd.read_csv(filepath)
            x_values = data.iloc[:, 0]
            y_values = data.iloc[:, 1]

            # Generate the plot
            img = io.BytesIO()
            plt.figure(figsize=(6, 4))
            plt.plot(x_values, y_values, marker='o')
            plt.title('CSV Input Plot')
            plt.xlabel('X-axis')
            plt.ylabel('Y-axis')
            plt.grid(True)
            plt.savefig(img, format='png')
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode()
            plt.close()

            return render_template('plot.html', plot_url=plot_url)

    return render_template('home.html')