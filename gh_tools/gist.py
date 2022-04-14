from requests import (
	get,
	post,
	delete,
)
from .config import Config


class Gist:
	def __init__(self):
		gist = self.subparsers.add_parser(
			"gist",
			help=f"{self.cmd} gist -h"
		).add_subparsers()



