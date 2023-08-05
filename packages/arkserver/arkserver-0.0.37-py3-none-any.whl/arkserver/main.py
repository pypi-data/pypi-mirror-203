from arkserver import GameBotServer, Base



def run():
    """s.bind(('', 80)) specifies that the socket is reachable by any address the machine happens to have"""
    server = Base(host='')  # same as 0.0.0.0
    # game_server = GameBotServer(host='0.0.0.0')
    # game_server = GameBotServer(host='172.20.176.1')
    # game_server = GameBotServer(host='192.168.56.1')
    # game_server = GameBotServer(host='192.168.1.135')
    # game_server = GameBotServer(host=socket.gethostname())
    # game_server = GameBotServer(host=socket.gethostbyname(socket.gethostname()))
    server.run()


if __name__ == "__main__":
    run()

