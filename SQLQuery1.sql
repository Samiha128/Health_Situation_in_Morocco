USE health; -- S�lectionnez votre base de donn�es

-- Cr�er un nouveau sch�ma appel� 'table'
CREATE SCHEMA [table];
-- D�placer une table sp�cifique vers le nouveau sch�ma 'table'
ALTER SCHEMA [table] TRANSFER dbo.calcule;
ALTER SCHEMA [table] TRANSFER dbo.indicateur_sur_la_repartition_des_secteur;
ALTER SCHEMA [table] TRANSFER dbo.Effectif_des_assures_actifs;
ALTER SCHEMA [table] TRANSFER dbo.Health_in_Morocco_wikipedia;
ALTER SCHEMA [table] TRANSFER dbo.indic_soc_sante_mef_2014_3_MEF;
ALTER SCHEMA [table] TRANSFER dbo.indicateur_sur_la_repartition_des_affilies;
ALTER SCHEMA [table] TRANSFER dbo.indicateurs_sur_les_declarations;
ALTER SCHEMA [table] TRANSFER dbo.infrastructures_privees;
ALTER SCHEMA [table] TRANSFER dbo.offre_de_soins_privees_ms_2013;
ALTER SCHEMA [table] TRANSFER dbo.stastique;
ALTER SCHEMA [table] TRANSFER dbo.Suicide_deaths;
USE health;

-- V�rifiez l'existence des tables dans le sch�ma 'dbo'
SELECT TABLE_SCHEMA, TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'table';
