# Wrapper Red Hat Security Data APIs.
import logging

from requests import request

logger = logging.getLogger(__name__)
API_HOST = "https://access.redhat.com/hydra/rest/securitydata"

COMMON_PARAMS = ["after", "before", "bug", "created_days_ago", "page", "per_page", "severity"]

CVRF_PARAMS = COMMON_PARAMS + ["cve", "package", "rhsa_ids"]
CVE_PARAMS = COMMON_PARAMS + [
    "advisory",
    "cvss3_score",
    "cvss_score",
    "cwe",
    "ids",
    "package",
    "product",
]
OVEL_PARAMS = COMMON_PARAMS + ["cve", "rhsa_ids"]
OVALSTREAM_PARAMS = ["after", "label"]


class ApiException(Exception):
    """API exception."""


def __call_api(endpoint, method="get", **kwargs):
    """Call Red Hat Sec Data API and retrieve data."""
    url = f"{API_HOST}/{endpoint}"
    logger.info(f"{url} with params {kwargs}")
    resp = request(method=method, url=url, params=kwargs)
    logger.info(resp.url)
    if resp.status_code != 200:
        raise ApiException(f"ERROR ({resp.status_code}): {resp.text}")

    if endpoint.endswith(".json"):
        data = resp.json()
    else:
        data = resp.content

    if not data:
        logger.info(f"No data found.")
    return data


def _validate_params(param_set, provided_params):
    """Param validation for respective endpoints."""
    for param in provided_params:
        if param not in param_set:
            raise ValueError(
                f"'{param}' is not valid parameter.\n" f"Applicable parameters are {param_set}"
            )


def _validate_call(type, format, param_set, **kwargs):
    _validate_params(param_set, kwargs.keys())
    endpoint = type if format == "html" else f"{type}.{format}"
    return __call_api(endpoint=endpoint, **kwargs)


def get_cvrf(format="json", **kwargs):
    return _validate_call(type="cvrf", format=format, param_set=CVRF_PARAMS, **kwargs)


def get_cve(format="json", **kwargs):
    return _validate_call(type="cve", format=format, param_set=CVE_PARAMS, **kwargs)


def get_ovel(format="json", **kwargs):
    return _validate_call(type="ovel", format=format, param_set=OVEL_PARAMS, **kwargs)


def get_ovelstream(format="json", **kwargs):
    return _validate_call(type="ovelstream", format=format, param_set=OVALSTREAM_PARAMS, **kwargs)
