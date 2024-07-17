import numpy as np
import pandas as pd

def gcparser(mat):
    """
    Extracts essential data from a Matlab formatted GCMS object loaded
    by sio.loadmat and wrangles this into a pandas dataframe
    
    Parameters:
    mat (dict): Dictionary produced by loading a file using sio.loadmat

    Return:
    DataFrame: Total ion counts (TIC) arranged by samples (columns) and
               retention time (rows)
    
    """    
    data = np.transpose(mat['XTIC'])  #XTIC is a matix of measured values from GC-MS
    sample_names = mat['SAM']  # SAM contains the name of each sample
    sample_names = np.hstack(np.hstack(sample_names)).tolist()  # convert nested numpy arrays into a list
    RT = mat['RT']  # RT is retention time (in minutes)
    RT = np.hstack(np.hstack(RT)).tolist()  # convert nested numpy arrays into a list
    y = mat['CLASS']  #CLASS is the diagnosis of each sample (in this casse 1=control; 2=CD)
    y = np.hstack(y).tolist()  # convert nested numpy arrays into a list
    # put pieces back together in a pandas dataframe
    return pd.DataFrame(data, columns=sample_names, index=RT)