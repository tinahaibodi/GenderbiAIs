# Removing Gender Bias

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes

### Clone repository

`git clone git@github.com:MidoAssran/removing_gender_bias.git`

### Prerequisites

`Python 2.7, numpy, BeautifulSoup`

### Installing

`pip install <package_name>`

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