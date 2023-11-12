import os

import requests
from infrastructure.acceptance_config import get_settings

_config = get_settings()

if __name__ == "__main__":
    print(f"Fetching coverage report from {_config.genos_url}/coverage")
    res = requests.get(f"{_config.genos_url}/coverage", verify=False)
    with open("build/acceptance-coverage.xml", "w") as f:
        f.write(res.text)
        filepath = os.path.abspath(f.name)
        print(f"Wrote coverage to {filepath}")
