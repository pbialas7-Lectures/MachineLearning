# Machine Learning 

Materials for the Machine Learning course. 


## Setting up the python environment

In this course you will be working with python using jupyter notebooks or jupyter lab (prefered). So first you have to set up a proper python environment. I strongly encourage you to use some form of a virtual environment. I recommend the [Anaconda](https://docs.anaconda.com/anaconda/install/index.html) or its smaller subset [miniconda](https://docs.conda.io/en/latest/miniconda.html). Personally I recommend using 
[mambaforge](https://github.com/conda-forge/miniforge#mambaforge) as `conda` tends to be rather slow. 
After installing `mambaforge` create a new virtual environment `ml` (or any other name you want):

```
conda create -n ml python=3.9
```
Then activate the environment  by running
```
conda activate ml
```
To close environment you type 
```
conda deactivate
```

Now you can install required packages (if you are using Anaconda some maybe already installed):

```
mamba install  jupyterlab jupytext  ipywidgets
mamba install numpy scipy  scikit-learn
mamba install matplotlib
```
If you didn't install `mamba` then you can substitute `conda -c conda-forge`(`-c conda-forge` tells to add `conda-forge` channel which is turned on by default in `mambaforge` ) for `mamba`. I tend to use `mamba` as it is markedly faster then `conda`.  

After installing all required packages you can start `jupyter lab` by running 
```
jypyter lab
```

## Rmd format

The notebooks in the repository are stored in [Rmd (R Markdown)](https://rmarkdown.rstudio.com/articles_intro.html) format. Thanks to the `jupytext` package you can open them right in the jupyter lab, by clicking the file name with righthand mouse button and choosing `open with` and then `Notebook`. If you are using jupyter notebook the you have to convert them prior to opening by running   
```shell
jupytext --to notebook <Rmd file name>
```

## Using python in lab

When using the computers in lab, please log to your linux account and then run
```
source /app/Python/3.10.4/VE/defaults/bin/activate
```
Then you can run 
```
jupyter lab
```








