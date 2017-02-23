videos_MAX = 10000
endpoint = 1000
request_descriptions = 1000000
cache_servers = 1000
x_cache_server_capacity = 500000


# optimize how videos is delivered to the users


# check popularity function by request
def calc_popularity(requests, endpoints):
    # TODO video storage to cache server - database implementation
    # popular video by requests and endpoints
    video = {}
    print('Done popular video')
    return video


def can_video_be_store(video ,cacheserver):
   return video.size <= cacheserver.size


# cache store video to cache servers
def make_store(video, cacheserver):
    #TODO make video store to cachserver
    pass


def store_video(videos, cacheservers):
    #for each cache server in cache servers
    for cacheserver in cacheservers:
        #for each video in videos
        for video in videos:
            if can_video_be_store(video, cacheserver):
                make_store(video, cacheserver)


    # TODO video storage to cache server - database implementation
    print('Done storing video to some decided cache server')

# optimize distribute to cache servers based on popularity
