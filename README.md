💳 **Proyecto: Puntuación de Crédito**

📊 **Análisis de Riesgo de Incumplimiento en Préstamos**


**Autor:** Edwin Alexander Herrera

**Lenguaje:** Python

**Librerías utilizadas:** ``pandas`` , ``numpy`` , ``os`` 

**Tipo de proyecto:** Exploración y análisis de datos (EDA)

**Nivel:** Analista de Datos Jr. — Intermedio


⚙️**Configuración del entorno:**

Para garantizar la correcta ejecución del proyecto, se recomienda crear un entorno virtual y usar las dependencias listadas en requirements.txt.

```
1️⃣ Crear el entorno virtual
python -m venv venv

2️⃣ Activarlo (Windows)
. ./.venv/Scripts/activate

3️⃣.2️⃣  Activarlo (Mac / Linux)
source venv/bin/activate

 4️⃣ clonar el repositortio
git clone https://github.com/code-ALX79/Credit_Scoring_Analitics.git

5️⃣ Instalar las dependencias
pip install -r requirements.txt

```


🧩 **Descripción general**

Este proyecto está dirigido al área de préstamos de una entidad bancaria y tiene como propósito *analizar los factores que pueden influir en el incumplimiento de pago de créditos personales.*

A través de datos históricos de clientes, se evalúan variables como **número de hijos, estado civil, nivel de ingresos y propósito del préstamo**, con el fin de identificar patrones de riesgo y mejorar los criterios de evaluación crediticia.

El proyecto aplica técnicas de **limpieza, transformación y análisis exploratorio de datos (EDA)** utilizando Python y pandas, siguiendo buenas prácticas de programación y documentación reproducible


🎯 **Objetivos**

*1- Analizar la relación entre **factores demográficos y familiares** (número de hijos, estado civil, estatus familiar) y el riesgo de incumplimiento.*

*2- Evaluar si el **nivel de ingresos** influye significativamente en la probabilidad de retraso en pagos.*

*3- Aplicar técnicas profesionales de **limpieza y preparación del dataset** (tratamiento de valores nulos, duplicados y normalización).*

*4- **Categorizar los propósitos** de crédito para mejorar la interpretación de los resultados.*

*5- Establecer un flujo de trabajo analítico claro, reproducible y bien documentado.*


⚙️ **Estructura del proyecto**

```Credit-Scoring/
│
├── data/
│   └── credit_scoring_eng.csv        # Dataset original con información de prestatarios
│
├── notebooks/
│   └── Proyecto_Puntuacion_Credito.ipynb   # Notebook principal con el análisis completo
│
├── scripts/
│   └── credit_scoring.py             # Script ejecutable del proyecto
│
├── requirements.txt                  # Librerías necesarias
└── README.md                         # Documentación del proyecto
```

🧹 **Etapas del análisis**
1️⃣ Carga y exploración inicial

*- Lectura del dataset con ``pandas.read_csv().`` *

*- Revisión general del contenido con ``.info()`` , ``.head()`` y ``.describe()``*

*- Identificación de valores nulos y tipos de datos inconsistentes.*

2️⃣ Limpieza y preparación de datos

*- Eliminación de duplicados.*

*- Corrección de valores ausentes en columnas críticas (days_employed, total_income).*

*- Normalización de texto (``education`` , ``family_status``).*

*- Agrupación de edades por rangos ( ``dob_years_group``).*

*- Creación de funciones personalizadas para imputación de valores nulos.*

3️⃣ Transformación y categorización

*-Estandarización de la columna ``purpose`` para clasificar los tipos de préstamo en categorías generales:*

``wedding, car_p, real_state, rw_home, education, other``

*- Conversión de datos negativos a positivos ``children``,  ``days_employed``.*

*- Revisión de coherencia en las columnas de ``gender`` e ``income_type``.*

5️⃣ **Resultados y conclusiones**

*- No se observan diferencias significativas en incumplimiento según número de hijos o estado civil.*

*- Los clientes con ingresos bajos presentan una mayor tasa de incumplimiento.*

*- Los préstamos con propósito educativo o de bienes raíces tienen más riesgo de retraso en el pago.*

*- El nivel de ingresos es una variable crítica en la evaluación de riesgo crediticio.*

🧪 **Cómo ejecutar el proyecto**

📘 *Opción 1: Desde el Notebook*

*1.Desplazate al direcotorio con ``cd notebooks``.*

*2. Abre el archivo **Proyecto_Puntuacion_Credito.ipynb** en **Jupyter Notebook**, **Colab** o **VSCode**.*

*3. Ejecuta las celdas en orden para reproducir el análisis paso a paso.*

🐍 **Opción 2: Desde consola (versión .py)**

Ejecuta el análisis directamente desde el script con:

*1.Desplazate al direcotorio con ``cd scripts``.*

``python credit-scoring.py``

💡 **Habilidades demostradas**

*-Limpieza avanzada de datos con pandas*

*-Manejo de valores ausentes y duplicados*

*-Creación de funciones para imputación de datos*

*-Agrupación y categorización de variables*

*-Análisis exploratorio (EDA) y generación de insights*

*-Documentación clara y profesional de procesos analíticos*

🧭 **Conclusiones y próximos pasos**

*-El análisis confirma que el **nivel de ingresos** es un predictor relevante del incumplimiento crediticio, mientras que variables familiares como el **estado civil** o **número de hijos** tienen un impacto limitado.*

*-Como evolución natural del proyecto, se propone implementar **modelos predictivos de scoring crediticio** mediante técnicas de Machine Learning (por ejemplo, ``Logistic Regression``, ``Random Forest``  ``o`` ``XGBoost`` ), para estimar el riesgo de impago con mayor precisión.*

🔗 Si deseas contribuir o mejorar el proyecto, puedes clonar el repositorio y participar en su desarrollo futuro.
