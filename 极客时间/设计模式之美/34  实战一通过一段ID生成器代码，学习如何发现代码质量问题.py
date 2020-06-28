class UnknownHostException(TypeError):
    pass

class IdGenerator():

    def __init__(self):
        import logging
        self.logger = logging.getLogger()

    def generator(self):
        import random
        import socket
        import string
        from datetime import datetime
        id = ''
        try:
            hostName = socket.gethostname()
            tokens = hostName.split("\\.")
            if len(tokens) > 0:
                hostName = tokens[len(tokens)-1]

            timeString = datetime.now().strftime('%Y%m%d%H%M%S')

            randomlib = string.ascii_letters + string.digits
            randomString = ''.join(random.sample(randomlib,6))
            randomChars = []
            count = 0
            while count < 8:
                randomascii = random.randint(0,122)
                if randomascii >= 48 and randomascii <= 57:
                    randomChars[count] = str('0' + (randomascii - 48))
                    count += 1
                elif randomascii >= 65 and randomascii <= 90:
                    randomChars[count] = str('A' + (randomascii - 65))
                    count += 1
                elif randomascii >= 97 and randomascii <= 122:
                    randomChars[count] = str('a' + (randomascii - 97))
                    count += 1
            id = f'{hostName}{timeString}{randomChars}'
        except UnknownHostException as e:
            self.logger.warn("Failed to get the host name.", e)
        return id


