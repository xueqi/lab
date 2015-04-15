import sys, os
from shutil import copy, copytree

def main():
    resource_name = sys.argv[1]
    resource_name = resource_name.lower()
    
    model_name = resource_name[0].upper() + resource_name[1:]
    pwd = os.getcwd()
    tpl_dir = os.path.join(pwd, "rest_tpl")
    if os.path.exists(resource_name):
        print "'%s' already exists" % resource_name
        return
    os.mkdir(resource_name)
    for d in ["templates", "migrations"]:
        os.mkdir(os.path.join(resource_name, d))
    open(os.path.join(resource_name, "migrations", "__init__.py"), 'w').close()
    for f in ["views.py", "models.py", "urls.py"]:
        copy(os.path.join(tpl_dir, f), resource_name)
    copytree(os.path.join(tpl_dir, "templates"), os.path.join(resource_name, "templates", resource_name))

if __name__ == "__main__":
    main()
