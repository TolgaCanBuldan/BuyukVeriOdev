def listele(database,sorgu):
    imlec=database.cursor()
    kmt=sorgu
    imlec.execute(kmt)
    database.commit()
    return imlec

def parametreliliste(database,sorgu):
    imlec=database.cursor()
    kmt=sorgu
    imlec.execute(kmt)
    database.commit()
    return imlec

