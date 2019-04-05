/***KYALO KELVIN MUINDI***/
/***P15/37561/2016***/
/***CLIENT PROGRAM TO PROMPT FOR USER NUMBER***/
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.Socket;

public class  clientroot
{
	public static void main(String args[]) throws Exception
	{
 
		Socket s=new Socket("localhost",6666);
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		String Y;
		System.out.println("Input a number: ");
		Y=br.readLine();
		PrintStream ps=new PrintStream(s.getOutputStream());
		ps.println(Y);
		BufferedReader fs=new BufferedReader(new InputStreamReader(s.getInputStream()));
		String result=fs.readLine();
		System.out.println("From Server : "+result);
		br.close();
		fs.close();	
		ps.close();
		
		s.close();
	}
}