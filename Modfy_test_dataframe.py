"""The data is imprase from a url"""
import pandas as pd
URL = 'https://data.mo.gov/api/views/vpge-tj3s/rows.csv?accessType=DOWNLOAD'
DATAFRAME = pd.read_csv(URL)

def test_dataframe(DATAFRAME):
    """Starting testing"""
    #check value type in each column is the same
    for i in range(DATAFRAME.shape[1]):
        value_type = type(DATAFRAME.iloc[0, i])
        air = 0
        for j in range(len(DATAFRAME)):
            if isinstance(DATAFRAME.iloc[j, i]) == value_type:
                air += 1
        if air != len(DATAFRAME):
            print('Have '+str(len(DATAFRAME)-air)+' different value type in '+DATAFRAME.columns[i])
        else:
            print('No different value type in '+DATAFRAME.columns[i])

    #check if there is NaN value
    nan = DATAFRAME[DATAFRAME['Location 1'].isnull()]
    index = list(nan.index)
    if index is True:
        print('DataFrame has no NaN')
    else:
        print('DataFrame has NaN')

    #check there is at least on row in dataframe
    DATAFRAME.empty = True
    if DATAFRAME.empty is True:
        print('DataFrame is empty')
    else:
        print('DataFrame is not empty')

test_dataframe(DATAFRAME)
