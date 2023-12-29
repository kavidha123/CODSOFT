public class App {
    public static void main(String[] args) {
        Account account = new Account(1000); // Initial balance set to 1000
        ATM atm = new ATM(account);
        atm.showMenu();
    }
}
