import sys
import os

class Git:
	def __init__(self, name, username="rekib0023", private=True, remote=False, init=True):
		self.name = name
		self.username = username
		self.private = private
		self.remote = remote
		self.init = init
		if self.init:
			os.system("git init")
		os.system(f'echo "# {self.name}" >> README.md')
		os.system(f'echo "The project is setup with .py scripts" >> README.md')
		os.system("git add .")
		os.system('git commit -m "initial commit"')

	def push(self):
		private = " --private " if self.private else " --public "
		os.system("gh repo create " + self.name + private + "-y")
		os.system("git push --set-upstream origin master")
		os.system("git push -u origin master")

def flask_app(path, name, private_repo, remote_repo):
	os.mkdir(path)
	os.chdir(path)
	git = Git(name=proj_name, private=private_repo, remote=remote_repo)
	os.system("cp -r /home/rekib/scripts/flask_app/. .")
	os.system("git add .")
	os.system('git commit -m "project setup"')
	if remote_repo:
		git.push()
		os.system(f"echo Your remote repo is https://github.com/rekib0023/{name}")
	os.system("pipenv install")
	os.system("code .")
	
def react_app(path, name, private_repo, remote_repo):
	os.system(f"npx create-react-app {name}")
	os.chdir(path)
	git = Git(name=proj_name, private=private_repo, remote=remote_repo)
	# os.system("git add .")
	# os.system('git commit -m "project setup"')
	if remote_repo:
		git.push()
		os.system(f"echo Your remote repo is https://github.com/rekib0023/{name}")
	os.system("code .")

def django_app(path, name, private_repo, remote_repo):
	pass

def node_app(path, name, private_repo, remote_repo):
	pass	

def flutter_app(path, name, private_repo, remote_repo):
	os.system(f"flutter create {name}")
	os.chdir(path)
	git = Git(name=proj_name, private=private_repo, remote=remote_repo)
	os.system("mkdir lib/components lib/constants lib/models lib/screens lib/utils lib/utils/services lib/utils/ui")
	os.system("git add .")
	os.system('git commit -m "project setup"')
	if remote_repo:
		git.push()
		os.system(f"echo Your remote repo is https://github.com/rekib0023/{name}")
	os.system("code .")

def ml_app(path, name, private_repo, remote_repo):
	pass


if __name__ == "__main__":
	# project details
	proj_type = sys.argv[2]
	proj_name = sys.argv[4]

	# project directory
	parent_dir = '/home/rekib/Documents/MyProjects'
	os.chdir(parent_dir)
	path = os.path.join(parent_dir, proj_name) 

	# git version control
	private_repo = True if "--private" in sys.argv else False
	remote_repo = True if "--remote" in sys.argv else False


	if proj_type == "flask":
		flask_app(path, proj_name, private_repo, remote_repo)
	elif proj_type == "react":
		react_app(path, proj_name, private_repo, remote_repo)
	elif proj_type == "django":
		django_app(path, proj_name, private_repo, remote_repo)
	elif proj_type == "node":
		node_app(path, proj_name)
	elif proj_type == "flutter":
		flutter_app(path, proj_name, private_repo, remote_repo)
	elif proj_type == "ml":
		ml_app(path, proj_name, private_repo, remote_repo)