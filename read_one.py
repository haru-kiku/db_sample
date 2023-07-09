from db_config import Message


def find_message():
    id = 1
    msg = Message.get_by_id(id)
    print(msg.id, msg.user, msg.content, msg.pub_date)


if __name__ == "__main__":
    find_message()
