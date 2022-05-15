# 📕 Description 📕
This is a project for create automatically a repository from console in Github with a LICENSE and README.<br/>
It is a simple and powerfull idea where you can choose the title, the description and the privacity of the repository.<br/>

# 📖 How to use 📖
The structure is REPO_NAME FLAGS [DESCRIPTION]<br/><br/>
If the REPO_NAME or the DESCRIPTION have more than ONE word should go between " "<br/>
Order of the flags is indiferent and must start with '-'<br/><br/>
Flags could be:<br/>
    n to set a repository name (MANDATORY)
    p for make it private, for default is public<br/>
    d for add a description after the flags<br/>
    r custom local path, by default ~/Programing/repo_name
Example:python create.py -n DjangoApp -d "This is the example for the description" -p<br/>

# 📂 Installation 📂

First of all you have to clone the project:<br/>
```bash
git clone https://github.com/JarssS8/AutomaticRepositoryCreate.git
```

Install requirements from pip
```bash
pip install -r requirements.txt
```

You need to create a enviroment variable persistent (https://unix.stackexchange.com/questions/117467/how-to-permanently-set-environmental-variables) with the name GITHUB_TOKEN (https://github.com/settings/tokens)

The last step is create an alias in our .bashrc with the path of our bash script:<br/>
```bash
alias create='python ~/repo_path/create.py'
```
