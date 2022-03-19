import dns.resolver
from time import sleep
import os

os.system("cls")

lista_tipos = [
    "> A           Host Address",
    "> NS          Authoritative name server",
    "> MD          Mail destination",
    "> MF          Mail forwarder",
    "> CNAME       Canonical name for an alias",
    "> SOA         Start of a zone of authority",
    "> MB          Mailbox domain name",
    "> MG          Mail group member",
    "> MR          Mail rename domain name",
    "> NULL        Null RR",
    "> WKS         Well known service description",
    "> PTR         Domain name pointer",
    "> HINFO       Host information",
    "> MINFO       Mailbox or mail list information",
    "> MX          Mail exchange",
    "> TXT         Text strings",
    "> AXFR        Transfer of an entire zone",
    "> MAILB       Mailbox-related records",
    "> MAILA       Mail agent RR",
    "> ANY         All records",
    " ",
]


def main():
    try:
        print("\nTIPOS DE BUSQUEDA:")
        for tipos in lista_tipos:
            print(tipos)
            sleep(0.5)

        print("\n\nIngrese el tipo de busqueda que deseas:")
        tipo = input("")
        print("\n\nIngrese la direccion deseada:")
        direccion = input("")

        objetivo = dns.resolver.resolve(direccion, tipo)
        for x in objetivo:
            print(f"\n {direccion} = ", x, "\n")
            sleep(0.3)
    except:
        print("\n ~ERROR: --No se pudo obtener informacion-- \n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
