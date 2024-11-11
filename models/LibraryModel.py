

from sqlalchemy import create_engine, Column, Integer, String, TEXT, or_
from sqlalchemy.orm import sessionmaker, declarative_base

Engine = create_engine(
    "mssql+pyodbc://@./library?driver=ODBC+Driver+18+for+SQL+Server&trusted_connection=yes&TrustServerCertificate=yes"
)

Base = declarative_base()
class Library(Base):
    __tablename__ = "tbl_books"

    bk_id=Column(Integer,primary_key=True)
    bk_title=Column(TEXT,nullable=False)
    bk_author=Column(TEXT,nullable=False)
    bk_year=Column(String,nullable=False)
    bk_isbn=Column(String,nullable=False)

    def __init__(self,Title="",Author="",Year="",Isbn=""):
        self.bk_title=Title
        self.bk_author=Author
        self.bk_year=Year
        self.bk_isbn=Isbn

Base.metadata.create_all(Engine)

Session = sessionmaker(bind=Engine)
session = Session()


class Repository():
    def add(self, Obj):
        session.add(Obj)
        session.commit()
        return Obj.bk_id
    
    def delete(self, ID):
        book = session.query(Library).filter(bk_id == ID).first()
        if book:
            session.delete(book)  # حذف رکورد
            session.commit()  # ثبت تغییرات
            return "deleted"
        
    def update(self, ID, Table, Object):
        session.commit()

    def SelectAll(self, obj):
        return session.query(obj).all()

    def Search(self, str):
        results = session.query(Library).filter(
        or_(
            Library.bk_title.like(f"%{str}%"),
            Library.bk_author.like(f"%{str}%"))
        ).all()
        return results

# r = Repository()
# lib = Library("کتاببب", "خودم", "1403", "31231231231")
# r.add(lib)
# print(lib.bk_id)

# r = Repository()
# re = r.SelectAll(Library)
# for i in re:
#     print(i.bk_title)
#     def SelectById(self, ID):
#         return session.get(entity=human, ident=ID)

#     def GetField(self,List, Index):
#         for item in List:
#             print( getattr(item, Index))


#     def update2(self, ID, Object, **args):
#         record = self.SelectById(ID)
#         for key, val in args.items():
#             setattr(record , key, val)

#         session.commit()

#     def search(**args):
#         for item in args:
#             print(item.fname)
#         return session.query(human).filter(args)

# Base.metadata.create_all(engin)
