Lemmatizer evaluation regarding polymorphism
============================================

### Introduction
By polymorphism, we refer to orthographic variations such as:
- verbal endings (*aient* vs *ayent* or *faisoit* vs *faisait*);
- plural endings (*changements* vs *changemens*);
- diacritics (*défaire* vs *deffaire* or *mesme* vs *même*};
- double consonants (*afin* vs *affin*);
- single vowel (*voilà* vs *voylà*);
- etc. 

To evaluate the lemmatizer regarding polymorphism, we have to i) extract a list of graphic variations, ii) create two testing set (including including different
graphic spellings) and iii) evaluate the lemmatizer efficiency on this list.

### Graphic variations extraction
Our in-domain corpus, the *presto gold* corpus, counts about 60,000 tokens where lemma, POS-tags and morphology are available. To extract a list of
graphic variations, lines (form, lemma, POS-tag and morphology) have first been ordered by lemma, then by POS-tag and finally by morphology, assuming that graphic
variations should have the same lemma, POS-tag and morphology. The simplest way to do so is to use a spreadsheet. Then, when two lines are exactly the same except in their forms, they
are considered as graphic polymorphism candidates. Candidates, because this limited rule can return absolus and absolu when morphology
is missing (*{morph=empty}*). 1299 candidates have been extracted (see the file `variations_candidates.txt`). After cleaning, it resulted in 611 pairs of graphic polymorphisms
(see the file `variations_clean.txt`). It is also important to remind that this list of graphic polymorphisms is not rationalised; no rule has been infered (e.g. *-ments* to 
*-mens*).

### Creation of testing set variations
As we have at our disposal a testing corpus and a list of pairs of graphic polymorphisms, it is possible to create two testing corpora, or two variations of the same testing corpus.
These two new testing corpora are equal to the original one for each token that does not belong to the list of polymorphisms; for tokens that do belong to the list, the first component of the pair is used for the first new testing corpus and the second one for the second new testing corpus. At the end,
we obtain two testing corpora including different polymorphisms. 

For example, let's consider this pair of polymorphisms: (*besoin* ; *besoing). Two variations can be produced from the original text 
*sans éprouver le besoin d'une lampe*: the first variation with the first component of the pair (*besoin*) and the second one with the second compenent (*besoing*). 
Thus, the two resulting texts are: *sans éprouver le **besoin** d'une lampe* and *sans éprouver le **besoing** d'une lampe*.

3 files are provided:
- `1_remove_lemmas.py`: it removes lemmas from the original testing corpus
- `2_transform_test_corpus_with_variantes.py`: it transforms the tokens in its graphic variation (as said just above)
(Here, you have to run `pie tag` using the lemmatizer you want to evaluate.)
- `3_evaluate_lemmatizer_on_variations.py`: the file counts how many graphic variations share the same and different lemmas.

### Results
As shown in the article, 92.5% of the graphic variation pairs have the same and correct lemma; it represents 86.5% of the graphic variation occurrencies in the testing set.