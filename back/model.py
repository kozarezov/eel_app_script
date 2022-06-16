import peewee


db_settings = peewee.SqliteDatabase('settings.db')
db_script = peewee.SqliteDatabase('script.db')

class Settings(peewee.Model):
    abil1 = peewee.CharField()
    abil1_bool = peewee.BooleanField()
    abil2 = peewee.CharField()
    abil2_bool = peewee.BooleanField()
    abil3 = peewee.CharField()
    abil3_bool = peewee.BooleanField()
    abil4 = peewee.CharField()
    abil4_bool = peewee.BooleanField()

    item1 = peewee.CharField()
    item1_bool = peewee.BooleanField()
    item2 = peewee.CharField()
    item2_bool = peewee.BooleanField()
    item3 = peewee.CharField()
    item3_bool = peewee.BooleanField()
    item4 = peewee.CharField()
    item4_bool = peewee.BooleanField()
    item5 = peewee.CharField()
    item5_bool = peewee.BooleanField()
    item6 = peewee.CharField()
    item6_bool = peewee.BooleanField()
    item7 = peewee.CharField()
    item7_bool = peewee.BooleanField()
    item8 = peewee.CharField()
    item8_bool = peewee.BooleanField()

    choose_self = peewee.CharField()
    choose_all = peewee.CharField()
    choose_next = peewee.CharField()
    choose_another = peewee.CharField()

    class Meta:
        database = db_settings


class Script(peewee.Model):
    net = peewee.CharField()
    puf_choosen = peewee.CharField()
    combo = peewee.CharField()
    blink_slot = peewee.CharField()
    activate = peewee.CharField()

    class Meta:
        database = db_script

db_script.create_tables([Script])
db_settings.create_tables([Settings])