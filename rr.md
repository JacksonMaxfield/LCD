# Registered Report

## Questions

1.  What is the main question being addressed in your study?

    How do data science students and workers (data scientists, data engineers, machine learning engineers and scientists, etc.) label a dataset controversial and how do they use such controversial datasets in practice?

    There is a concept in software engineering of the "sticky dependency" or "sticky framework" which is roughly, once you adopt a technology and build with it, it becomes hard to rip it out. We have seen a rising trend in machine learning to adopt and use large datasets _quickly_. COCO (common objects in context) and Flickr datasets are commonly used as benchmark sets and as the starting points for many production machine learning models. However, while COCO has problems it is largely considered "uncontroversial," while the Flickr dataset is considered controversial and is falling out of fashion. But it is in this "falling out of fashion" that relates to the idea of a typical "sticky dependency" -- in other words, "how long does it take for a dataset to be removed from typical usage after being deemed as controversial?

    _Note: while I am labelling the Flickr dataset controversial, part of the study is to understand what the average data science student or worker considers controversial._

2.  Describe the key independent and dependent variable(s), specifying how they will be measured.

    - Independent Variables
      (general demographics information of each survey respondent)

      - Respondent age: integer
      - Respondent gender: categorical
      - Respondent years of education: binned / categorical
      - Respondent years of experience: binned / categorical
      - Respondent expertise (data scientists vs data engineer for example): categorical

    - Dependent Variables
      (does the respondent consider the following datasets [`DSn` = `Dataset n`] controversial or not)

      - DSn name: categorical
      - DSn controversial: boolean
      - DSn why? (encode free form text response): text
      - DSn learning usage? (have you ever used this dataset for learning): boolean
      - DSn learning context?: categorical
      - DSn production usage? (have you ever used this dataset "in production"): boolean
      - DSn production context?: categorical
      - DSn production application? (are you still using this dataset "in production"): boolean
      - DSn last usage of DS in learning or production?: date

      The `DSn why` becomes encoded as a list of characteristics of the dataset in question. For example:
      "data scraping w/o permission", "commonly used for facial recognition" (this could be reframed as the end result of the use of the dataset not the dataset itself), etc.

3.  What are your hypothesis?

    - H1:
      H0: There are differences between demographic groups in terms of which datasets are considered controversial.

      This is a basic question to understand how different age groups, different genders, different educational and expertise background collectively decide what is and isn't controversial.

    - H2:
      H0: Datasets are typically labelled either highly or minimally controversial (i.e. 75% or more people -- highly or 25% or less people).

      I can't imagine we would find a dataset that is labelled controversial 50% of the time.

    - H3:
      H0: Highly controversial datasets (over 75% of people labelled the dataset as controversial) that were once used in learning application or production, are now used descriptive learning.

      This hypothesis begins to answer two questions, the first is whether or not we a see a shift in context of the dataset usage or if the dataset is entirely phased out of use altogether. The second, is because we are collecting demographic information about age and date of last use, we can _potentially_ build a timeline of "controversy shift" regarding a dataset.

4.  How many and which conditions will participants/samples be assigned to?

    There are a lot of questions in this survey that would take a bit of time / remembering so I am leaning toward asking a subset of datasets to each participant. I don't want the participants answering the survey to be fatigued by too many questions.

    If we have 10 datasets we want to use, we could ask each participant about a random 3. This is a single factor survey however with the single factor being which dataset they are asked about.

    The conditions then are simply DS1, DS2, and DS3.

5.  How many observations will be collected and what rule will you use to terminate data collection?

    More than >200? ...

6.  What are your study inclusion criteria?

    Participants:

    - Individuals who have are enrolled or have completed an undergraduate degree in a data science related field
    - Individuals who work in a data science related position

    Datasets:

    - Dataset must be able to be found on [papers-with-code](https://paperswithcode.com/datasets)
    - Dataset must have more than 10 citations
    - Dataset must have a "standardized import / usage method" -- i.e. zip file(s), API, mass download, etc.

7.  What are you data exclusion criteria?

8.  What positive controls or quality checks will confirm that the obtained results are able to provide a fair test of the stated hypothesis?

9.  Specify exactly which analysis you will conduct to examine the main question/hypothesis(es).

10. Are you proposing to collect new data or analysis existing data

    New

## Notes

- I want to add a question / variable about "dataset ease of use" -- I have a hypothesis about but didn't include it along the lines of:

  > H0: More respondents consider a dataset "not-controversial" as its "ease of use" increases.

- I feel I am missing something about the "timeline" of controversial datasets. I have a question about the last usage of a dataset but that doesn't quite get the root of the "why was the dataset removed from learning use or production"...

- Interestingly, [MegaFace has a warning / retraction on papers-with-code](https://paperswithcode.com/dataset/megaface)
