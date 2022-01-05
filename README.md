# LCD

A study on the **L**ong tail of **C**ontroversial **D**atasets

## Planning

We know that there will be roughly two parts of the study. The first is defining
the term controversial and what makes datasets controversial.

The next is using that definition to

1. Define -- What makes a dataset controversial?

   - By features?
     - "Would you use a **{release method}** **{content type}** dataset from **{data source}** for **{example work}**?"
     - Ex: "Would you use a **leaked** _(release method)_ **human faces** _(images)_ dataset from **a dating website** _(data source)_ for **training ...** _(example work)_?"
   - By usage?

     - Ex: "For learning / study?"
     - Ex: "In production?"
     - Ex: "Is the dataset readily available / easy to use?"

   - What are the most well known "controversial" datasets? Plain text, what makes them controversial?

   - Target IT related fields

2. Understand -- How usage changes over time?

   - Find a few datasets that have been deemed controversial that have common import patterns, i.e. scikit-learns housing dataset. Scrape GitHub for such patterns and look at time of usage and topic of content.

   - This part should be specific to a few datasets to limit the number of variables.

   - We want to try to understand the context around the usage. Did the dataset move from "production" to "an example for students on why it was bad" or similar? Was there an immediate drop-off? How "long of a tail" is there is active usage of the dataset?

### Datasets

Examples from Adam Harvey: https://twitter.com/adamhrv/status/1278604672408997889

Additional examples:

- OKCupid Dataset
- IBM Diversity in Faces (2019)
- ENRON Emails
- Ashley Madison Dataset
