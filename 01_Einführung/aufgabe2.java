public class ShoppingCart {
    List<String> items;
    boolean bookAdded;

    public ShoppingCart(List<String> items) {
        this.items = items;
        this.bookAdded = false;
    }

    public void addItem(String item) {
        items.add(item);
        if (item.equals("book")) {
            bookAdded = true;
        }
    }

    public void removeItem(String item) {
        items.remove(item);
        if (!items.contains("book")) {
            bookAdded = false;
        }
    }    
}

public double getDiscountPercentage(List<String> items) {
    if (items.contains("book")) {
        return 0.1;
    }
    return 0.0;
}