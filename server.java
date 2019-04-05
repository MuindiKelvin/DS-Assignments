package mutualExc;

import java.io.*;
import java.net.*;
 
class JavaServ {
    public static void main(String args[]) throws Exception {
        String fromClient;
        String toClient;
 
        @SuppressWarnings("resource")
		ServerSocket server = new ServerSocket(8080);
        System.out.println("wait for connection on port 8080");
 
        boolean run = true;
        while(run) {
            Socket client = server.accept();
            System.out.println("got connection on port 8080");
            BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
            PrintWriter out = new PrintWriter(client.getOutputStream(),true);
 
            fromClient = in.readLine();
            System.out.println("received: " + fromClient);
 
            if(fromClient.equals("Hello")) {
                toClient = "olleH";
                System.out.println("send olleH");
                out.println(toClient);
                fromClient = in.readLine();
                System.out.println("received: " + fromClient);
 
                if(fromClient.equals("Bye")) {
                    toClient = "eyB";
                    System.out.println("send eyB");
                    out.println(toClient);
                    client.close();
                    run = false;
                    
                    @SuppressWarnings("resource")
                    ServerSocket server1 = new ServerSocket(8081);
                    System.out.println("wait for connection on port 8081");
             
                    boolean run2 = true;
                    while(run2) {
                        Socket client1 = server1.accept();
                        System.out.println("got connection on port 8081");
                        BufferedReader in1 = new BufferedReader(new InputStreamReader(client1.getInputStream()));
                        PrintWriter out1 = new PrintWriter(client1.getOutputStream(),true);
             
                        fromClient = in1.readLine();
                        System.out.println("received: " + fromClient);
             
                        if(fromClient.equals("Hello")) {
                            toClient = "olleH";
                            System.out.println("send olleH");
                            out1.println(toClient);
                            fromClient = in1.readLine();
                            System.out.println("received: " + fromClient);

                            if(fromClient.equals("Bye")) {
                                toClient = "eyB";
                                System.out.println("send eyB");
                                out1.println(toClient);
                                client1.close();
                                run2 = false;
                                System.out.println("socket closed");
                            }
                        }
                    }
                    
                    System.out.println("socket closed");
                }
            }
        }
        
       
        System.exit(0);
    }
}
