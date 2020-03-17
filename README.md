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
  * `cd ../midas-exp-pub`
* `jupyter notebook`, then with Chrome open `http://localhost:8888/`

At the end of the experiment, please do the follow

* `zip -r midas-exp-pub.zip midas-exp-pub`
* `jupyter nbextension uninstall notetaker --user`

## Submission

At the end of the session, you should zip up this directory and then email Yifan as attachment. She will then send you the Amazon gift card electronically.

## Clean Up

Note that you should be sure to remove the `notetaker` extension with the following:

`jupyter nbextension uninstall notetaker`

If you have successfully removed this extension, you will not see the 🧽 and ⏸ buttons in the menubar.

## Credit

The dataset `fires.csv` is sampled from this [kaggle data set](https://www.kaggle.com/rtatman/188-million-us-wildfires).

The dataset `berkeley_faculty.csv` is taken from [the Daily Cal](https://github.com/dailycal-projects/ucb-faculty-salary).

The dataset `recent_grads.csv` is taken from [fivethirtyeight](https://github.com/fivethirtyeight/data/tree/master/college-majors).

The loans dataset is referenced from [kaggle](https://www.kaggle.com/c/home-credit-default-risk/data).