"""
The expected version of analysis/dataset_definition.py at the end of the workshop steps.
"""
from ehrql import create_dataset
from ehrql.tables.core import patients, clinical_events

index_date = "2020-03-31"

dataset = create_dataset()

age = patients.age_on(index_date)

dataset.define_population((age > 18) & (age < 80))
dataset.age = age
dataset.sex = patients.sex

events = clinical_events.sort_by(clinical_events.date).first_for_patient()
dataset.event_date = events.date
dataset.dob_year = patients.date_of_birth.year
dataset.dod_year = patients.date_of_death.year
