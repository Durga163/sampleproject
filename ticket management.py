class Ticket:
    def __init__(self, ticket_id, description):
        self.ticket_id = ticket_id
        self.description = description
        self.status = "open"

    def resolve(self):
        self.status = "resolved"

class TicketSystem:
    def __init__(self):
        self.tickets = []
        self.next_id = 1

    def create_ticket(self, description):
        ticket = Ticket(self.next_id, description)
        self.tickets.append(ticket)
        self.next_id += 1
        print(f"Ticket #{ticket.ticket_id} created.")

    def view_tickets(self):
        if not self.tickets:
            print("No tickets found.")
        else:
            for ticket in self.tickets:
                print(f"Ticket ID: {ticket.ticket_id}, Description: {ticket.description}, Status: {ticket.status}")

    def resolve_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                ticket.resolve()
                print(f"Ticket #{ticket_id} resolved.")
                return
        print(f"Ticket #{ticket_id} not found.")

def main():
    system = TicketSystem()
    while True:
        print("\nTicket Management System")
        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Resolve Ticket")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            description = input("Enter the ticket description: ")
            system.create_ticket(description)
        elif choice == "2":
            system.view_tickets()
        elif choice == "3":
            try:
                ticket_id = int(input("Enter the ticket ID to resolve: "))
                system.resolve_ticket(ticket_id)
            except ValueError:
                print("Invalid ticket ID. Please enter a number.")
        elif choice == "4":
            print("Exiting the Ticket Management System.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
