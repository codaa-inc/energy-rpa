from django.db import models

class CmnAreaGb(models.Model):
    area_gb_cd = models.AutoField(primary_key=True)
    area_gb_nm = models.CharField(max_length=255)
    use_yn = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmn_area_gb'


class CmnPart(models.Model):
    part_cd = models.AutoField(primary_key=True)
    part_nm = models.CharField(max_length=255)
    use_yn = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmn_part'


class CmnPrgStat(models.Model):
    prg_stat_cd = models.AutoField(primary_key=True)
    prg_stat_nm = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmn_prg_stat'


class CmnProject(models.Model):
    project_cd = models.AutoField(primary_key=True)
    project_nm = models.CharField(max_length=150, blank=True, null=True)
    company = models.CharField(max_length=150, blank=True, null=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    purps_cd = models.IntegerField()
    purps_nm = models.CharField(max_length=150, blank=True, null=True)
    area_gb_cd = models.IntegerField()
    prg_stat_cd = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=255)
    sigungu_cd = models.CharField(max_length=5)
    bjdong_cd = models.CharField(max_length=5)
    pnu = models.CharField(max_length=30)
    tot_area = models.FloatField(blank=True, null=True)
    lndcgr_code_nm = models.CharField(max_length=45, blank=True, null=True)
    plat_area = models.FloatField(blank=True, null=True)
    jijigu_cd_nm = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmn_project'



class CmnPurps(models.Model):
    purps_cd = models.AutoField(primary_key=True)
    purps_nm = models.CharField(max_length=255)
    is_resident = models.CharField(max_length=10, blank=True, null=True)
    use_yn = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmn_purps'