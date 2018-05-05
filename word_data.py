import pyspark as ps
from pyspark.ml.feature import RegexTokenizer, Tokenizer
from pyspark.ml.feature import CountVectorizer
from pyspark.ml.clustering import LDA
from pyspark.ml.feature import StopWordsRemover
from nltk.corpus import stopwords

if __name__ == '__main__':
    spark = ps.sql.SparkSession.builder.master("local")\
                                    .appName("case-study")\
                                    .getOrCreate()

    word = spark.read.csv('corpus.csv')
    word = word.selectExpr('_c0 as doc','_c1 as text')

    word.registerTempTable('word')
    word_trunc = spark.sql('''
                            SELECT text
                            FROM word
                            WHERE text is not null
                            ''')

    tokenizer = RegexTokenizer(inputCol='text', outputCol='tokens', pattern='\\W',minTokenLength=4)
    token = tokenizer.transform(word_trunc)
    sw = list(stopwords.words(['english','french','spanish']))
    swr = StopWordsRemover(inputCol='tokens',outputCol='stop',stopWords=sw)
    word_sw = swr.transform(token)
    word_sw.show(1)
    cv = CountVectorizer(inputCol='stop',vocabSize=5000,minDF=10,outputCol='features')
    cv_model = cv.fit(word_sw)
    word_cv = cv_model.transform(word_sw)

    lda = LDA(k=5,optimizer='em')

    lda_model = lda.fit(word_cv)
    lda_model.describeTopics().show()
