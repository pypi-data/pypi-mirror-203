class Database:
    def __init__(self):
        self.data = {}

    def create_db(self, name):
        self.data[name] = {}

    def store_data(self, db_name, key, value):
        if db_name not in self.data:
            raise ValueError(f"Database '{db_name}' does not exist. Use create_db() to create it.")
        self.data[db_name][key] = value
    def retrieve_data(self, db_name, key):
        if db_name not in self.data:
            raise ValueError(f"Database '{db_name}' does not exist. Use create_db() to create it.")
        if key not in self.data[db_name]:
            raise ValueError(f"Key '{key}' not found in database '{db_name}'")
        return self.data[db_name][key]