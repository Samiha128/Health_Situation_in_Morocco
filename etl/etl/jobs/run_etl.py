from dagster import job, op

from etl.ops.etl import extract_dim_product_category, load_dim_product_category


from dagster import job

@job
def etl():
    extract_results = extract_dim_product_category()
    load_dim_product_category(extract_results[0], extract_results[1])
    load_dim_product_category(extract_results[2], extract_results[3])
    load_dim_product_category(extract_results[4], extract_results[5])
    load_dim_product_category(extract_results[6], extract_results[7])
    load_dim_product_category(extract_results[8], extract_results[9])
    load_dim_product_category(extract_results[10], extract_results[11])
    load_dim_product_category(extract_results[12], extract_results[13])
    load_dim_product_category(extract_results[14], extract_results[15])
    load_dim_product_category(extract_results[16], extract_results[17])
    load_dim_product_category(extract_results[18], extract_results[19])
    load_dim_product_category(extract_results[20], extract_results[21])



