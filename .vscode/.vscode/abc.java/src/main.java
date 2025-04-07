import java.util.Scanner;
class CheckNumException extends Exception{
    int x=-1;
    public CheckNumException(int num){
        x=num;
    }
    public String getMessage(){
        return("數字"+x+"超出題目範圍");
    }
};
public class main
{
	public static void main(String[] args) {
	    int m=0;
	    Scanner sc=new Scanner(System.in);
	    int n=(1+(int)(Math.random()*100));
	    System.out.println(n);
	    m = sc.nextInt();
	    if(m==n){
	                System.out.println("猜中了");
	                }
	    while(m!=n){
	    try{
	                System.out.println("猜錯了");
	                m = sc.nextInt();
	            if(m<1||m>100){
	                throw new CheckNumException(m);
	            }
	        }
	       catch(CheckNumException e){
	           System.out.println(e.getMessage());
	           break;
	       }
	    }
	}
}
