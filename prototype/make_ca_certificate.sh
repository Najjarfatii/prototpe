#! /bin/bash
openssl req -new -x509 -days 365 -in cle_aut -out cert_aut
openssl ca -create_serial -out ca_crt.pem -days 999 -keyfile ca_key.pem -selfsign -extensions v3_ca -in ca_csr.pem