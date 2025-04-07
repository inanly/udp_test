class Person{
    private String name;
    private double height;
    private double weight;

    public Person (String name, double height, double weight){
        this.name = name;
        this.height = height;
        this.weight = weight;
    }

    public void SetName(String name){
        this.name = name;
    }
    public void SetHeight(double height){
        this.height = height;
    }
    public void SetWeight(double weight){
        this.weight = weight;
    }

    public String GetName(){
        return name;
    }
    public double GetHeight(){
        return height;
    }
    public double GetWeight(){
        return weight;
    }

    public double GetBmi(){
        return weight / ((height/100) * (height/100));
    }

}

public class HW3 {
    public static void main (String[] args){
        if (args.length/3 != 0){
            Person[] p = new Person[args.length / 3];
            int p_num = 0;
            
            for (int i = 0 ; i < args.length ; i+=3, p_num++){
                p[p_num] = new Person( args[i + 0], Double.parseDouble(args[i + 1]), Double.parseDouble(args[i + 2]));
            }

            Sort(p);

            for (int j = 0 ; j < args.length/3 ; j++){
                System.out.println(p[j].GetName() + ": " + p[j].GetHeight() + "cm, " + p[j].GetWeight() + "kg, BMI: " + p[j].GetBmi());
            }
            
            System.out.println(HeightMax(p).GetName() + " " + HeightMax(p).GetHeight());
            System.out.println(WeightMin(p).GetName() + " " + WeightMin(p).GetWeight());
        }
    }
        

    public static void Sort(Person[] p){
        
        for (int i = 1 ; i < p.length ; i++){
            if (p[i].GetBmi() > p[i-1].GetBmi()){
                Person temp = p[i];
                p[i] = p[i-1];
                p[i-1] = temp;
            }
            
        }
    }

    public static Person HeightMax(Person[] p){
        Person max = p[0];
        for (int i = 1 ; i < p.length ; i++){
            if (p[i].GetHeight() > max.GetHeight()){
                max = p[i];
            }
        }
        return max;
    }
    public static Person HeightMin(Person[] p){
        Person min = p[0];
        for (int i = 1 ; i < p.length ; i++){
            if (p[i].GetHeight() < min.GetHeight()){
                min = p[i];
            }
        }
        return min;
    }

    public static Person WeightMax(Person[] p){
        Person max = p[0];
        for (int i = 1 ; i < p.length ; i++){
            if (p[i].GetHeight() > max.GetHeight()){
                max = p[i];
            }
        }
        return max;
    }
    public static Person WeightMin(Person[] p){
        Person min = p[0];
        for (int i = 1 ; i < p.length ; i++){
            if (p[i].GetHeight() < min.GetHeight()){
                min = p[i];
            }
        }
        return min;
    }
}

