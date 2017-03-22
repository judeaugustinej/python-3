### What is Paramiko
* Provides ssh login(ssh), file-transfer(scp and sftp) & keymanagement.
* Its build on PyCrypto to provide a python interface to the SSH2 protocol.
* It also offers an implementation of the SSH and SFTP server protocols.
* It can be used on threaded application.
* Application deployment utilities via SSH Fabric

### Paramiko main classes.
* SSHClient - server connection and file transfer.

### Login to machine
```
import paramiko

HOST_IP = ''
USERNAME = ''
PASSWORD = ''

ssh = paramiko.SSHClient()
ssh.connect(HOST_IP, username=USERNAME, password=PASSWORD)

```
