# Setting up the repository

Start by cloning my repository to your local machine. You can do this by running
```shell
git clone https://github.com/pbialas7-Lectures/MachineLearning.git 
```
Then change the name of the default remote repository that at this moment points back to my repository by running
```shell
git remote rename origin lecture
```
Now you can update your repo from mine by issuing the command 
```shell
git pull lecture 
```
Please note that if you have changed some files, then you can have merge problems that you will have to resolve. 

Next, please create a **private** repository on [GitHub](https://github.com).
Then add this repository as remote to the repo you have just cloned by running
```shell
git remote add origin  url_to_jusr_crated_github_repo
```
You can find the url by clicking on the  `Code` button on the main page of the repo on GitHu. 
Then please push the content of the local repo using the command
```shell
git push -u origin main
```
Now you can push your changes to repository  using `git push`.

And finally please add me as a collaborator (Select tab `Settings` and nex `Collaborators and teams`). 
My [GitHub id is `pbialas7`](https://github.com/pbialas7). 
