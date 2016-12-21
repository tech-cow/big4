  //Link
public class Link{

    public String bookname;
    public int millionSold;

    public Link next;

    //Constructor
    public Link(String bookname, int millionSold){
      this.bookname = bookname;
      this.millionSold = millionSold;
    }

    public void display(){
      System.out.println(bookname + ": " + millionSold + ",000,000");
    }

    public String toString(){
      return bookname;
    }
}


class LinkList{
    public Link cur_link;

    LinkList(){
      cur_link == null;
    }

    public boolean isEmpty(){
      return (cur_link == null);
    }

    public void insertFirstLink(String bookname, int millionSold){
      Link newlink = new Link(bookname, millionSold);
      newlink.next = cur_link;

      firstlink = newlink;
    }

    public void removeFirst(){
      Link linkReference = firstlink;

      if(!isEmpty())
    }


}
