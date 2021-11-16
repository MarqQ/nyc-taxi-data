from django.db import models


class TaxiData(models.Model):
    vendor_id = models.IntegerField(default=False)
    tpep_pickup_datetime = models.DateTimeField(default=False)
    tpep_dropoff_datetime = models.DateTimeField(default=False)
    passenger_count = models.FloatField(default=False)
    trip_distance = models.FloatField(default=False)
    ratecode_id = models.FloatField(default=False)
    store_and_fwd_flag = models.CharField(max_length=1)
    pulocation_id = models.IntegerField(default=False)
    dolocation_id = models.IntegerField(default=False)
    payment_type = models.FloatField(default=False)
    fare_amount = models.FloatField(default=False)
    extra = models.FloatField(default=False)
    mta_tax = models.FloatField(default=False)
    tip_amount = models.FloatField(default=False)
    tolls_amount = models.FloatField(default=False)
    improvement_surcharge = models.FloatField(default=False)
    total_amount = models.FloatField(default=False)
    congestion_surcharge = models.FloatField(default=False)

    class Meta:
        db_table = 'nyc_taxi_data'

    def __str__(self):
        return self.vendor_id
