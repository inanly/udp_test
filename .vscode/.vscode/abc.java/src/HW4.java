import java.util.*;
import java.io.*;

class Person{
	String name;
	double height;
	double weight;
	Person(String name,double height,double weight){
		this.name=name;
		this.height=height;
		this.weight=weight;	
	}
	public void show(){
        System.out.println("Person: " + name + " Height: " + height + " Weight: " + weight);
    }
}

class Teacher extends Person{
	double bmi;
	
	public Teacher (String name, double height, double weight){
        super(name, height, weight);
        bmi = weight / ((height/100) * (height/100));
    }
    @Override
    public void show(){
        System.out.println("Teacher: " + name + " Height: " + height + " Weight: " + weight + " BMI: " + bmi);
    }
	
}

class Student extends Person{
	double[] score = new double[3];
	double bmi;
	public Student (String name, double height, double weight){
        super(name, height, weight);
        bmi = weight / ((height/100) * (height/100));
    }
    @Override
    public void show(){
        System.out.println("Student: " + name + " Height: " + height + " Weight: " + weight + " BMI: " + bmi);
}
class PU_Class{	
	Student[] st=new Student[3];
	Teacher t2;
	String class_name = "資工一";
	String[] course={"程式語言","進階程式語言","物件導向程式語言"};

	int pro1,pro2,pro3;
	int promn1,promn2,promn3;
	int average1,average2,average3;

	void average_score(Person[] p,String course){
		average1=(st[0].score[0],st[1].score[0],st[2].score[0])/3;
		average2=(st[0].score[1],st[1].score[1],st[2].score[1])/3;
		average3=(st[0].score[2],st[1].score[0],st[2].score[2])/3;
		System.out.println(course[0]+"的平均分為: "average1);
		System.out.println(course[0]+"的平均分為: "average2);
		System.out.println(course[0]+"的平均分為: "average3);
	}
	void search(Person[] p,String st_name){
		String se;
		Student[] st ; 
		if(se==st[0].name){
			System.out.println("名稱: "+st[0].name+"體重: "st[0].weight+"身高: "+st[0].height+"程式語言:"+st[0].score[0]+"進階程式語言:"+st[0].score[1]+"物件導向程式語言: "+st[0].score[2]);

		}
		else(se==st[1].name){
			System.out.println("名稱: "+st[1].name+"體重: "st[2].weight+"身高: "+st[1].height+"程式語言:"+st[1].score[0]+"進階程式語言:"+st[1].score[1]+"物件導向程式語言: "+st[1].score[2]);
		}
		else(se==st[2].name){
			System.out.println("名稱: "+st[2].name+"體重: "st[2].weight+"身高: "+st[2].height+"程式語言:"+st[2].score[0]+"進階程式語言:"+st[2].score[1]+"物件導向程式語言: "+st[2].score[2]);
		}
		else{
			System.out.println("查無此人");
		}
	}
	void max_score(String course){
		pro1=int max(st[0].score[0],st[1].score[0],st[2].score[0]);
		pro2=int max(st[0].score[1],st[1].score[1],st[2].score[1]);
		pro3=int max(st[0].score[2],st[1].score[2],st[2].score[2]);
		System.out.println(course[0]+"的最高分為: "pro1);
		System.out.println(course[0]+"的最高分為: "pro2);
		System.out.println(course[0]+"的最高分為: "pro3);

	}
	void min_score(String course){
		promn1=int min(st[0].score[0],st[1].score[0],st[0].score[0]);
		promn2=int min(st[0].score[1],st[1].score[1],st[0].score[1]);
		promn3=int min(st[0].score[2],st[1].score[2],st[0].score[2]);
		System.out.println(course[0]+"的最低分為: "promn1);
		System.out.println(course[1]+"的最低分為: "promn2);
		System.out.println(course[2]+"的最低分為: "promn3);
		
	}


}
class HW4{
	Scanner sc = new Scanner(System.in);
	String name;
	Double height;
	Double weight;
	Student st;
	int count=0;
	Person[] p =new Person[3];
	void menu(String name,Double height,Double weight){
		this.name = name;
		this.height=height;
		this.weight=weight;
		int a=0;
		System.out.println(
			"(1)更改“班級基本資料”。\n"+
			"(2)秀出全班所有人BMI的情況。\n"+
			"(3)亂數產生學生科目成績。\n"+
			"(4)計算單科總平均，單科最高最低分。\n"+
			"(5)輸入姓名，查詢某學生基本資料，和相關成績。\n"+
			"(6) Exit");
		a=sc.nextInt();
		PU_Class c;
		Student[] stbmi;
		
		while(a!=6){
			switch(a){
				case 1:
					update(c);
				case 2:
					bmiCaculate(st,t);
				case 3:
					rand_score(sco);
					count++;
				case 4:
					if(count==1){
						c.average_score(p, course);
						c.max_score(course);
						c.min_score(course);
					}
					else{
						break;
					}
				case 5:
					if(count==1){
						c.search(p, st_name);
					}
					else{
						break;
					}
				case 6:
			}
		}
	}
	void bmiCaculate(Student[] st,Teacher t){
		for(int i=0;i<st.length;i++){
			st[i].bmi=st[i].weight / ((st[i].height/100) * (st[i].height/100));
		}
		t.bmi=t.weight / (t.height/100) * (t.height/100);

	}
	void update(PU_Class c){
		System.out.println("(1)更改“班級基本資料”:");
		name=sc.nextLine();
		c.class_name=name;
		System.out.println("新班級名稱:"+c.class_name);
	}
	void rand_score(Student[] sco){
		PU_Class cla;
		
		for(int i=0;i<sco.length;i++){
			for(int j=0;j<3;i++){
				sco[i].score[j]=(int)(Math.random() * 41)+60;
			}
		}
		for(int i=0;i<3;i++){
			System.out.println(cla.course[i]);
		}

	}	
	
	public static void main(String[] args){
		Student[] st=new Student[args.length/3-1];
		Scanner sc = new Scanner(System.in);
		int p_num = 0;
		for (int i = 0 ; i < args.length-3 ; i+=3, p_num++){
			st[p_num] = new Student( args[i + 0], Double.parseDouble(args[i + 1]), Double.parseDouble(args[i + 2]));
		}
		
		Teacher t=new Teacher(args[p_num*3],Double.parseDouble(args[p_num*3+1]),Double.parseDouble(args[p_num*3+2]));
		menu();
	}
}