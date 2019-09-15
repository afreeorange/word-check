Uncommon Word Checker
=====================

Check text for uncommon words in the English language. An uncommon word is one that's not on any list in `sources`. These are several "1,000 Most Common Words in English" lists which I combined to make mine.

```bash
cat ./samples/sample-1.txt | python word-check.py
```

Looks like this

<img src="https://i.imgur.com/xxg8MJz.png" />

Generating the List
-------------------

```bash
# Add tr '\n' '|' for a huge JavaScript regex.
cat sources/source-*.txt | grep -v "#" | sort -u | tr '[:upper:]' '[:lower:]'
```

TODO: Remove a few words by hand. Not sure that I want to be warned about using "Ireland"

Sources
-------

* [Wikipedia: _Punctuation of English_](https://en.wikipedia.org/wiki/Punctuation_of_English)
* Fry, Kress & Fountoukidis, _The Reading Teache's Book of Lists_, 4e, (c) 2000 by Prentice Hall

> The first 25 make up about a third of all printed material. The first 100 make up about half of all written material, and the first 300 make up about 65% of all written material.

Left these in order in `source-1.txt`

* [Wiktionary: _Most frequent 1000 words in English_](https://simple.wiktionary.org/wiki/Wiktionary:Most_frequent_1000_words_in_English)
* [1000MostCommonWords.com: _1000 Most Common English Words_
](https://1000mostcommonwords.com/1000-most-common-english-words/)
* [`deekayan@github`: 1,000 most common US English words
](https://gist.github.com/deekayen/4148741)
