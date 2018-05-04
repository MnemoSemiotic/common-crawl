import re
import pandas as pd
from nltk.stem.snowball import SnowballStemmer


def read_cards(file_path):
    '''
    INPUT: file_path with string of file holding flash card data

    OUTPUT: dataframe representing values read from file
    '''
    df = pd.read_csv(file_path, sep='\t', names=['question','answer'])
    return df

def clean_dataframe(df):
    df2 = df.copy()

    df2 = df2.applymap(lambda x: stemmer(strip_anki(strip_html(x))) if type(x) is str else ' ')

    print(df2['answer'][79])

    return df2

def strip_html(raw_html):
    '''
    INPUT:   string, potentially with html

    RETURNS: string of the text with html removed
    '''
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', raw_html)
    cl_1 = cleantext.replace('&nbsp;',' ')
    cl_2 = cl_1.replace('&gt;','>')
    cl_3 = cl_2.replace('&lt;','<')
    cl_4 = cl_3.replace('?',' ')
    return cl_4

# def strip_latex(text):
#     latex_remove = ltx.get_latex_dict()
#     latex_keys = latex_remove.keys()
#     output = text
#
#     for string in latex_remove:
#         output = output.replace(string, ' ')
#
#     return output

def strip_anki(text):
    cl_1 = text.replace('c1::', '')
    cl_2 = text.replace('c2::', '')
    cl_3 = text.replace('c3::', '')
    cl_4 = text.replace('c4::', '')
    cl_5 = text.replace('c5::', '')
    cl_6 = text.replace('c6::', '')
    return cl_6

def collapse_df(df):
    # df_collapsed =  df['question'] + ' ' + str(df['answer'])
    df_collapsed = df.copy()

    df_collapsed["record"] = df["question"].map(str) + ' ' + df["answer"].map(str)
    return df_collapsed['record']

def stemmer(text):
    snowball = SnowballStemmer('english')
    text_split = text.split()
    text_snowball = [snowball.stem(word) for word in text_split]
    return_text = ' '.join(text_snowball)
    return return_text



''' ######################################################################## '''
if __name__ == '__main__':

    data = 'data/ds_flashcards_2.txt'
    df = read_cards(data)

    df_clean = clean_dataframe(df)

    # df_clean.tail()

    df_collapsed = collapse_df(df_clean)

    # df_collapsed.str.contains('ttt').nunique()
    df_collapsed[79]

    df_collapsed.isnull().sum()
    ## There are 110 NaN values after cleaning

    # Create series as mask for nan values
    nulls = pd.isnull(df_collapsed)

    nulls[nulls == True].index[0]

    df_collapsed[79]
    df['question'][79]
