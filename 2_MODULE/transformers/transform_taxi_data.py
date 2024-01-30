import re
import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def camel_to_snake(name):
    """
    Convert a camel case string to snake case.
    """
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
    return re.sub('([A-Z])([A-Z][a-z0-9])', r'\1_\2', name).lower()

@transformer
def transform(data, *args, **kwargs):
    data.columns = [camel_to_snake(col) for col in data.columns]

    # Convert 'lpep_pickup_datetime' to datetime if it's not already
    data['lpep_pickup_datetime'] = pd.to_datetime(data['lpep_pickup_datetime'])
    
    # Create a new column 'lpep_pickup_date' by extracting the date from 'lpep_pickup_datetime'
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    print(f"Preprocessing: rows with zero passengers: {data['passenger_count'].isin([0]).sum()}")
    print(f"Preprocessing: rows with zero trip distance: {data['trip_distance'].isin([0]).sum()}")

    unique_dates = data['lpep_pickup_date'].unique()
    sum_of_unique_dates = len(unique_dates)
    print("Sum of unique dates:", sum_of_unique_dates)

    # Filter rows with non-zero 'passenger_count' and non-zero 'trip_distance'
    return data[(data['passenger_count'] > 0) & (data['trip_distance'] != 0)]


@test
def test_output(output, *args):
    passenger_count_zeros = output['passenger_count'].isin([0]).sum()
    trip_distance_zeros = output['trip_distance'].isin([0]).sum()
    vendor_id_valid = output['vendor_id'].isin(output['vendor_id'].unique()).all()
    
    assert passenger_count_zeros == 0, f'There are {passenger_count_zeros} rides with zero passengers'
    assert trip_distance_zeros == 0, f'There are {trip_distance_zeros} rides with zero trip distance'
    assert vendor_id_valid, 'Not all vendor_id values are valid'
