from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    # Carga tu archivo batalla_aura.html desde la carpeta templates
    return render_template('batalla_aura.html')

# Ruta de registro
@app.route('/api/registrar', methods=['POST'])
def registrar():
    datos = request.get_json()
    alias = datos.get('alias', '')
    barrio = datos.get('barrio', '')
    
    print(f"¡Nuevo registro! Alias: {alias}, Barrio: {barrio}")
    
    return jsonify({
        "status": "success",
        "mensaje": f"Has sido inscrito exitosamente desde el barrio {barrio}."
    })

if __name__ == '__main__':
    # host='0.0.0.0' te permite abrir la página desde tu iPhone en la misma red Wi-Fi
    app.run(host='0.0.0.0', port=5000, debug=True)