#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys


#Variables that contains the user credentials to access Twitter API 
access_token = "101973377-Wb4deNtdXdSfsdfoUo7SKVOnHjf8SEZlAJ8s7JAl"
access_token_secret = "GNcU23gzwfRY8BLSUIQmea1SCc9BnZtHGsWPyWwKhgwtq"
consumer_key = "rNQwltpJhYMOVK6NdEPMDNgK7"
consumer_secret = "JZzweIEuGCi4NbY2SvEvvfDw8UyOetVAJ2SY7s6Y7QkTBpGYay"

print("Collecting Data for: #{}".format(sys.argv[1]))
tf = open('data/twitter_stream_{}.txt'.format(sys.argv[1]),'a')

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        #print(data)
        tf.write(data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['python', 'javascript', 'ruby'])
    
    stream.filter(track=['#{}'.format(sys.argv[1])])
    
tf.close()
    