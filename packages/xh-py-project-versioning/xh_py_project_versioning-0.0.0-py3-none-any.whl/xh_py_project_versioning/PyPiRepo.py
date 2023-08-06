import requests
from xh_py_project_versioning.versioning import SemVer


class PyPiRepo:
    def __init__(self, project_name: str):
        self.project_name = project_name

    def getInfo(self)->dict:
        return requests.get(f"https://pypi.org/pypi/{self.project_name}/json", headers={'max-age': '0'}).json()

    def getVersion(self)->SemVer:
        return SemVer(self.getInfo()['info']['verion'])
