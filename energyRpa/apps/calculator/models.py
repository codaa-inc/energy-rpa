from django.db import models

class CalcAerConc(models.Model):
    aer_conc_cd = models.AutoField(primary_key=True)
    aer_conc_nm = models.CharField(max_length=255)
    cvalue = models.FloatField(blank=True, null=True)
    use_yn = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calc_aer_conc'


class CalcExFinm(models.Model):
    ex_finm_cd = models.AutoField(primary_key=True)
    ex_finm_nm = models.CharField(max_length=255)
    cvalue = models.FloatField(blank=True, null=True)
    use_yn = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calc_ex_finm'


class CalcInsulm(models.Model):
    insulm_cd = models.AutoField(primary_key=True)
    insulm_nm = models.CharField(max_length=255)
    cvalue = models.FloatField(blank=True, null=True)
    use_yn = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calc_insulm'


class CalcLocalgvPoint(models.Model):
    localgv_point_cd = models.AutoField(primary_key=True)
    ex_wall_point = models.FloatField(blank=True, null=True)
    roof_point = models.FloatField(blank=True, null=True)
    floor_point = models.FloatField(blank=True, null=True)
    purps_cd = models.ForeignKey('common.CmnPurps', models.DO_NOTHING, db_column='purps_cd', blank=True, null=True)
    area_gb_cd = models.ForeignKey('common.CmnAreaGb', models.DO_NOTHING, db_column='area_gb_cd')
    point_yn = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calc_localgv_point'


class CalcMeanUvalue(models.Model):
    mean_uvalue_cd = models.AutoField(primary_key=True)
    ex_wall = models.FloatField(blank=True, null=True)
    roof = models.FloatField(blank=True, null=True)
    floor = models.FloatField(blank=True, null=True)
    point = models.FloatField(blank=True, null=True)
    purps_cd = models.ForeignKey('common.CmnPurps', models.DO_NOTHING, db_column='purps_cd')
    area_gb_cd = models.ForeignKey('common.CmnAreaGb', models.DO_NOTHING, db_column='area_gb_cd')

    class Meta:
        managed = False
        db_table = 'calc_mean_uvalue'


class CalcSalbRvalue(models.Model):
    slab_rvalue_cd = models.AutoField(primary_key=True)
    direct = models.FloatField(blank=True, null=True)
    indirect = models.FloatField(blank=True, null=True)
    area_gb_cd = models.ForeignKey('common.CmnAreaGb', models.DO_NOTHING, db_column='area_gb_cd')

    class Meta:
        managed = False
        db_table = 'calc_salb_rvalue'


class CalcSrfcRvalue(models.Model):
    srfc_rvalue_cd = models.AutoField(primary_key=True)
    outdoor = models.FloatField(blank=True, null=True)
    indoor = models.FloatField(blank=True, null=True)
    part_cd = models.ForeignKey('common.CmnPart', models.DO_NOTHING, db_column='part_cd')

    class Meta:
        managed = False
        db_table = 'calc_srfc_rvalue'


class CalcUvalue(models.Model):
    uvalue_cd = models.AutoField(primary_key=True)
    uvalue = models.FloatField()
    part_cd = models.ForeignKey('common.CmnPart', models.DO_NOTHING, db_column='part_cd')
    purps_cd = models.ForeignKey('common.CmnPurps', models.DO_NOTHING, db_column='purps_cd')
    area_gb_cd = models.ForeignKey('common.CmnAreaGb', models.DO_NOTHING, db_column='area_gb_cd')

    class Meta:
        managed = False
        db_table = 'calc_uvalue'


class CalcUvalueTmpl(models.Model):
    uvalue_tmpl_cd = models.BigAutoField(primary_key=True)
    wall_direct_width = models.FloatField(blank=True, null=True)
    wall_indirect_width = models.FloatField(blank=True, null=True)
    wall_direct_kind_1 = models.IntegerField(blank=True, null=True)
    wall_direct_thick_1 = models.IntegerField(blank=True, null=True)
    wall_indirect_kind_1 = models.IntegerField(blank=True, null=True)
    wall_indirect_thick_1 = models.IntegerField(blank=True, null=True)
    wall_direct_kind_2 = models.IntegerField(blank=True, null=True)
    wall_direct_thick_2 = models.IntegerField(blank=True, null=True)
    wall_indirect_kind_2 = models.IntegerField(blank=True, null=True)
    wall_indirect_thick_2 = models.IntegerField(blank=True, null=True)
    wall_direct_kind_3 = models.IntegerField(blank=True, null=True)
    wall_direct_thick_3 = models.IntegerField(blank=True, null=True)
    wall_indirect_kind_3 = models.IntegerField(blank=True, null=True)
    wall_indirect_thick_3 = models.IntegerField(blank=True, null=True)
    wall_direct_kind_4 = models.IntegerField(blank=True, null=True)
    wall_direct_thick_4 = models.IntegerField(blank=True, null=True)
    wall_indirect_kind_4 = models.IntegerField(blank=True, null=True)
    wall_indirect_thick_4 = models.IntegerField(blank=True, null=True)
    win_direct_width = models.FloatField(blank=True, null=True)
    win_indirect_width = models.FloatField(blank=True, null=True)
    win_direct_kind_1 = models.IntegerField(blank=True, null=True)
    win_indirect_kind_1 = models.IntegerField(blank=True, null=True)
    roof_direct_width = models.IntegerField(blank=True, null=True)
    roof_indirect_width = models.IntegerField(blank=True, null=True)
    roof_direct_kind_1 = models.IntegerField(blank=True, null=True)
    roof_direct_thick_1 = models.IntegerField(blank=True, null=True)
    roof_indirect_kind_1 = models.IntegerField(blank=True, null=True)
    roof_indirect_thick_1 = models.IntegerField(blank=True, null=True)
    roof_direct_kind_2 = models.IntegerField(blank=True, null=True)
    roof_direct_thick_2 = models.IntegerField(blank=True, null=True)
    roof_indirect_kind_2 = models.IntegerField(blank=True, null=True)
    roof_indirect_thick_2 = models.IntegerField(blank=True, null=True)
    roof_direct_kind_3 = models.IntegerField(blank=True, null=True)
    roof_direct_thick_3 = models.IntegerField(blank=True, null=True)
    roof_indirect_kind_3 = models.IntegerField(blank=True, null=True)
    roof_indirect_thick_3 = models.IntegerField(blank=True, null=True)
    floorb_direct_width = models.FloatField(blank=True, null=True)
    floorb_indirect_width = models.FloatField(blank=True, null=True)
    floorb_direct_kind_1 = models.IntegerField(blank=True, null=True)
    floorb_direct_thick_1 = models.IntegerField(blank=True, null=True)
    floorb_indirect_kind_1 = models.IntegerField(blank=True, null=True)
    floorb_indirect_thick_1 = models.IntegerField(blank=True, null=True)
    floorb_direct_kind_2 = models.IntegerField(blank=True, null=True)
    floorb_direct_thick_2 = models.IntegerField(blank=True, null=True)
    floorb_indirect_kind_2 = models.IntegerField(blank=True, null=True)
    floorb_indirect_thick_2 = models.IntegerField(blank=True, null=True)
    floor_direct_width = models.FloatField(blank=True, null=True)
    floor_indirect_width = models.FloatField(blank=True, null=True)
    floor_direct_kind_1 = models.IntegerField(blank=True, null=True)
    floor_direct_thick_1 = models.IntegerField(blank=True, null=True)
    floor_indirect_kind_1 = models.IntegerField(blank=True, null=True)
    floor_indirect_thick_1 = models.IntegerField(blank=True, null=True)
    floor_direct_kind_2 = models.IntegerField(blank=True, null=True)
    floor_direct_thick_2 = models.IntegerField(blank=True, null=True)
    floor_indirect_kind_2 = models.IntegerField(blank=True, null=True)
    floor_indirect_thick_2 = models.IntegerField(blank=True, null=True)
    floor_direct_kind_3 = models.IntegerField(blank=True, null=True)
    floor_direct_thick_3 = models.IntegerField(blank=True, null=True)
    floor_indirect_kind_3 = models.IntegerField(blank=True, null=True)
    floor_indirect_thick_3 = models.IntegerField(blank=True, null=True)
    floor_direct_kind_4 = models.IntegerField(blank=True, null=True)
    floor_direct_thick_4 = models.IntegerField(blank=True, null=True)
    floor_indirect_kind_4 = models.IntegerField(blank=True, null=True)
    floor_indirect_thick_4 = models.IntegerField(blank=True, null=True)
    floor_direct_kind_5 = models.IntegerField(blank=True, null=True)
    floor_direct_thick_5 = models.IntegerField(blank=True, null=True)
    floor_indirect_kind_5 = models.IntegerField(blank=True, null=True)
    floor_indirect_thick_5 = models.IntegerField(blank=True, null=True)
    purps_cd = models.IntegerField(blank=True, null=True)
    area_gb_cd = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    project_cd = models.IntegerField(blank=True, null=True)
    wrt_dt = models.DateTimeField(auto_now_add=True)

    def tmpl_save(self):
        self.save()

    class Meta:
        managed = False
        db_table = 'calc_uvalue_tmpl'


class CalcWin(models.Model):
    win_cd = models.AutoField(primary_key=True)
    win_nm = models.CharField(max_length=255)
    uvalue = models.FloatField(blank=True, null=True)
    use_yn = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calc_win'