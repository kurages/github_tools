from requests import (
	get,
	post
)
from .config import Config

class User:
	def __init__(self):
		#profile
		profile = self.subparsers.add_parser("profile", help=f"{self.cmd} profile -h")
		profile.set_defaults(subcommand_func=self.profile)

	def _show(self, a, b):
		print(f"{a}{' '*(10-len(a))}{b}")

	def profile(self):
		res = self._request(get, Config.USER)
		if res.status_code == 200:
			data = res.json()
			self._show("username", data['name'])
			self._show("userid", data['login'])
			self._show("email", data['email'])
			self._show("company", data['company'])
			self._show("location", data['location'])
			self._show("plan", data['plan']['name'])
		#else:
			print(res.json())
		return (res.status_code, res)





