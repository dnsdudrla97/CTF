# -*- coding: utf-8 -*- 
from Crypto.Cipher import AES
import base64

def a(c, i):
    return (c & ((1 << i) ^ 65535)) & 0xffff
    
def b(c, i):
    return (c | (1 << i)) & 0xffff

def c(c, i):
    return ((c & (1 << i)) >> i) & 0xffff

def d(s, num):
    res = ''
    if num == 0:
        return ''
    for i in range(len(s)):
        charAt = ord(s[i])
        cc = num >> (i % 4)
        i3 = i % 3
        if i3 == 0:
            for j in range(0, 8, 2):
                c2 = c(charAt, j) ^ c(cc, j)
                if c2 == 0:
                    charAt = a(charAt, j)
                elif c2 == 1:
                    charAt = b(charAt, j)
        elif i3 == 1:
            for j in range(1, 8, 2):
                c3 = c(charAt, j) ^ c(cc, j)
                if c3 == 0:
                    charAt = a(charAt, j)
                elif c3 == 1:
                    charAt = b(charAt, j)
        elif i3 == 2:
            for j in range(8):
                c4 = c(charAt, j) ^ c(cc, j)
                if c4 == 0:
                    charAt = a(charAt, j)
                elif c4 == 1:
                    charAt = b(charAt, j)
        res += chr(charAt ^ 1)
    return res

# a_class_decrypt = [
#     d(base64.b64encode(">JÂ0ûDwù¯0Õ´zhÝ!ë\u000ff"), -989022505),
#     d(base64.b64encode("rî:MGì0BSvn"), -2055632580),
#     d(base64.b64encode("+À0­0G¤nò\r3È6"), 675347394),
#     d(base64.b64encode("QLÜkh^F,j_È\u0015%Yî Oukd"), -1263812037),
#     d(base64.b64encode("zè3`y§&QiquL>ú5db§\u0016FssdW[ì<Rqì&"), -451507951),
#     d(base64.b64encode("KË"), -867135215),
#     d(base64.b64encode(":È1¥4Å½jð\"À7"), 336766939),
#     d(base64.b64encode("\u0005fã"), -930415931),
#     d(base64.b64encode("obVpûlcsþ0U~+pPtàlIw×!SphfTtñ\u0011pdä"), -768401274),
#     d(base64.b64encode("\u000eé"), 194738646),
#     d(base64.b64encode("*À§ {2[;põ\u0006nâ¸1kÅ#"), -822830269),
#     d(base64.b64encode("\u0014lþ\u0007ú(AT¿\u001fí\u001a"), 1548356339),
#     d(base64.b64encode(";È!aq6Ù uwÅê>paÈ'"), 370203992),
#     d(base64.b64encode("lmiu"), 1209022468),
#     d(base64.b64encode(";È)e\u0005Ð4Å\u001c:BÀ%Ì8aY"), -341371526),
#     d(base64.b64encode("AR|P"), 1490185396),
#     d(base64.b64encode("kà\u0017p¯²$Bô3HEx¯*tø"), -1361421952),
#     d(base64.b64encode("nbÞ4 ebÑ#À!}-Û%Ä0.@È6Æ'mwÀ8ñ2r`É4Ý0vPØ0Â"), -702764379),
#     d(base64.b64encode("jú$Y5gqLaý(;Hå5I~v"), 1547207220),
#     d(base64.b64encode("0Dpyå\u000fx"), 148803807),
#     d(base64.b64encode("NI"), -1487124972)
# ]

a_class_decrypt = [
    d(">JÂ0ûDwù¯0Õ´zhÝ!ë\u000ff", -989022505),
    d("rî:MGì0BSvn", -2055632580),
    d("+À0­0G¤nò\r3È6", 675347394),
    d("QLÜkh^F,j_È\u0015%Yî Oukd", -1263812037),
    d("zè3`y§&QiquL>ú5db§\u0016FssdW[ì<Rqì&", -451507951),
    d("KË", -867135215),
    d(":È1¥4Å½jð\"À7", 336766939),
    d("\u0005fã", -930415931),
    d("obVpûlcsþ0U~+pPtàlIw×!SphfTtñ\u0011pdä", -768401274),
    d("\u000eé", 194738646),
    d("*À§ {2[;põ\u0006nâ¸1kÅ#", -822830269),
    d("\u0014lþ\u0007ú(AT¿\u001fí\u001a", 1548356339),
    d(";È!aq6Ù uwÅê>paÈ'", 370203992),
    d("lmiu", 1209022468),
    d(";È)e\u0005Ð4Å\u001c:BÀ%Ì8aY", -341371526),
    d("AR|P", 1490185396),
    d("kà\u0017p¯²$Bô3HEx¯*tø", -1361421952),
    d("nbÞ4 ebÑ#À!}-Û%Ä0.@È6Æ'mwÀ8ñ2r`É4Ý0vPØ0Â", -702764379),
    d("jú$Y5gqLaý(;Hå5I~v", 1547207220),
    d("0Dpyå\u000fx", 148803807),
    d("NI", -1487124972)
]

print a_class_decrypt

# dec = [a.decode('base64') for a in a_class_decrypt]
# print dec

