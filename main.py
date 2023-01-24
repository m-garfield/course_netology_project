import psycopg2


def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
               
                
                CREATE TABLE IF NOT EXISTS users(
                id_user SERIAL PRIMARY KEY,
                last_name VARCHAR(40) NOT NULL,
                first_name VARCHAR(40) NOT NULL,
                  int NOT NULL);

                CREATE TABLE IF NOT EXISTS city(
                id_city SERIAL PRIMARY KEY,
                city VARCHAR(40) NOT NULL);

                CREATE TABLE IF NOT EXISTS users_city(
                id_user int NOT NULL,
                id_city int NOT NULL,
                FOREIGN KEY (id_city) REFERENCES city(id_city), 
                FOREIGN KEY (id_user) REFERENCES users(id_user),
                PRIMARY KEY (id_user,id_city));
                
                CREATE TABLE IF NOT EXISTS favorites(
                id_user int NOT NULL,
                id_favorites int NOT NULL,
                FOREIGN KEY (id_city) REFERENCES city(id_city), 
                FOREIGN KEY (id_user) REFERENCES users(id_user),
                PRIMARY KEY (id_user,id_city));          
          
                   """

                    )




with psycopg2.connect(database="project_netology", user="postgres", password="64082") as conn:
    create_db(conn)
conn.close()
