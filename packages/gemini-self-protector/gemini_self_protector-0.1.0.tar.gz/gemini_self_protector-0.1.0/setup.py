# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gemini_self_protector']

package_data = \
{'': ['*']}

install_requires = \
['colorlog>=6.7.0,<7.0.0']

setup_kwargs = {
    'name': 'gemini-self-protector',
    'version': '0.1.0',
    'description': 'Runtime Application Self-Protection',
    'long_description': '# gemini_self_protector\n\nRuntime Application Self-Protection\n\n## Installation\n\n```bash\n$ pip install gemini_self_protector\n```\n\n## Protect Mode & Sensitive\n\nGemini supports 3 modes and recommends sensitivity levels for the application to operate at its best state.\n\n| Mode    | Sensitive |\n| ------- | --------- |\n| off     | N/A       |\n| monitor | 70        |\n| block   | 50        |\n\n## License Key\n\nThe license key is used for authentication with the API.\n| | |\n| ------- | --------- |\n|Key|988907ce-9803-11ed-a8fc-0242ac120002|\n\n## Basic Usage\n\nWith the basic usage, Gemini runs in the default mode of "monitor" and allows a sensitivity level of under 50, above which requests will be stored for monitoring purposes. The protection mode and sensitivity can be adjusted in the config.yml file after the first run.\n\n```\nfrom flask import Flask\nfrom flask import jsonify\nfrom flask import request\n\nfrom gemini_self_protector import GeminiManager\n\napp = Flask(__name__)\ngemini = GeminiManager(license_key=os.getenv("GEMINI_LICENSE_KEY"))\n\n@app.route(\'/api/login\', methods=[\'POST\'])\n@gemini.flask_protect_extended()\ndef login():\n    username = request.json[\'username\']\n    password = request.json[\'password\']\n    if username == "test" and password == "test":\n        response = jsonify({\n            "status": "Success",\n            "message": "Login successful",\n            "access_token": access_token\n            })\n        return response\n    else:\n        return jsonify({\n            "status": "Fail",\n            "message": "Incorrect Username or Password"\n            }), 401\n\nif __name__ == "__main__":\n    app.run()\n```\n\n## Advance Usage\n\nThe advanced usage of Gemini allows for deeper customization. Specifically, it is possible to specify individual modes for each router and have a dashboard to monitor the activity of the application. The running mode and sensitivity can be adjusted directly on the dashboard, and additional features are currently being developed.\n\n```\nfrom flask import Flask\nfrom flask import jsonify\nfrom flask import request\n\nfrom gemini_self_protector import GeminiManager\n\napp = Flask(__name__)\ngemini = GeminiManager(app, license_key=os.getenv("GEMINI_LICENSE_KEY"))\n\n@app.route(\'/api/login\', methods=[\'POST\'])\n@gemini.flask_protect_extended(protect_mode=\'block\')\ndef login():\n    username = request.json[\'username\']\n    password = request.json[\'password\']\n    if username == "test" and password == "test":\n        response = jsonify({\n            "status": "Success",\n            "message": "Login successful",\n            "access_token": access_token\n            })\n        return response\n    else:\n        return jsonify({\n            "status": "Fail",\n            "message": "Incorrect Username or Password"\n            }), 401\n\nif __name__ == "__main__":\n    app.run()\n```\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`gemini_self_protector` was created by lethanhphuc. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`gemini_self_protector` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'lethanhphuc',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
