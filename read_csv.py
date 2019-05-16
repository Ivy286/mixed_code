import pandas as pd

def csv_reader(csv_file, headers=[], sep=','):
    """
    inputs
    ------
    csv_file: csv file
    headers: field names
    sep: ',' or ' ', and so on

    return
    ------
    tuple of lists
    """
    df = pd.read_csv(csv_file, sep=sep)
    data = []
    for h in headers:
        try:
            item = df[h].values.tolist()
        except KeyError:
            item = []
        data.append(item)

    return tuple(data)
