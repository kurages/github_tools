from requests import (
	get,
	post,
	delete,
)
from .config import Config


class Issues:
	def __init__(self):
		gist = self.subparsers.add_parser(
			"issues",
			help=f"{self.cmd} gist -h"
		).add_subparsers()



