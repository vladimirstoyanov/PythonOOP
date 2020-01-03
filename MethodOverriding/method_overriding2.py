import datetime

class Logger(object):
        def log(self, message):
                print message

class TimestampLogger(Logger):
        def log(self, message):
                message = "{ts} {msg}".format(ts=datetime.datetime.now().isoformat(), msg=message)
                super(TimestampLogger, self).log(message)


if __name__ == "__main__":
        l = Logger()
        l.log('Hi!')
        t = TimestampLogger()
        t.log('Hi!')
        #result:
        #Hi!
        #2018-11-19T10:53:31.109373 Hi!

