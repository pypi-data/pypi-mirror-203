#!/usr/bin/env python

# stdlib imports
import json
import os.path
from datetime import datetime, timedelta

# third party imports
import numpy as np

from libcomcat.classes import DetailEvent

# local imports
from libcomcat.search import count, get_event_by_id, get_product_bytes, search
from libcomcat.test_utils import vcr


@vcr.use_cassette()
def test_get_event():
    eventid = "ci3144585"
    event = get_event_by_id(eventid)

    assert isinstance(event, DetailEvent)
    assert event.id == eventid
    assert (event.latitude, event.longitude) == (34.213, -118.537)


@vcr.use_cassette()
def test_count():
    nevents = count(
        starttime=datetime(1994, 1, 17, 12, 30),
        endtime=datetime(1994, 1, 18, 12, 35),
        minmagnitude=6.6,
        updatedafter=datetime(2010, 1, 1),
    )

    assert nevents == 1


@vcr.use_cassette()
def test_search_nullmag():
    tstart = datetime(2018, 1, 18, 5, 56, 0)
    tend = tstart + timedelta(seconds=60)
    eventlist = search(starttime=tstart, endtime=tend)
    assert np.isnan(eventlist[1].magnitude)


@vcr.use_cassette()
def test_search():
    eventlist = search(
        starttime=datetime(1994, 1, 17, 12, 30),
        endtime=datetime(1994, 1, 18, 12, 35),
        minmagnitude=6.6,
    )
    event = eventlist[0]
    assert event.id == "ci3144585"

    events = search(
        minmagnitude=9.0,
        maxmagnitude=9.9,
        starttime=datetime(2008, 1, 1),
        endtime=datetime(2010, 2, 1),
        updatedafter=datetime(2010, 1, 1),
    )

    events = search(
        maxmagnitude=0.1,
        starttime=datetime(2017, 1, 1),
        endtime=datetime(2017, 1, 30),
    )


@vcr.use_cassette()
def test_url_error():
    passed = True
    try:
        eventlist = search(
            starttime=datetime(1994, 1, 17, 12, 30),
            endtime=datetime(1994, 1, 18, 12, 35),
            minmagnitude=6.6,
            host="error",
        )
    except Exception as e:
        passed = False
    assert passed == False


@vcr.use_cassette()
def test_get_product_bytes():
    eventid = "nc216859"
    product = "shakemap"
    content = "rupture.json"
    rupture = json.loads(get_product_bytes(eventid, product, content).decode("utf8"))
    rupture["metadata"]["mag"] == 6.9


if __name__ == "__main__":
    test_get_product_bytes()
    test_search_nullmag()
    test_get_event()
    test_count()
    test_search()
    test_url_error()
