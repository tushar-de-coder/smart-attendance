from database.db import initialize_database
from ui.dashboard import SmartAttendDashboard


def main():

    # Make sure database and tables exist
    initialize_database()

    # Start the dashboard
    app = SmartAttendDashboard()
    app.mainloop()


if __name__ == "__main__":
    main()