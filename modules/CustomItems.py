import re
class Errors:
    class UnknownError:
        pass
    class TestError:
        pass
    class JackBooooksError:
        pass
class RegExTypes():
    email = r'^[A-Za-z0-9_]+@[A-Za-z0-9_]+\.[A-Za-z]{2,}$'
    allOrEmpty = r'^[\s\S]*$'
    allButNotEmpty = r'^[\s\S]+$'
    @staticmethod
    def rematch(type,text):
        return bool(re.match(type,text))
    @staticmethod
    def compile(type_,text):
        pattern = re.compile(type_,flags=0)
        return pattern.match(text)
def runtest(f,*a,**ka):
    try:
        r = f(*a,**ka)
        return r, None
    except Exception as e:
        return None, e