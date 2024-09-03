from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        mensaje = request.form['mensaje']
        
        # Aquí puedes guardar la carta en una base de datos o enviar un correo con los datos.
        
        return render_template('confirmation.html', nombre=nombre)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")