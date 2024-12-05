# TAREA
PYTHON API DEVELOPER
Lutzgardo Saavedra

## Errores detectados
+ Agrega redirect
+ Se comenta /home
+ cambiar fetchone() por fetchall()
+ Agrega los methods=['GET', 'POST']
+ Cambia contend por content
+ Cambia ! por ?
+ cambia return redirect(url_for('get_all_post')) por redirect(url_for('get_all_post'))
+ Agrega elif para request.method == "GET":
+ Agrega return render_template('post/create.html') al elif
+ Cambia <str:post_id> por <string:post_id>
+ Cambia (post_id) por (post_id,)
+ Modificar el puerto y completar el host


### CORRECCIÓN DE LOS SIGUIENTES ERRORES: 

1. (Realizado) No necesitamos pandas, o al menos no en esa versión. 
2. (Realizado) Prácticamente todo el archivo app.py contiene errores; las plantillas, en su mayoría, están correctas, pero es necesario o pertinente hacer modificaciones lo puedes hacer.
3. (Realizado) Faltó importar correctamente la función desde el archivo db.py.
4. (Realizado)Crea un enlace en base.html para visualizar el favicon.ico en la aplicación; es necesario mover el archivo a la carpeta adecuada.
5. (Se agregó atributo required a los elementos input:text del título y textare para el contenito para que no se realice el submit) Agrega validación para el título; si no se llena, activa un mensaje de alerta, impidiendo el submit. 


        git add .
        git commit -m "fix: errores ....."
        git push origin main