import numpy as np
import pandas as pd

def blend_csv(csv_paths, name):
    if len(csv_paths) < 2:
        print("Blending takes two or more csv files!")
        return
    
    # Read the first file
    df_blend = pd.read_csv(csv_paths[0], index_col=0)
    
    # Loop over all files and add them
    for csv_file in csv_paths[1:]:
        df = pd.read_csv(csv_file, index_col=0)
        df_blend = df_blend.add(df)
        
    # Divide by the number of files
    df_blend = df_blend.div(len(csv_paths))

    # Save the blend file
    df_blend.to_csv(name)
    print(df_blend.head(10))
    
blend_csv(['../output/submiM.csv', '../output/xgb_dimensions.csv'], '../output/average_ss.csv')