from db_config import Message

def update_message():
    msg_id = input("編集するメッセージのIDを入力してください > ")
    msg = Message.select().where(Message. id == msg_id).get()
    print(f"{msg.id} {msg.user} {msg.content} {msg.pub_date}")
    msg.content = input("新しいメッセージを入力してください｡")

    msg.save()
    


def delete_message():
    msg_id = input("削除するメッセージのIDを入力してください > ")
    msg = Message.select().where(Message. id == msg_id).get()
    if not msg.delete_instance():
        print("削除に失敗しました｡IDを再度確認してください｡")


def main():
    user_name = input("ユーザー名を入力してください > ")

    message = ""  # 繰り返し条件の初期化

    while True:
        for msg in Message.select():
            print(f"{msg.id} {msg.user} {msg.content} {msg.pub_date}")

        message = input("メッセージを入力してください > ")

        if message == "\\q":
            break

        if message == "\\d":
            delete_message()
            continue  # 以降の処理をスキップして次のループに映る
        
        if message == "\\e":
            update_message()
            continue
            

        Message.create(user=user_name, content=message)



if __name__ == "__main__":
    main()
