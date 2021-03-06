import json, os
from .config import Config

class Account:
	def __init__(self):
		os.makedirs(f"{Config.CONFIG_DIR}", exist_ok=True)
		if os.path.isfile(Config.CONFIG_FILE):
			with open(Config.CONFIG_FILE) as f:
				self.data = json.load(f)
		else:
			with open(Config.CONFIG_FILE, "w") as f:
				f.write("{}")
			self.data = {}
		self.select_user = self.get_default_user()

		#account
		user = self.subparsers.add_parser(
			"user",
			help=f"{self.cmd} user -h"
		).add_subparsers()
		#list
		list_user = user.add_parser("list", help="get logined user")
		list_user.set_defaults(subcommand_func=self.get_user_list)

		#set default
		set_default_user = user.add_parser("set-default")
		set_default_user.add_argument("name")
		set_default_user.set_defaults(subcommand_func=self.set_default_user)


	def __save(self):
		with open(Config.CONFIG_FILE, "w") as f:
			json.dump(self.data, f, indent=4)

	def _get_user_list(self):
		return list(self.data)
	
	def get_user_list(self):
		users = []
		for i in self._get_user_list():
			if i == self.get_default_user():
				users.append(f"*{i}")
			else:
				users.append(f" {i}")
		print("\n".join(users))
		return users

	def set_default_user(self):
		name = self.args.name
		if self.data.get(name, None) == None:
			return print("Incorrect user name")
		defaulted_user = self.get_default_user()
		if defaulted_user:
			self.data[defaulted_user]["x-gh-default"] = False
		self.data[name]["x-gh-default"] = True
		self.__save()

	def get_default_user(self):
		for name, val in self.data.items():
			if val.get("x-gh-default", False):
				return name
		return None
	
	def get_user_id(self, name):
		return self.data[name]["id"]

	def get_token(self, name=None):
		if not name:
			name = self.select_user
		return self.data.get(name, {}).get("x-gh-token", None)

	def set_token(self, name, token, val={}, default=None):
		if default == None:
			if self.data == {}:
				default = True
			elif list(self.data.keys()) == [name]:
				default = True
			else:
				default = False
		self.data[name] = val
		self.data[name]["x-gh-token"] = token
		self.data[name]["x-gh-default"] = default
		self.__save()

