# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Daneuzytkownikow(models.Model):
    iduzytkownika = models.AutoField(db_column='IdUzytkownika', primary_key=True)  # Field name made lowercase.
    plec = models.PositiveIntegerField()
    wiek = models.PositiveIntegerField()
    ulica = models.CharField(max_length=45)
    numerbudynku = models.PositiveIntegerField(db_column='numerBudynku')  # Field name made lowercase.
    numermieszkania = models.PositiveIntegerField(db_column='numerMieszkania', blank=True, null=True)  # Field name made lowercase.
    miasto = models.CharField(max_length=45)
    kodpocztowy = models.CharField(db_column='kodPocztowy', max_length=45)  # Field name made lowercase.
    nip = models.PositiveBigIntegerField(db_column='NIP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'daneuzytkownikow'


class Danezamowien(models.Model):
    iddanezamowien = models.AutoField(primary_key=True)
    iduzytkownika = models.CharField(db_column='idUzytkownika', max_length=45)  # Field name made lowercase.
    idkoszyka = models.PositiveIntegerField(db_column='idKoszyka')  # Field name made lowercase.
    numerbudynku = models.PositiveIntegerField(db_column='numerBudynku')  # Field name made lowercase.
    numermieszkania = models.PositiveIntegerField(db_column='numerMieszkania', blank=True, null=True)  # Field name made lowercase.
    kodpocztowy = models.CharField(db_column='kodPocztowy', max_length=45)  # Field name made lowercase.
    miasto = models.CharField(max_length=45)
    sposobplatnosci = models.PositiveIntegerField(db_column='sposobPlatnosci')  # Field name made lowercase.
    statusrealizacji = models.PositiveIntegerField(db_column='statusRealizacji')  # Field name made lowercase.
    data = models.DateField()

    class Meta:
        managed = False
        db_table = 'danezamowien'
        unique_together = (('iddanezamowien', 'iduzytkownika'),)


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
    id = models.BigAutoField(primary_key=True)
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


class Kategoria(models.Model):
    idkategoria = models.AutoField(db_column='idKategoria', primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='Nazwa', max_length=45)  # Field name made lowercase.
    kategoria = models.CharField(db_column='Kategoria', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kategoria'
        unique_together = (('idkategoria', 'nazwa'),)


class Koszyk(models.Model):
    idtab = models.AutoField(db_column='idTab', primary_key=True)  # Field name made lowercase.
    idkoszyk = models.PositiveIntegerField(db_column='idKoszyk')  # Field name made lowercase.
    idproduktow = models.PositiveIntegerField(db_column='idProduktow')  # Field name made lowercase.
    ilosc = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'koszyk'
        unique_together = (('idtab', 'idkoszyk'),)


class Liczbasztuk(models.Model):
    idliczbasztuk = models.AutoField(primary_key=True)
    idproduktu = models.PositiveIntegerField(db_column='idProduktu', unique=True)  # Field name made lowercase.
    ilosc = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'liczbasztuk'
        unique_together = (('idliczbasztuk', 'idproduktu'),)


class Produkty(models.Model):
    idprodukty = models.AutoField(db_column='idProdukty', primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(max_length=45)
    opis = models.TextField()
    zdjecie = models.CharField(max_length=500)
    netto = models.FloatField()
    brutto = models.FloatField(blank=True, null=True)
    podatek = models.FloatField()
    kategoria = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'produkty'


class Rabaty(models.Model):
    idrabaty = models.AutoField(db_column='idRabaty', primary_key=True)  # Field name made lowercase.
    iduzytkownika = models.PositiveIntegerField(db_column='idUzytkownika')  # Field name made lowercase.
    wartoscrabatu = models.FloatField(db_column='wartoscRabatu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rabaty'
        unique_together = (('idrabaty', 'iduzytkownika'),)


class Uzytkownicy(models.Model):
    iduzytkownicy = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=45)
    haslo = models.CharField(max_length=45, blank=True, null=True)
    iduzytkownika = models.PositiveIntegerField(db_column='idUzytkownika', unique=True, blank=True, null=True)  # Field name made lowercase.
    statuskonta = models.PositiveIntegerField(db_column='statusKonta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'uzytkownicy'
        unique_together = (('iduzytkownicy', 'imie', 'nazwisko', 'email'),)


class Zamowienia(models.Model):
    idzamowienia = models.AutoField(db_column='idZamowienia', primary_key=True)  # Field name made lowercase.
    iduzytkownika = models.PositiveIntegerField(db_column='idUzytkownika')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zamowienia'
