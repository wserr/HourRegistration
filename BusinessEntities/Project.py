from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from BusinessEntities.RecordType import RecordType
from DataAccess.DataBaseConnection import DataBaseConnection


class Project(DataBaseConnection.Base):
    __tablename__ = "Project"
    ID = Column(Integer, primary_key=True)
    Description = Column(String, nullable=False)
    ExterneID = Column(String, nullable=False)
    Button = Column(Integer, nullable=True)
    Actief = Column(Integer, nullable=False)
    __timerecord__ = relationship("TimeRecord")

    def __str__(self):
        addString = ''
        if not str(self.Button) == 'None':
            addString = '       ' + str(self.Button)
        return self.Description + addString
