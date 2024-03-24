def inet6_to_str(inet):
    if isinstance(inet, bytes):
       return ":".join([f'{b:x}' for b in inet])



def inet_to_str(inet):
    if isinstance(inet, bytes):
       return ".".join([f'{b}' for b in inet])
def p_ipv4(inet):
    if isinstance(inet, bytes):
        print(f'versao -> {inet[0] >> 4}')
        print(f'IHL -> {(inet[0] & 0x0F)*4} (bytes)')
        print(f'type -> {inet[1]}')
        print(f'Comprimento -> {int.from_bytes(inet[2:4], "big")}')
        print(f'identificador -> 0x{int.from_bytes(inet[4:6], "big"):x}')
        print(f'Flag -> 0x{(inet[6] >> 5):x}')
        print(f'TTL -> {inet[8]}')
        print(f'Protocol -> {inet[9]}')
        print(f'checksum -> 0x{int.from_bytes(inet[10:12], "big"):x}')
        print(f'IP origem -> {inet_to_str(inet[12:16])}')
        print(f'IP destino -> {inet_to_str(inet[16:20])}')


def p_ipv6(inet6):
    if isinstance(inet6, bytes):
        print(f'versao -> {inet6[0] >> 4}')
        print(f'payload -> {int.from_bytes(inet6[4:6], "big")}')
        print(f'Next header -> {inet6[6]}')
        print(f'HOT Limit -> {inet6[7]}')
        print(f'IP origem -> {inet6_to_str(inet6[8:24])}')
        print(f'IP destino -> {inet6_to_str(inet6[24:40])}')