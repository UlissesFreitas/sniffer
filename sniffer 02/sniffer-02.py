import sys
import Camada3

LINE_HDR = 16

ETH_HDR_LEN = 14

ETH_LEN_MIN = 64
ETH_LEN_MAX = 1500

ETH_TYPE_IPV4 = 0X0800
ETH_TYPE_IPV6 = 0X86DD


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("argumentos insuficientes")
        sys.exit()

    try:
        fd = open(sys.argv[1], "rb")

    except:
        print("arquivo de entrada nao encontrado")

    fd.seek(24)

    header = fd.read(16)

    while len(header) == LINE_HDR:

        len_pacote = int.from_bytes(header[8:12], 'little')

        frame = fd.read(len_pacote)
        eth_type = int.from_bytes(frame[12:14], 'big')

        pacote = frame[ETH_HDR_LEN:]

        # ETHERNET 802.3
        # caso o pacote seja arp, arp pula o pacote pois nao usa cabecalho IP
        if eth_type <= 1500:
            header = fd.read(LINE_HDR)
            continue

        c4_proto = 0  # protocolo usado na camada 4

        # IPV4
        if eth_type == ETH_TYPE_IPV4:
            c4_proto = pacote[9]
            Camada3.p_ipv4(pacote)

        # IPV6
        elif eth_type == ETH_TYPE_IPV6:
            c4_proto = pacote[6]
            Camada3.p_ipv6(pacote)

        print()

        # Leitura do cabeçalho da proxima linha
        header = fd.read(LINE_HDR)
