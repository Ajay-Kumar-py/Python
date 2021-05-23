
import paramiko
import pysftp

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='mftdev-dr.rubrik.com',username='birch-user',password="FtXkXwdQ3P8H",port=22)
sftp_client = ssh.open_sftp()

sftp_client.get('/home/birch-user/riversand_productmasterdata/production_application/pdmtoapps/2f8f5978-9de4-4e74-93a1-23e7aceb8cda.csv','C:\my-doc\python files\Paramiko_test.csv')
print(sftp_client.listdir("/home/birch-user/riversand_productmasterdata/production_application/pdmtoapps"))
#print(dir(sftp_client))

ssh.close()