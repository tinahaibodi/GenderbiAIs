# Removing Gender Bias from Candidate Application System

note: this repo is missing my csv data due to privacy so when cloning/using this repo keep in mind that you must use your own raw csv data to make this work

## Getting Started

Follow these instructions to get you a copy of the project up and running on your local machine for development and testing purposes

### Clone repository

`git clone git@github.com:tinahaibodi/gender-bias-AI.git`

### Prerequisites

`Python 2.7, numpy, BeautifulSoup`

### Installing

`pip install <gender-biAIs>`

### Running the code

#### To mine and generate the data set, run:

`python feature_builder.py`

#### To append personal info and job descriptions to the data set, run:

`python fetch_personal_info.py`

#### To rank candidates:

`python rank_candidates.py`

#### To analyze the results and generate graphs and figures:

`python analyze.py`

### Generated data files:

All generated csv files can be found in the data folder.
