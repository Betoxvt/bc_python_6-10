import vaex

arquivo_txt = "data/measurements.txt"
arquivo_hdf5 = "data/measurements.txt.hdf5"


def process_data(df):
    df_agrupado = df.groupby("estacao").agg({"temperatura": ["min", "max", "mean"]})
    df_agrupado["temperatura_mean"] = df_agrupado["temperatura_mean"].round(1)
    df_final = df_agrupado.sort("estacao")
    return df_final


if __name__ == "__main__":
    import time

    print("\033[32mIniciando o processamento do arquivo.\033[m")
    start_time = time.time()
    vaex.from_csv(
        arquivo_txt, names=["estacao", "temperatura"], delimiter=";", convert=True
    )
    df = vaex.open(arquivo_hdf5)
    df_final = process_data(df)
    took = time.time() - start_time
    print(df_final.head())
    print(f"Processing took: \033[32m{took:.2f}\033[m sec")
