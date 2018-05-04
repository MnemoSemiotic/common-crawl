import matplotlib.pyplot as plt

'''
Generating a square wordcloud from a dataframe.
adapted from https://github.com/amueller/word_cloud/
'''

from os import path
from wordcloud import WordCloud

def create_wordcloud_from_df(df):
    '''
    INPUT: pandas.core.series.Series

    OUTPUT: returns NONE
          : Calls create_wordcloud and generates text from
            pandas series
    '''

    list_of_strings = [str(i) for i in df]

    create_wordcloud(' '.join(list_of_strings))

def create_wordcloud(text):
    '''
    INPUT: string

    OUTPUT: returns NONE
          : saves a figure of a wordcloud in working directory
    '''
    wordcloud = WordCloud().generate(text)

    dpi=300

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    # lower max_font_size
    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure(figsize=(12, 8),dpi=dpi, facecolor='w', edgecolor='k')
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    # plt.show()
    plt.savefig('wordmap_temp.png', dpi=dpi)

if __name__ == '__main__':
    pass
    #
    # d = path.dirname('/Users/tbot/Dropbox/galvanize/a-smarter-flashcard/data/')
    #
    # # Read the whole text.
    # text = open(path.join(d, 'ds_flashcards_2.txt')).read()
    # create_wordcloud(text)
