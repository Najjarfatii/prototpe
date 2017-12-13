#! /bin/bash
openssl req -new -x509 -newkey rsa:2048 -keyout ca_key.pem -out ca_csr.pem -nodes