
<p align="center">
  <img src="https://raw.githubusercontent.com/vaneseltine/nominally/master/docs/_static/nominally_logo.png" alt="Nominally Logo" width=100 />
</p>

<h2 align="center">Nominally in Action: Examples and Snippets</h2>

<h1 align="center">This repo is neither fully armed nor operational. Please come back in a few days. </h1>


Nominally is a name parsing package for Python.

- Install: `pip install nominally`
- Repository: https://github.com/vaneseltine/nominally/
- Documentation: https://nominally.readthedocs.io/en/latest/

## Notebook in Pandas
A live example using Pandas:
https://colab.research.google.com/gist/vaneseltine/964fc9dec60e59410b91bbcaf1fe2d11/nom_pandas.ipynb

Go from list...

```
# raw_names
["Graham Arthur Chapman",
 "cleese, john m",
 "Gilliam, Terrence (Terry) Vance",
 "Eric Idle",
 'Mr. Terence "Terry" Graham Parry Jones',
 "M E Palin",
 "Neil James Innes",
 "carol cleveland",
 "Adams, Douglas N"]
```
...to DataFrame in a couple simple notebook cells.
```
                                        0  title     first        middle       last  suffix  nickname
0                   Graham Arthur Chapman           graham        arthur    chapman
1                          cleese, john m             john             m     cleese
2         Gilliam, Terrence (Terry) Vance         terrence         vance    gilliam             terry
3                               Eric Idle             eric                     idle
4  Mr. Terence "Terry" Graham Parry Jones     mr   terence  graham parry      jones             terry
5                               M E Palin                m             e      palin
7                         carol cleveland            carol                cleveland
6                        Neil James Innes             neil         james      innes
8                        Adams, Douglas N          douglas             n      adams
```

## Notebook hosts

https://mybinder.readthedocs.io/en/latest/user-guidelines.html

https://colab.research.google.com/