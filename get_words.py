import re
import csv
import time

from collections import Counter

from pyspark.sql.types import StructType, StructField, StringType, LongType

from sparkcc import CCSparkJob


class DocWordsJob(CCSparkJob):
    """ Word count (frequency list) from texts in Common Crawl WET files"""

    name = "DocWords"

    # output is <URI, word list>
    output_schema = StructType([
        StructField("key", StringType(), True),
        StructField("val", StringType(), True)
    ])

    # simple Unicode-aware tokenization
    # (not suitable for CJK languages)
    #Change REGEX here to include non-alpha characters
    word_pattern = re.compile('[a-zA-Z]+', re.UNICODE)
    # html_tag_pattern = re.compile(b'(?:<html lang=)(.{3})')

    @staticmethod
    def reduce_by_key_func(a, b):
        # sum values of tuple <term_frequency, document_frequency>
        return ((a[0] + b[0]), (a[1] + b[1]))

    def process_record(self, record):
        if not self.is_wet_text_record(record):
            return
        uri = record.rec_headers.get_header('WARC-Target-URI')
        data = record.content_stream().read().decode('utf-8')
        word_list = WordCountJob.word_pattern.findall(data)
        if not word_list:
            return
        yield uri, word_list

if __name__ == '__main__':
    job = DocWordsJob()
    job.run()
