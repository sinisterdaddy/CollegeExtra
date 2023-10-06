package bottle;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class HashBreakerhidden4  {

	static char[][] name=new char[62][4];    //A-Z, a-z and 0-9 total 62 characters  and 4 hidden positions 
	public static void main(String[] args) {
		for(int i=0;i<62;i++) {
			for(int j=0;j<4;j++)
			try {
				if(i<10) {
					name[i][j]= (char) (i+48);   //0 ASCII value 48 after these numbers i=10
					                               //0,1,2,3 number of hidden positions 
					
				}
				else if(i<36) {
				name[i][j]= (char) (i+55);          //A ASCII value 65 after these alphabets i=36
				}
				else {
					name[i][j]= (char) (i+61);     // a ASCII value 97
				
				}
				
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
	        findHashCode(name);
	}

	public static String bytesToHex(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
	}
	static void findHashCode(char test[][]) {
		
		  try {
			  String name="VITAP"; //Intitial String
			  String name1="ebaf35e6560c354a6a3bd568e691928685b444d4e3bfe6e0032679276cff5993"; //lowercase
			  int i,j,k,l;
	              MessageDigest md = MessageDigest.getInstance("SHA-256");
	       
           for(i=0;i<62;i++) {
        	   for(j=0;j<62;j++) {
        		   for(k=0;k<62;k++) {
        			   for(l=0;l<62;l++) {
            			     name=name+""+test[i][3]+""+test[j][2]+""+test[k][1]+""+test[l][0];  //change required
            			     byte[] result = md.digest(name.getBytes());
            			    if(bytesToHex(result).compareTo(name1)==0) {
            				    System.out.println("test is success"+name); 
            				    System.out.println(bytesToHex(result)+"\n"+name1);
            				    break;} //break from third inner loop
            	                System.out.println(test[i][3]+" "+test[j][2]+" "+test[k][1]+" "+test[l][0]);  //change required
            	                name="VITAP";
           }
        	   if(l!=62) {break;}     //break from second inner loop
           }
        	   if(k!=62) {break;}     //break from first inner loop
           }
        	   if(j!=62) {break;}     //break from main loop
           }
             } catch (NoSuchAlgorithmException e) {
	            throw new IllegalArgumentException(e);
	        }
		
	}
}

