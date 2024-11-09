
```bash
virtualenv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
python app.py
```

II. INSTRUCCIONES

• El examen consta de 2 partes
• Una parte teórica de 5 preguntas con un valor de 2 puntos cada una
• Una parte práctica de 1 pregunta con un valor de 10 puntos
• Se tomará en cuenta el esfuerzo para notas parciales.
• Se puede consultar en línea, pero no se permite la interacción con compañeros de
clase
• El examen dura un máximo de 2 horas, al terminar compartir resultados al correo del
instructor.

III. PARTE TEORICA (10 PUNTOS)

1. Para qué se puede usar Python en lo que respecta a datos. Dar 5 casos y explicar
brevemente

caso 1 - Preparación y limpieza de datos: Con librerías como Pandas y NumPy, Python permite organizar y transformar datos de manera eficiente, manejando valores faltantes y asegurando que los datos estén listos para el análisis. Esto facilita el manejo de grandes volúmenes de datos y la detección de posibles errores que afecten la calidad del análisis.

caso 2 -Exploración de datos y análisis descriptivo: Python facilita el análisis exploratorio, ayudando a los analistas a identificar patrones y tendencias en los datos mediante cálculos estadísticos y gráficos. Herramientas como Pandas, Matplotlib y Seaborn permiten crear visualizaciones que apoyan el proceso de descubrimiento y comprensión inicial de los datos.

caso 3 -Visualización y comunicación de resultados: La visualización es fundamental para presentar hallazgos de manera clara. Python incluye librerías como Matplotlib, Seaborn, y Plotly, que permiten crear gráficos y visualizaciones interactivas, facilitando que los datos se interpreten de manera efectiva y atractiva para diversos públicos.

caso 4 -Modelado predictivo y aprendizaje automático: Python es muy usado en el desarrollo de modelos predictivos mediante aprendizaje automático. Librerías como Scikit-learn y TensorFlow facilitan la creación de modelos de clasificación, regresión y redes neuronales, lo cual es fundamental para aplicaciones que requieren predicciones o clasificaciones precisas.

caso 5 -Análisis estadístico avanzado: Para un análisis más profundo, Python ofrece herramientas como SciPy y Statsmodels, que permiten realizar operaciones estadísticas complejas, incluyendo pruebas de hipótesis y análisis de regresión. Esto es esencial para obtener insights detallados y tomar decisiones informadas basadas en datos.

2. ¿Cómo se diferencian Flask de Django? Argumentar.

- Enfoque: Flask es un micro-framework ligero que ofrece solo lo esencial para aplicaciones pequeñas, mientras que Django es más completo, con muchas funcionalidades integradas para proyectos grandes y estructurados.

- Flexibilidad y Estructura: Flask proporciona mayor flexibilidad en la organización del proyecto, dejando al desarrollador decidir cómo estructurarlo, mientras que Django impone una estructura más rígida y guiada, ideal para proyectos de mayor envergadura.

- Escalabilidad: Flask es adecuado para aplicaciones sencillas o APIs, mientras que Django, con su amplia gama de herramientas, es mejor para aplicaciones más complejas y que requieren una gran escalabilidad.

3. ¿Qué es un API? Explicar en sus propias palabras

Una API es como un mensajero que le pide a un sistema o aplicación que realice una tarea y luego devuelve la respuesta. Permite que diferentes aplicaciones se comuniquen entre sí.

4. ¿Cuál es la principal diferencia entre REST y WebSockets?

REST es un sistema de comunicación que funciona bajo el modelo de solicitud-respuesta, donde cada vez que necesitas algo, haces una solicitud. WebSockets, en cambio, permite una comunicación continua y en tiempo real entre el servidor y el cliente.

5. Describir un ejemplo de API comercial y como funciona – usar otros ejemplos no vistos
en el curso.

Un ejemplo común es la API de Google Maps. Cuando una aplicación necesita mostrar un mapa o direcciones, hace una solicitud a la API de Google Maps, que responde con la información del mapa o la ruta. Esto permite integrar mapas fácilmente en otras aplicaciones sin tener que crear uno desde cero.

IV. PARTE PRACTICA (10 PUNTOS)

Extender la aplicación de REST API estudiantes visto en el capítulo 2 e incluir lo siguiente:
• Método GET – lista de estudiantes (2 puntos)
• Método GET <id> - estudiante por id (2 puntos)
• Método POST – crear estudiante nuevo (2 puntos)
• Método PUT <id> - actualizar estudiante (2 puntos)
• Método DELETE <>id – eliminar estudiante (2 puntos)
Se debe compartir el código de la aplicación, así como pantallazos para exponer los
resultados (de preferencia en POSTMAN)