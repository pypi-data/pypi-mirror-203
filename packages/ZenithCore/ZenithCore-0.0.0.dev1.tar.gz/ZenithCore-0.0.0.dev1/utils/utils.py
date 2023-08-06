from sqlalchemy import create_engine
import pandas as pd

class UpsertData:
    
    def __init__(self, project_id, instance_name, db_name, user, password):
        self.project_id = project_id
        self.instance_name = instance_name
        self.db_name = db_name
        self.user = user
        self.password = password
        self.engine = None
        
    def _get_connection_string(self):
        connection_name = f"{self.project_id}:{self.instance_name}"
        return f"postgresql+psycopg2://{self.user}:{self.password}@/dbname?host=/cloudsql/{connection_name}"
    
    def _connect_to_database(self):
        if not self.engine:
            connection_string = self._get_connection_string()
            self.engine = create_engine(connection_string)
        
    def upsert_dataframe(self, dataframe, table_name):
        self._connect_to_database()
        dataframe.to_sql(name=table_name, con=self.engine, index=False, if_exists='append', method='multi', chunksize=1000, schema=self.db_name)
