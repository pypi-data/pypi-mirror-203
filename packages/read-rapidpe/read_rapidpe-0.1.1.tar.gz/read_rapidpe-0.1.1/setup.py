# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['read_rapidpe']

package_data = \
{'': ['*']}

install_requires = \
['joblib>=1.2.0,<2.0.0',
 'lalsuite>=7.14,<8.0',
 'matplotlib>=3.6.2,<4.0.0',
 'numpy>=1.23.4,<2.0.0',
 'python-ligo-lw>=1.8.3,<2.0.0',
 'scipy>=1.9.3,<2.0.0']

setup_kwargs = {
    'name': 'read-rapidpe',
    'version': '0.1.1',
    'description': '',
    'long_description': 'Read Rapid-PE\n===\n\nThis is a package to read Rapid-PE outputs.\n\n# Install (dev mode)\n```\ngit clone git@git.ligo.org:yu-kuang.chu/read-rapidpe.git\ncd read-rapidpe\npip install -e . \n```\n\n# Example Usage\n\n## Plot marginalized log-likelihood on m1-m2 grid points\n```python\nfrom read_rapidpe import RapidPE_result\nimport matplotlib.pyplot as plt\nimport glob\n\n\nresults_dir = "path/to/results"\nresult_xml_files = glob.glob(results_dir+"*.xml.gz")\nresult = RapidPE_result.from_xml_array(result_xml_files)\n\n\n# Plot marginalized-log-likelihood over intrinsic parameter (mass_1/mass_2) grid points\nplt.scatter(result.mass_1, result.mass_2, c=result.marg_log_likelihood )\nplt.xlabel("$m_1$")\nplt.ylabel("$m_2$")\nplt.colorbar(label="$\\ln(L_{marg})$")\n```\n\n## Plot interpolated likelihood\n```python\nfrom read_rapidpe import RapidPE_result\nimport matplotlib.pyplot as plt\nimport glob\nimport numpy as np\n\n\nresults_dir = "path/to/results"\nresult_xml_files = glob.glob(results_dir+"*.xml.gz")\nresult = RapidPE_result.from_xml_array(result_xml_files)\n\n\n# Create Random m1, m2 samples\nm1 = np.random.random(10000)*5\nm2 = np.random.random(10000)*5\n\n\n# After calling result.do_interpolate_marg_log_likelihood_m1m2(), \n# the method result.log_likelihood(m1, m2) will be avalible.\nresult.do_interpolate_marg_log_likelihood_m1m2()\n\n# Calculate interpolated log_likelihood\nlog_likelihood = result.log_likelihood(m1, m2)\n\n\n# =============== Plotting ===============\n# Plot interpolated likelihood \nplt.scatter(m1, m2, c=np.exp(log_likelihood), marker=".", s=3, alpha=0.1)\n\n# Plot marginalized likelihood on grid points\nplt.scatter(result.mass_1, result.mass_2, c=np.exp(result.marg_log_likelihood), marker="+", vmin=0)\n\nplt.xlabel("$m_1$")\nplt.ylabel("$m_2$")\nplt.colorbar(label=r"$\\mathcal{L}$")\n```\n\n\n## Convert to Pandas DataFrame\n\n```python\nimport pandas as pd\nfrom read_rapidpe import RapidPE_grid_point\n\n\ngrid_point = RapidPE_grid_point.from_xml("ILE_iteration_xxxxxxxxxx.samples.xml.gz")\npd.DataFrame(grid_point.extrinsic_table)\n```\n\n',
    'author': 'Cory Chu',
    'author_email': 'cory@gwlab.page',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
