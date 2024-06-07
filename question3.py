class Message:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.message_body = ""

    def get_sender(self):
        return self.sender

    def get_recipient(self):
        return self.recipient

    def append(self, text):
        self.message_body += text + "\n"

    def to_string(self):
        return f"From: {self.get_sender()} \nTo: {self.get_recipient()}\n{self.message_body}"
# Instead of using def to_string... I could have used the __str__ method.
# I think that would have been better because it would have called the method automatically when trying to
# convert the object to a string.
# Like this:
# def __str__(self):
# return f"From: {self.get_sender()} \nTo: {self.get_recipient()}\n{self.message_body}"
# Then I could have used print(message) instead of print(message.to_string())


message = Message("Harry Morgan", "Rudolf Reindeer")
message.append("Hey Rudolf. Hows the weather? Is it snowing? Are you ready for Christmas? \nBest regards, "
               "\nHarry Morgan")

print(message.to_string())
