from services.db_config import get_connection



def get_all_customers():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM Customers"
            cursor.execute(query)
            customers = cursor.fetchall()
            return customers
    except Exception as e:
        return {"error": str(e)}
    finally:
        connection.close()
