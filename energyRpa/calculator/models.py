from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CalcAerConc(models.Model):
    aer_conc_cd = models.AutoField(primary_key=True)
    aer_conc_nm = models.CharField(max_length=255)
    cvalue = models.FloatField(blank=True, null=True)
    use_yn = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calc_aer_conc'


class CalcAreaGb(models.Model):
    area_gb_cd = models.AutoField(primary_key=True)
    area_gb_nm = models.CharField(max_length=255)
    use_yn = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calc_area_gb'


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
    purps_cd = models.ForeignKey('CalcPurps', models.DO_NOTHING, db_column='purps_cd', blank=True, null=True)
    area_gb_cd = models.ForeignKey(CalcAreaGb, models.DO_NOTHING, db_column='area_gb_cd')
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
    purps_cd = models.ForeignKey('CalcPurps', models.DO_NOTHING, db_column='purps_cd')
    area_gb_cd = models.ForeignKey(CalcAreaGb, models.DO_NOTHING, db_column='area_gb_cd')

    class Meta:
        managed = False
        db_table = 'calc_mean_uvalue'


class CalcPart(models.Model):
    part_cd = models.AutoField(primary_key=True)
    part_nm = models.CharField(max_length=255)
    use_yn = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calc_part'


class CalcPurps(models.Model):
    purps_cd = models.AutoField(primary_key=True)
    purps_nm = models.CharField(max_length=255)
    use_yn = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calc_purps'


class CalcSalbRvalue(models.Model):
    slab_rvalue_cd = models.AutoField(primary_key=True)
    direct = models.FloatField(blank=True, null=True)
    indirect = models.FloatField(blank=True, null=True)
    area_gb_cd = models.ForeignKey(CalcAreaGb, models.DO_NOTHING, db_column='area_gb_cd')

    class Meta:
        managed = False
        db_table = 'calc_salb_rvalue'


class CalcSrfcRvalue(models.Model):
    srfc_rvalue_cd = models.AutoField(primary_key=True)
    outdoor = models.FloatField(blank=True, null=True)
    indoor = models.FloatField(blank=True, null=True)
    part_cd = models.ForeignKey(CalcPart, models.DO_NOTHING, db_column='part_cd')

    class Meta:
        managed = False
        db_table = 'calc_srfc_rvalue'


class CalcUvalue(models.Model):
    uvalue_cd = models.AutoField(primary_key=True)
    uvalue = models.FloatField()
    part_cd = models.ForeignKey(CalcPart, models.DO_NOTHING, db_column='part_cd')
    purps_cd = models.ForeignKey(CalcPurps, models.DO_NOTHING, db_column='purps_cd')
    area_gb_cd = models.ForeignKey(CalcAreaGb, models.DO_NOTHING, db_column='area_gb_cd')

    class Meta:
        managed = False
        db_table = 'calc_uvalue'


class CalcUvalueTmpl(models.Model):
    uvalue_tmpl_cd = models.AutoField(primary_key=True)
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
    purps_cd = models.ForeignKey(CalcPurps, models.DO_NOTHING, db_column='purps_cd')
    area_gb_cd = models.ForeignKey(CalcAreaGb, models.DO_NOTHING, db_column='area_gb_cd')
    username = models.CharField(max_length=150, blank=True, null=True)
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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
