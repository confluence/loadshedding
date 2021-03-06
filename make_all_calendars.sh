#!/bin/bash

for zone in {1..16}
do
    for stage in {1..8}
    do
        for only in "" "--only"
        do
            ./cape_town_load_shedding.py --zone $zone --stage $stage $only
        done
    done
done

mv zone_*_only.ics calendars/individual/
mv zone_*.ics calendars/combined/
