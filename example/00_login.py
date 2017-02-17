from xing.xasession import Session

session = Session()
session.login('credential.conf')

print(session.account())
print(session.heartbeat())

session.logout()
