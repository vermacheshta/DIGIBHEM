import java.util.Scanner;

public class StudentGrades {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of students: ");
        int numberOfStudents = scanner.nextInt();
        int[] grades = new int[numberOfStudents];

        for (int i = 0; i < numberOfStudents; i++) {
            System.out.print("Enter grade for student " + (i + 1) + ": ");
            grades[i] = scanner.nextInt();
        }

        int sum = 0;
        for (int grade : grades) {
            sum += grade;
        }

        double average = (double) sum / numberOfStudents;
        System.out.println("The average grade is: " + average);
    }
}