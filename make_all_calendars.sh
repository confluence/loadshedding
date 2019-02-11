#!/bin/bash

for zone in {1..15}
do
    for stage in {1..4}
    do
        for only in "" "only"
        do
            ./cape_town_load_shedding.py $zone $stage $only
        done
    done
done

mv zone_*_only.ics calendars/individual/
mv zone_*.ics calendars/combined/
