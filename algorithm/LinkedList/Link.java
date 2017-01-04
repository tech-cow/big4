public class Link{
/* create basic elements*/
  public String bookname;
  public int millionsold;

  Link next;

/*Constructor*/
  public Link(String bookname, int millionsold){
    this.bookname = bookname;
    this.millionsold = millionsold;
  }

/*Display function*/
  public void display(){
    System.out.println(bookname + ": " + millionsold + ",000,000 sold");
  }
}


public class Linkedlist{
/* create basic elements*/
  public Link currentLink;

/*Constructor*/
  public Linkedlist(){
    Link currentLink = null;
  }
/*Assert the Link is empty*/
  public void isEmpty(){
    return(currentLink == null);
}
/*Insert a Link*/
  public void insertLink(){
    Link newlink = new Link(bookname,millionsold);
    newlink.next = currentLink;
    currentLink = newlink;
    }

/*Delete a Link*/
  public void deleteLink(){
    currentLink = currentLink.next;
  }

}
