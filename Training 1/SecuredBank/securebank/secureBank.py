import datetime
import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from commonlib.bankLogger import BankLogger
from mortgage.mortgage import Mortgage

class SecureBank():
    def __init__(self):
        logger = BankLogger.__call__().get_logger()
        self.is_authenticated = ''

        def print_menu():
            print(30 * "-", "SECURE BANK MENU", 30 * "-")
            print("1. Banking system")
            print("2. Credit Card system")
            print("3. Mortgage system")
            print("4. Logout")
            print(78 * "-")
            self.last_login = currentDT.strftime("%Y%m%d%H%M%S")

        flag = 1
        while flag != "0":
            currentDT = datetime.datetime.now()
            if self.is_authenticated:
                if int(currentDT.strftime("%Y%m%d%H%M%S")) - int(self.last_login) < 1000:
                    loop = True
                    int_choice = -1

                    while loop:
                        print_menu()
                        choice = input("Enter your choice [1-4]: ")

                        if choice == '1':
                            print("Banking section")
                        elif choice == '2':
                            print("Credit Card section")
                        elif choice == '3':
                            mortgage_obj = Mortgage()
                            mortgage_obj.set_principal(150000)
                            mortgage_obj.get_monthyly_interest()
                            mortgage_obj.get_yearly_interest()
                            print(mortgage_obj.monthyly_interest)
                            print(mortgage_obj.yearly_interest)
                        elif choice == '4':
                            print("Exiting")
                            loop = False
                        else:
                            input("Wrong menu selection. Enter any key to try again..")

                    self.exit_program()

                else:
                    self.is_authenticated = ''
                    logger.info("Session Expired.")
                    logger.info("Re-directing to login form.")
            else:
                count = 0
                while count < 3:
                    username = input('Enter username: ')
                    password = input('Enter password: ')

                    if password=='pgoupal' and username=='pgoupal':
                        logger.info(username + " Sucessfully Authenticated")
                        self.is_authenticated = 'True'
                        self.last_login = currentDT.strftime("%Y%m%d%H%M%S")
                        count = 4
                    else:
                        print('Access denied. Try again.')
                        if count != 2:
                            logger.info(username + ' : Access denied. Try again.')
                            count += 1
                        else:
                            logger.info(username + ' : Access denied. Terminating script.')
                            self.exit_program()

    def exit_program(self):
        print("terminating program")
        sys.exit(1)

if __name__ == "__main__":
    SecureBankObj = SecureBank()
    pprint.pprint(SecureBankObj)

