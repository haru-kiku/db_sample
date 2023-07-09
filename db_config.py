import os
import datetime
import logging
from playhouse.db_url import connect
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField, TextField, TimestampField

# .envの読み込み
load_dotenv()


logger = logging.getLogger("peewee")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

# データベースの接続設定
db = connect(os.environ.get("DATABASE"))

# 接続NGの場合はメッセージを表示
if not db .connect():
    print("接続NG")
    exit()

# メッセージのモデル
class Message(Model):
    """Message Model"""

    id = IntegerField(primary_key=True)  # idは自動で追加されるが明示
    user = CharField()
    content = TextField()
    pub_date = TimestampField(default=datetime.datetime.now())  # 何も指定しない場合は現在時刻が入る

    class Meta:
        database = db
        table_name = "messages"


db.create_tables([Message])
