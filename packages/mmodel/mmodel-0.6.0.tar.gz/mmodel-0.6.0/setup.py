# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mmodel']

package_data = \
{'': ['*']}

install_requires = \
['graphviz>=0.16', 'h5py>=3.6.0', 'networkx>=2.8.3']

extras_require = \
{'docs': ['sphinx>=6.1.3,<7.0.0',
          'sphinx-book-theme==1.0.0',
          'pydata-sphinx-theme==0.13.1',
          'nbsphinx==0.9.1'],
 'test': ['pytest>=7.1.1', 'pytest-cov>=3.0.0']}

setup_kwargs = {
    'name': 'mmodel',
    'version': '0.6.0',
    'description': 'Modular modeling framework for scientific modeling and prototyping.',
    'long_description': 'MModel\n======\n\n|GitHub version| |PyPI version shields.io| |PyPI pyversions| |Unittests|\n|Docs|\n\nMModel is a lightweight and modular model-building framework\nfor small-scale and nonlinear models. The package aims to solve\nscientific program prototyping and distribution difficulties, making\nit easier to create modular, fast, and user-friendly packages.\n\nQuickstart\n----------\n\nTo create a nonlinear model that has the result of\n`(x + y)log(x + y, base)`:\n\n.. code-block:: python\n\n    import math\n    import numpy as np\n\n    def func(sum_xy, log_xy):\n        """Function that adds a value to the multiplied inputs."""\n\n        return sum_xy * log_xy + 6\n\nThe graph is defined using grouped edges (the ``networkx`` syntax of edge\nthe definition also works.)\n\n.. code-block:: python\n\n    from mmodel import ModelGraph, Model, MemHandler\n    # create graph edges\n    grouped_edges = [\n        ("add", ["log", "function node"]),\n        ("log", "function node"),\n    ]\n\nThe functions are then added to node attributes. The order of definition\nis node_name, node_func, output, input (if different from original function),\nand modifiers.\n\n.. code-block:: python\n\n    # define note objects\n    node_objects = [\n        ("add", np.add, "sum_xy", ["x", "y"]),\n        ("log", math.log, "log_xy", ["sum_xy", "log_base"]),\n        ("function node", func, "result"),\n    ]\n\n    G = ModelGraph(name="example_graph")\n    G.add_grouped_edges_from(grouped_edges)\n    G.set_node_objects_from(node_objects)\n\nTo define the model, the name, graph, and handler need to be specified. Additional\nparameters include modifiers, descriptions, and returns lists. The input parameters\nof the model are determined based on the node information.\n\n.. code-block:: python\n\n    example_model = Model("example_model", G, handler=MemHandler, description="Test model.")\n\nThe model behaves like a Python function, with additional metadata. The graph can\nbe plotted using the ``draw`` method.\n\n.. code-block:: python\n\n    >>> print(example_model)\n    example_model(log_base, x, y)\n    returns: z\n    graph: example_graph\n    handler: MemHandler\n\n    Test model.\n\n    >>> example_model(2, 5, 3) # (5 + 3)log(5 + 3, 2) + 6\n    30.0\n\n    >>> example_model.draw()\n\nThe resulting graph contains the model metadata and detailed node information.\n\n.. .. |br| raw:: html\n    \n..     <br/>\n\n.. .. image:: example.png\n..   :width: 300\n..   :alt: example model graph\n\nOne key feature of ``mmodel`` that differs from other workflow is modifiers, \nwhich modify callables post definition. Modifiers work on both the node level\nand model level.\n\nExample: Use ``loop_input`` modifier on the graph to loop the nodes that require the\n"log_base" parameter.\n\n.. code-block:: python \n\n    from mmodel import loop_input\n\n    H = G.subgraph(inputs=["log_base"])\n    H.name = "example_subgraph"\n    loop_node = Model("submodel", H, handler=MemHandler)\n\n    looped_G = G.replace_subgraph(\n        H,\n        "loop_node",\n        loop_node,\n        output="looped_z",\n        modifiers=[loop_input("log_base")],\n    )\n    looped_G.name = "looped_graph"\n\n    looped_model = Model("looped_model", looped_G, loop_node.handler)\n\n\nWe can inspect the loop node as well as the new model.\n\n.. code-block:: python \n\n    >>> print(looped_model)\n    looped_model(log_base, x, y)\n    returns: looped_z\n    graph: looped_graph\n    handler: MemHandler()\n    \n    >>> print(looped_model.node_metadata("loop_node"))\n    submodel(log_base, sum_xy)\n    return: looped_z\n    functype: mmodel.Model\n    modifiers:\n      - loop_input(\'log_base\')\n\n    >>> looped_model([2, 4], 5, 3) # (5 + 3)log(5 + 3, 2) + 6\n    [30.0, 18.0]\n\n\nUse the ``draw`` method to draw the graph. There are three styles\n"plain", "short", and "verbose", which differ by the level of detail of the\nnode information. A graph output is displayed in Jupyter Notebook\nor can be saved using the export option.\n\n.. code-block:: python\n\n    G.draw(style="short")\n    example_model.draw(style="plain", export="example.pdf") # default to draw_graph\n\nInstallation\n------------\n\nGraphviz installation\n^^^^^^^^^^^^^^^^^^^^^\n\nTo view the graph, Graphviz needs to be installed:\n`Graphviz Installation <https://graphviz.org/download/>`_\nFor windows installation, please choose "add Graphviz to the\nsystem PATH for all users/current users" during the setup.\n\nMModel installation\n^^^^^^^^^^^^^^^^^^^^^^^\n\n.. code-block::\n\n    pip install mmodel\n\nDevelopment installation\n^^^^^^^^^^^^^^^^^^^^^^^^\nMModel uses `poetry <https://python-poetry.org/docs/>`_ as\nthe build system. The package works with both pip and poetry\ninstallation. For macos systems, sometimes `brew install` results\nin unexpected installation path, it is recommended to install\nwith conda::\n\n    conda install -c conda-forge pygraphviz\n\nTo install test and docs, despondencies run::\n\n    pip install .[test] .[docs]\n\nTo run the tests in different python environments and cases \n(py38, py39, py310, py311, coverage and docs)::\n\n    tox\n\nTo create the documentation, run under the "/docs" directory::\n\n    make html\n\n\n.. |GitHub version| image:: https://badge.fury.io/gh/peterhs73%2FMModel.svg\n   :target: https://github.com/Marohn-Group/mmodel\n\n.. |PyPI version shields.io| image:: https://img.shields.io/pypi/v/mmodel.svg\n   :target: https://pypi.python.org/pypi/mmodel/\n\n.. |PyPI pyversions| image:: https://img.shields.io/pypi/pyversions/mmodel.svg\n\n.. |Unittests| image:: https://github.com/Marohn-Group/mmodel/actions/workflows/tox.yml/badge.svg\n    :target: https://github.com/Marohn-Group/mmodel/actions\n\n.. |Docs| image:: https://img.shields.io/badge/Documentation--brightgreen.svg\n    :target: https://github.com/Marohn-Group/mmodel-docs/\n',
    'author': 'Peter Sun',
    'author_email': 'hs859@cornell.edu',
    'maintainer': 'Peter Sun',
    'maintainer_email': 'hs859@cornell.edu',
    'url': 'https://peterhs73.github.io/mmodel-docs/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
