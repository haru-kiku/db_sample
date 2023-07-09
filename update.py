from db_config import Message
from read_all import display_all_message




def update_message():
    msg = Message.get_by_id(3)
    msg.user = "Tom Ford"
    msg.save()


if __name__ == "__main__":
    display_all_message()
    update_message()
