from rdkit import DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit import Chem
import pandas as pd
import matplotlib.pyplot as plt
import traceback
import time


def tanimoto_similarity(smi_1, smi_2):
    ms = [Chem.MolFromSmiles(smi_1), Chem.MolFromSmiles(smi_2)]
    fps = [FingerprintMols.FingerprintMol(x) for x in ms]
    similarity = DataStructs.FingerprintSimilarity(fps[0], fps[1])
    return similarity


def write_similarity(file_path, write_path):
    df = pd.read_csv(file_path)
    smi_list = df['smiles'].tolist()
    id_list = df['id_new'].tolist()
    pic_list = df['PIC50_RET wild'].tolist()

    print(len(smi_list))
    similarity_list = []
    id1_list = []
    id2_list = []
    pic1_list = []
    pic2_list = []

    n = 0
    for id1, smi1, pic1 in zip(id_list, smi_list, pic_list):
        n = n + 1
        list1 = smi_list[n:]
        list2 = id_list[n:]
        list3 = pic_list[n:]
        print(len(list1))
        for id2, smi2, pic2 in zip(list2, list1, list3):
            s = tanimoto_similarity(smi1, smi2)
            similarity_list.append(s)
            id1_list.append(id1)
            id2_list.append(id2)
            pic1_list.append(pic1)
            pic2_list.append(pic2)
    df1 = pd.DataFrame({'id1_list': id1_list, 'pic1': pic1_list, 'id2_list': id2_list, 'pic2': pic2_list,
                        'similarity': similarity_list})
    # df = pd.concat([df, df1], axis=1)
    df1.to_csv(write_path, index=False)


def del_smi(simi_csv, final_csv):
    df = pd.read_csv(simi_csv)
    df_new = df[df['smilarity'] <= 0.6]
    print(len(df_new))

    id1 = df_new['id1_list'].tolist()
    id2 = df_new['id2_list'].tolist()
    pic1 = df_new['pic1'].tolist()
    pic2 = df_new['pic2'].tolist()
    simi = df_new['smilarity'].tolist()

    pic_new = []
    id_new = []
    simi_new = []

    for one, two, three, four, five in zip(id1, id2, pic1, pic2, simi):

        if pic1 >= pic2:
            id_new.append(one)
            pic_new.append(three)
        else:
            id_new.append(two)
            pic_new.append(four)
        simi_new.append(five)

    df_final = pd.DataFrame({'id_new': id_new, 'pic': pic_new, 'similarity': simi_new})
    df_final.drop_duplicates('id_new', 'first', inplace=True)
    print(len(df_final))
    df_final.to_csv(final_csv, index=False)


def del_high_similarity(simi_csv, write_csv):
    df = pd.read_csv(simi_csv)

    print(len(df))

    id1 = df['id1_list'].tolist()
    id2 = df['id2_list'].tolist()
    pic1 = df['pic1'].tolist()
    pic2 = df['pic2'].tolist()
    simi = df['smilarity'].tolist()

    pic_new = []
    id_new = []
    simi_new = []

    for one, two, three, four, five in zip(id1, id2, pic1, pic2, simi):
        if five >= 0.9:
            if one not in id_new and two not in id_new:
                if three >= four:
                    id_new.append(one)
                    pic_new.append(three)
                    simi_new.append(five)
        else:
            if one not in id_new and two not in id_new:
                id_new.append(one)
                id_new.append(two)
                pic_new.append(three)
                pic_new.append(four)
                simi_new.append(five)
                simi_new.append(five)

    print(len(id_new), len(pic_new))
    df_final = pd.DataFrame({'id_new': id_new, 'pic': pic_new, 'similarity': simi_new})
    df_final.drop_duplicates('id_new', 'first', inplace=True)
    print(len(df_final))
    df_final.to_csv(write_csv, index=False)


def del_high_similarity1(simi_csv):
    df = pd.read_csv(simi_csv)
    print('the length of all_id is ', len(df))

    id1 = df['id1_list'].tolist()
    # id2 = df['id2_list'].tolist()
    simi = df['similarity'].tolist()

    id_new = list(set(id1))
    print('the length of id_new is ', len(id_new))
    id_del = []

    for one in id_new:
        for id_name, val in zip(id1, simi):
            if id_name == one:
                if val > 0.96 and id_name not in id_del:
                    id_del.append(one)

    id_del_new = list(set(id_del))
    print('the length of id need to delete: ', len(id_del_new))
    id_select = [i for i in id_new if i not in id_del_new]
    print('the length of id need to select: ', len(id_select))

    with open('id_del_0.96.csv', 'w') as f:
        f.write('Title,\n')
        for i in id_del_new:
            f.write(str(i) + '\n')

    return id_select, id_del_new


def write_final_csv(id_del_csv, simi_csv, write_csv):
    df = pd.read_csv(id_del_csv)
    id_del_list = pd.read_csv(id_del_csv)['Title'].tolist()
    df = pd.read_csv(simi_csv)
    id1 = df['id1_list'].tolist()
    id2 = df['id2_list'].tolist()
    simi = df['similarity'].tolist()

    with open(write_csv, 'w') as f:
        f.write('Title,similarity,\n')
        print(len(id1), len(id2))

        for one, two, five in zip(id1, id2, simi):
            if one not in id_del_list and two not in id_del_list:
                a = str(one) + ',' + str(five) + ',\n'
                f.write(a)
            else:
                pass


def plot_hist(input_csv):
    df = pd.read_csv(input_csv)
    sim = df['similarity'].tolist()
    plt.hist(sim, bins=2000)
    fontdict = {'family': 'Times New Roman', 'size': 12}
    plt.xlabel('Tanimoto Similarity', fontdict)
    plt.ylabel('Frequence', fontdict)
    plt.xticks(fontproperties='Times New Roman', size=10)
    plt.yticks(fontproperties='Times New Roman', size=10)
    # plt.xlim(0.42, 0.95)
    plt.title('0.96_all Remaining', fontdict)
    plt.grid(ls='--')
    plt.show()


def convert_normal_smi(smi2_list):
    smi2_list_new = []
    for smi2 in smi2_list:
        try:
            smi2_new = Chem.MolToSmiles(Chem.MolFromSmiles(smi2))
            # print(smi2_new)
            smi2_list.append(smi2_new)
        except Exception:
            print(traceback.format_exc())
    return smi2_list


def read_smis_file(file1):
    df = pd.read_csv(file1)
    smi_list = df.iloc[:10, 0].tolist()
    id_list = df.iloc[:10, 1].tolist()
    print(smi_list[:5])
    return smi_list


if __name__ == '__main__':
    time_start = time.time()
    file_path = './all_ret_inhibitors_data.csv'
    similarity_patent_path = 'tanimoto_similarity_patent.csv'
    similarity_all_path = './tanimoto_similarity_all.csv'
    id_del_path = 'id_del_0.96.csv'
    final_path = './final_0.96_allData.csv'

    # write_similarity(file_path, similarity_path)

    # id_select_list, id_del_list = del_high_similarity1(similarity_all_path)

    # write_final_csv(id_del_path, similarity_all_path, final_path)

    '''
    folder_550w = '/data/RET_pasterad_fd_550w_zl_66w'
    file_32w = '/data/RET_pasterad_fd_550w_zl_66w/ret_snd_32w.csv'
    smiles1 = 'C1NCCO[C@H]1COc(c2)cc(c(n23)c(cn3)C#N)-c4ncc(nc4)N(C[C@@H]56)C[C@@H](C6)N5Cc7ccc(nc7)OC'
    smi1_new = Chem.MolToSmiles(Chem.MolFromSmiles(smiles1))

    smi2_list = read_smis_file(file_32w)
    smi2_list_new = convert_normal_smi(smi2_list)
    similarity_list = [tanimoto_similarity(smiles1, smi2) for smi2 in smi2_list_new]
    df_simi = pd.DataFrame({'Smiles': smi2_list_new, 'similarity': similarity_list})
    df_simi.to_csv('32w_loxo292_similarity.csv', index=False)
    print(len(similarity_list))
    plt.hist(similarity_list, bins=200)
    plt.show()
    '''

    time_end = time.time()
    print('all cost time is: ', (time_end - time_start)/60.0, ' min')
    plot_hist(final_path)
