import json  
import paramiko  
import torndb
import pymongo

def connect(host):  
    'this is use the paramiko connect the host,return conn'  
    ssh = paramiko.SSHClient()  
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
    try:  
        ssh.connect(host,username='root',password='redhat',allow_agent=True)  
        return ssh  
    except:  
        return None  
  
def command(args,outpath):  
    'this is get the command the args to return the command'  
    cmd = '%s %s' % (outpath,args)  
    return cmd  
  
def exec_commands(conn,cmd):  
    'this is use the conn to excute the cmd and return the results of excute the command'  
    stdin,stdout,stderr = conn.exec_command(cmd)  
    results=stdout.read()  
    return results  
  
def excutor(host,outpath,args):  
    conn = connect(host)  
    if not conn:  
        return [host,None]  
    #exec_commands(conn,'chmod +x %s' % outpath)  
    cmd =command(args,outpath)  
    result = exec_commands(conn,cmd)  
    result = json.dumps(result)  
    return [host,result]

def copy_module(conn,inpath,outpath):  
    'this is copy the module to the remote server'  
    ftp = conn.open_sftp()  
    ftp.put(inpath,outpath)  
    ftp.close()  
    return outpath  
  
  
if __name__ == '__main__':
    exec_commands(connect('192.168.1.15'),'mkdir /tmp/test2')
    
