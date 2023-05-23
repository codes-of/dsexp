import org.omg.CORBA.*;
import org.omg.CosNaming.*;

public class sample {
    public static void main(String[] args) {
        try {
            // Initialize the ORB (Object Request Broker)
            ORB orb = ORB.init(args, null);

            // Obtain the Naming Service's root naming context
            org.omg.CORBA.Object objRef = orb.resolve_initial_references("NameService");
            NamingContextExt ncRef = NamingContextExtHelper.narrow(objRef);

            // Bind the CORBA object to a name in the Naming Service
            String name = "MyCORBAObject";
            org.omg.CORBA.Object corbaObj = // create or obtain the CORBA object
            NameComponent[] path = ncRef.to_name(name);
            ncRef.rebind(path, corbaObj);
            System.out.println("CORBA object bound to name: " + name);

            // Retrieve the CORBA object from the Naming Service
            org.omg.CORBA.Object retrievedObj = ncRef.resolve(path);
            System.out.println("CORBA object retrieved from the Naming Service");

            // Perform operations on the retrieved CORBA object
            // ...

            // Shutdown the ORB
            orb.shutdown(true);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
