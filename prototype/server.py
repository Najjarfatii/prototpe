# Certificate Related Imports
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.backends import default_backend

# Network Imports
import socket, ssl

# context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH,cafile='ca_crt.pem')
context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='server_crt.pem', keyfile='server_key.pem')
context.load_verify_locations(cafile='cert_aut.pem')
context.verify_mode = ssl.CERT_REQUIRED
# context.verify_flags = ssl.VERIFY_CRL_CHECK_LEAF
# context.check_hostname = False


serv_sock = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
serv_sock.bind(('',4444))
serv_sock.listen(5)

client_sock, addr_port = serv_sock.accept()
client_sock_secure = context.wrap_socket(client_sock,server_side=True)
client_crt_der = client_sock_secure.getpeercert(binary_form=True)
client_crt = x509.load_der_x509_certificate(data=client_crt_der,backend=default_backend())

print('We got here')
# Do shit with the certificate
# Do authorization
#
# client_sock_secure.shutdown(socket.SHUT_RDWR)
# client_sock_secure.close()
