public class AprilHW {
    public static void main(String[] args){
        String given = "1'm g3ing t2 fi4d";
        String [] splits =given.split("[\\s+]");
        
     //   for (int i = 0; i < splits.length; i++){
         //   print("" + splits[i]);
       // }
        /*
        split into seperate letters(u can use a .toCharArray())
        test to see if its a number (u can do this with a simple if statement and for loop)
        print out dictionary in numerical order (simple for loop)
        */
        
        
        
        
        
        int a= 1;
        int b=2;
        int c=3;
        int d=4;
        
        //given sentence
        String[] sort= new String[4]; //list that fragments will go in
        for (int k =0; k< 4; k++){ //length of sentence
            //String [] temp = splits[k].split("[\\s]"); //the kth word in sentence
             String word= splits[k];
                 /*if(the number is in there){
                    print it
                    place it in list(sort)
                    l=2
                }
                elseif{
                 l=3
                }
                elseif{
                    l=4
                }
                if l is more than 4,
                l=1
                */
                Boolean found1= splits[k].contains(""+a); //searches for 1
                Boolean found2= splits[k].contains(""+b); //searches for 2
                Boolean found3= splits[k].contains(""+c); //searches for 3
                Boolean found4= splits[k].contains(""+d); //searches for 4
                //find the number in the word
                if (found1=true){
                   sort[0]=splits[k];
                   System.out.println(splits[k]);
                }
                else if(found2=true) {
                    sort[1]=splits[k];
                    System.out.println(splits[k]);
                }
                else if(found3=true){
                    sort[2]=splits[k];
                    System.out.println(splits[k]);
                }
                else if(found4=true){
                    sort[3]=splits[k];
                    System.out.println(splits[k]);
                }
            }
            System.out.println(sort); 
        }
    }



        //sort them
   // }

  //  private static void print(String word) {
    //    System.out.println(word);
    //}

    //private static void print(String[] input) {
      //  System.out.println(Arrays.toString(input));
