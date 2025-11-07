from flask import Flask, render_template_string
import socket
import os

app = Flask(__name__)

# Utilizamos f-strings para inyectar el hostname y otros detalles.
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Saludos desde el Contenedor</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f0f2f5;
            color: #333;
            text-align: center;
        }
        .container {
            background-color: #ffffff;
            padding: 40px 60px;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            width: 90%;
            animation: fadeIn 1s ease-out;
        }
        h1 {
            color: #4CAF50;
            margin-bottom: 20px;
            font-size: 2.5em;
            animation: slideIn 0.8s ease-out;
        }
        p {
            font-size: 1.2em;
            line-height: 1.6;
            margin-bottom: 10px;
        }
        .hostname {
            color: #2196F3;
            font-weight: 700;
            word-wrap: break-word; 
            background-color: #e3f2fd;
            padding: 8px 15px;
            border-radius: 6px;
            display: inline-block;
            margin-top: 15px;
            font-family: 'Courier New', Courier, monospace;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        .footer {
            margin-top: 30px;
            font-size: 0.9em;
            color: #888;
        }
        .icon {
            font-size: 1.5em;
            vertical-align: middle;
            margin-left: 5px;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-50px); }
            to { opacity: 1; transform: translateX(0); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>¡Hola desde tu Backend Escalable!</h1>
        <p>Esta solicitud ha sido procesada por uno de nuestros contenedores.</p>
        <p>Te saluda el contenedor con el hostname:</p>
        <div class="hostname">{{ hostname }}</div>
        <div class="footer">
            <p>Servicio provisto por Axel en Docker.</p>
            <p>¡Disfruta de la distribución de carga!</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    hostname = socket.gethostname()
    return render_template_string(HTML_TEMPLATE, hostname=hostname) # app_version=app_version

if __name__ == '__main__':
    # Es crucial que Flask escuche en '0.0.0.0' dentro de Docker
    # para que sea accesible desde fuera del contenedor.
    app.run(host='0.0.0.0', port=5000)
