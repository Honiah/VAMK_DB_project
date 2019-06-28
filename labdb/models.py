# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Feed(models.Model):
    user = models.CharField(db_column='User', max_length=255, blank=True, null=True)  # Field name made lowercase.
    feed = models.CharField(db_column='Feed', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Feed'


class VamkCSmd(models.Model):
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    strenght = models.CharField(db_column='Strenght', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manufacturer_part_number = models.CharField(db_column='Manufacturer_Part_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location = models.CharField(db_column='Storing_Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location_ec19 = models.CharField(db_column='Storing_Location_EC19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ptypename = models.CharField(db_column='PtypeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tolerance = models.CharField(db_column='Tolerance', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_elfa = models.CharField(db_column='Order_Number_Elfa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_farnell = models.CharField(db_column='Order_Number_Farnell', max_length=255, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amount = models.CharField(db_column='Amount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ordered = models.CharField(db_column='Ordered', max_length=255, blank=True, null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='Signature', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VAMK_C_SMD'


class Vamk74Hcxx(models.Model):
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ptypename = models.CharField(db_column='PtypeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manufacturer_part_number = models.CharField(db_column='Manufacturer_Part_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location = models.CharField(db_column='Storing_Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location_ec19 = models.CharField(db_column='Storing_Location_EC19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_elfa = models.CharField(db_column='Order_Number_Elfa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_farnell = models.IntegerField(db_column='Order_Number_Farnell', blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ordered = models.CharField(db_column='Ordered', max_length=255, blank=True, null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='Signature', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vamk_74HCXX'


class VamkAna(models.Model):
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parttype = models.CharField(db_column='Parttype', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manufacturer_part_number = models.CharField(db_column='Manufacturer_Part_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location = models.CharField(db_column='Storing_Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location_ec19 = models.CharField(db_column='Storing_Location_EC19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    decal = models.CharField(db_column='Decal', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_elfa = models.CharField(db_column='Order_Number_Elfa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_farnell = models.CharField(db_column='Order_Number_Farnell', max_length=255, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ordered = models.CharField(db_column='Ordered', max_length=255, blank=True, null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='Signature', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vamk_Ana'


class VamkC(models.Model):
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    strenght = models.CharField(db_column='Strenght', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manufacturer_part_number = models.CharField(db_column='Manufacturer_Part_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location = models.CharField(db_column='Storing_Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location_ec19 = models.CharField(db_column='Storing_Location_EC19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ptypename = models.CharField(db_column='PtypeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tolerance = models.CharField(db_column='Tolerance', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_elfa = models.CharField(db_column='Order_Number_Elfa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_farnell = models.IntegerField(db_column='Order_Number_Farnell', blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    ordered = models.CharField(db_column='Ordered', max_length=255, blank=True, null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='Signature', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vamk_C'


class VamkCpu(models.Model):
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parttype = models.CharField(db_column='Parttype', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manufacturer_part_number = models.CharField(db_column='Manufacturer_Part_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location = models.CharField(db_column='Storing_Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location_ec19 = models.CharField(db_column='Storing_Location_EC19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_elfa = models.CharField(db_column='Order_Number_Elfa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_farnell = models.CharField(db_column='Order_Number_Farnell', max_length=255, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ordered = models.CharField(db_column='Ordered', max_length=255, blank=True, null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='Signature', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vamk_CPU'


class VamkCpuSmd(models.Model):
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parttype = models.CharField(db_column='Parttype', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manufacturer_part_number = models.CharField(db_column='Manufacturer_Part_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location = models.CharField(db_column='Storing_Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location_ec19 = models.CharField(db_column='Storing_Location_EC19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_elfa = models.CharField(db_column='Order_Number_Elfa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_farnell = models.CharField(db_column='Order_Number_Farnell', max_length=255, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ordered = models.CharField(db_column='Ordered', max_length=255, blank=True, null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='Signature', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amount = models.CharField(db_column='Amount', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vamk_CPU_SMD'


class VamkCon(models.Model):
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parttype = models.CharField(db_column='Parttype', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manufacturer_part_number = models.CharField(db_column='Manufacturer_Part_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location = models.CharField(db_column='Storing_Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location_ec19 = models.CharField(db_column='Storing_Location_EC19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_elfa = models.CharField(db_column='Order_Number_Elfa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_farnell = models.CharField(db_column='Order_Number_Farnell', max_length=255, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ordered = models.CharField(db_column='Ordered', max_length=255, blank=True, null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='Signature', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vamk_Con'


class VamkD(models.Model):
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manufacturer_part_number = models.CharField(db_column='Manufacturer_Part_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location = models.CharField(db_column='Storing_Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location_ec19 = models.CharField(db_column='Storing_Location_EC19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ptypename = models.CharField(db_column='PtypeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    voltage_rating = models.CharField(db_column='Voltage_Rating', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_elfa = models.CharField(db_column='Order_Number_Elfa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_farnell = models.CharField(db_column='Order_Number_Farnell', max_length=255, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ordered = models.CharField(db_column='Ordered', max_length=255, blank=True, null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='Signature', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vamk_D'


class VamkIc(models.Model):
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parttype = models.CharField(db_column='Parttype', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manufacturer_part_number = models.CharField(db_column='Manufacturer_Part_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location = models.CharField(db_column='Storing_Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location_ec19 = models.CharField(db_column='Storing_Location_EC19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_elfa = models.CharField(db_column='Order_Number_Elfa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_farnell = models.CharField(db_column='Order_Number_Farnell', max_length=255, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ordered = models.CharField(db_column='Ordered', max_length=255, blank=True, null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='Signature', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vamk_IC'


class VamkIcSmd(models.Model):
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parttype = models.CharField(db_column='Parttype', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manufacturer_part_number = models.CharField(db_column='Manufacturer_Part_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location = models.CharField(db_column='Storing_Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location_ec19 = models.CharField(db_column='Storing_Location_EC19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_elfa = models.CharField(db_column='Order_Number_Elfa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_farnell = models.CharField(db_column='Order_Number_Farnell', max_length=255, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ordered = models.CharField(db_column='Ordered', max_length=255, blank=True, null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='Signature', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vamk_IC_SMD'


class VamkMisc(models.Model):
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parttype = models.CharField(db_column='Parttype', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manufacturer_part_number = models.CharField(db_column='Manufacturer_Part_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location = models.CharField(db_column='Storing_Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location_ec19 = models.CharField(db_column='Storing_Location_EC19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_elfa = models.CharField(db_column='Order_Number_Elfa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_farnell = models.CharField(db_column='Order_Number_Farnell', max_length=255, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ordered = models.CharField(db_column='Ordered', max_length=255, blank=True, null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='Signature', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vamk_Misc'


class VamkR(models.Model):
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    strenght = models.CharField(db_column='Strenght', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manufacturer_part_number = models.CharField(db_column='Manufacturer_Part_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location = models.CharField(db_column='Storing_Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location_ec19 = models.CharField(db_column='Storing_Location_EC19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ptypename = models.CharField(db_column='PtypeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tolerance = models.CharField(db_column='Tolerance', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_elfa = models.CharField(db_column='Order_Number_Elfa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_farnell = models.CharField(db_column='Order_Number_Farnell', max_length=255, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ordered = models.CharField(db_column='Ordered', max_length=255, blank=True, null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='Signature', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amount = models.CharField(db_column='Amount', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vamk_R'


class VamkRSmd(models.Model):
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    strenght = models.CharField(db_column='Strenght', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manufacturer_part_number = models.CharField(db_column='Manufacturer_Part_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location = models.CharField(db_column='Storing_Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location_ec19 = models.CharField(db_column='Storing_Location_EC19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ptypename = models.CharField(db_column='PtypeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tolerance = models.CharField(db_column='Tolerance', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_elfa = models.CharField(db_column='Order_Number_Elfa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_farnell = models.IntegerField(db_column='Order_Number_Farnell', blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ordered = models.CharField(db_column='Ordered', max_length=255, blank=True, null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='Signature', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amount = models.CharField(db_column='Amount', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vamk_R_SMD'


class VamkSocket(models.Model):
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    socket = models.CharField(db_column='Socket', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manufacturer_part_number = models.CharField(db_column='Manufacturer_Part_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    storing_location = models.CharField(db_column='Storing_Location', max_length=11, blank=True, null=True)  # Field name made lowercase.
    storing_location_ec19 = models.CharField(db_column='Storing_Location_EC19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_elfa = models.CharField(db_column='Order_Number_Elfa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_number_farnell = models.IntegerField(db_column='Order_Number_Farnell', blank=True, null=True)  # Field name made lowercase.
    order_number_partco = models.CharField(db_column='Order_Number_Partco', max_length=255, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ordered = models.CharField(db_column='Ordered', max_length=255, blank=True, null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='Signature', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vamk_Socket'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
