# ADS-suggestions
This script uses the API for NASA's ADS to suggest references related to those listed in a bibtex file.

It takes as input the path to the bibtex file and the number of related references to produce.
Related references are sorted by the number of times they appear either referencing or being referenced by papers in the bibtex file.
The output is printed out with one reference per line.
Each line begins with the number of occurences in the citation graph, the title of the paper and the author list.

Note that this package requires the [bibtexparser](https://bibtexparser.readthedocs.io/en/v0.6.2/) and [ads](https://ads.readthedocs.io/en/latest/) packages.
It also requires that you create a file in the directory above the one containing refs.py (though it is easy to change this location).
This file must be called `adstoken' and contain your NASA ADS API token.
If you don't have a token you can obtain one here(https://github.com/adsabs/adsabs-dev-api).
