public int calculateTip(List<String> names){
   if(names.size() > 5) {
       return 20;
   } else if(names.size() > 0) {
       return 10;
   }
   return 0;
}