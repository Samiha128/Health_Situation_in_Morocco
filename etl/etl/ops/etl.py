from dagster import Out, Output, op
from dagster import op
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table

@op(out={"file_path_1": Out(str), "table_name_1": Out(str),
         "file_path_2": Out(str), "table_name_2": Out(str),
         "file_path_3": Out(str), "table_name_3": Out(str),
         "file_path_4": Out(str), "table_name_4": Out(str),
         "file_path_5": Out(str), "table_name_5": Out(str),
         "file_path_6": Out(str), "table_name_6": Out(str),
         "file_path_7": Out(str), "table_name_7": Out(str),
         "file_path_8": Out(str), "table_name_8": Out(str),
         "file_path_9": Out(str), "table_name_9": Out(str),
         "file_path_10": Out(str), "table_name_10": Out(str),
         "file_path_11": Out(str), "table_name_11": Out(str)})
def extract_dim_product_category(context):
    try:
        files_to_load = [
            ('C:\\Users\\hp\\Desktop\\health\\data\\Suicide deaths.csv', 'Suicide_deaths'),
            ('C:\\Users\\hp\\Desktop\\health\\data\\calcule.csv', 'calcule'),
            ('C:\\Users\\hp\\Desktop\\health\\data\\\Effectif des assurés actifs par Tranche d\'âge.csv', 'Effectif_des_assures_actifs'),
            ('C:\\Users\\hp\\Desktop\\health\\data\\Health in Morocco_wikipedia.csv', 'Health_in_Morocco_wikipedia'),
            ('C:\\Users\\hp\\Desktop\\health\\data\\Indicateurs sur les déclarations de salaires CNSS effectuées au titre de l\'année 2020 ( cnss).csv', 'Indicateurs_sur_les_declarations'),
            ('C:\\Users\\hp\\Desktop\\health\\data\\indicateur-sur-la-repartition-des-affilies-par-region.csv', 'indicateur_sur_la_repartition_des_affilies'),
            ('C:\\Users\\hp\\Desktop\\health\\data\\indicateur-sur-la-repartition-des-affilies-par-secteur-dactivite cnss.csv', 'indicateur_sur_la_repartition_des_secteur'),
            ('C:\\Users\\hp\\Desktop\\health\\data\\indic-soc-sante-mef-2014-3 MEF.csv', 'indic_soc_sante_mef_2014_3_MEF'),
            ('C:\\Users\\hp\\Desktop\\health\\data\\infrastructures-privees-2022.csv', 'infrastructures_privees'),
            ('C:\\Users\\hp\\Desktop\\health\\data\\offre-de-soins-privees-ms-2013.csv', 'offre_de_soins_privees_ms_2013'),
            ('C:\\Users\\hp\\Desktop\\health\\data\\stastique.csv', 'stastique'),
        ]

        for i, (file_path, table_name) in enumerate(files_to_load, start=1):
            context.log.info(f"Chargement des données à partir de {file_path} pour la table {table_name}")
            yield Output(file_path, f"file_path_{i}")
            yield Output(table_name, f"table_name_{i}")

    except Exception as e:
        context.log.error(f"Erreur lors de l'extraction des données : {str(e)}")
        raise




@op
def load_dim_product_category(context, file_path: str, table_name: str):
    try:
        # Connexion à la base de données SQL Server
        server_name = 'DESKTOP-EOHPBP3\\PROJECT'
        database_name = 'health'
        connection_string = f'mssql+pyodbc://{server_name}/{database_name}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'

        engine = create_engine(connection_string)
        conn = engine.connect()

        # Charger le fichier CSV en utilisant pandas
        df = pd.read_csv(file_path, encoding='utf-8-sig')

        # Créer la table dans SQL Server si elle n'existe pas déjà
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)

        context.log.info(f"Les données ont été importées avec succès dans la table {table_name}.")

        # Fermer la connexion
        conn.close()

    except Exception as e:
        context.log.error(f"Erreur lors du chargement des données dans SQL Server : {str(e)}")
        raise

