public class MyRemoteClass extends java.rmi.server.UnicastRemoteObject implements MyInterface {

    // The class constructor that needs to be initialized

    /**
     * 
     * @throws java.rmi.RemoteException
     *                                  This will always throw a RemoteException as
     *                                  we are using Java Remote Method Invocation
     */
    public MyRemoteClass() throws java.rmi.RemoteException {
        super();
    }

    /**
     * @throws java.rmi.RemoteException
     *                                  Throw a remote exception
     */
    public String sayHello() throws java.rmi.RemoteException {
        return "Hello, world!";
    }
}
