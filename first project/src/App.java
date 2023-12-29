import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the number of subjects: ");
        int numberOfSubjects = scanner.nextInt();

        double[] marks = new double[numberOfSubjects];

        for (int i = 0; i < numberOfSubjects; i++) {
            System.out.println("Enter marks for subject " + (i + 1) + ": ");
            marks[i] = scanner.nextDouble();
        }

        GradeCalculator calculator = new GradeCalculator(marks);
        double totalMarks = calculator.getTotalMarks();
        double averagePercentage = calculator.getAveragePercentage();
        char grade = calculator.calculateGrade();

        System.out.println("Total Marks: " + totalMarks);
        System.out.println("Average Percentage: " + averagePercentage);
        System.out.println("Grade: " + grade);
    }
}
