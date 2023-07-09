from db_config import Message


def display_all_message():
    for msg in Message.select():
        print(msg.id, msg.user, msg.content, msg.pub_date)


if __name__ == "__main__":
    # 以下の２行をdisplay_all_message()関数にまとめる
    display_all_message()
