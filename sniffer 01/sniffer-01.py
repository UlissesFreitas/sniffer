import dpkt
import datetime
import socket
from dpkt.compat import compat_ord

filename = "captura.pcap"


def mac_addr(address):
	return ":".join('%02x' % compat_ord(b) for b in address )


def ip_addr(inet):
	try:
		return socket.inet_ntop(socket.AF_INET, inet)
	except ValueError:
		return socket.inet_ntop(socket_AF_INET6, inet)

def print_packet(pcap):
	for timestamp, buf in pcap:
		print("\033[95m[+]", datetime.datetime.utcfromtimestamp( timestamp), "\033[0m")
		eth = dpkt.ethernet.Ethernet(buf)
		print("\033[91m", "\tEthernet:", "\033[0m", mac_addr(eth.src), " -> ", mac_addr(eth.dst), " " , eth.type)

		if not isinstance(eth.data, dpkt.ip.IP):
			continue

		ip = eth.data
		print("\033[92m", "\tNetwork", "\033[0m", ip_addr( ip.src), " -> ", ip_addr(ip.dst))


if __name__ == "__main__":
	with open(filename, "rb") as f:
		pcap = dpkt.pcap.Reader(f)
		print_packet(pcap)
