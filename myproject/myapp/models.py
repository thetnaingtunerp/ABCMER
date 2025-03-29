from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class generator(models.Model):
    power_model = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.power_model


class anchor_site(models.Model):
    site_id = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    township = models.CharField(max_length=255, blank=True, null=True)
    generator = models.ForeignKey(generator, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_id

class team(models.Model):
    team_name = models.CharField(max_length=255)
    leader = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.team_name

class engineer_group(models.Model):
    team_name = models.ForeignKey(team, on_delete=models.CASCADE)
    team_member = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.team_member

class report_data(models.Model):
    site = models.ForeignKey(anchor_site, on_delete=models.CASCADE)
    engineer = models.ForeignKey(User, on_delete=models.CASCADE)
    fuel_cm = models.FloatField(default=0.00)
    fuel_liter = models.FloatField(default=0.00)

    dg_rh = models.FloatField(default=0.00)
    dg_kwh = models.FloatField(default=0.00)
    dg_avg_rh_day = models.FloatField(default=0.00)

    grid_kwh = models.FloatField(default=0.00)

    oml_load = models.FloatField(default=0.00)
    atom_load = models.FloatField(default=0.00)
    mpt_load = models.FloatField(default=0.00)
    mytel_load = models.FloatField(default=0.00)

    cabinet_vol = models.FloatField(default=0.00)

    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)