from exchangelib import Credentials, Account, DELEGATE, Configuration, FaultTolerance, Message, Mailbox

credentials = Credentials(username='jingshengshi0616@163.com', password='sjszues616')
config = Configuration(server='IMAP.163.com:143', credentials=credentials)
account = Account(primary_smtp_address='jingshengshi0616@163.com', config=config,
                  autodiscover=True, access_type=DELEGATE)
from exchangelib.autodiscover import Autodiscovery
Autodiscovery.INITIAL_RETRY_POLICY = FaultTolerance(max_wait=30)

m = Message(
    account=account,
    subject='Daily motivation',
    body='All bodies are beautiful',
    to_recipients=[
        Mailbox(email_address='jingshengshi0616@163.com'),
    ],
    # cc_recipients=['carl@example.com', 'denice@example.com'],  # Simple strings work, too
    # bcc_recipients=[
    #     Mailbox(email_address='erik@example.com'),
    #     'felicity@example.com',
    # ],  # Or a mix of both
)
m.send()