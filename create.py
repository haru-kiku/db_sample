from db_config import Message


def create_message():
    # インスタンスを作成してから保存
    message = Message(user="Bob", content="Hello Tom!")
    message.save()
    # インスタンスをそのまま保存
    Message.create(user="Tom", content="Hello Bob!")


if __name__ == "__main__":
    create_message()
