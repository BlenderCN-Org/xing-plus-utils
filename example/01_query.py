from xing.xasession import Session
from xingutils.query import Query
from pprint import pprint
import time


if __name__ == "__main__":
    session = Session()
    session.login('credential.conf')
    session.heartbeat()

    data = Query("주식현재가호가조회").send(shcode="122630")
    pprint(data)

    session.logout()
