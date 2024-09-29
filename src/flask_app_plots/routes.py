from flask_app_plots import app
import base64
import io
import matplotlib.pyplot as plt
from flask import render_template, request
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for non-GUI rendering


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        x_values = request.form.get('x_values')
        y_values = request.form.get('y_values')

        # Convert input strings to lists of floats
        x_values = list(map(float, x_values.split(',')))
        y_values = list(map(float, y_values.split(',')))

        # Generate the plot
        img = io.BytesIO()
        plt.figure(figsize=(6, 4))
        plt.plot(x_values, y_values, marker='o')
        plt.title('User Input Plot')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.grid(True)
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        plt.close()

        return render_template('plot.html', plot_url=plot_url)

    return render_template('home.html')
