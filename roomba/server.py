import socket
import roomba.setting as st
def run_server():
        HOST = socket.gethostname() # Server IP or Hostname
        PORT = 12397 # Pick an open Port (1000+ recommended), must match the client sport
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print 'Socket created'

        #managing error exception
        try:
                s.bind(("", PORT))
        except socket.error:
                print 'Bind failed'
                
        s.listen(5)
        print('server is runing')
        (conn, addr) = s.accept()
        print 'Connected'

        # awaiting for message
        while True:
                try:
                        data = conn.recv(1024)
                        st.received_message.append(data)
                except:
                        print("something happened to server")
                while not st.send_message:
                        sleep(1)
                conn.send(st.send_message[0])
                sleep(1)
                st.send_message.pop()

                
                # process your message
##                if data == 'Hello':
##                        reply = 'Hi, back!'
##                elif data == 'This is important':
##                        reply = 'OK, I have done the important thing you have asked me!'
##
##                #and so on and on until...
##                elif data == 'quit':
##                        conn.send('Terminating')
##                        break
##                else:
##                        reply = 'Unknown command'
##
##                # Sending reply
                
#               conn.send(reply)
        conn.close() # Close connections

