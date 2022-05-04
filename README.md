Dear Students,

The following notebooks will contain my part of the Machine Learning course. I have done my best to annotate them and make them self-contained. However this is still very far from "textbook quality" :( 

The notebooks assume some basic understanding of probability and statistics, but that anyway were the prerequisites for the course. The notebooks contain Python code without much explanation. It's up to you to look up the documentation of the library functions that I have used. 

To run the notebooks you need a python environment. I strongly suggest you use `conda`. 


First install [anaconda](https://www.anaconda.com/distribution/) or [miniconda](https://docs.conda.io/en/latest/miniconda.html). Please install python 3.8 or higher. 

Then create a new _virtual environment_ for your projects e.g.
```
conda -n machinelearning python=3.9
```
This will create a virtual environment named `machinelearning`. 

To activate the environment you type:
```
conda activate machine_earning 
```


In case of Anaconda distribution most of the needed packages will be preinstalled. In case of miniconda you have to install them yourself using `conda install`. 

Here is a hopefully complete list of packages you will need:

```
conda install jupyterlab
conda install jupytext -c conda-forge
conda install numpy scipy 
conda install matplotlib
conda install seaborn
conda install pandas
conda install scikit-learn
conda install scrapbook
```
 
It can happen that thos commands take ages ! :( In that case install `mamba` with
```
conda install mamba -c conda-forge
```

and run same installation commands using `mamba` instead of `conda`. 
 
Then you can type
```
jupyter lab 
```
to open jupyter notebook  and start working :)

To close environment you type 
```
conda deactivate
```
 
Hope this helps. 







