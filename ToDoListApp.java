import java.util.LinkedList;
import java.util.Scanner;
class Task{
    String description;
    boolean isCompleted;

    Task(String description){
        this.description = description;
        this.isCompleted = false;
    }
    void markCompleted(){
        isCompleted = true;
    }
    void markIncompleted(){
        isCompleted = false;
    }
    @Override
    public String toString(){
        return (isCopleted ? "Done" : "[ ]") + description;

    }
}
public class ToDoListApp{
    private static final LinkedList<Task> tasks = new LinkedList<>();
    private static final Scanner scanner = new Scanner(System.in);
}
public static void main(String[] args){
    int choice;

    do{
        System.out.println("\n*** TO-DO LIST MENU ***");
        System.out.println("1. Add Task" );
        System.out.println("2. View Task");
        System.out.println("3. Mark as Completed");
        System.out.println("4. Mark as Incomplete ");
        System.out.println("5. Delete Task");
        System.out.println("6. Exit");
        choice = scanner.nextInt();
        scanner.nextLine();

        switch (choice){
            case 1 : addTask();
            case 2 : ViewTask();
            case 3 : updateTask( true);
            case 4 : updateTask(false);
            case 5 : deleteTask();
            case 6: System.out.println("Exiting...");
            default : System .out.println(" Invalid choice : Try Again");

        }
    } while (choice !=0);
}
private static void addTask(){
    System.out.printlin("Enter Task description");
    String desc = scanner.nextLine();
    tasks.add(new Task(desc));
    System.out.println("Task Added Successfully");
}
private static void viewTasks(){
    if (tasks.isEmpty()){
        System.out.println("Your To-DO List is Empty.");

    }else{
        System.out.println("Your Tasks");
        for(int i =0; i<tasks.size(); i++){
            System.out.println((i+1) + ". "+ tasks.get(i));
        }
    }
}
private static void updateTask( boolean complete){
    viewTask();
    if (tasks.isEmpty());
      return;

      
    System.out.println("Enter Task Number to Update");
    int num = scanner .nextInt();
    scanner.nextLine();
    if(num>0 && num<=tasks.size()){
        Task task = tasks.get(num-1);
        if (complete) task.markCompleted();
        else task.markIncompleted();
        System.out.println("Task Update");
    }else{
        System.out.println("Invalid task number");
    }
}
private static void deleteTask(){
    viewTask();
    if (task.isEmpty());
      return;
    System.out.println("Enter Task Number to deleted");
    int num = scanner.nextInt();
    scanner.nextLine();
    if (num > 0 && num<= tasks.size()){
        tasks.remove(num-1);
        System.out.println("Task deleted");
    }else{
        System.out.println("Invalid task number");
    }


}

