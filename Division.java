public class Division {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java Division <number1> <number2>");
            return;
        }

        double a = Double.parseDouble(args[0]);
        double b = Double.parseDouble(args[1]);

        if (b == 0) {
            System.out.println("Error: Division by zero is not allowed.");
            return;
        }

        double quotient = a / b;

        System.out.println(a + " / " + b + " = " + quotient);
    }
}
