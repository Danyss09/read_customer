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
def get_customer_by_id(customer_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM Customers WHERE CustomerID = %s"
            cursor.execute(query, (customer_id,))
            customer = cursor.fetchone()
            return customer
    except Exception as e:
        return None
    finally:
        connection.close()