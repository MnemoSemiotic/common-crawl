import pyspark as ps
from pyspark.ml.feature import RegexTokenizer, Tokenizer
from pyspark.ml.feature import CountVectorizer
from pyspark.ml.clustering import LDA
from pyspark.ml.feature import StopWordsRemover
from nltk.corpus import stopwords
from pyspark.ml import Pipeline

def generate_pipeline(lda_k=5,vocab=5000,min_token=4):
    tokenizer = RegexTokenizer(inputCol='val', outputCol='tokens', pattern='\\W',minTokenLength=min_token)
    sw = list(stopwords.words(['english','french','spanish']))
    swr = StopWordsRemover(inputCol='tokens',outputCol='stop',stopWords=sw)
    cv = CountVectorizer(inputCol='stop',vocabSize=vocab,minDF=10,outputCol='features')
    lda = LDA(k=lda_k,optimizer='em')
    pipeline = Pipeline(stages=[tokenizer,swr,cv,lda])
    return pipeline

def get_topic_words(pipeline):
    topic = pipeline.stages[-1].describeTopics()
    topic.registerTempTable('topic')
    vocab = pipeline.stages[-2].vocabulary
    topic_dict=dict()
    for x in spark.sql('select topic,termIndices from topics').collect():
        for y in x['termIndices']:
            topic_dict.setdefault(x['topic'],[]).append(vocab[y])
    return topic_dict

if __name__ == '__main__':
    spark = ps.sql.SparkSession.builder.master("local")\
                                    .appName("case-study")\
                                    .getOrCreate()

    word = spark.read.parquet('spark-warehouse/test/')
    word.registerTempTable('word')

    word_trimmed = spark.sql('''SELECT *
                                FROM test
                                WHERE size(split(val,",")) > 10
                                ''')

    pipeline = generate_pipeline()
    pipeline.fit(word_trimmed)

    # lda_model.describeTopics().show()
