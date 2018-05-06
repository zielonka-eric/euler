import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
        System.out.println("Bound of 10: " + sumOfThreesAndFives(10));
        System.out.println("Bound of 1000: " + sumOfThreesAndFives(1000));

        System.out.println("Bound of 10: " + functionalSumOfThreesAndFives(10));
        System.out.println("Bound of 1000: " + functionalSumOfThreesAndFives(1000));

        System.out.println("Bound of 10: " + sumOfMultiples(3, 5, 0, 10));
        System.out.println("Bound of 1000: " + sumOfMultiples(3, 5, 0, 1000));
    }

    public static int sumOfThreesAndFives(int bound) {
        int sum = 0;
        for(int i = 1; i < bound; i++) {
            if ((i % 3 == 0) || (i % 5 == 0)) {
                sum += i;
            }

            // or you can do this
            // one line, but a little less readable?
            //sum = ((i % 3 == 0) && (i % 5 == 0)) ? sum + i : sum;
        }
        return sum;
    }

    public static int functionalSumOfThreesAndFives(int bound) {
        return IntStream.range(1, bound).parallel()
            .filter(n -> ((n % 3 == 0) || (n % 5 == 0)))
            .reduce(0, (a, b) -> (a + b));
    }

    public static int sumOfMultiples(int a, int b, int lowerBound, int upperBound) {
        int sum = 0;
        for(int i = lowerBound; i < upperBound; i++) {
            if ((i % a == 0) || (i % b == 0)) {
                sum += i;
            }
        }
        return sum;
    }
}