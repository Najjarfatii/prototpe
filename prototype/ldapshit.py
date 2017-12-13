from ldap3 import Server, Connection, ALL
server = Server('ipa.demo1.freeipa.org')
conn = Connection(server)
conn.bind()


 # Create a container for new entries
conn.add('ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'organizationalUnit')
# True
# Add a new user
conn.add('cn=b.young,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'inetOrgPerson', {'Name': 'Fatma', 'sn': 'Young', 'password': 'Fatma', 'telephoneNumber': 1111})
# True

#  # Looking at the schema for the inetOrgPerson object class we find that there are no mandatory attributes:
#  server.schema.object_classes['inetOrgPerson']
# Object class: 2.16.840.1.113730.3.2.2
#   Short name: inetOrgPerson
#   Superior: organizationalPerson
#   May contain attributes: audio, businessCategory, carLicense, departmentNumber, displayName, employeeNumber, employeeType, givenName, homePhone, homePostalAddress, initials, jpegPhoto, labeledURI, mail, manager, mobile, o, pager, photo, roomNumber, secretary, uid, userCertificate, x500UniqueIdentifier, preferredLanguage, userSMIMECertificate, userPKCS12
#   Extensions:
#     X-ORIGIN: RFC 2798
#
# # The inetOrgPerson object class is a subclass of the organizationalPerson object that again doesn’t include any mandatory attributes:
# >>> server.schema.object_classes['organizationalPerson']
# Object class: 2.5.6.7
#   Short name: organizationalPerson
#   Superior: person
#   May contain attributes: title, x121Address, registeredAddress, destinationIndicator, preferredDeliveryMethod, telexNumber, teletexTerminalIdentifier, internationalISDNNumber, facsimileTelephoneNumber, street, postOfficeBox, postalCode, postalAddress, physicalDeliveryOfficeName, ou, st, l
#   Extensions:
#     X-ORIGIN: RFC 4519
#   OidInfo: ('2.5.6.7', 'OBJECT_CLASS', 'organizationalPerson', 'RFC4519')
# # The organizationalPerson object class is a subclass of the person object where we finally find two mandatory attributes:
# >>> server.schema.object_classes['person']
# Object class: 2.5.6.6
#   Short name: person
#   Superior: top
#   Must contain attributes: sn, cn
#   May contain attributes: userPassword, telephoneNumber, seeAlso, description
#   Extensions:
#     X-ORIGIN: RFC 4519
#   OidInfo: ('2.5.6.6', 'OBJECT_CLASS', 'person', 'RFC4519')
#
# # Renaming an entry in LDAP means changing its RDN (Relative Distinguished Name) without changing the container where the entry is stored. It is performed with the ModifyDN operation:
# >>> conn.modify_dn('cn=b.young,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'cn=b.smith')
# True
#

