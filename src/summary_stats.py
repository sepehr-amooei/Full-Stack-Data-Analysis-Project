def print_basic_info(df):
    print(f"info() output: \n ")
    df.info()
    print("\n")
    print(f"describe() output: \n{df.describe()} \n")
    print(f"number of nulls in each column: \n{df.isnull().sum()} \n")
    print(f"columns data types: \n{df.dtypes} \n")
