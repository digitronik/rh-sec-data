<h1 align="center"> rh-sec-data </h1>
<h3 align="center"> Python wrapper Red Hat Security Data API</h3>

<p align="center">
    <a href="https://pypi.org/project/rh-sec-data/">
    <img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/rh-sec-data.svg?style=flat">
    </a>
    <a href="https://pypi.org/project/rh-sec-data/#history">
    <img alt="PyPI version" src="https://badge.fury.io/py/rh-sec-data.svg">
    </a>
    <a href="https://codecov.io/gh/digitronik/rh-sec-data">
      <img src="https://codecov.io/gh/digitronik/rh-sec-data/branch/main/graph/badge.svg" />
    </a>
    <a href="https://github.com/digitronik/rh-sec-data/actions/workflows/tests.yml">
    <img alt="github actions" src="https://github.com/digitronik/rh-sec-data/actions/workflows/tests.yml/badge.svg">
    </a>
    <a href="https://github.com/digitronik/rh-sec-data/blob/master/LICENSE">
    <img alt="License: GPLv3" src="https://img.shields.io/pypi/l/rh-sec-data.svg?version=latest">
    </a>
    <a href="https://pypi.org/project/black">
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
    </a>
</p>

It simply provides Python wrapper API for [Red Hat Security Data API](https://access.redhat.com/documentation/en-us/red_hat_security_data_api/1.0/)

### Installation

```
pip install rh-sec-data
```

### Usage
#### Wrapper API:
You can import methods from `rh_sec_data`
```python
In [1]: from rh_sec_data import get_cve

In [2]: cves = get_cve() # Call without any filter. It will return list of dict for first 1000 CVEs.

In [3]: len(cves)
Out[3]: 1000

In [4]: cves = get_cve(advisory="RHSA-2016:0614") # Filter with specific advisory.

In [5]: len(cves)
Out[5]: 8

In [6]: get_cve(advisory="RHSA-2016:0614", bug="1317990") # Filter with specific advisory and bug.
Out[6]:
[{'CVE': 'CVE-2016-2118',
  'severity': 'important',
  'public_date': '2016-04-12T00:00:00Z',
  'advisories': ['RHSA-2016:0618',
   'RHSA-2016:0619',
   'RHSA-2016:0623',
   'RHSA-2016:0612',
   'RHSA-2016:0613',
   'RHSA-2016:0624',
   'RHSA-2016:0625',
   'RHSA-2016:0614',
   'RHSA-2016:0620',
   'RHSA-2016:0621',
   'RHSA-2016:0611'],
  'bugzilla': '1317990',
  'bugzilla_description': 'CVE-2016-2118 samba: SAMR and LSA man in the middle attacks',
  'cvss_score': 6.8,
  'cvss_scoring_vector': 'AV:N/AC:M/Au:N/C:P/I:P/A:P',
  'CWE': 'CWE-300',
  'affected_packages': ['samba4-0:4.2.10-6.el6_2',
   'samba4-0:4.2.10-6.el6_4',
   'samba4-0:4.2.10-6.el6_5',
   'samba3x-0:3.6.23-12.el5_9',
   'samba4-0:4.2.10-6.el6_6',
   'samba4-0:4.2.10-6.el6_7',
   'samba-0:3.6.23-30.el6_6',
   'samba3x-0:3.6.23-12.el5_11',
   'samba-0:3.6.23-30.el6_7',
   'samba-0:4.2.11-2.el6rhs',
   'samba-0:3.6.23-30.el6_2',
   'samba-0:4.2.10-6.el7_2',
   'samba-0:3.6.23-30.el6_4',
   'samba-0:3.6.23-30.el6_5',
   'samba-0:3.0.33-3.41.el5_11',
   'samba-0:4.2.11-2.el7rhgs',
   'samba-0:3.0.33-3.40.el5_9',
   'samba-0:4.2.10-5.ael7b_1',
   'samba-0:3.0.33-3.37.el4'],
  'resource_url': 'https://access.redhat.com/hydra/rest/securitydata/cve/CVE-2016-2118.json'}]

```

#### CLI:
It's in WIP state.

```shell
❯❯❯ rh-sec-data
Usage: rh-sec-data [OPTIONS] COMMAND [ARGS]...

  Red Hat Security Data API.

Options:
  --help  Show this message and exit
```
