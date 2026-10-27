public class Multiplication {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java Multiplication <number1> <number2>");
            return;
        }

        double a = Double.parseDouble(args[0]);
        double b = Double.parseDouble(args[1]);
        double product = a * b;

        System.out.println(a + " * " + b + " = " + product);
    }
}
