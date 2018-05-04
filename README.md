# common-crawl
Looking at the Common Crawl Web Corpus

--------------------------------------------------------

# Common Crawl
  * non-profit using crawlers to index the web

--------------------------------------------------------

# WARC (Web Archive) Full File Format
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
      * Don't know the crawl method specifics yet (ie random selection of next link in the recursion/document dump?),
        * letting this stand for now
  * In all languages
    * Intend to apply english vocabulary to strip non-English (for this)
      * In Pipeline with tokenizers, lemmatizers

--------------------------------------------------------

# Our Plan: Topic Modeling
  * Using WARC files
    * Drop all rows that are not English
      * `<html lang="en">`
    * Preprocess Text
      * remove HTML
      * Stem/Lemmatize
    * Term Frequency (LDA "should" take TF Matrix)
  * Apply basic LDA model to TF matrix
  * Move to AWS

--------------------------------------------------------

# Future Considerations for More Robust Model
  * Use CDX Server API (https://github.com/webrecorder/pywb/wiki/CDX-Server-API)
  * Better to split out english language based on metatags in the full WARC files
  *
