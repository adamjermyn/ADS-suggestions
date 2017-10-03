import sys

fname = sys.argv[1]
num = int(sys.argv[2])

import ads
fi = open('../adstoken','r')
line = fi.readline().strip()
ads.config.token = line
fi.close()

import bibtexparser
with open(fname) as bibtex_file:
    bibtex_str = bibtex_file.read()

bib_database = bibtexparser.loads(bibtex_str)

from collections import Counter

papers = list(list(ads.SearchQuery(bibcode=b[u'ID'], fl=['citation', 'reference'])) for b in bib_database.entries)
papers = list(p[0] for p in papers if len(p) > 0)

refCounter = Counter()

for p in papers:
	refCounter.update(p.reference)
	refCounter.update(p.citation)

for b in bib_database.entries:
	del refCounter[b[u'ID']]

for c in refCounter.most_common(num):
	if c[1] > 1:
		p = list(ads.SearchQuery(bibcode=c[0], fl=['title','author']))[0]
		print(c[1], p.title, p.author)

