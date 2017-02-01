public class Husband extends Person{
    // private Wife wife;

    public  String toString(){
        setName("chenssy");    //调用父类的setName() ;
        return  super.toString();    //调用父类的toString()方法
    }

    public static void main(String[] args) {
        Husband husband = new Husband();

        System.out.println(husband.toString());
    }
}
