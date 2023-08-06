#!/usr/bin/env python

# stdlib
import os.path
import sys
from datetime import datetime

# third party imports
import pandas as pd
import pytest
from obspy.core.event.magnitude import Magnitude
from obspy.core.event.resourceid import ResourceIdentifier

# local imports
from libcomcat.test_utils import vcr
from libcomcat.utils import (
    _get_country_shape,
    _get_utm_proj,
    check_ccode,
    filter_by_country,
    get_catalogs,
    get_contributors,
    get_country_bounds,
    get_mag_src,
    makedict,
    maketime,
    read_phases,
)


def test_reader():
    homedir = os.path.dirname(os.path.abspath(__file__))  # where is this script?
    datadir = os.path.abspath(os.path.join(homedir, "..", "data"))
    datafile = os.path.join(datadir, "us2000ahv0_phases.xlsx")
    hdr, dataframe = read_phases(datafile)
    assert hdr["id"] == "us2000ahv0"
    assert dataframe.iloc[0]["Channel"] == "GI.HUEH.HHZ.--"

    datafile = os.path.join(datadir, "us2000ahv0_phases.csv")
    hdr, dataframe = read_phases(datafile)
    assert hdr["id"] == "us2000ahv0"
    assert dataframe.iloc[0]["Channel"] == "GI.HUEH.HHZ.--"

    try:
        read_phases("foo")
    except FileNotFoundError:
        pass

    try:
        fname = os.path.abspath(__file__)
        read_phases(fname)
    except Exception as e:
        assert str(e).find("Filenames with extension") > -1


def test_makedict():
    string = "reviewstatus:approved"
    mydict = makedict(string)
    assert mydict["reviewstatus"] == "approved"

    try:
        makedict("foo")
        assert 1 == 2
    except Exception:
        pass


def test_maketime():
    str1 = "2000-01-02T03:04:05"
    str2 = "2000-01-02T03:04:05.678"
    str3 = "2000-01-02"
    time1 = maketime(str1)
    time2 = maketime(str2)
    time3 = maketime(str3)
    assert time1 == datetime(2000, 1, 2, 3, 4, 5)
    assert time2 == datetime(2000, 1, 2, 3, 4, 5, 678000)
    assert time3 == datetime(2000, 1, 2)

    try:
        maketime("foo")
        assert 1 == 2
    except Exception:
        pass


@vcr.use_cassette()
def test_catalogs():
    catalogs = get_catalogs()
    assert "us" in catalogs


@vcr.use_cassette()
def test_contributors():
    contributors = get_contributors()
    assert "ak" in contributors


@pytest.mark.skipif(
    sys.platform == "win32", reason="proj related functionality broken."
)
def test_get_utm_proj():
    tuples = [
        (36, -76, "+proj=utm +zone=18 +datum=WGS84 +units=m +no_defs"),
        (-66, 0, "+proj=utm +zone=31 +south +datum=WGS84 +units=m +no_defs"),
        (-81, 0, "+proj=utm +zone=31 +south +datum=WGS84 +units=m +no_defs"),
        (85, 0, "+proj=utm +zone=31 +datum=WGS84 +units=m +no_defs"),
        (76, 178, "+proj=utm +zone=60 +datum=WGS84 +units=m +no_defs"),
        (4, 122, "+proj=utm +zone=51 +datum=WGS84 +units=m +no_defs"),
    ]

    for tpl in tuples:
        lat, lon, projstr = tpl
        proj = _get_utm_proj(lat, lon)
        assert proj.srs == projstr


def test_get_mag_src():
    resource_ids = ["gcmt", "us", "duputel", "at", "pt", "ak", "pr"]
    for resource_id in resource_ids:
        resource = ResourceIdentifier(id=f"{resource_id}1000")
        mag = Magnitude(resource_id=resource, force_resource_id=True)
        assert get_mag_src(mag) == resource_id
    resource = ResourceIdentifier(id="none1000")
    mag = Magnitude(resource_id=resource, force_resource_id=True)
    assert get_mag_src(mag) == "unknown"


def test_check_ccode():
    for ccode in ["AFG", "CHN", "USA", "FRA"]:
        assert check_ccode(ccode)

    try:
        assert check_ccode("foo")
    except Exception:
        pass


def test_get_country_bounds():
    bounds = get_country_bounds("FRA")
    assert len(bounds) == 10
    tbounds = (
        7.944129165762711,
        10.177941146737316,
        40.54592258835411,
        43.860473896020885,
    )
    assert bounds[0] == tbounds


def test_get_country_shape():
    shape = _get_country_shape("JAM")
    assert len(shape.exterior.coords[:]) == 48


@pytest.mark.skipif(
    sys.platform == "win32", reason="proj related functionality broken."
)
def test_filter_by_country():
    # first event is in Haiti, second is in Dom. Rep.
    data = {
        "id": ["us1000h8hi", "pr2019035005"],
        "latitude": [20.041, 18.136],
        "longitude": [-73.014, -68.552],
    }
    df = pd.DataFrame(data)
    df2 = filter_by_country(df, "DOM")
    assert len(df2) == 1
    assert df2.iloc[0]["id"] == "pr2019035005"


if __name__ == "__main__":
    test_filter_by_country()
    test_get_country_shape()
    test_get_country_bounds()
    test_check_ccode()
    test_get_utm_proj()
    test_get_mag_src()
    print("Testing reader...")
    test_reader()
    print("Testing makedict...")
    test_makedict()
    print("Testing maketime...")
    test_maketime()
    print("Testing catalogs...")
    test_catalogs()
    print("Testing contributors...")
    test_contributors()
