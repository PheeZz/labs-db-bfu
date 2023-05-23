from labs_db_bfu.cfg.db_connector import DbConnector


class Lab1(DbConnector):
    def __init__(self):
        super().__init__()

    def _create_table_rescue_brigade(self) -> None:
        self.cursor.execute("""--sql
        CREATE TABLE IF NOT EXISTS rescue_brigade (
            Brigade_ID SERIAL PRIMARY KEY,
            Brigade_Number INTEGER NOT NULL,
            Rescuers_Per_Vehicle INTEGER NOT NULL
        )
        """)

    def _create_table_rescuer(self) -> None:
        self.cursor.execute("""--sql
        CREATE TABLE IF NOT EXISTS rescuer (
            Rescuer_ID SERIAL PRIMARY KEY,
            Brigade_ID INTEGER NOT NULL,
            First_Name VARCHAR(50) NOT NULL,
            Last_Name VARCHAR(50) NOT NULL,
            FOREIGN KEY (Brigade_ID) REFERENCES rescue_brigade(Brigade_ID)
        )
        """)

    def _create_table_incident_type(self) -> None:
        self.cursor.execute("""--sql
        CREATE TABLE IF NOT EXISTS incident_type (
            Type_ID SERIAL PRIMARY KEY,
            Type_Name VARCHAR(50) NOT NULL
        )
        """)

    def _create_table_incident_cause(self) -> None:
        self.cursor.execute("""--sql
        CREATE TABLE IF NOT EXISTS incident_cause (
            Cause_ID SERIAL PRIMARY KEY,
            Cause_Name VARCHAR(50) NOT NULL
        )
        """)

    def _create_table_incident(self) -> None:
        self.cursor.execute("""--sql
        CREATE TABLE IF NOT EXISTS incident (
            Incident_ID SERIAL PRIMARY KEY,
            Brigade_ID INTEGER NOT NULL,
            Incident_Type_ID INTEGER NOT NULL,
            Incident_Cause_ID INTEGER NOT NULL,
            Incident_Address VARCHAR(50) NOT NULL,
            Start_Datetime TIMESTAMP NOT NULL,
            End_Datetime TIMESTAMP NOT NULL,
            Count_of_Teams INTEGER NOT NULL,
            FOREIGN KEY (Brigade_ID) REFERENCES rescue_brigade(Brigade_ID),
            FOREIGN KEY (Incident_Type_ID) REFERENCES incident_type(Type_ID),
            FOREIGN KEY (Incident_Cause_ID) REFERENCES incident_cause(Cause_ID)
        )
        """)

    def _create_table_victims(self) -> None:
        self.cursor.execute("""--sql
        CREATE TABLE IF NOT EXISTS victims (
            Victim_ID SERIAL PRIMARY KEY,
            Incident_ID INTEGER NOT NULL,
            First_Name VARCHAR(50) NOT NULL,
            Last_Name VARCHAR(50) NOT NULL,
            Is_Rescuer BOOLEAN NOT NULL
        )
        """)

    def create_tables(self) -> None:
        self._create_table_rescue_brigade()
        self._create_table_rescuer()
        self._create_table_incident_type()
        self._create_table_incident_cause()
        self._create_table_incident()
        self._create_table_victims()

    def run(self) -> None:
        self.create_tables()
