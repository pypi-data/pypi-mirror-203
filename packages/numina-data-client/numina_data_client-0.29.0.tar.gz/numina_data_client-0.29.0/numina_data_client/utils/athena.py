#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from typing import List, Dict

import awswrangler as wr
import pandas as pd

from .. import constants

###############################################################################

ATHENA_DATABASE = "numina_data_lake_v20220720_prod"


def query_tracks(
    feed_id: str,
    start_datetime: datetime,
    end_datetime: datetime,
    obj_classes: List[str] = constants.ALL_OBJECT_CLASSES,
) -> pd.DataFrame:
    """
    Query for all tracks from a single feed and between two datetimes.

    Parameters
    ----------
    feed_id: str
        The feed id to query for. This is specifically tied to a device.
    start_datetime: datetime
        The datetime to query from.
    end_datetime: datetime
        The datetime to query to.
    obj_classes: List[str]
        Which objects to retrieve track data for.
        Default: All numina standard objects.

    Returns
    -------
    tracks: pd.DataFrame
        The selected tracks for that feed between the provided datetimes.
    """
    # Convert obj class to tuple for string addition
    # If there is only one object class selected, the query will fail due
    # to text formatting of tuples (the trailing comma)
    if len(obj_classes) == 1:
        obj_classes = f"('{obj_classes[0]}')"
    else:
        obj_classes = tuple(obj_classes)

    # Create basic query
    QUERY = f"""
    SELECT * FROM "numina_data_lake_v20220720_prod"."raw_tracks"
    WHERE feedid = '{feed_id}'
    AND class in {obj_classes}
    """

    # Add between datetimes
    if start_datetime is not None and end_datetime is not None:
        # Create iso_start_datetime and iso_end_datetime for ATHENA TIMESTAMP casts
        iso_start_datetime = start_datetime.isoformat(" ")
        iso_end_datetime = end_datetime.isoformat(" ")

        # Append to query
        QUERY += f"""
        AND (time
            BETWEEN CAST('{iso_start_datetime}' AS TIMESTAMP)
            AND CAST('{iso_end_datetime}' AS TIMESTAMP)
        )
        """

    # Finish the SQL formatting
    QUERY += ";"

    # Fetch and return
    return wr.athena.read_sql_query(QUERY, ATHENA_DATABASE)


def query_matrices(
    feed_id: str,
    start_datetime: datetime,
    end_datetime: datetime,
    obj_classes: List[str] = constants.ALL_OBJECT_CLASSES,
) -> pd.DataFrame:
    """
    Query for all tracks matrices from a single feed and between two datetimes.

    Parameters
    ----------
    feed_id: str
        The feed id to query for. This is specifically tied to a device.
    start_datetime: datetime
        The datetime to query from.
    end_datetime: datetime
        The datetime to query to.
    obj_classes: List[str]
        Which objects to retrieve track data for.
        Default: All numina standard objects.

    Returns
    -------
    tracks: pd.DataFrame
        The selected track matrices for that feed between the provided datetimes.
    """
    # Convert obj class to tuple for string addition
    # If there is only one object class selected, the query will fail due
    # to text formatting of tuples (the trailing comma)
    if len(obj_classes) == 1:
        obj_classes = f"('{obj_classes[0]}')"
    else:
        obj_classes = tuple(obj_classes)

    # Create basic query
    QUERY = f"""
    SELECT * FROM "numina_data_lake_v20220720_prod"."track_matrices"
    WHERE feedid = '{feed_id}'
    AND class in {obj_classes}
    """

    # Add between datetimes
    if start_datetime is not None and end_datetime is not None:
        # Create iso_start_datetime and iso_end_datetime for ATHENA TIMESTAMP casts
        iso_start_datetime = start_datetime.isoformat(" ")
        iso_end_datetime = end_datetime.isoformat(" ")

        # Append to query
        QUERY += f"""
        AND (track_date
            BETWEEN CAST('{iso_start_datetime}' AS TIMESTAMP)
            AND CAST('{iso_end_datetime}' AS TIMESTAMP)
        )
        """

    # Finish the SQL formatting
    QUERY += ";"
    return wr.athena.read_sql_query(QUERY, ATHENA_DATABASE)
