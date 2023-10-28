class Email:
    def __init__(self, sender, receiver, content):
        self.is_sent = False
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


email_list = []
while True:
    command = input().split()
    if command[0] == "Stop":
        break
    else:
        sending = command[0]
        receiving = command[1]
        contender = command[2]
        email = Email(sending, receiving, contender)
        email_list.append(email)

indices = input().split(", ")
for index in indices:
    index = int(index)
    email_list[index].send()
for mails in email_list:
    print(mails.get_info())

