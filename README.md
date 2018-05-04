--------------------------------------------------------

# Common Crawl
  * non-profit using crawlers to index the web

--------------------------------------------------------
# 3 File Formats
  * WARC (Web Archive) Full File Format
    *
  * WAT Files : Metadata
  * WET Files: extracted plaintext data

--------------------------------------------------------

# Naming Conventions of Dumps
  * http://commoncrawl.org/2018/05/april-2018-crawl-archive-now-available/
  * CC-MAIN-<Year>-<dump#> : these are happening monthly

--------------------------------------------------------

# Data
  * Chose CC-MAIN-2018-17, April 2018
    * Getting the first segment of this data
      * For current purposes, assuming random-enough sample from the head of this data
  * In all languages
    * Keeping all records BUT removing all non-alpha characters
      * Export to new corpus csv in order to re-import
      * Pipeline with tokenizers, stemming
      * Many documents are just a single link
  * There's lots of porn on the internet

--------------------------------------------------------
# Common Crawl WARC File format
  * WARC Header Info
    * Crawler Data
  * HTTP Response Info
    * Standard
  * HTML (For Successful Responses)

![warc format](images/00_warc-format.png)
--------------------------------------------------------
# How the Crawler Works, ie "How Random is Our Sample?"
  * Breadth-first traversal of multi-child tree
   * Within 4 links of homepages of top 40 million domains
     * Consider there are ~1.8 billion sites active websites

![Breadth](images/breadth-first.png)

--------------------------------------------------------
# Our Current Corpus

![current corpus word map](images/word_map.png)
 * Thoughts:
   * Seems that our subsample is not very random
     * Probably pulled links from a financial report or link farm
   * We should random sample from multiple Segments of the Data instead of just the first segment

![data_rows.png](images/data_rows.png)
--------------------------------------------------------
# Our Plan: Topic Modeling
  * Using WARC files
    * Drop all rows that are not English
      * `<html lang="en">`
    * Preprocess Text
      * remove HTML
      * Stem/Lemmatize
    * Term Frequency (LDA "should" take TF Matrix)
      * However, TF-IDF is often used
  * Apply basic LDA model to TF matrix
  * Attempting move to AWS

--------------------------------------------------------
# Our Reality
  * Using WET files
    * Trouble extracting just HTML Document from HTTP response in WARC
    * Dropping all non-alpha characters using regex
      * Exporting each document to .csv file to read into Spark Dataframe
    * HTML already stripped
    * Using regex to remove all non alpha characters
      * preserves some letters with accents
      * thus latin character languages are included
  * Run LDA in Spark locally on first segment
    * 5 topics
    * 1-grams, TF matrix as input
    * token length > 3
    * English, Spanish and French stop words
  * Attempting Spark.ML LDA on AWS EMR (Elastic Map Reduce)
--------------------------------------------------------
# A little about LDA (Latent Dirichlet Allocation)
  * Model sees words in documents
  * Documents are represented as a distribution of topics
  * Topics are considered to be distributions of words
  * Alpha and Beta priors are taken from Dirichlet distribution

![lda image](images/lda.png)
--------------------------------------------------------
# Results
  * Working local model



--------------------------------------------------------
# Future Considerations for More Robust Model
  * During text pre-processing, drop all documents less than a certain number of words
  * Use CDX Server API (https://github.com/webrecorder/pywb/wiki/CDX-Server-API)
  * Better to split out english language based on metatags in the full WARC files
    * OR, use language detection on documents and separate into separate corpora for analysis
  * If subsampling, random sample from each Segment of a given Crawl dump
