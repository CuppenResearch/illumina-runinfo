from app import db
from app.models import Platform

db.create_all()

hiseq = Platform('HiSeq',"HiSeq Control Software")
miseq = Platform('MiSeq',"MiSeq Control Software")
nextseq = Platform('NextSeq',"NextSeq Control Software")

db.session.add_all([hiseq, miseq, nextseq])

db.session.commit()
