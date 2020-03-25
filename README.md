# Midas Experiment

Welcome to Midas experiment!

You can find the consent form under the title `consent.pdf` in this directory.

## Requirements

**Skills**: you should know how to do data analysis, and basic modeling/"machine learning".  Specifically, you should already be familiar with dataframes (e.g., `pandas`), know how to read basic visualizations (e.g., bar chart, scatter plot), and know how to build a classification algorithm (e.g., `LogisticRegression` from `sklearn.linear_model`).

**Technical**: you should have **Python 3.7, Jupyter**, and **Chrome** installed on your computer.

## Setup

First, download a zip of this repository, which contains the data and relevant notebooks.

For this experiment, you will need to install two extensions to Jupyter. Follow the steps:

* `mkdir midas-exp && cd midas-exp`
* `git clone git@github.com:yifanwu/midas-exp-pub.git`
* `git clone git@github.com:yifanwu/notetaker.git`
  * `cd notetaker`
  * `jupyter nbextension install notetaker --user`
  * `jupyter nbextension enable notetaker/main`
  * `cd ..`
* `git clone git@github.com:yifanwu/midas.git`
  * `cd midas`
  * `pip install -r requirements.txt`
  * `python setup.py develop`
  * `jupyter nbextension install --py --symlink midas`
  * `jupyter nbextension enable midas/index`
  * `cd ../midas-exp-pub`
* `jupyter notebook`, then with Chrome open `http://localhost:8888/`

At the end of the experiment, please do the follow

* `zip -r midas-exp-pub.zip midas-exp-pub`
* `jupyter nbextension uninstall notetaker --user` (If you have successfully removed this extension, you will not see the 🧽 and ⏸ buttons in the menubar.)

## Setup with Virtual Env

Run the following **before** we start the installation process. Note that you might also need to install other tools like Jupyter.

* `python3 -m venv midas-env`
* `source midas-env/bin/activate`

## Data Source Credit

* The dataset `fires.csv` is sampled from this [kaggle data set](https://www.kaggle.com/rtatman/188-million-us-wildfires).
* The dataset `berkeley_faculty.csv` is taken from [the Daily Cal](https://github.com/dailycal-projects/ucb-faculty-salary).
* The dataset `recent_grads.csv` is taken from [fivethirtyeight](https://github.com/fivethirtyeight/data/tree/master/college-majors).
* The loans dataset is referenced from [kaggle](https://www.kaggle.com/c/home-credit-default-risk/data).
* The cars dataset is referenced from [kaggle](https://www.kaggle.com/austinreese/craigslist-carstrucks-data).
