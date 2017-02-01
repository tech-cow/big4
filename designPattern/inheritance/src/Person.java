public class Person {
    /**Protected区别于Private的地方，
    在于子类可以Access Protected的信息**/
    protected String name;
    protected int age;
    protected String sex;

    protected String getName(){
        return name;
    }

    protected void setName(String name) {
        this.name = name;
  }

    public String toString(){
        return "this name is " + name;
    }


}
