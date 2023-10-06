package bottle;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class HashBreakerhidden3  {

	static char[][] name=new char[62][3];    //A-Z, a-z and 0-9 total 62 characters  and 4 hidden positions 
	public static void main(String[] args) {
		for(int i=0;i<62;i++) {
			for(int j=0;j<3;j++)
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
			  String name1="20b764645ab8db1f46ca09a1e35ca84d4de8a5bc4e00c44ce8884f7ae083000e"; //lowercase
			  int i,j,k,l1;
	              MessageDigest md = MessageDigest.getInstance("SHA-256");
	       
           for(i=0;i<62;i++) {
        	   for(j=0;j<62;j++) {
        		   for(k=0;k<62;k++) {
            			     name=name+""+test[i][2]+""+test[j][1]+""+test[k][0];
            			     byte[] result = md.digest(name.getBytes());
            			    if(bytesToHex(result).compareTo(name1)==0) {
            				    System.out.println("test is success"+name); 
            				    System.out.println(bytesToHex(result)+"\n"+name1);
            				    break;} //break from second inner loop
            	                System.out.println(test[i][2]+" "+test[j][1]+" "+test[k][0]);
            	                name="VITAP";
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

