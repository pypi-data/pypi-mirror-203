# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_soap']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.95.0,<0.96.0',
 'lxml>=4.9.2,<5.0.0',
 'pydantic-xml[lxml]>=0.6.0,<0.7.0',
 'pydantic>=1.10.5,<2.0.0']

setup_kwargs = {
    'name': 'fastapi-soap',
    'version': '0.0.2',
    'description': '',
    'long_description': '# FastAPI Soap\n\nThis package helps to create Soap WebServices using FastAPI (What?!?!)\n\n## Motivation\nI know, FastAPI is a REST micro framework, but sometimes is needed to expose a Soap Interface on a already running FastAPI application for an legacy client/application that only supports, well, the Soap protocol...\n\n## Installation and dependencies\nOnly FastAPI, Pydantic and Pydantic XML are required.\n\n\n## First steps\n\n```python\nfrom fastapi import FastAPI\nfrom fastapi_soap.models import BodyContent\n\n\nclass Operands(BodyContent, tag="Operands"):\n    operands: list[float] = element(tag="Operand")\n\nclass Result(BodyContent, tag="Result"):\n    value: float\n\nsoap = SoapRouter(name=\'Calculator\', prefix=\'/Calculator\')\n\n@soap.operation(\n    name="SumOperation",\n    request_model=Operands,\n    response_model=Result\n)\ndef sum_operation(body: Operands = XMLBody(Operands)):\n    result = sum(body.operands)\n    \n    return SoapResponse(\n        Result(value=result)\n    )\n\n\napp = FastAPI()\napp.include_router(soap)\n\nif __name__ == \'__main__\':\n    import uvicorn\n    uvicorn.run("example.main:app")\n```\n_(This script is complete, it should run "as is")_\n\n\nThe WSDL is available on webservice root path for GET method.\n```\nGET http://localhost:8000/Calculator/\n```\n\n',
    'author': 'Cleiton Junior Mittmann',
    'author_email': 'mittmannv8@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
