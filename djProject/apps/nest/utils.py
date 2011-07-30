import pusher

def get_pusher():
    pusher.app_id = '6417'
    pusher.key = '93d0509ce62dd993b05a'
    pusher.secret = 'c824cb5eb3b9c96f863b'

    return pusher.Pusher()

                
