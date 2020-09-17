
def read_yaml():
    import yaml
    f_name = "parameters.yaml"
    with open(f_name, "r") as f:
        prm_yaml = yaml.load(f, Loader=yaml.FullLoader)
    
    prm_E = prm_yaml["Material parameters"]["E"]
    assert prm_E["unit"] == "MPa"
    E = prm_E["value"]
    print(f"Read parameter E from {f_name} as {E} with type {type(E)}")

def read_txt(prm_name):
    f_name = "parameters.txt"
    with open(f_name, "r") as f:
        for line in f:
            name, value = line.split("=")
            if name == prm_name:
                return float(value)
            



def read_excel(f_name, prm_name, row_offset=0, col_offset=1):
    """ 
    Finds the location (row, col) of the string `prm_name` in the `f_name`
    and returns the entry left of it.
    
    f_name:
        name of the excel file
        
    prm_name:
        string to search for
        
    row_offset, col_offset:
        location of the value of interest relative to the `prm_name` location.
        row_offset = 1, col_offset = 0: returns the entry below it
        row_offset =-1, col_offset = 1: returns the entry above left
        

    """

    import pandas as pd
    import numpy as np
    df = pd.read_excel(f_name, header=2)
    numpy_df = df.astype(str).to_numpy()
    index = np.where(numpy_df == prm_name)
    
    row = index[0][0]
    col = index[1][0]
   
    assert df.iloc[row, col] == prm_name 
    
    return float(df.iloc[row, col+1])


if __name__ == "__main__":
    read_yaml()
    
    print(read_txt("P1"))
    print(read_txt("P2"))
    print(read_excel("parameters.xlsx", "P2"))
