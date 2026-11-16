from .database import Base
from sqlalchemy import  BigInteger, String,DateTime,UniqueConstraint,func,Integer,CheckConstraint,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Searches(Base):
    __tablename__ = "searches"

    __table_args__ = (
        UniqueConstraint("phrase", "region", name="search_query"),
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    phrase: Mapped[str] = mapped_column(String(200),nullable=False)
    region: Mapped[str] = mapped_column(String(100),nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),nullable=False,server_default=func.now())

class Measurements(Base):
    __tablename__ = "measurements"

    id: Mapped[int] = mapped_column(BigInteger,primary_key=True)
    search_id: Mapped[int] = mapped_column(BigInteger,ForeignKey("searches.id",ondelete="CASCADE"),nullable=False,index=True)
    count: Mapped[int] = mapped_column(Integer,CheckConstraint("count >= 0", name="count_non_negative"),nullable=False)
    measured_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),nullable=False,server_default=func.now(),index=True)
