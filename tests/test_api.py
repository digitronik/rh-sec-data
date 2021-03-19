from rh_sec_data import get_cve

ADVISORY = {
    "name": "RHSA-2016:0614",
    "total_cve": 8,
    "bug": "1317990",
    "expected_cves_with_bug": ["CVE-2016-2118"],
}


def test_get_cve():
    cves = get_cve()
    # expecting 1000 count without any filter
    assert len(cves) == 1000


def test_get_cve_with_advisory():
    cves = get_cve(advisory=ADVISORY["name"])
    assert len(cves) == ADVISORY["total_cve"]

    # apply bug filter
    cves = get_cve(advisory=ADVISORY["name"], bug=ADVISORY["bug"])
    assert len(cves) == len(ADVISORY["expected_cves_with_bug"])
    for cve in cves:
        assert cve["CVE"] in ADVISORY["expected_cves_with_bug"]
