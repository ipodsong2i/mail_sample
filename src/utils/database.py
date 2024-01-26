from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from utils.config import config


class DatabaseBase:
    engine: any = None
    session_local: sessionmaker[Session] = None
    base: any = None
    debug_mode: bool = False


class Database(DatabaseBase):
    def __init__(
        self,
        connection_string: str = "",
        debug_mode: bool = False,
        pool_size: int = 10,
        max_overflow: int = 10,
        autocommit: bool = False,
        autoflush: bool = False
    ):
        self.engine = create_engine(connection_string, pool_size=pool_size, max_overflow=max_overflow, echo=debug_mode)
        self.session_local = sessionmaker(autocommit=autocommit, autoflush=autoflush, bind=self.engine)


    # Dependency (재활용될 dependency 코드)
    def __call__(self):
        db = self.session_local()
        try:
            yield db
        finally:
            db.close()

            
db = {}

# config 파일에서 db 환경을 가져옴
db_configs = {
    "black": config.get_config("MARIA_DB.BLACK"),
    "red": config.get_config("MARIA_DB.RED")
}

for schema, db_config in db_configs.items():
    db_address = db_config["HOST"]
    db_port = db_config["PORT"]
    db_user = db_config["USERNAME"]
    db_password = db_config["PASSWORD"]
    db_name = db_config["DB_NAME"]

    db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_address}:{db_port}/{db_name}"
    db[schema] = Database(connection_string=db_url)



