from persistence import CustomerRepository


class CustomerService:
    def __init__(self):
        self.repo = CustomerRepository()

    def list_customers(self):
        # Aquí podrías filtrar, paginar, formatear datos, etc.
        return self.repo.fetch_all()

    def remove_customer(self, customer_id):
        # Validaciones previas (por ej. comprobar existencia)
        self.repo.delete(customer_id)

    # añadir métodos create_customer, update_customer, etc.
