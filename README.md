# 📕 Description 📕
This is a project for create automatically a repository from console in Github with a LICENSE and README.<br/>
It is a simple and powerfull idea where you can choose the title, the description and the privacity of the repository.<br/>

# 📖 How to use 📖
The structure is REPO_NAME FLAGS [DESCRIPTION]<br/><br/>
If the REPO_NAME or the DESCRIPTION have more than ONE word should go between " "<br/>
Order of the flags is indiferent and must start with '-'<br/><br/>
Flags could be:<br/>
    p for make it private, for default is public<br/>
    d for add a description after the flags<br/>
Example: TestName -dp "This is the example for the description"<br/>

# 📂 Installation 📂

First of all you have to clone the project:<br/>
```bash
git clone https://github.com/JarssS8/AutomaticRepositoryCreate.git
```

I prefer use a Python virtual enviroment for make it more clean.<br/>
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install virtual enviroment.<br/>

If you don't have it, you can download pasting this on a terminal:<br/>

```bash
pip install virtualenv
```

After that you can create your vitual enviroment with:<br/>
```bash
python3 -m venv venv
```
The last venv is the name of the virtual enviroment, you can choose other if you want.<br/>

Then we have to access to the venv, for that we open a terminal in ours project folder and type:<br/>
```bash
source ./venv/bin/activate
```
Now we can see we are in the virtual enviroment because the first word in our terminas is (venv)<br/>

For install all the dependencies on the venv we type:<br/>
```bash
pip install -r requirements.txt
```

The next step is create a JSON file with our Github credentials, something like this:<br/>
```json
{
    "username" : "my_username", 
    "password" : "my_password"
}
```
** CHANGE THE PATHS IN MAIN.PY FOR YOUR REPOSITORIES FOLDER AND YOUR CREDENTIALS FILE**<br/>

Now we have to write a bash script for can run the python script from console and after that opens Visual Studio Code with our folder:<br/>
```bash
#!/bin/bash

source /home/jars/Programming/Python/GithubAPI/venv/bin/activate && python3 /home/jars/Programming/Python/GithubAPI/main.py $@ && deactivate
code /home/jars/Programming/Autocreated/$1
```

The last step is create an alias in our .bashrc with the path of our bash script:<br/>
```bash
alias create='bash /home/jars/Programming/Python/GithubAPI/script.sh'
```
If you logout and login all should be ok. And now you can create your repositories using your console.<br/><br/>
You can use the github credentials store for don't have to write your credentials everytime that you want create a new project, presonally I recommend this guide: https://www.shellhacks.com/git-config-username-password-store-credentials<br/>


** CHANGE THE PATHS IN MAIN.PY FOR YOUR REPOSITORIES FOLDER AND YOUR CREDENTIALS FILE**
