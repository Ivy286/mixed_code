def read_excel(excel_file_path, sheetname=0, header=0, column_name=[]):
    '''
    :param excel_file_path:
    :param sheetname: excel sheet name, default=0
    :param header: default 0
    :param column_name: column name
    :return:
    '''

    a = pd.read_excel(excel_file_path, sheetname=sheetname, header=header)

    # print a

    if column_name == []:
        raise ValueError("column_name list should have column name :", column_name)

    all_list = []
    for column in column_name:
        all_list.append([x for x in a[column]])

    return all_list
