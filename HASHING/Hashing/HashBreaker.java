package bottle;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class HashBreaker  {

	static char[][] name=new char[62][5];    //A-Z, a-z and 0-9 total 62 characters  and 4 hidden positions 
	public static void main(String[] args) {
		for(int i=0;i<62;i++) {
			for(int j=0;j<5;j++)
			try {
				if(i<10) {
					name[i][j]= (char) (i+48);   //0 ASCII value 48 after these numbers i=10
					
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
			  String name="ZAM"; //Intitial String
			  String name1="d0a26218b4ad3c4c7b93a3f1b94d7687006a0b65ee0395e4696326f24f6dfb5d";
			  int i,j,k,l,m;
	              MessageDigest md = MessageDigest.getInstance("SHA-256");
	       
           for(i=0;i<62;i++) {
            	for(j=0;j<62;j++) {
            		for(k=0;k<62;k++) {
            			for(l=0;l<62;l++) {
            				for(m=0;m<62;m++) {
            			     name=name+""+test[m][4]+""+test[l][3]+""+test[k][2]+""+test[j][1]+""+test[i][0];
            			     byte[] result = md.digest(name.getBytes());
            			    if(bytesToHex(result).compareTo(name1)==0) {
            				    System.out.println("test is success"+name); 
            				    System.out.println(bytesToHex(result)+"\n"+name1);
            				    break;}
            	                System.out.println(test[m][4]+"  "+test[l][3]+"  "+test[k][2]+"  "+test[j][1]+"  "+test[i][0]);
            	                name="ZAM";
            			}
            			   if(m!=62){break;}
            				}
            			    if(l!=62){break;}
            	        }
            		
            		if(k!=62){break;}
            	}
            	if(j!=62){break;}}
             } catch (NoSuchAlgorithmException e) {
	            throw new IllegalArgumentException(e);
	        }
		
	}
}

