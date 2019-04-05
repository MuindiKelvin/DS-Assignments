/***KYALO KELVIN MUINDI***/
/***P15/37561/2016***/
/***SERVER ROOT PROGRAM TO CALCULATE SQUARE_ROOT OF A NUMBER***/
import java.net.*;
import java.io.*;
public class  serverroot
{
	public static void main(String args[]) throws Exception
	{
		ServerSocket ss=new ServerSocket(6666);
		Socket s=ss.accept();
		BufferedReader br=new BufferedReader(new InputStreamReader(s.getInputStream()));
		double Y,root;
		String result;
		
		Y=Double.parseDouble(br.readLine());
		
		System.out.println("From Client : "+Y);
		root=Math.sqrt(Y);
		result= "Answer is "+root;	
		PrintStream ps=new PrintStream(s.getOutputStream());
		ps.println(result);
		br.close();
		ps.close();
		s.close();
		ss.close();
	}
}