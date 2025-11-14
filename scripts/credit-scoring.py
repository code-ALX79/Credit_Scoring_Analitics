
# Análisis del riesgo de incumplimiento de los prestatarios
# Este proyecto  esta diriguido diriguido a la division de prestamos de un banco. Con el objetivo de veriguar si el numero de hijos, estado civil, o estatus familia tienen alguna relacion con el incumplimiento del pago a tiempo de un prestamo. gracias a que el banco tienen algunos datos sobre el historial crediticio de algunos clientes, vamos a proceder a analizarlos.
# Esperando que sea de gran utilidad para la correcta calificasion de cada uno de los clientes, procederemos a realizar un analisis minucioso y limpio, para lograr excelentes resultados al momento de tomar esta desicion tan importante.

# Se el archivo de datos para mirar la información general.

import pandas as pd

credit_scoring = "credit_scoring_eng.csv"

credit_scoring = pd.read_csv('credit_scoring_eng.csv')

print()

print("se muestran las primeras filas del dataset")

print()

print(credit_scoring.head())

print()

print("se muestra la informacion general de los datos")

print()

print(credit_scoring.info())

print()

print("evaluacion de valores ausentes")

print()

print(credit_scoring.isna().sum())

credit_scoring[['days_employed', 'total_income']].isna().value_counts()

print()

print("Eliminacion de valores ausentes")

print()

print((credit_scoring[(credit_scoring['days_employed'].isnull()) & (
    credit_scoring['total_income'].isnull())]))

print()

print("Evaluarcion de columnas por separado")

print()

print(credit_scoring['days_employed'])

print()

print("Descripcion general  de los datos")

print()

print(credit_scoring.describe())

credit_scoring[credit_scoring['days_employed'].isna()].groupby('income_type')[
    'income_type'].count()

credit_scoring[credit_scoring['days_employed'].isna()].groupby(
    credit_scoring['education'])['education'].count()

credit_scoring[credit_scoring['days_employed'].isna()].groupby('family_status')[
    'family_status'].count()

credit_scoring[credit_scoring['days_employed'].isna()].groupby('children')[
    'children'].count()

credit_scoring[credit_scoring['days_employed'].isna()].groupby('gender')[
    'gender'].count()

print()

print("Descrpcion de los datos despues de eliminar valores ausentes en las columnas por separado")

print()

print(credit_scoring.describe())

print()

print("Se imprimes los tipos de datos con los que contamos en el nuevo dataframe")

print()

print(credit_scoring.dtypes)

credit_scoring['days_employed'].astype('float32')


credit_scoring['dob_years'].astype('float64')

print()

print("Se evalua columnas de años trabajados para agruparlas porsteriorimente")

print()

print(credit_scoring['dob_years'])


def dob_years_group(dob_years):
    if dob_years < 30:
        return '20-30'
    if dob_years < 40:
        return '30-39'
    if dob_years < 50:
        return '40-49'
    if dob_years < 60:
        return '50-59'
    else:
        return '+60'


print()

print("verificasion de la agrupacion despues de aplicar la funcion")

print()

print(credit_scoring['dob_years'].apply(dob_years_group).value_counts())

print()

print("Luego de realizar la agrupacion de los años trabajados, realizamos una union de los datos")

print()

credit_scoring['dob_years_group'] = credit_scoring['dob_years'].apply(
    dob_years_group)

print()

print("Luego imprimmos las primeras filas del nuevo datset para verificar como vamos con nuestros datos")

print()

print(credit_scoring.head())


credit_scoring['total_income'].isna().groupby(
    credit_scoring['dob_years_group']).mean()

credit_scoring.groupby([credit_scoring['dob_years_group'],
                       credit_scoring['education']])['total_income'].mean()

credit_scoring.groupby([credit_scoring['dob_years_group'],
                       credit_scoring['education']])['days_employed'].mean()

print()

print("Luego de realizar algunas agrupaciones de la columna de dias trabajados y notar que tienen relacion con la comlmna de educasion, proederemos ha eveluar esta columna  por individual")

print()

print(credit_scoring['education'])

print()

credit_scoring['education'] = credit_scoring['education'].str.lower()
credit_scoring['education']

print()

print("Luego de realizar las transformaciones pertinentes, procedemos con una decripcion de general de la columna 'children'")

print()

print(credit_scoring.children.describe())

credit_scoring.groupby('family_status')['children'].mean().sort_values()

credit_scoring.groupby('children')['children'].count()


credit_scoring['children'] = credit_scoring['children'].abs()


credit_scoring.groupby('children')['children'].count()

credit_scoring.loc[credit_scoring['children'] == 20]

credit_scoring['children'] = credit_scoring['children'].replace({20: 2})

credit_scoring.groupby('children')['children'].count()

print("Despues de realizar el analisis y realizar los metodos de remplazo conteo y evaluar metricas medias para aboradar la columna teniendo una vision mas clara de los datos, realizaremos otra descripcion de la misma columna")

print()

print(credit_scoring['children'].describe())

print("Una vez que vemos que la columna 'childern' tiene una buena descripcion, prodecemos con la columna 'days_employed', para verificar sus datos")

print()

print(credit_scoring['days_employed'])

credit_scoring['days_employed'] = abs(credit_scoring['days_employed'])

print("se muestra el resultado de la columna de dias trabajados despues de una  pequeña modificasion")

print()

credit_scoring['days_employed']

credit_scoring.loc[credit_scoring['days_employed'] > 36500,
                   'days_employed'] = credit_scoring.loc[credit_scoring['days_employed'] > 36500, 'days_employed']/24
print(credit_scoring['days_employed'])

print()

print("verificasion de la columna 'dob_years', para su analisis")

print()

print(credit_scoring['dob_years'])


def dob_years_group(dob_years):
    if dob_years < 30:
        return '20-30'
    if dob_years < 40:
        return '30-39'
    if dob_years < 50:
        return '40-49'
    if dob_years < 60:
        return '50-59'
    else:
        return '+60'


credit_scoring['dob_years'].apply(dob_years_group).value_counts()

credit_scoring['dob_years_group'] = credit_scoring['dob_years'].apply(
    dob_years_group)

print()

print("luego de aplicar una funcionde agrupe los años de los trabajadores en grupos, y unirla a nuestro dataframe, exponemos las filas y columnas del mismo para verificar esta quedando nuestra tabla")

print()

print(credit_scoring.head())


credit_scoring.groupby('dob_years_group')['days_employed'].mean()


def fill_by_group(row):
    if (row['days_employed'] > 0) and (row['days_employed'] <= 20):
        return 1346.485726
    elif (row['days_employed'] > 20) and (row['days_employed'] <= 30):
        return 2103.700591
    elif (row['days_employed'] > 30) and (row['days_employed'] <= 40):
        return 3065.967424
    elif (row['days_employed'] > 40) and (row['days_employed'] <= 50):
        return 7541.593571
    else:

        return row['days_employed']


credit_scoring.loc[credit_scoring['days_employed'].isna(
), 'days_employed'] = credit_scoring.loc[credit_scoring['days_employed'].isna()].apply(fill_by_group, axis=1)

print()

print("Se aplica otra funcion. Esta vez para agrupar la edad de los trabajadores, y se une la columna agrupada al dataframe mantenindo las modificasiones realizadas hasta el momento")

print()


print(credit_scoring.head())

print()

print("Se reliza una descripcion general de la columna de estatus de familia para analizar sus metricas  mas importantes")

print()

print(credit_scoring.family_status.describe())

credit_scoring['family_status'].unique()

credit_scoring['family_status']

credit_scoring.groupby('family_status')['family_status'].count()

print()

print("Luego de aplicar algunos metodos y agrupaciones para modificar la columna 'family_status', vamos a analizar la siguinete columna 'gender', con una descripcion general de la misma")

print()

print(credit_scoring.gender.describe())

credit_scoring['gender'].unique()

credit_scoring['gender'].value_counts(normalize=True)

credit_scoring = credit_scoring[credit_scoring['gender'] != 'XNA']

credit_scoring.groupby('gender')['gender'].count()

print()

print("Una vez que realizamos las modificasiones pertinentes en la columna que indica el genero del cliente.Procederemos a realizar el analisis a la columna 'income_type', que muestra el tipo de eingreso del cliente")

print()

print(credit_scoring.income_type.describe())

credit_scoring['income_type'].unique()

credit_scoring.groupby('income_type')['total_income'].mean().sort_values()

credit_scoring = credit_scoring[credit_scoring['income_type']
                                != 'paternity / maternity leave']
credit_scoring = credit_scoring[credit_scoring['income_type'] != 'unemployed']

print()

print("Despues de realizar los calculos pertinentes la columna 'income_type', diferenciarlas de los dias que no han trabajado, exponemos los valores unicos mofificados, para virificar las modificasiones")

print()

print(credit_scoring['income_type'].unique())

credit_scoring.groupby('income_type')['income_type'].count()

print()

print("Luego de realizar un conteo de la columna 'income_type', verificamos los valores duplicados en nuestro dataframe")

print()

print(credit_scoring.duplicated().sum())


credit_scoring.drop_duplicates()

credit_scoring = credit_scoring.drop_duplicates()

credit_scoring.duplicated().sum()

print()

print("Al realizar una eolimacion de duplicados, realizaremos un conteo de valores para verififcar que los valores sean los correctos ")

print()

print(credit_scoring.count())

credit_scoring.set_index('education_id')['education'].to_dict()

credit_scoring[['family_status_id', 'family_status']
               ].value_counts(sort=False).index

credit_scoring.groupby('income_type')['total_income'].median()


def ausent_sust(row):
    edid = row['education_id']
    total = row['total_income']
    if total == "":
        if edid == 0:
            x = 27571.0825
        if edid == 1:
            x = 24071.6695
        if edid == 2:
            x = 22815.1035
        if edid == 3:
            x = 79866.1030
        if edid == 4:
            x = 18962.3180
            row['total_income'] = x
    return row


credit_scoring['ausent_sust'] = credit_scoring.apply(ausent_sust, axis=1)[
    'total_income']

print()

print("Para reemplazar los valores ausentes de la tabla se crea una funcion llamada 'asent_sust()', que los reemplaza por un valor de media en la columna 'total_income'")

print()

print(credit_scoring['ausent_sust'])

print()

print("Realizamos una descripcion general de los datos hasta a hora con la columna 'asuent_sust', ya integrada")

print()

print(credit_scoring.describe())

credit_scoring.groupby('total_income')['days_employed'].mean().sort_values()


credit_scoring.groupby([credit_scoring['dob_years_group'],
                       credit_scoring['income_type']])['total_income'].mean()

print()

print("Como nuestra columna aun trenia incontingecias en algunos datos, se realiza una agrupacion de remplazo de valores en diferenters columnas y se reapite la descripcion para comprobar el resultado")

print()

print(credit_scoring.describe())


def rem_pm(credit_scoring):
    return credit_scoring['total_income'].fillna(credit_scoring.groupby(['dob_years_group', 'education'])['total_income'].transform('median'))


df_filled = rem_pm(credit_scoring)

print()

print("definimos una fucnion ,para reemplazar valores ausentes, y se imprimen las primeras filas para la comprobacion respectiva de sus columnas")

print()

print(credit_scoring.head())

print()

print("Se comprueba la sumatoria de valores ausentes")

print()

print(credit_scoring.isna().sum())

print()

print("Como comprobasion final, para este apartado de reemplazaremos nuestros valores nulos con nuestra mediana general del DataFrame. utilizando un bloque try-except. Para antelarnos a posibles errores.")

print()


try:
    def rem_pm(credit_scoring):
        return credit_scoring.fillna(credit_scoring.mean())
    df_filled = rem_pm(credit_scoring)
except:
    df_filled.fillna(0)


print(df_filled.reset_index().head(10))


df_filled.isna().sum()

# %%
credit_scoring.isna().sum()

print(credit_scoring.info())

credit_scoring.groupby('income_type')['days_employed'].median()

credit_scoring.groupby('days_employed')['dob_years'].mean().sort_values()

credit_scoring.groupby('dob_years_group')['days_employed'].mean()


def rem_pm(credit_scoring):
    return credit_scoring['days_employed'].fillna(credit_scoring.groupby(['dob_years_group', 'days_employed'])['days_employed'].transform('mean'))


df_sust_d = rem_pm(credit_scoring)

print(df_sust_d)


credit_scoring['income_type'].fillna(df_sust_d)


credit_scoring['income_type'].isna().sum()

print()

print("Remplazamos los valores ausentes de 'income_type' con los valores medios de la agrupacion entre las columnas del grupo de edad y los dias laborados, ya que el tipo de ingreso que un cliente tiene al mes, esta relacionado de manera creciente con su edad y sus dias laborados.")

print()


print(credit_scoring.dropna().isna().sum())

clasf1 = ['education', 'family_status', 'purpose', 'gender', 'income_type']

for column in clasf1:
    print()
    print(credit_scoring[column].value_counts())

clasf2 = ['children', 'days_employed', 'debt', 'total_income']

for column in clasf2:
    print()
    print(credit_scoring[column].describe())

    print()

print("Tambien vamos ha hacer una comprovacion de valores unicos para ver que tan relevantes son en mis columnas")

print()


clasf1 = ['education', 'family_status', 'purpose', 'gender', 'income_type']
for column in clasf1:
    print()
    print(credit_scoring[column].unique())

print()

print("Al denotar los valores unicos de cada una de las columnas que contienen variables categoricas, observamos una cantidad")

print()

print("exageradas de este tipo de valors en la columna 'prupose', vamos a explorar una solucion para esta columna.")

print()

clasf2 = ['children', 'days_employed', 'debt', 'total_income']
for column in clasf2:
    print()
    print(credit_scoring[column].unique())

print()

print("En cunato a los valores unicos de las columnas numericas, no tenemos una cantidad relevante de ellos en estas columnas asi que no vamos a clasificar en este tipo de variables")

print()

print("La clasificasion que haremos sera para variables categoricas, completando la columna 'prupose' que contiene mayor cantidad de valores unicos. Atravez de una funcion.")

print()


def category_rt(purpose):
    purpose = purpose.lower()

    if 'wedding' in purpose:
        return 'wedding'
    elif 'car' in purpose:
        return 'car_p'
    elif 'real estate' in purpose:
        return 'real_state'
    elif 'house' in purpose or 'housing' in purpose or 'property' in purpose:
        return 'rw_home'
    elif 'education' in purpose or 'educated' in purpose or 'university' in purpose:
        return 'education'
    else:
        return 'other'


print(credit_scoring['purpose'].apply(category_rt))

print()

print("Nuestra columna se ve bien, vamos a aplicarla en nuestros datos originales para evaluar el resultado de sus relaciones con otras columnas.")

print()

credit_scoring['category_rt'] = credit_scoring['purpose'].apply(category_rt)

print(credit_scoring.head())

credit_scoring.groupby('category_rt')['debt'].mean().sort_values()

credit_scoring.groupby('children')['debt'].median().sort_values()

print()

print(
    "Para este apartado haremos dos relaciones. La  la columna ['children'],para averiguar si tiene alguna relacion especifica entre el numero de hijos del cliente y el incumplimineto del pago a tiempo de su prestamo.")

print()

print(credit_scoring.groupby('family_status')['debt'].mean().sort_values())


print(credit_scoring.groupby('total_income')['debt'].mean().sort_values())

# **Conclusión**
#
# Despues de realcionar el nivel de ingresos de cada cliente ['total_income'] con el incumplimiento de un pago a tiempo ['debt']. Podriamos concluir los singuiente:
#
# *En esta columna si econtramos una coorrelacion entre los clientes que tienen un nivel de ingresos bajos y el incumplimineto de un pago a tiempo.
#
# *Los clientes que en promedio manejan un nivel de igresos bajos, si han tenido inconvenientes en el pago a tiempo de sus deudas, asi que el nivel de ingresos en este caso si representa un factor de riesgo para dar una buena calificasion a este tipo de clientes
#

print()

print("¿Cómo afecta el propósito del crédito a la tasa de incumplimiento?")

print()


credit_scoring.groupby(['category_rt'])['debt'].mean().sort_values()


# **Conclusión**
#
# Vamos a utilizar la columna ['category_rt'], para menejar resultados mas generales. Y en promedio, los clientes que tienen un  incumplimineto del pago a tiempo ['debt'] se ven  mayormente reflejado en el prestamos cuyo proposito comprende fines educativos o en la compra o venta de automoviles.
# # Conclusión general
#
# Evaluar correctamente los fatores que puedan influir en el incumplimieto de un pago a tiempo de un prestamo, no es tarea facil, y mas si se requiere un grado de exactitud  relevante para  dar una calificasion  especifica al cliente.
# Este dataframe ha representado un reto para my, sin embargo,se logro manejar de manera adecuada los valores ausentes,duplicados como tambien los valores unicos, tratando de no afectar en lo mas minimo los datos originales del dataframe, ulizando medianas y medias de los mismos datos para rellenar los valores ausentes y utilizando columnas diferentes en base a nuestras columnas originales, para no afectar los datos originales de las mismas, en cuanto a valores unicos, no se realizo muchas modificasiones ya que son importantes para nuestra tabla general.  Concluyendo lo siguiente:
#
# *Tanto el numero de hijos como el estatus de familia no tienen un porcentanje en promedio relevante que afecte al incumplimineto del pago de un prestamo a tiempo, ya que los promedios no reflejan que el cliente haya incumplido alguna vez un prestamo, idepentientemente si tiene o no tiene hijos o si tiene un alto estatus familiar.
#
#
# *La agrupacion de clientes por rango de edad, resulta muy conveniente al momento de averiguar el tipo de ingresosos mensuales que estos podrian tener.
#
#
# *En promedio,el nivel de ingresos de un cliente si afecta significativamente el icumplimineto del pago de un prestamo ya que aquellos clientes cuyo ingreso mensual es mas bajo  tienen  incumplidos al menos 1 pago a tiempo.
#
#
# *Aquellas personas cuyo proposito de prestamos son fines educativos o de compra y venta de bienes, tienen mayor probabilidad de incumplir en el pago de su prestamo ya que en promedio este tipo de propositos tienen algun incumplimineto de pago a tiempo en su prestamo.
#
#
# *Para finalizar se espera que este analisis se tome muy en cuenta al momento de calificar al cliente,segun my analisis solamente el nivel de ingresos de cada cliente representa una relevancia en el incumplimineto de un pago a tiempo.
