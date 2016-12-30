from __future__ import unicode_literals

from django.db import models
import uuid

class Config(models.Model):
    config_name = (
            ('BackupMethod', 'BackupMethod'),
            ('BackupScheduling', 'BackupScheduling'),
            ('BackupMonthlyDate', 'BackupMonthlyDate'),
            ('BackupWeeklyDate', 'BackupWeeklyDate'),
            ('BackupTime', 'BackupTime'),
            ('BackupLocation', 'BackupLocation'),
            ('BackupLocal', 'BackupLocal'),
            ('BackupRemoteHost', 'BackupRemoteHost'),
            ('BackupRemotePort', 'BackupRemotePort'),
            ('BackupRemoteAccount', 'BackupRemoteAccount'),
            ('BackupRemotePassword', 'BackupRemotePassword'),
            ('LogLimit', 'LogLimit'),
            ('LogPreservation', 'LogPreservation'),
            ('PicCreateSave', 'PicCreateSave'),
            ('PicFaceSave', 'PicFaceSave'),
    )
    oid = models.CharField(db_column = 'OId', primary_key = True, default = uuid.uuid1, max_length = 36)
    name = models.CharField(db_column = 'Name', choices = config_name, unique = True, max_length = 32)
    value = models.CharField(db_column = 'Value', max_length = 512)
    createdate = models.DateTimeField(db_column = 'CreateDate', auto_now_add = True)
    updatedate = models.DateTimeField(db_column = 'UpdateDate', auto_now = True)

    class Meta:
        db_table = 'config'

    def __str__(self):
        return '%s (%s)' % (self.name, self.oid)


class Role(models.Model):
    role_category = (
            ('System', 'System'),
            ('User', 'User'),
    )
    oid = models.CharField(db_column = 'OId', primary_key = True, default = uuid.uuid1, max_length = 36)
    name = models.CharField(db_column = 'Name', unique = True, max_length = 32)
    sort = models.IntegerField(db_column = 'Sort')
    category = models.CharField(db_column = 'Category', choices = role_category, default = 'User', max_length = 68)
    createdate = models.DateTimeField(db_column = 'CreateDate', auto_now_add = True)
    updatedate = models.DateTimeField(db_column = 'UpdateDate', auto_now = True)

    class Meta:
        db_table = 'role'

    def __str__(self):
        return '%s (%s)' % (self.name, self.oid)


class Acl(models.Model):
    acl_acl = (
            ('Enable', 'Enable'),
            ('Disable', 'Disable'),
    )
    oid = models.CharField(db_column = 'OId', primary_key = True, default = uuid.uuid1, max_length = 36)
    functionname = models.CharField(db_column = 'FunctionName', max_length = 32)
    roleoid = models.ForeignKey('Role', on_delete = models.CASCADE, db_column = 'RoleOId', max_length = 36)
    acl = models.CharField(db_column = 'ACL', choices = acl_acl, default = 'Enable', max_length = 8)
    createdate = models.DateTimeField(db_column = 'CreateDate', auto_now_add = True)
    updatedate = models.DateTimeField(db_column = 'UpdateDate', auto_now = True)

    class Meta:
        db_table = 'acl'

    def __str__(self):
        return '%s (%s)' % (self.functionname, self.oid)


class Devices(models.Model):
    devices_state = (
            ('Proposed', 'Proposed'),
            ('Approved', 'Approved'),
            ('Setting', 'Setting'),
            ('Getting', 'Getting'),
            ('Online', 'Online'),
            ('Offline', 'Offline'),
    )
    devices_welcome = (
            ('Do0', 'None'),
            ('Do1', 'Pulse 3 Sec'),
    )
    devices_accessdenied = (
            ('Do0', 'On'),
            ('Do1', 'Off'),
    )
    devices_screensaver = (
            ('5', '5 Minutes'),
            ('30', '30 Minutes'),
            ('60', '60 Minutes'),
    )
    devices_timezone = (
            ('UTC-12', 'UTC-12'),
            ('UTC-11', 'UTC-11'),
            ('UTC-10', 'UTC-10'),
            ('UTC-9', 'UTC-9'),
            ('UTC-8', 'UTC-8'),
            ('UTC-7', 'UTC-7'),
            ('UTC-6', 'UTC-6'),
            ('UTC-5', 'UTC-5'),
            ('UTC-4', 'UTC-4'),
            ('UTC-3', 'UTC-3'),
            ('UTC-2', 'UTC-2'),
            ('UTC-1', 'UTC-1'),
            ('UTC+0', 'UTC+0'),
            ('UTC+1', 'UTC+1'),
            ('UTC+2', 'UTC+2'),
            ('UTC+3', 'UTC+3'),
            ('UTC+4', 'UTC+4'),
            ('UTC+5', 'UTC+5'),
            ('UTC+6', 'UTC+6'),
            ('UTC+7', 'UTC+7'),
            ('UTC+8', 'UTC+8'),
            ('UTC+9', 'UTC+9'),
            ('UTC+10', 'UTC+10'),
            ('UTC+11', 'UTC+11'),
            ('UTC+12', 'UTC+12'),
            ('UTC+13', 'UTC+13'),
            ('UTC+14', 'UTC+14'),
    )
    devices_audio = (
            ('Enable', 'Enable'),
            ('Disable', 'Disable'),
    )
    devices_bioscore = (
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('High', 'High'),
    )
    devices_language = (
            ('en', 'en'),
            ('zh-cn', 'zh-cn'),
            ('zh-tw', 'zh-tw'),
    )
    oid = models.CharField(db_column = 'OId', primary_key = True, default = uuid.uuid1, max_length = 36)
    name = models.CharField(db_column = 'Name', unique = True, max_length = 32)
    state = models.CharField(db_column = 'State', choices = devices_state, default = 'Proposed', max_length = 8)
    mac = models.CharField(db_column = 'MAC', max_length = 32, blank = True, null = True)
    ip = models.GenericIPAddressField(db_column = 'IP', max_length = 32, blank = True, null = True)
    welcome = models.CharField(db_column = 'Welcome', choices = devices_welcome, max_length = 8, blank = True, null = True)
    accessdenied = models.CharField(db_column = 'AccessDenied', choices = devices_accessdenied, max_length = 8, blank = True, null = True)
    screensaver = models.CharField(db_column = 'ScreenSaver', choices = devices_screensaver, max_length = 8, blank = True, null = True)
    ntp = models.CharField(db_column = 'NTP', max_length = 256, blank = True, null = True)
    timezone = models.CharField(db_column = 'Timezone', choices = devices_timezone, max_length = 8, blank = True, null = True)
    audio = models.CharField(db_column = 'Audio', choices = devices_audio, max_length = 8, blank = True, null = True)
    bioscore = models.CharField(db_column = 'BioScore', choices = devices_bioscore, max_length = 8, blank = True, null = True)
    language = models.CharField(db_column = 'Language', choices = devices_language, max_length = 8, blank = True, null = True)
    createdate = models.DateTimeField(db_column = 'CreateDate', auto_now_add = True)
    updatedate = models.DateTimeField(db_column = 'UpdateDate', auto_now = True)

    class Meta:
        db_table = 'devices'

    def __str__(self):
        return '%s (%s)' % (self.name, self.oid)


class Users(models.Model):
    oid = models.CharField(db_column = 'OId', primary_key = True, default = uuid.uuid1, max_length = 36)
    account = models.CharField(db_column = 'Account', unique = True, max_length = 255)
    password = models.CharField(db_column = 'Password', max_length = 64)
    name = models.CharField(db_column = 'Name', max_length = 32, blank = True, null = True)
    email = models.EmailField(db_column = 'Email', max_length = 256, blank = True, null = True)
    roleoid = models.ForeignKey(Role, on_delete = models.CASCADE, db_column = 'RoleOId', max_length = 36)
    createdate = models.DateTimeField(db_column = 'CreateDate', auto_now_add = True)
    updatedate = models.DateTimeField(db_column = 'UpdateDate', auto_now = True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return '%s (%s)' % (self.account, self.oid)


class Usergroups(models.Model):
    oid = models.CharField(db_column = 'OId', primary_key = True, default = uuid.uuid1, max_length = 36)
    name = models.CharField(db_column = 'Name', unique = True, max_length = 32)
    createdate = models.DateTimeField(db_column = 'CreateDate', auto_now_add = True)
    updatedate = models.DateTimeField(db_column = 'UpdateDate', auto_now = True)

    class Meta:
        db_table = 'usergroups'

    def __str__(self):
        return '%s (%s)' % (self.name, self.oid)


class Usergroupmember(models.Model):
    oid = models.CharField(db_column = 'OId', primary_key = True, default = uuid.uuid1, max_length = 36)
    groupoid = models.ForeignKey('Usergroups', on_delete = models.CASCADE, db_column = 'GroupOId', max_length = 36)
    useroid = models.ForeignKey('Users', on_delete = models.CASCADE, db_column = 'UserOId', max_length = 36)
    createdate = models.DateTimeField(db_column = 'CreateDate', auto_now_add = True)
    updatedate = models.DateTimeField(db_column = 'UpdateDate', auto_now = True)

    class Meta:
        db_table = 'usergroupmember'

    def __str__(self):
        return '%s %s' % (self.groupoid, self.useroid)


class Usergroupdevices(models.Model):
    oid = models.CharField(db_column = 'OId', primary_key = True, default = uuid.uuid1, max_length = 36)
    groupoid = models.ForeignKey('Usergroups', on_delete = models.CASCADE, db_column = 'GroupOId', max_length = 36)
    deviceoid = models.ForeignKey('Devices', on_delete = models.CASCADE, db_column = 'DeviceOId', max_length = 36)
    createdate = models.DateTimeField(db_column = 'CreateDate', auto_now_add = True)
    updatedate = models.DateTimeField(db_column = 'UpdateDate', auto_now = True)

    class Meta:
        db_table = 'usergroupdevices'

    def __str__(self):
        return '%s %s' % (self.groupoid, self.deviceoid)


class Frusers(models.Model):
    frusers_gender = (
            ('Male', 'Male'),
            ('Female', 'Female'),
    )
    frusers_state = (
            ('Enable', 'Enable'),
            ('Disable', 'Disable'),
    )
    oid = models.CharField(db_column = 'OId', primary_key = True, default = uuid.uuid1, max_length = 36)
    fruserid = models.CharField(db_column = 'FRUserId', max_length = 16)
    name = models.CharField(db_column = 'Name', max_length = 32, blank = True, null = True)
    gender = models.CharField(db_column = 'Gender', choices = frusers_gender, max_length = 8, blank = True, null = True)
    age = models.IntegerField(db_column = 'Age', blank = True, null = True)
    personid = models.CharField(db_column = 'PersonId', max_length = 32, blank = True, null = True)
    face1 = models.CharField(db_column = 'Face1', max_length = 256, blank = True, null = True)
    face2 = models.CharField(db_column = 'Face2', max_length = 256, blank = True, null = True)
    face3 = models.CharField(db_column = 'Face3', max_length = 256, blank = True, null = True)
    faceid1 = models.CharField(db_column = 'FaceID1', max_length = 32, blank = True, null = True)
    faceid2 = models.CharField(db_column = 'FaceID2', max_length = 32, blank = True, null = True)
    faceid3 = models.CharField(db_column = 'FaceID3', max_length = 32, blank = True, null = True)
    rfidcard = models.CharField(db_column = 'RFIDCard', max_length = 16, blank = True, null = True)
    state = models.CharField(db_column = 'State', choices = frusers_state, default = 'Enable', max_length = 8)
    disablecauses = models.CharField(db_column = 'DisableCauses', max_length = 256, blank = True, null = True)
    createdate = models.DateTimeField(db_column = 'CreateDate', auto_now_add = True)
    updatedate = models.DateTimeField(db_column = 'UpdateDate', auto_now = True)

    class Meta:
        db_table = 'frusers'

    def __str__(self):
        return '%s %s (%s)' % (self.fruserid, self.name, self.oid)


class Frusergroups(models.Model):
    oid = models.CharField(db_column = 'OId', primary_key = True, default = uuid.uuid1, max_length = 36)
    name = models.CharField(db_column = 'Name', unique = True, max_length = 32)
    createdate = models.DateTimeField(db_column = 'CreateDate', auto_now_add = True)
    updatedate = models.DateTimeField(db_column = 'UpdateDate', auto_now = True)

    class Meta:
        db_table = 'frusergroups'

    def __str__(self):
        return '%s (%s)' % (self.name, self.oid)


class Frusergroupmember(models.Model):
    oid = models.CharField(db_column = 'OId', primary_key = True, default = uuid.uuid1, max_length = 36)
    groupoid = models.ForeignKey('Frusergroups', on_delete = models.CASCADE, db_column = 'GroupOId', max_length = 36)
    fruseroid = models.ForeignKey('Frusers', on_delete = models.CASCADE, db_column = 'FRUserOId', max_length = 36)
    createdate = models.DateTimeField(db_column = 'CreateDate', auto_now_add = True)
    updatedate = models.DateTimeField(db_column = 'UpdateDate', auto_now = True)

    class Meta:
        db_table = 'frusergroupmember'

    def __str__(self):
        return '%s %s' % (self.groupoid, self.fruseroid)


class Frusergroupdevices(models.Model):
    oid = models.CharField(db_column = 'OId', primary_key = True, default = uuid.uuid1, max_length = 36)
    groupoid = models.ForeignKey('Frusergroups', on_delete = models.CASCADE, db_column = 'GroupOId', max_length = 36)
    deviceoid = models.ForeignKey('Devices', on_delete = models.CASCADE, db_column = 'DeviceOId', max_length = 36)
    createdate = models.DateTimeField(db_column = 'CreateDate', auto_now_add = True)
    updatedate = models.DateTimeField(db_column = 'UpdateDate', auto_now = True)

    class Meta:
        db_table = 'frusergroupdevices'

    def __str__(self):
        return '%s %s' % (self.groupoid, self.deviceoid)


class Fruserlogs(models.Model):
    oid = models.CharField(db_column = 'OId', primary_key = True, default = uuid.uuid1, max_length = 36)
    logdatetime = models.DateTimeField(db_column = 'LogDateTime', auto_now_add =  True)
    fruseroid = models.ForeignKey('Frusers', on_delete = models.DO_NOTHING, db_column = 'FRUserOId', max_length = 36, blank = True, null = True)
    deviceoid = models.ForeignKey('Devices', on_delete = models.DO_NOTHING, db_column = 'DeviceOId', max_length = 36)
    logcontent = models.CharField(db_column = 'LogContent', max_length = 256, blank = True, null = True)

    class Meta:
        db_table = 'fruserlogs'

    def __str__(self):
        return '%s %s' % (self.fruseroid,  self.deviceoid)


class Systemlogs(models.Model):
    systemlogs_category = (
            ('System', 'System'),
            ('Device', 'Device'),
            ('User', 'User'),
            ('FRUser', 'FRUser'),
    )
    oid = models.CharField(db_column = 'OId', primary_key = True, default = uuid.uuid1, max_length = 36)
    logdatetime = models.DateTimeField(db_column = 'LogDateTime', auto_now_add = True)
    category = models.CharField(db_column = 'Category', choices = systemlogs_category, max_length = 8)
    logcontent = models.CharField(db_column = 'LogContent', max_length = 256, blank = True, null = True)

    class Meta:
        db_table = 'systemlogs'

    def __str__(self):
        return '%s %s' % (self.category, self.logdatetime)
