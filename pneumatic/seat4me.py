from network.udp_server import Server
pneumatic_server = ("192.168.1.78", 6789)
streamer_server  = ("192.168.1.50", 6799)
udp_server = Server(*streamer_server)
udp_server.bind()
udp_server.receive()