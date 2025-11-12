from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('principal.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    error = None

    if request.method == 'POST':
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            # Validación de rangos
            if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70 and 0 <= asistencia <= 100):
                error = "Los valores están fuera del rango permitido."
            else:
                promedio = round((nota1 + nota2 + nota3) / 3, 2)
                estado = "APROBADO" if promedio >= 40 and asistencia >= 75 else "REPROBADO"
                resultado = {'promedio': promedio, 'estado': estado}

        except ValueError:
            error = "Por favor ingresa valores numéricos válidos."

    return render_template('ejercicio1.html', resultado=resultado, error=error)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None

    if request.method == 'POST':
        nombre1 = request.form['nombre1'].strip()
        nombre2 = request.form['nombre2'].strip()
        nombre3 = request.form['nombre3'].strip()

        nombres = [nombre1, nombre2, nombre3]

        # 🔴 Validar nombres repetidos (sin distinguir mayúsculas/minúsculas)
        nombres_minus = [n.lower() for n in nombres]
        if len(set(nombres_minus)) < 3:
            resultado = "No se pueden repetir los nombres."
        else:
            longitudes = [len(n) for n in nombres]

            # 🔴 Validar que no haya longitudes repetidas
            if len(set(longitudes)) < 3:
                resultado = "Hay nombres con la misma cantidad de caracteres."
            else:
                # ✅ Si todo está correcto, mostrar el nombre más largo
                max_long = max(longitudes)
                indice_mas_largo = longitudes.index(max_long)
                nombre_mas_largo = nombres[indice_mas_largo]
                resultado = (f"El nombre con mayor cantidad de caracteres es: {nombre_mas_largo}"
                            f"<br>El nombre tiene: {max_long} caracteres")

    return render_template('ejercicio2.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)